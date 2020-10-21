CREATE DATABASE IF NOT EXISTS autumn_hack DEFAULT CHARACTER SET utf8mb4;
SET CHARSET UTF8;
CREATE TABLE IF NOT EXISTS autumn_hack.user
(
	id int auto_increment,
	name VARCHAR(30) null,
	twitter_id VARCHAR(30) null,
	access_token VARCHAR(255) null,
	access_token_secret VARCHAR(255) null,
	secret_word VARCHAR(30),
	create_at TIMESTAMP null,
	update_at TIMESTAMP null,
	constraint usr_pk
		primary key (id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS autumn_hack.task
(
	 id               int auto_increment primary key,
    title             varchar(100)  not null,
    tweet             int default 0 null,
    deadline_at       timestamp     null,
    create_at         timestamp     null,
    update_at         timestamp     null,
    user_id           int           null,
    constraint task_user_id_fk
        foreign key (user_id) references user (id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


INSERT INTO autumn_hack.user (id, name, twitter_id, access_token, access_token_secret, secret_word, create_at, update_at) VALUES (1, '田中', 'dummy_id', 'tmp_toke_najofjadjfoiaj', 'tmp_token_secret_dfajdofijadjf', '実は○○なんです...', '2020-10-14 04:31:41', '2020-10-14 04:32:40');
INSERT INTO autumn_hack.user (id, name, twitter_id, secret_word, create_at, update_at) VALUES (2, 'tama', 'dummy_id2', '昔XXをやらかしました', '2020-10-14 04:33:59', '2020-10-14 04:34:03');

INSERT INTO autumn_hack.task (id, title, tweet, deadline_at,  create_at, update_at, user_id) VALUES (1, '課題を終わらせる', 0, '2020-10-17 18:20:00', '2020-10-14 04:20:49', '2020-10-14 04:21:23', 1);
INSERT INTO autumn_hack.task (id, title, tweet, deadline_at,  create_at, update_at, user_id) VALUES (2, '朝7時30分に起きる', 1, '2020-10-18 07:30:00', '2020-10-14 04:23:13', '2020-10-14 04:23:18', 2);
INSERT INTO autumn_hack.task (id, title, tweet, deadline_at,  create_at, update_at, user_id) VALUES (3, '朝7時30分に起きる', 1, '2020-10-18 07:30:00', '2020-10-14 04:23:13', '2020-10-14 04:23:18', 2);



