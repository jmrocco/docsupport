import os
import sys
import json
from flask import Flask, jsonify,request
from builder.backend.wordpress import WpConverter
app = Flask(__name__)
import pprint
#home screen

kauri_gateway = 'https://api.kauri.io/graphql'

"""
user flow:
1) determine where user is importing content from
2) user chooses and provides information: url, xml file
3) main file logic routes data to appropriate backend builder

the way we did this in the importer was using flask's request.args.get() module
see link: http://flask.pocoo.org/docs/1.0/reqcontext/
"""


@app.route('/')
def entry_point():
    # ask user where they're importing documentation from
    # current choices: medium, mkdocs, wordpress, github (soon)
    return('Home page: go to /link')

@app.route('/link', methods =['GET', 'POST'])
def retrieve_content():
    # use our backends to retrieve the requested content
    print('Getting your content!')

    # pseudocode

    if request.args.get('mkdocs_repo_url'):
        #send to MkDocs backend, and then return our article_list
        url = request.args.get('mkdocs_repo_url')
        #
        # community = Community(url)
        # builder = Builder(url)
        #
        # mk_article_list = MkDocsBuilder(
        #     builder.proj_dir,
        #     builder.docs_dir,
        #     builder.repo_url,
        # )

        return mk_article_list

    elif request.args.get('wordpress_xml_file'):

        path = request.args.get('wordpress_xml_file')
        filename,file_extension = os.path.splitext(path)

        if (file_extension == ".xml"):
            #send the path to wordpress WpConverter
            wp_article_list = WpConverter(path)
            # change to a string
            wp_string = str(wp_article_list)
            # convert to a list/json object
            wp_json_object = json.loads(wp_string)
            #print one of the article contents
            print(wp_json_object[2]['content'])
            #pprint.pprint(wp_json_object)

        else:
            return ('Not a wordpress file.')



    elif request.args.get('medium_url'):
        #send to Medium backend
        return medium_article_list

    else:
        print('error retrieving your documentation')
        # more sophisticated error handling here later

    return('Getting your documents!')

if __name__ == '__main__':
    app.run(debug=True)

## problems: I can't import the WpConverter to use in this file
## ModuleNotFoundError: No module named 'builder'
