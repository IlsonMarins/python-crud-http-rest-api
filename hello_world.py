from flask import Flask, json

companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]

api = Flask(__name__)
#restServer.add_resource(TaskById, "/api/v1.0/task/id/<string:taskId>")
#Request: PUT /hello/<username> { “dateOfBirth”: “YYYY-MM-DD” }
#Response: 204 No Content

@api.route('/hello', methods=['PUT'])
def get_companies():
  return json.dumps(companies)

if __name__ == '__main__':
    api.run()