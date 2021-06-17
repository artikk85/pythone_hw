CREATE DATABASE vk;



CREATE TABLE users (
 id int UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
 first_name varchar(100) NOT NULL,
 last_name varchar(100) NOT NULL,
 email varchar(255) NOT NULL,
 phone varchar(255) NOT NULL,
 created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
 updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE profiles (
 USER_id int UNSIGNED NOT NULL PRIMARY KEY,
 birthday date,
 gender char(1) NOT NULL,
 city varchar(60) NOT NULL,
 country varchar(60) NOT NULL,
 created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
 updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- таблица сообщений
CREATE TABLE messages (
 id int UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY comment 'индентификатор стороки',
 from_user_id int UNSIGNED NOT NULL comment 'ссылка на отправителя сообщения',
 to_user_id int UNSIGNED NOT NULL comment 'ссылка на получателя сообщения',
 body text NOT NULL comment 'текст сообщения',
 is_important boolean comment 'признак важности',
 is_delivered boolean comment 'признак доставки',
 created_at datetime DEFAULT now() comment 'время создания строки',
 updated_at datetime DEFAULT current_timestamp ON UPDATE current_timestamp comment 'время обновления строки'
) comment 'сообщения';

-- таблица дружбы
CREATE TABLE friendship (
 user_id int UNSIGNED NOT NULL comment 'ссылка на инициатора дружеских отношений',
 friend_id int UNSIGNED NOT NULL comment 'ссылка на получателя приглашения дружить',
 status_id int UNSIGNED NOT NULL comment 'ссылка на статус, текущее состояние отношений',
 requested_at datetime DEFAULT now() comment 'время отправления приглашения дружить',
 confirmed_at datetime comment 'время подтверждения приглашения',
 created_at datetime DEFAULT current_timestamp comment 'время создания строки',
 updated_at datetime DEFAULT current_timestamp ON UPDATE current_timestamp comment 'время обновления строки',
 PRIMARY KEY (user_id, friend_id) comment 'составной первичный ключ'
) comment 'таблица дружить';

-- таблица статусов дружеских отношений
CREATE TABLE friendship_statuses (
 id int UNSIGNED NOT NULL auto_INCREMENT PRIMARY KEY comment 'идентификатор строки',
 name varchar(150) NOT NULL UNIQUE comment 'название статуса',
 created_at datetime DEFAULT current_timestamp comment 'время создание статуса',
 updated_at datetime DEFAULT current_timestamp ON UPDATE current_timestamp comment 'время обновления строки'
) comment 'статусы дружбы';

CREATE TABLE communities (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(150) NOT NULL UNIQUE,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- таблица связи пользователя и группы
CREATE TABLE communities_user (
 communities_id int UNSIGNED NOT NULL comment 'ссылка на группу',
 user_id int UNSIGNED NOT NULL comment 'ссылка на пользователя',
 created_at datetime DEFAULT current_timestamp comment 'время создание строки',
 PRIMARY KEY (community_id, user_id) comment 'составной первичный ключ'
) comment 'участники групп, связь между пользователями и группами';

-- таблица медиафайлов
CREATE TABLE media (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT "идентификатор строки",
  user_id INT UNSIGNED NOT NULL COMMENT "ссылка на пользователя, загрузившего файл",
  filename VARCHAR(255) NOT NULL COMMENT "путь к файлу",
  size INT NOT NULL COMMENT "размер файла",
  metadata JSON COMMENT "методанные файла",
  media_type_id INT UNSIGNED NOT NULL COMMENT "ссылка на тип контента",
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT "время создания строки",
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT "время обновления строки"
) COMMENT "медиафайлы";

-- таблица типов медиафайлов
CREATE TABLE media_types (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT "идентификатор строки",
  name VARCHAR(255) NOT NULL UNIQUE COMMENT "название типа",
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT "время создание строки",
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT "время обновления строки"
) COMMENT "типы медиафайлов";

-- таблица пользовательских постов
CREATE TABLE posts_user (
id int UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY comment 'идентификатор строки',
user_id int UNSIGNED NOT NULL comment 'идентификатор пользователя, публикующего пост',
posttypes int UNSIGNED NOT NULL comment 'тип поста',
filename VARCHAR(255) NOT NULL COMMENT "путь к файлу",
size INT NOT NULL COMMENT "размер файла",
metadata JSON COMMENT "методанные файла",
created_at DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT "время создание поста",
updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT "время обновления поста"
) comment 'польтзовательские посты';

-- таблица типов постов
CREATE TABLE posts_user_types (
 id int UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY comment 'идентификатор строки',
 name varchar(255) NOT NULL UNIQUE comment 'название типа',
 created_at DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT "время создание строки",
 updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT "время обновления строки"
) comment 'типы постов';

-- таблица использования лайков
CREATE TABLE like_media_user_post (
 id int UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY 'идентификатор строки',
 from_user_id int UNSIGNED NOT NULL comment 'ссылка на пользователя, ставящего лайк',
 to_user_id int UNSIGNED NOT NULL comment 'ссылка на пользователя, которому поставили лайк',
 media_id int UNSIGNED NOT NULL comment 'ссылка на медиафайл',
 post_user_id int UNSIGNED NOT NULL comment 'сылка на пост пользователя'
 created_at DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT "время создания строки",
 updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT "время обновления строки"
) comment 'лайки';
