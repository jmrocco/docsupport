import pprint
import tomd
import json
from bs4 import BeautifulSoup

class WpConverter():

    def __init__(s,path):
        s.path = path
        s.create_file = s.createFile()
        s.find_contents = s.findContents()
        s.empty_contents = s.emptyContents()
        s.to_markdown = s.toMarkdown()

    # take file and create soup object
    def createFile(s):
        file = open(s.path,"r")
        content = file.read()
        global soup
        soup = BeautifulSoup(content,features = "xml")
        global my_list
        my_list = []

    #clear blank articles from list
    def emptyContents(s):
        count = 0
        while(count!= len(my_list)):
            if(my_list[count]['content'] == ' '):
                del my_list[count]
            elif(my_list[count]['content'] == ''):
                del my_list[count]
            else:
                count += 1

    #find content in xml file
    def findContents(s):

        """
        -finds the first element of each
        -we don't need the first element since
        it is associated with web details
        """

        temp_title = soup.find('title')
        title = temp_title
        temp_link = soup.find('link')
        link = temp_link
        temp_date = soup.find('pubDate')
        date = temp_date
        temp_author = soup.find('dc:creator')
        author = temp_author
        temp_content = soup.find('content:encoded')
        content = temp_content

        #number of articles/content found
        num_of_articles = len(soup.find_all('title'))

        """
        -finds the next item in the xml file and
        appends the list
        -content and author are after the append because
        they appear less times than the rest and this
        prevents errors
        """

        x = 1
        for x in range(num_of_articles - 1):
            title = title.findNext('title')
            link = link.findNext('link')
            date = date.findNext('pubDate')
            my_list.append({'title': title.get_text(), 'link': link.get_text(), 'date': date.get_text(), 'author':
                            author.get_text(), 'content': content.get_text()})
            content = content.findNext('content:encoded')
            author = author.findNext('dc:creator')

    # converts to markdown
    def toMarkdown(s):
        for y in range(len(my_list)):
            #makes sure every list item is on a new line
            my_list[y]['content'] = my_list[y]['content'].replace('</li>','</li>\n')
            my_list[y]['content']= tomd.convert(my_list[y]['content'])

        # double checks that empty articles are removed from list
        s.emptyContents()

    #onverts to proper string format
    def __str__(s):
        string = json.dumps(my_list)
        return string

    #converts to proper string format 
    def __repr__(s):
        string = json.dumps(my_list)
        return string
