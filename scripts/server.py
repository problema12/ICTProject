#import dependencies

from flask import Flask, Blueprint, render_template

server = Blueprint('index', __name__)


@server.route('/boring/', methods=['POST'])
def boring():
    return render_template('Boring.html')

@server.route('/')
def index():
    return render_template('index.html')