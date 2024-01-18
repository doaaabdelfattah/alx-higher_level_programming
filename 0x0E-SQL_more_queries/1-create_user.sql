--  creates the MySQL server user user_0d_1
CREATE USER user_0d_1@localhost BY 'user_0d_1_pwd';
GRANT ALL
ON *.*
TO user_0d_1@localhost;