import os
import sys
import json
import logging
from flask import Flask, jsonify,request
from builder.backend.wordpress import WpConverter
from sync import syncToKauri

#TODO: Implement other article types

#create the flask app
app = Flask(__name__)
kauri_gateway = 'https://api.kauri.io/graphql'

"""
user flow:
1) determine where user is importing content from
2) user chooses and provides information: url, xml file
3) main file logic routes data to appropriate backend builder

the way we did this in the importer was using flask's request.args.get() module
see link: http://flask.pocoo.org/docs/1.0/reqcontext/
"""

#home screen
@app.route('/')
def entry_point():
    # ask user where they're importing documentation from
    # current choices: medium, mkdocs, wordpress, github (soon)
    return('Home page: go to /link')

#choice screen
@app.route('/link', methods =['GET', 'POST'])
def retrieve_content():
    # use our backends to retrieve the requested content
    print('Getting your content!')

    #mkdocs approach
    if request.args.get('mkdocs_repo_url'):
        #send to MkDocs backend, and then return our article_list
        url = request.args.get('mkdocs_repo_url')

        # community = Community(url)
        # builder = Builder(url)
        #
        # mk_article_list = MkDocsBuilder(
        #      builder.proj_dir,
        #      builder.docs_dir,
        #      builder.repo_url,
        #  )

        return mk_article_list

    # wordpress approach
    elif request.args.get('wordpress_xml_file'):
        # checks path to see if it's an xml file
        path = request.args.get('wordpress_xml_file')
        filename,file_extension = os.path.splitext(path)


        if (file_extension == ".xml"):
            # convert the file, change to a string and put it
            # in json object form to send
            wp_article_list = WpConverter(path)
            wp_string = str(wp_article_list)
            wp_json_object = json.loads(wp_string)

            #individually send the articles to sync
            # for x in range(len(wp_json_object)):
            #     object = wp_json_object[x]
            #     syncToKauri(object)

        #recognized that it is not a wordpress supported file
        else:
            return ('Not a wordpress file.')


    #medium approach
    elif request.args.get('medium_url'):
        #send to Medium backend
        return medium_article_list

    else:
        # more sophisticated error handling here later
        print('Error retrieving your documentation.')

    #displays success message on the screen
    return('Getting your documents!')

#allows for debugging
if __name__ == '__main__':
    app.run(debug=True)
