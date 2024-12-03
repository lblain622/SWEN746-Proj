First you need to create a new db.yml file inside the folder config which is inside the root
It should contain something like this:

host: localhost
database: databasename
user: postgrestuser
password: postgrespassword
port: 5432

To run requirements:  pip install -r requirements.txt
To run the project: python src/server.py
To run the tests: python -m unittest -v
