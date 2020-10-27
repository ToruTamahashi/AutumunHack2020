from datetime import datetime
import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm
from sqlalchemy.orm import relationship

from ..config import DB_USERNAME
from ..config import DB_PASS
from ..config import DB_HOST
from ..config import DB_PORT
from ..config import DB_NAME


USERNAME = DB_USERNAME
PASSWORD = DB_PASS
HOST = DB_HOST
PORT = DB_PORT
DATABASE = DB_NAME

url = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(USERNAME, PASSWORD, HOST, PORT, DATABASE)
#url = 'mysql+pymysql://root:root@localhost:3333/autumn_hack?charset=utf8'
engine = sqlalchemy.create_engine(url, echo=True)
Base = sqlalchemy.ext.declarative.declarative_base()



class UserEntity(Base):
    __tablename__ = 'user'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(30))
    twitter_id = sqlalchemy.Column(sqlalchemy.String(30))
    session_id = sqlalchemy.Column(sqlalchemy.String(100))
    access_token = sqlalchemy.Column(sqlalchemy.String(255))
    access_token_secret = sqlalchemy.Column(sqlalchemy.String(255))
    secret_word = sqlalchemy.Column(sqlalchemy.String(255))
    create_at = sqlalchemy.Column(sqlalchemy.TIMESTAMP)
    update_at = sqlalchemy.Column(sqlalchemy.TIMESTAMP)
    #tasklist = relationship("TaskEntity", back_populates="user")
    # relationship({参照する側のクラス名}, backref={tablename})

    def user_entity_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'twitter_id': self.twitter_id,
            'session_id': self.session_id,
            'access_token': self.access_token,
            'access_token_secret': self.access_token_secret,
            'secret_word': self.secret_word,
            'create_at': self.create_at,
            'update_at': self.update_at,
        }



class TaskEntity(Base):
    __tablename__ = 'task'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String(100))
    tweet = sqlalchemy.Column(sqlalchemy.Integer)
    mail = sqlalchemy.Column(sqlalchemy.String(100))
    deadline_at = sqlalchemy.Column(sqlalchemy.TIMESTAMP)
    create_at = sqlalchemy.Column(sqlalchemy.TIMESTAMP)
    update_at = sqlalchemy.Column(sqlalchemy.TIMESTAMP)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('user.id'))
    user = relationship("UserEntity")
    # userにはuser_idに該当したUserEntityが入る

    def task_entity_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'tweet': self.tweet,
            'mail' : self.mail,
            'deadline_at': self.deadline_at,
            'create_at': self.create_at,
            'update_at': self.update_at,
            'user_id': self.user_id,
        }



Base.metadata.create_all(engine)
Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

class UserService(object):

    def find_all(self):
        """
          # userテーブル全件取得
        :return: Array(UserEntity)
        """
        return session.query(UserEntity).all()

    def find(self, twitter_id):
        """
          #  userテーブルから該当するtwitter_idを持つ行を取得
        :param twitter_id: String
        :return: UserEntity
        """
        # twitter_idが一致する行を全権取得（でもidはユニークなので1つしか取得されない）
        user = session.query(UserEntity).filter(UserEntity.twitter_id == twitter_id).all()
        if len(user) != 0:
            return user[0]
        else:
            return None


    def findBySessionID(self, session_id):
        """
          #  userテーブルから該当するtwitter_idを持つ行を取得
         :param session_id: String
         :return: UserEntity
        """
        # twitter_idが一致する行を全権取得（でもidはユニークなので1つしか取得されない）
        user = session.query(UserEntity).filter(
            UserEntity.session_id == session_id).all()
        if len(user) != 0:
            return user[0]
        else:
            return None

    def create(self, user_entity):
        """
          # userテーブル挿入
        :param user_entiy: UserEntity
        :return: 正常終了：ok , 例外発生：error
        """
        try:
            session.add(user_entity)
            session.commit()
            return "ok"
        except Exception as ex:
            print("Exception:{}".format(ex))
            return "error"

    def update(self,upd_user_entity):
        """
         # userテーブルを更新
        :param upd_user_entity: UserEntity
        :param id: int
        :return: 正常終了：updしたid,  例外発生：error
        """

        try:
            # userテーブルから指定のidに該当する行を更新
            user = self.find(upd_user_entity.twitter_id)
            user.name = upd_user_entity.name
            user.twitter_id = upd_user_entity.twitter_id
            user.session_id = upd_user_entity.session_id
            user.access_token = upd_user_entity.access_token
            user.access_token_secret = upd_user_entity.access_token_secret
            user.secret_word = upd_user_entity.secret_word
            user.update_at = datetime.now()
            new_user = session.query(UserEntity).filter(
                UserEntity.id == user.id).first()
            new_user = new_user
            session.commit()
            return 'true'
        except Exception as ex:
            print("Exception:{}".format(ex))
            return 'false'


    def delete(self, id):
        """
          # userテーブルから指定のidを持つ行を削除
        :param id: int
        :return: 正常終了：削除したid  例外発生：error
        """
        try:
            session.query(UserEntity).filter(UserEntity.id == id).delete()
            session.commit()
            return id
        except Exception as ex:
            print("Exception:{}".format(ex))
            return "error"



class TaskService(object):
    def find_all(self):
        tasks = session.query(TaskEntity).all()
        task_info=[]
        for task in tasks:
            task_change = task.task_entity_dict()
            task_info.append(task_change)
        return task_info


    def find(self, id):
        """
          #  taskテーブルから該当するidを持つ行を取得
        :param id: int
        :return: List(TaskEntity)
        """
        tasks = session.query(TaskEntity).filter(
            TaskEntity.user_id == id).all()
        if len(tasks) != 0:
            print("aaa")
            print(type(tasks[0].deadline_at))
            return tasks
        else:
            return None


    def create(self, task_entity):
        """
          # taskテーブル挿入
        :param task_entiy: TaskEntity
        :return: json ex) {'result':'success'} or {'result':'failure'}
        """
        try:
            task_entity.create_at = datetime.now()
            task_entity.update_at = datetime.now()
            session.add(task_entity)
            session.commit()
            return {'result':'success'}
        except Exception as ex:
            print("Exception:{}".format(ex))
            return {'result':'failure'}




    def update(self,upd_task_entity):
        """
         # userテーブルを更新
        :param upd_task_entity: TaskEntity
        :return: json ex) {'result':'success'} or {'result':'failure'}
        """
        try:
            task = self.find(upd_task_entity.id)[0]
            task.title = upd_task_entity.title
            task.tweet = upd_task_entity.tweet
            task.mail = upd_task_entity.mail
            task.deadline_at = upd_task_entity.deadline_at
            task.update_at = datetime.now()
            new_task = session.query(TaskEntity).filter(
                TaskEntity.id == task.id).first()
            new_task = new_task
            session.commit()
            return {'result':'success'}
        except Exception as ex:
            print("Exception:{}".format(ex))
            return {'result':'failure'}


    def delete(self, id):
        """
          # taskテーブルから指定のidを持つ行を削除
        :param id: int
        :return: json ex) {'result':'success'} or {'result':'failure'}
        """
        try:
            task = session.query(TaskEntity).get(int(id))
            session.delete(task)
            session.commit()
            return {'result':'success'}
        except Exception as ex:
            print("Exception:{}".format(ex))
            return {'result':'failure'}
