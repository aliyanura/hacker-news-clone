# hacker-news-clone

* Activate virtual environment:
```
python3 -m venv venv
sourse venv/bin/activate
```
* Install all packages
```
pip install -m requrements.txt
```

* Create private `.env` file inside of project directory. Copy all data from 
```
DB_NAME =<name>
DB_USER =<user>
DB_PASSWORD =<password>
SECRET_KEY =<key>
```
and paste inside of `.env` file. **Note**: Change the values of secrets to yours. 

* This project uses Postgresql, so, create Postgresql database:
```
sudo apt-get update
sudo apt-get install python3-pip python3-dev libpq-dev postgres postgres-contrib
sudo -i -u postgres
```
* Enter postgres console:
```
psql
CREATE DATABASE <database name>;
CREATE USER <database user> WITH PASSWORD 'your_super_secret_password';
ALTER ROLE <database user> SET client_encoding TO 'utf8';
ALTER ROLE <database user> SET default_transaction_isolation TO 'read committed';
ALTER ROLE <database user> SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE <database name> TO '<database user>';
```

* Sycn your code with database:
```
- python manage.py makemigrations
- python manage.py migrate
```

* Create superuser
```
- python manage.py createsuperuser
```
* Finally, run project with command: `python3 manage.py runserver`


postman collection: https://hackernewsclone.postman.co/workspace/Hacker-news-clone~24e6343f-5da6-46b4-8f2b-efce90346214/overview
