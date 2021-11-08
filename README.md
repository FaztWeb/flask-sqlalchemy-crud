## Flask SQLAlchemy CRUD

this project is a CRUD application using flask and mysql using SQLAlchemy

### Installation with docker-compose

```
git clone https://github.com/FaztWeb/flask-sqlalchemy-crud
cd flask-sqlalchemy-crud
docker-compose up
```

### Manual Installation

##### Requirements

* Python3
* Mysql

before run the app you must create the following environnment variables:

```
MYSQL_USER=
MYSQL_PASSWORD=
MYSQL_DATABASE=
MYSQL_HOST=
MYSQL_PORT=
```

```
git clone https://github.com/FaztWeb/flask-sqlalchemy-crud
cd flask-sqlalchemy-crud
pip install -r requirements.txt
python index.py
```
