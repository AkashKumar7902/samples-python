from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS
import collections.abc
import middleware

app = Flask(__name__)
app.wsgi_app = middleware.CoverageMiddleware(app.wsgi_app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['studentsdb']
students_collection = db['students']    

@app.route('/joke', methods=['GET']) 
def get_joke():
    joke = {"joke": "Why did the tomato turn red? Because it saw the salad dressing!"}
    return jsonify(joke)

@app.route('/students', methods=['GET'])
def get_students():
    students = list(students_collection.find({}, {'_id': 0}))
    return jsonify(students)

@app.route('/students/<student_id>', methods=['GET'])
def get_student(student_id):
    student = students_collection.find_one({'student_id': student_id}, {'_id': 0})
    return jsonify(student)

@app.route('/students', methods=['POST'])
def create_student():
    new_student = request.json
    students_collection.insert_one(new_student)
    return jsonify({'message': 'Student created successfully'})

@app.route('/students/<student_id>', methods=['PUT'])
def update_student(student_id):
    updated_student = request.json
    students_collection.update_one({'student_id': student_id}, {'$set': updated_student})
    return jsonify({'message': 'Student updated successfully'})

@app.route('/students/<student_id>', methods=['DELETE'])
def delete_student(student_id):
    students_collection.delete_one({'student_id': student_id})
    return jsonify({'message': 'Student deleted successfully'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000, debug=False)
