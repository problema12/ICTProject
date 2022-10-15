#this is the main file of the project

# firstly we import the flask library and the create_app function 
from flask import Flask, render_template
from scripts import create_app

#we are going to create the flask app
app = Flask(__name__)

#we are going to create the blueprint of the app
app = create_app()

#we are going to start the flask server with the specified host and port and we are going to set the debug boolean as True
if __name__ == '__main__':
    app.run(host='192.168.1.207', port=5000, debug=True)