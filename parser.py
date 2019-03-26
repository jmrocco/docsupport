#!/usr/bin/python3
# -*- coding: utf8 -*-
import re
from urllib.parse import urlparse, unquote
import requests
from bs4 import BeautifulSoup

from model import User, Post, Publication, Tag, Image, OutputFormat, to_dict
from constant import ROOT_URL, HTML_PARSER



def parse_post_detail(post_url, token):
    print(post_url)
    # driver = webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME)
    # for json format, just return medium json response
    # driver.get(post_url)
    r = requests.get(post_url)
    if r.ok:
        # content_elements = driver.find_element_by_class_name("postArticle-content")
        inner_html = BeautifulSoup(r.text, HTML_PARSER).find("div", {"class": "postArticle-content"})
        content_tags = inner_html.find_all()
        response = ""
        for i in range(0, len(content_tags)):
            tag = content_tags[i]
            md = to_markdown(tag, token)
            if md is not None and md and md is not 'None':
                response += md + "\n"
        print(response)
        return response
