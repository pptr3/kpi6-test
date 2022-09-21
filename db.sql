CREATE TABLE roles (
    role_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    role_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (role_id)
);


CREATE TABLE users (
    id_user INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(255) NOT NULL,
    role_id_user INT UNSIGNED NOT NULL,
    FOREIGN KEY (role_id_user) REFERENCES roles(role_id)
);

insert into roles (role_name) values('Engineer');

insert into users (user_name, role_id_user) values('Petru', 1)    