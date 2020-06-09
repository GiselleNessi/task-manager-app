import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster-naitp.mongodb.net/task_manager?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_task')
def get_task():
    return render_template('task.html', task=mongo.db.tasks.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'), port=os.environ.get('PORT', 5000), debug=True)

