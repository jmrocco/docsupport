import os
import sys
import easygui
from flask import Flask, jsonify
#from builder.backend.wordpress import WpConverter
app = Flask(__name__)
#home screen

kauri_gateway = 'https://api.kauri.io/graphql'

"""
user flow:
1) determine where user is importing content from
2) user chooses and provides information: url, xml file
3) main file logic routes data to appropriate backend builder
"""


@app.route('/')
def entry_point():
    # ask user where they're importing documentation from
    # current choices: medium, mkdocs, wordpress, github (soon)
    return('Home page: go to /link or /file')

@app.route('/link', methods =['GET'])
def retrieve_content():
    # use our backends to retrieve the requested content
    print('Getting your content!')

    # pseudocode

    user_content_origin = request.args.get('origin')

    if user_content_origin  == mkdocs:
        #send to MkDocs backend
        community = Community

    elif user_content_origin == wordpress:
        #send to Wordpress backend

    elif user_content_origin == medium:
        #send to Medium backend

    else:
        print('error retrieving your documentation')
        # more sophisticated error handling here later

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
