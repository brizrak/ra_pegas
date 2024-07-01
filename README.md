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

sudo nano .env 
cd wagtail
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd ra_pegas



python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
sudo cp -r /home/bibza/ra_pegas/wagtail/ra_pegas/static /usr/share/nginx/html
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
sudo systemctl restart nginx
