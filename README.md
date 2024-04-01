# ra_pegas


source wagtail/ra_pegas/venv/bin/activate


sudo su - postgres

psql

CREATE USER <user name> WITH PASSWORD <'password'> CREATEDB;

CREATE DATABASE <database name> WITH OWNER <user name>;

GRANT ALL PRIVILEGES ON DATABASE <db name> TO <user name>;

???????
psql mydatabase -c "GRANT ALL ON ALL TABLES IN SCHEMA public to dbuser;"

psql mydatabase -c "GRANT ALL ON ALL SEQUENCES IN SCHEMA public to dbuser;"

psql mydatabase -c "GRANT ALL ON ALL FUNCTIONS IN SCHEMA public to dbuser;"
???????
