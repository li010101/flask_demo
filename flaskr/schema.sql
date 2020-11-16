
CREATE DATABASE flask_demo;


USE flask_demo;

CREATE TABLE user (
  id int PRIMARY KEY AUTO_INCREMENT,
  username varchar(20) UNIQUE NOT NULL,
  password varchar(20) NOT NULL
);

CREATE TABLE post (
  id INT PRIMARY KEY AUTO_INCREMENT,
  author_id INT NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);