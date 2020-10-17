import sqlalchemy
from datetime import datetime
import sqlalchemy.ext.declarative
import sqlalchemy.orm
from sqlalchemy.orm import relationship


USERNAME = 'root'
PASSWORD = 'root'
HOST = 'db'
PORT = '3306'
DATABASE = 'autumn_hack'

url = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(USERNAME, PASSWORD, HOST, PORT, DATABASE)
#url = 'mysql+pymysql://root:root@localhost:3333/autumn_hack?charset=utf8'
engine = sqlalchemy.create_engine(url, echo=True)
Base = sqlalchemy.ext.declarative.declarative_base()



class UserEntity(Base):
    __tablename__ = 'user'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(30))
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
    declaration_tweet = sqlalchemy.Column(sqlalchemy.Integer)
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
            'declaration_tweet': self.declaration_tweet,
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

    def find(self, id):
        """
          #  userテーブルから該当するidを持つ行を取得
        :param id: int
        :return: UserEntity
        """
        # idが一致する行を全権取得（でもidはユニークなので1つしか取得されない）
        users = session.query(UserEntity).all()
        users_find_id = users[int(id)-1].user_entity_dict()
        return users_find_id
        # try:
        #     user = session.query(UserEntity).filter(UserEntity.id == id).all()
        #     return user[0]
        # except Exception as ex:
        #     print("Exception:{}".format(ex))
        #     return "error"

    def create(self, user_entiy):
        """
          # userテーブル挿入
        :param user_entiy: UserEntity
        :return: 正常終了：ok , 例外発生：error
        """
        try:
            session.add(user_entiy)
            session.commit()
            return "ok"
        except Exception as ex:
            print("Exception:{}".format(ex))
            return "error"

    def update(self,upd_user_entity,id):
        """
         # userテーブルを更新
        :param upd_user_entity: UserEntity
        :param id: int
        :return: 正常終了：updしたid,  例外発生：error
        """
        try:
            # userテーブルから指定のidに該当する行をフィルタリングし抽出結果をfirst()で返す
            user = session.query(UserEntity).filter(UserEntity.id == id).first()
            user = upd_user_entity
            session.commit()
            return id
        except Exception as ex:
            print("Exception:{}".format(ex))
            return "error"

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
        :return: TaskEntity
        """
        # idが一致する行を全権取得（でもidはユニークなので1つしか取得されない）
        tasks = session.query(TaskEntity).all()
        task_info=[]
        for task in tasks:
            task_change = task.task_entity_dict()
            if task_change['user_id'] == int(id):
                task_info.append(task_change)
                print("in data")
            else:
                print("no data")
        return task_info

    def create(self, task_entity):
        """
          # taskテーブル挿入
        :param task_entiy: TaskEntity
        :return: 正常終了：ok , 例外発生：error
        """

        try:
            session.add(task_entity)
            session.commit()
            return "ok"
        except Exception as ex:
            print("Exception:{}".format(ex))
            return "error"


    def update(self,upd_task_entity,id):
        """
         # userテーブルを更新
        :param upd_task_entity: TaskEntity
        :param id: int
        :return: 正常終了：updしたid,  例外発生：error
        """
        try:
            task = session.query(TaskEntity).filter(TaskEntity.id == id).first()
            task = upd_task_entity
            session.commit()
            return id
        except Exception as ex:
            print("Exception:{}".format(ex))
            return "error"

    def delete(self, id):
        """
          # taskテーブルから指定のidを持つ行を削除
        :param id: int
        :return: 正常終了：削除したid  例外発生：error
        """
        try:
            session.query(TaskEntity).filter(TaskEntity.id == id).delete()
            session.commit()
            return id
        except Exception as ex:
            print("Exception:{}".format(ex))
            return "error"

