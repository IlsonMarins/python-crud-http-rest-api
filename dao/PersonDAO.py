from flask_restful import Resource
import logging as logger
from Connection import Connection

class PersonDAO(Resource):

    def get(self, taskId):
        logger.debug(" * inside get method of TaskById")
        return {"message": "inside get method of TaskById. Task ID = {}".format(taskId)}, 200

    def post(self, taskId):
        logger.debug(" * inside post method")
        return {"message": "inside post method of TaskById. Task ID = {}".format(taskId)}, 200
    
    def put(self, taskId):
        logger.debug(" * inside put method")


        conn = None
        try:
            conn = Connection.getConnection()
            # create a cursor
            cur = conn.cursor()
            
            # execute a statement
            print('PostgreSQL database version:')
            cur.execute('INSERT INTO hello.person ("name", birth_dt) VALUES('', '')')

            # display the PostgreSQL database server version
            db_version = cur.fetchone()
            print(db_version)
            
            # close the communication with the PostgreSQL
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print('Database connection closed.')


        #return {"message": "inside put method of TaskById. Task ID = {}".format(taskId)}, 200
    
    def delete(self, taskId):
        logger.debug(" * inside delete method")
        return {"message": "inside delete method of TaskById. Task ID = {}".format(taskId)}, 200