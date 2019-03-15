import os
import sys
import easygui
from flask import Flask, jsonify
#from builder.backend.wordpress import WpConverter
app = Flask(__name__)
#home screen
@app.route('/')
def home_screen():
    return('Home page: go to /link or /file')

#if you have a link
@app.route('/link', methods =['GET'])
def get_link():
    return('Getting your documents!')

#if you have a file
@app.route('/file', methods =['GET'])
def get_file():
    #opens file and determines extension
    path = easygui.fileopenbox()
    fn,fe = os.path.splitext(path)
    #xml file
    if (fe == ".xml"):
        return('You have an xml file!')
    #other file
    else:
        return ('Document not supported yet.')

if __name__ == '__main__':
    app.run(debug=True)

## problems: I can't import the WpConverter to use in this file
## ModuleNotFoundError: No module named 'builder'
