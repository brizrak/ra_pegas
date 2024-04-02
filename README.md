# ra_pegas


DATABASE:

sudo su - postgres

psql

CREATE USER <user name> WITH PASSWORD <'password'> CREATEDB;
CREATE DATABASE <database name> WITH OWNER <user name>;
GRANT ALL PRIVILEGES ON DATABASE <db name> TO <user name>;

\c <database name>

GRANT ALL ON ALL TABLES IN SCHEMA public to dbuser;
GRANT ALL ON ALL SEQUENCES IN SCHEMA public to dbuser;
GRANT ALL ON ALL FUNCTIONS IN SCHEMA public to dbuser;

CHANGE USER:

REASSIGN OWNED BY old_role TO new_role;



RUNNING:

cd wagtail/ra_pegas
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
