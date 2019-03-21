import logging
import requests
import json
from configparser import ConfigParser

class syncToKauri():
    global parser
    # reads from the config file
    parser = ConfigParser()
    parser.read('config.ini')

    def __init__(s,article):
        s.article = article
        s.printArticle = s.printArticle()
        s.importer = s.importer()

    def printArticle(s):
        global wp_json_object
        global wp_content
        #converts to a usable format
        wp_string = s.__str__(s.article)
        wp_json_object = json.loads(wp_string)

    def importer(s):
        # grabs token, gateway, and header
        token = parser.get('information','jwt')
        gateway = parser.get('information','gateway')
        headers = {"Content-Type": "application/json"}
        headers['X-Auth-Token'] = 'Bearer %s' % token

        #creates the article
        newArticle = {
            "query" : "mutation submitNewArticle($title: String, $description: String, $content: String, $attributes: Map_String_StringScalar) { submitNewArticle (title: $title, description: $description, content: $content, attributes: $attributes) {hash} }",
            "variables" : {
                "title": wp_json_object['title'],
                "content" : json.dumps({'markdown': wp_json_object['content']}),
                "attributes" : {
                    "origin_name" : "wordpress",
                    "origin_url" : wp_json_object['link'],
                },

            },
            "operationName" : "submitNewArticle"
            }
        #sends the article
        p = requests.post(gateway, headers = headers, data = json.dumps(newArticle))

    # makes sure the string is in the proper format
    def __str__(s,string):
        string = json.dumps(string)
        return string

    # makes sure the string is in the proper format
    def __repr__(s,string):
        string = json.dumps(string)
        return string
