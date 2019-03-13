import pprint
import tomd
from bs4 import BeautifulSoup

class WpConverter():

    def __init__(s,path):
        s.path = path
        s.create_file = s.createFile()
        s.find_contents = s.findContents()
        s.empty_contents = s.emptyContents()
        s.to_markdown = s.toMarkdown()

    def createFile(s):
        file = open(s.path,"r")
        content = file.read()
        global soup
        soup = BeautifulSoup(content,features = "xml")
        global my_list
        my_list = []


    def emptyContents(s):
        count = 0
        while(count!= len(my_list)):
            if(my_list[count]['content'] == ' '):
                del my_list[count]
            elif(my_list[count]['content'] == ''):
                del my_list[count]
            else:
                count += 1

    def findContents(s):
        temp_title = soup.find('title')
        title = temp_title
        temp_link = soup.find('link')
        link = temp_link
        temp_date = soup.find('pubDate')
        date = temp_date
        temp_author = soup.find('dc:creator')
        author = temp_author
        temp_description = soup.find('description')
        description = temp_description
        temp_content = soup.find('content:encoded')
        content = temp_content
        num_of_articles = len(soup.find_all('title'))

        x = 1
        for x in range(num_of_articles - 1):
            title = title.findNext('title')
            link = link.findNext('link')
            date = date.findNext('pubDate')
            description = description.findNext('description')
            my_list.append({'title': title.get_text(), 'link': link.get_text(), 'date': date.get_text(), 'author':
                            author.get_text(), 'description': description.get_text(), 'content': content.get_text()})
            content = content.findNext('content:encoded')
            author = author.findNext('dc:creator')

    def toMarkdown(s):
        for y in range(len(my_list)):
            my_list[y]['content'] = my_list[y]['content'].replace('</li>','</li>\n')
            my_list[y]['content']= tomd.convert(my_list[y]['content'])

        s.emptyContents()
        print(type(my_list))
        return my_list
    #    s.__repr__()
        #s.__str__()

    #def __repr__(s):
     #  return(str(my_list))

    #def __str__(s):
        #return(my_list)
