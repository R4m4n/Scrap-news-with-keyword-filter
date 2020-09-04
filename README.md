# RSS Parser For News Websites With Keyword Filters

This code will fetch the news headings from the news websites for the specific set of keywords defined by the user.

## Setup the virtual environment:

<p>To install virtualenv run:</p>
<code>pip install virtualenv</code>
<br><br>

<p>Set up virtualenv for that project by running:</p>
<code>virtualenv venv</code>
<br><br>
<p>This command creates a venv/ directory in your project where all dependencies are installed. You need to activate it first though (in every terminal instance where you are working on your project):</p>

<code>source venv/bin/activate</code>
<br><br>
<br><br>
<p>You should see a (venv) appear at the beginning of your terminal prompt indicating that you are working inside the virtualenv.<br><br> Now you can install all packages by running:</p>

<code>pip install -r requirements.txt</code>

<br /><br />
<h3>Running the app</h3>
<p>Then run app using:</p>
<code>python app.py</code>
<br><br>

## Database Configurations:
 - Change the Database configurations in the config.py file.
<br>
 - Import the newsparser.sql file in the database created.
<br>
 - Add keywords in the topics table in the database with comma separated values.
<br><br><br>

## Websites used to fetch data from:
<br>

### The Straits Times (https://www.straitstimes.com/)

### Channel NewsAsia (https://www.channelnewsasia.com/)

### Today (https://www.todayonline.com/)

### Mothership (https://mothership.sg/)

### The Online Citizen (https://www.theonlinecitizen.com/)

### The Independent Singapore (http://theindependent.sg/)

### The Guardian (https://www.theguardian.com/uk-news)

### The New York Times (https://www.nytimes.com/)

### South China Morning Post (english) https://www.scmp.com/)

