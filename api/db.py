#psql --host=localhost --port=5432 --username=hello_user --dbname=hello-world
# import 

conn = psycopg2.connect(
    host="localhost",
    database="hello-world",
    user="hello_user",
    port="5432",
    password="1")

