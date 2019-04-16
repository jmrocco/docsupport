import React, { Component } from 'react'
import { navigate } from 'gatsby'
import Layout from '../components/layout'
import styles from './base.module.css'
import { load } from './wordpress-choose-article.js'


export default class IndexPage extends Component {
    constructor(props){
        super(props);
        this.state ={
          getbtn: false,
          fbtn: false,
          file: ''
        };
        this.handleClick = this.handleClick.bind(this);
        this.importFromFileBodyComponent = this.importFromFileBodyComponent.bind(this);

      //if the user clicked the back button to get to this page
      //it will reload to clear the choose article page
      if (load){
        window.location.reload()
      }

    }

    //click event handler
    handleClick = (id) => () => {
      //sets state on the buttons and navigates to the choose article page
        if (id === 'getbtn' && this.state.fbtn === true) {
            this.setState({...this.state, getbtn: true});
            //passes the file to choose article
            navigate("/wordpress-choose-article/", { state: { file: this.state.file }})
        }
        else if (id === 'fbtn') {
            this.setState({fbtn : true});
        }
        else {
            alert('*Error* You need to choose a file first!')
        }
    }

    //converts the raw file into a string/readable content
    importFromFileBodyComponent(file) {
      try{
            let fileReader;

            const handleFileRead = (e) => {
            const content = fileReader.result;
            this.setState({file : content});
            };

            const handleFileChosen = (file) => {
                fileReader = new FileReader();
                fileReader.onloadend = handleFileRead;
                fileReader.readAsText(file);
            }
            handleFileChosen(file);
        }
        catch {
          console.log('cancelled event')
        }
    }


    render() {
        return (
            <Layout>
                <div>
                    <h3>Welcome to the Wordpress-to-Kauri importer!</h3>
                    <p>Select your Wordpress XML file below, and the importer will ask you to choose which articles to import to Kauri.</p>
                    <p>After importing, you'll be redirected to your Kauri profile and can view the articles in the "Drafts" section.</p>
                </div>
                <div>
                    <input onClick={this.handleClick('fbtn')} onChange={e => this.importFromFileBodyComponent(e.target.files[0])} type="file"id="file" accept=".xml"></input>
                    <button onClick={this.handleClick('getbtn')} className={styles.button}>Get Articles</button>
                </div>
                <div id= "guidelines">
                    <h3>Importer Guidelines</h3>
                    <p>Navigate to your Wordpress Site to export your xml file. Choose <strong>Tools -> Export</strong>.
                    Select whether to import <em>All content, posts, or pages.</em> Preferably choose either posts or pages.</p>
                    <p id="note"><strong>Note:</strong>If you've written content in HTML within Wordpress, please make sure tags are properly formatted.</p>
                    <img src = "https://premium.wpmudev.org/blog/wp-content/uploads/2015/08/wordpress-export.png"/>
                </div>
            </Layout>
        );
    }
};
