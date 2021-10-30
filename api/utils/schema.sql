DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS users;


CREATE TABLE users (
  uid INTEGER PRIMARY KEY AUTO_INCREMENT,
  username TEXT NOT NULL
);

CREATE TABLE posts (
  pid INTEGER PRIMARY KEY AUTO_INCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES users (uid)
);