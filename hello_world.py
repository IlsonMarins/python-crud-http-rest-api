from flask import Flask, jsonify
from dao.Connection import *
import psycopg2

def get_persons(keyword=''):
  conn = None
  try:
    conn = Connection.getConnection()
    # create a cursor
    cur = conn.cursor()    
    # execute a statement
    cur.execute("SELECT name, birth_dt FROM hello.person where name like '%"+keyword+"%'")
    persons = cur.fetchall()
    jsonResult = []
    for person in persons:
        jsonResult.append({
            'Name':person[0],
            'Bithday':person[1]
        })
    return jsonResult
    # close the communication with the PostgreSQL
    cur.close()
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)
  finally:
    if conn is not None:
      conn.close()
      print('Database connection closed.')
from pprint import PrettyPrinter
pp = PrettyPrinter()
pp.pprint(get_persons())

app = Flask(__name__)

@app.route('/')
def pageLoad():
    return jsonify({"Welcome Message " :"Hello there, visit 127.0.0.1:5000/persons"})

@app.route('/hello/<keyword>')
def loadHelloByKeyword(keyword):
    response = get_persons(keyword)
    print(response)
    if len(response) == 0:
        return jsonify({"Error":"Sorry could not find any persons with keyword "+keyword})
    else:
        return jsonify(response)

@app.route('/persons')
def loadAllPersons():
    response = get_persons()
    if len(response) == 0:
        return jsonify({"Error":"Sorry could not find any persons"})
    else:
        return jsonify(response)

@app.route('/persons/<keyword>')
def loadPersonsByKeyword(keyword):
    response = get_persons(keyword)
    print(response)
    if len(response) == 0:
        return jsonify({"Error":"Sorry could not find any persons with keyword "+keyword})
    else:
        return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000,debug=True)