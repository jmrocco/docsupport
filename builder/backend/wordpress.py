import pprint
import tomd
import json
import re
from bs4 import BeautifulSoup
from configparser import ConfigParser
from file_handler import IpfsHandler



class WpConverter():
    global parser
    # reads from the config file
    parser = ConfigParser()
    parser.read('config.ini')

    def __init__(s,path):
        s.path = path
        s.create_file = s.createFile()
        s.find_contents = s.findContents()
        s.empty_contents = s.emptyContents()
        s.format_contents = s.format()
        s.htmlParse_contents = s.htmlParse()
        s.to_markdown = s.toMarkdown()

    # open file and create soup object
    def createFile(s):
        global soup
        global my_list
        my_list = []

        file = open(s.path,"r",encoding = "utf8")
        content = file.read()
        soup = BeautifulSoup(content,features = "xml")

    def htmlParse(s):
        for q in range(len(my_list)):
            my_list[q]['content'] = my_list[q]['content'].replace('<br>', '')
            my_list[q]['content'] = my_list[q]['content'].replace(' </em>','</em>')
            my_list[q]['content'] = my_list[q]['content'].replace('<strong> ','<strong>')
            my_list[q]['content'] = my_list[q]['content'].replace(' </strong>','</strong>')


    #delete blank articles from list
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
            my_list.append({'title': title.get_text(), 'link': link.get_text(),'content': content.get_text()})
            content = content.findNext('content:encoded')

    # corrects format of lists and images before converting to markdown
    def format(s):
        for y in range(len(my_list)):
            #searches for the captions and singles them out
            pattern = re.compile(r'<figcaption>[a-z:,/.\-_? =&%0-9A-Z]*<\/figcaption>')
            caption = pattern.findall(my_list[y]['content'])

            #corrects caption and image tags
            for t in range(len(caption)):
                my_list[y]['content'] = my_list[y]['content'].replace(caption[t], '')
                caption[t] = caption[t].replace('<figcaption>', '')
                caption[t] = caption[t].replace('</figcaption>', '')
                #adds the caption to the end of the image
                my_list[y]['content'] = my_list[y]['content'].replace('/></figure>','></img>' + caption[t] + '</p>')

            #replaces image end tag and list tags
            my_list[y]['content'] = my_list[y]['content'].replace('/></figure>','></img></p>')
            my_list[y]['content'] = my_list[y]['content'].replace('<img','<p><img')
            my_list[y]['content'] = my_list[y]['content'].replace('</li>','</li>\n')




    # converts to markdown
    def toMarkdown(s):

        for z in range(len(my_list)):
            print(my_list[0]['content'])
            my_list[z]['content']= tomd.convert(my_list[z]['content'])
            print(z)
        # double checks that empty articles are removed from list
        s.emptyContents()
        s.ipfs_search()


    #takes links of images and adds them to kauri ipfs
    def ipfs_search(s):
        token = parser.get('information','jwt')
        for q in range(len(my_list)):
                # searches for the image
                pattern = re.compile(r'\!\[\]\([a-z:,/.\-_?=&%0-9A-Z]*\)')
                src = pattern.findall(my_list[q]['content'])
                #removes tags and creates a string of just the link
                for r in range(len(src)):
                    # gets rid of brackets to find the link
                    src[r]=src[r].replace('![]', '')
                    src[r]=src[r].replace('(', '')
                    src[r]=src[r].replace(')','')
                    #sends it to the ipfs handler to upload
                    ipfs = IpfsHandler(src[r],token)
                    ipfs_link = ipfs.ipfs_url
                    #replaces the link with the new ipfs link
                    my_list[q]['content']= my_list[q]['content'].replace(src[r],ipfs_link)


    #converts to proper string format
    def __str__(s):
        string = json.dumps(my_list)
        return string

    #converts to proper string format
    def __repr__(s):
        string = json.dumps(my_list)
        return string
