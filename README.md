# Docsupport Web API: Wordpress & Medium to Markdown Converter

While working at ConsenSys for team Kauri, I created a Wordpress to Markdown Converter. Users submit either an .xml Wordpress file or a link to their Wordpress site.The Wordpress script extracts articles/posts and converts them into a readable Markdown format which is the preferred format for https://kauri.io/.

Working on top of the pre-existing Medium to Markdown converter, I added Wordpress support and created a simple frontend user interface.

## Languages & Frameworks

I used the following languages and frameworks In this project:

    -Python
    -Javascript
    -HTML
    -CSS
    -React
    -Gatsby.js
    -Flask
    
## Usuage 
 
The docsupport API is configured to work with the https://kauri.io/ documentation website. It features a fully fledged frontend user interface that allows the user to select the articles they wish to import. 
 
**Note: All private tokens and API links have been removed from the program and thus while interaction with the frontend is possible, it will not sync or process any requests to https://kauri.io/**

## Components

Backend : Within the ```medium``` folder appropriate medium to markdown scripts can be found. ```wordpress``` houses the wordpress to markdown scripts. The specific file is in: wordpress/builder/backend/wordpress.py  This script will convert any .xml file into markdown.

Frontend: All frontend code is located within the ```src``` folder.
 
 ## To Run
 
```
git clone https://github.com/jmrocco/docsupport.git
 
cd docsupport
 
npm install -g gatsby-cli

gatsby develop

python main.py
```
**Note: gatsby develop starts the app and python main.py runs the wordpress and medium converter scripts**
