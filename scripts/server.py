#import dependencies

from flask import Flask, Blueprint, render_template, request

server = Blueprint('index', __name__)

step = 0


#function that will render the boring page
@server.route('/boring')
def boring():
    return render_template('Boring.html')

#function that goes back with 1 step for animation and music
@server.route('/back')
def back():
    global step
    step -= 1
    return render_template('creative.html', musicVariable = f'{step}', animationVariable= f'{step}')

#function that goes infornt with 1 step for animation and music
@server.route('/next')
def next():
    return render_template('creative.html', musicVariable = f'{step}', animationVariable = f'{step}')


#main function that will return the main HTML page
@server.route('/')
def index():
    return render_template('index.html')