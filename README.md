<div align="center">
<img src="https://github.com/tdignan87/traceVMS/blob/master/static/img/TSLogo.jpg" target="_blank" rel=""/>
</div>
<div align="center">
<h1>TraceVMS Visitor & Contractor Management System</h1>
</div>

## Introduction

TraceVMS was created by myself as I noticed through my day job that most factories and food companies use paper based systems for recording visitors to the site.
I can see the headache of paper based systems from working in the manufacturing industry for over 10 years. TraceVMS hopes to help with that problem by recording visitor and contractor information to help with record keeping, reduce paperwork and adhere to food safety compliance(BRC).

Tracesense is my own company i created in November 2019 and decided to go with that name for the software although its purely created for educational purposes.

## Table of Contents
1. [UX](#ux)
    - [Project Goals](#project-goals)
    - [User Goals](#user-goals)
    - [Business Goals](#business-goals)
    - [Developer Goals](#developer-goals)
    - [User Requirements & Expectations](#customer-stories)
        - [Design Choices](#design-choices)
    - [WireFrames](#wireframes)
    - [Flow Chart](#flowchart)
    

2. [Features](#features)
    - [Existing Features](#existing-features)
    - [Features Left To Implement](#features-left-to-implement)


3. [Information Architecture](#information-architecture)
    - [Database choice](#database-choice)
    - [Data Storage Types](#data-storage-types)
    - [Collections Data Structure](#collections-data-structure)
   

4. [Technologies Used](#technologies-used)

5. [Testing](#testing)

6. [Deployment](#deployment)
    - [Heroku Deployment](#heroku-deployment)
    - [How to run this project locally](#how-to-run-this-project-locally)

7. [Credits](#credits)
    - [Content](#content)
    - [Acknowledgements](#acknowledgements)

8. [Contact](#contact)

9. [Disclamer](#disclamer)
  

----

# UX

## Project Goals

The goal of this project is to create a suitable, easy to use application for recording visitors and contractors to your site. The software is aimed at food manufacturers specifically designed to help them be compliant with contractor management and also health and safety requirements. The system's focus will be ease of use for data input and data retrieve.

## User Goals
User goals are:

- Have a system for recording visitors to my site so i can remove paperwork records.

- Have confidence in the system so it keeps us compliant with food safety requirements.

- Ease of use and can be used across any device.

- Secure so data is compliant with GDPR.

- Functionality to add new questions to ask visitors and contractors as legislation changes.

## Business Goals

The target businesses to use this application are:

- Bakeries
- Food & drink manufacturers

Business user goals are:

- A well thought out, designed, user friendly platform that will benefit customers who need compliance.

- A user interface that allows me to input the data efficiently.

- Value for money (site is for a project, but eventually i will use this as part of my new business). I want the software to exceed requirements for the user as word of mouth spreads fast
in the food industry in scotland.

## Developer Goals

Developer goals are:

- Provide an effective, easy to use site for customers to add new visitors to there premises, ensure they have completed the compliance checks and data stored in the database correctly.

- I can learn more about frontend and backend technologies together for the first time.

- This is currently a student project although the future goal of traceVMS is to eventually sell it to manufacturers to use on there sites. This will come later when my experience in development gets better.

## User Requirements & Expectations

### Customer Stories

As a customer to traceVMS i expect/want/need:

1. To easily navigate across the application, the layout needs to make sense so i'm not put off from using the system and just stick to paper.

2. The information presented needs to be in a practical way for me to digest and follow easily. I need to be able to use the app quickly and efficiently as contractors may not have a lot of time at the customers site.

3. I need to have sufficient confidence in the system so i can remove paperwork from my processes. The system needs to tick the box for storing the data, and for us to retrieve it if we get audited from the BRC or Health and Safety executive. 

4.To use the administrator set up panel to be able to filter out on who is approved, not approved contractor and any other key information required.

5.I want to be able to search for users who have completed the site induction.

6. I want to be able to search for a list of everyone who is currently on site in case this needs to be printed in used in a fire evacuation emergency. I need to be able to print the list from the browser of the names of people on site. 

7. I want to be able to access data easily and within the 4 hour maximum BRC timeframe for retrieving company audit data.

### Developer Stories

As the developer and owner of traceVMS i expect/want:

1. To be able to create, delete, update, and read information to the database.

2. Allow customers to find the application easy to use.

3. The software helps and improves compliance.

4. For secure login to the administrator panel to amend the lists.

5. The data is secure and complies with GDPR for the customer.

6. The system is reliable for use and gives confidence the customer can remove the paperwork.


## Design Choices

traceVMS application has a professional feel that doesnt look too over complicated for the user. The following design choices were made:

### Fonts

* The google font applied across the whole application was 'lato' with a fall back of sans-serif. Lato feels very modest and text sizes look great either large or small. The font is easily recognizable.


### Colours

* The colors for this project were choosen based on the two primary colours in my company logo. These colours are

1. Dark Blue: CMYK 100,50,10,0; RGB 0,105,68; HEX #0069A8
2.Light Blue: CMYK 65,0,10,0; RGB 66,191,224; HEX #42BFE0

The Dark Blue #0069A8 was used for button controls and blended well with etiher the lighter blue background or the white background depending where it was placed. The light blue was my jumbotron's background colior and background colour for the menu choices option. 

I feel the colours i have chosen have complimented eachother well and blend well with the company logo.

## Wireframes

These wireframes were created using [Balsamiq](https://balsamiq.com/) during the scope part of the design and planning process for this project. I found Balsamiq very useful for helping me plan out exactly what i needed for my application to come together.

To go to the main wireframes page please click [this](https://github.com/tdignan87/traceVMS/tree/master/Wireframes) link.


- [Browser Home Page](https://github.com/tdignan87/traceVMS/blob/master/Wireframes/Browser%20Home%20Page.png)
- [Browser Visitor Sign In Page](https://github.com/tdignan87/traceVMS/blob/master/Wireframes/Browser%20Visitor%20Sign%20In.png)
- [Browser Visitor Sign Out Page](https://github.com/tdignan87/traceVMS/blob/master/Wireframes/Browser%20Visitor%20Sign%20Out%20Page.png)
- [Browser Administrator Set Up Page](https://github.com/tdignan87/traceVMS/blob/master/Wireframes/Browser%20Administrator%20Set%20Up.png)
- [Browser Add New Company Page](https://github.com/tdignan87/traceVMS/blob/master/Wireframes/Browser%20Add%20New%20Company.png)
- [Browser Edit Company Page](https://github.com/tdignan87/traceVMS/blob/master/Wireframes/Browser%20Edit%20Company.png)
- [Browser Delete Company Page](https://github.com/tdignan87/traceVMS/blob/master/Wireframes/Delete%20Company.png)
- [Browser Add Questions Page](https://github.com/tdignan87/traceVMS/blob/master/Wireframes/Browser%20Add%20New%20Question.png)
- [Browser Edit Questions Page](https://github.com/tdignan87/traceVMS/blob/master/Wireframes/Browser%20Edit%20Question.png)
- [Browser Delete Questions Page](https://github.com/tdignan87/traceVMS/blob/master/Wireframes/Browser%20Delete%20Questions.png)
- [Mobile Home Page](https://github.com/tdignan87/traceVMS/blob/master/Wireframes/Mobile%20Home%20Page.png)
- [Mobile Visitor Sign In Page](https://github.com/tdignan87/traceVMS/blob/master/Wireframes/Mobile%20Visitor%20Sign%20In%20Page.png)
- [Mobile Visitor Sign Out Page](https://github.com/tdignan87/traceVMS/blob/master/Wireframes/Mobile%20Visitor%20Sign%20Out%20Page.png)
- [Mobile Admin Set Up Page](https://github.com/tdignan87/traceVMS/blob/master/Wireframes/Mobile%20Admin%20Set%20Up.png)
- [Mobile Visitor Edit Page](https://github.com/tdignan87/traceVMS/blob/master/Wireframes/Mobile%20Visitor%20Edit%20Page.png)
- [Mobile Visitor Delete Page](https://github.com/tdignan87/traceVMS/blob/master/Wireframes/Mobile%20Visitor%20Delete%20Page.png)
- [Mobile Company Add New](https://github.com/tdignan87/traceVMS/blob/master/Wireframes/Mobile%20Company%20Add%20New.png)
- [Mobile Company Edit](https://github.com/tdignan87/traceVMS/blob/master/Wireframes/Mobile%20Company%20Edit.png)
- [Mobile Company Delete](https://github.com/tdignan87/traceVMS/blob/master/Wireframes/Mobile%20Company%20Delete.png)
- [Mobile Questions Add New](https://github.com/tdignan87/traceVMS/blob/master/Wireframes/Mobile%20Questions%20Add%20New.png)
- [Mobile Questions Edit](https://github.com/tdignan87/traceVMS/blob/master/Wireframes/Mobile%20Questions%20Edit.png)
- [Mobile Questions Delete](https://github.com/tdignan87/traceVMS/blob/master/Wireframes/Mobile%20Question%20Delete.png)
- [Tablet Home Page](https://github.com/tdignan87/traceVMS/blob/master/Wireframes/Tablet%20Home%20Page.png)
- [Tablet Visitor Sign In Page](https://github.com/tdignan87/traceVMS/blob/master/Wireframes/Tablet%20Visitor%20Sign%20In.png)
- [Tablet Visitor Sign Out Page](https://github.com/tdignan87/traceVMS/blob/master/Wireframes/Tablet%20Visitor%20Sign%20Out.png)
- [Tablet Administrator Page](https://github.com/tdignan87/traceVMS/blob/master/Wireframes/Tablet%20Administrator%20Page.png)
- [Tablet Add New Company Page](https://github.com/tdignan87/traceVMS/blob/master/Wireframes/Tablet%20Add%20New%20Company.png)
- [Tablet Edit Company Page](https://github.com/tdignan87/traceVMS/blob/master/Wireframes/Tablet%20Edit%20Company.png)
- [Tablet Delete Company Page](https://github.com/tdignan87/traceVMS/blob/master/Wireframes/Tablet%20Delete%20Company.png)
- [Tablet Add New Visitor Page](https://github.com/tdignan87/traceVMS/blob/master/Wireframes/Tablet%20Add%20New%20Visitor.png)
- [Tablet Edit Visitor Page](https://github.com/tdignan87/traceVMS/blob/master/Wireframes/Tablet%20Edit%20Visitor.png)
- [Tablet Delete Page](https://github.com/tdignan87/traceVMS/blob/master/Wireframes/Tablet%20Delete%20Visitor.png)

## Wireframe design changes

Throughout the design process i decided to move the logo from the top right and allocate the navbar across all pages. This made design quicker and easier.

## Flow Chart

This flowchart was created on Microsoft Powerpoint to explain the flow of how the application should run.<br>
User flowchart:
<img src="https://github.com/tdignan87/traceVMS/blob/master/Wireframes/flowchart/user-flowchart.png" target="_blank" rel=""/>


Administrator options:
<img src="https://github.com/tdignan87/traceVMS/blob/master/Wireframes/flowchart/admin_options.jpg" target="_blank" rel=""/>

# Features

## Existing Features

### Features on every page:

- Navbar
    - The navigation bar features the TraceSense logo in the top left corner.
    - For users using the app there is a list of navbar options available regardless of the page loaded. These are:
    1. Home
    2. Admin Panel
    3. Dashboard


### Features on main page:
 The navbar is collapsed into a burger icon on smaller displays.  The navbar is not fixed to the top of the page as the user scrolls as space is important, particularly when users are signing in as there could be lots of questions set up in the system.

### Features on sign in page for visitors:
A user can select if they are entering the bakery and if so the page will expand with questions which have been set up in the Administrator page. User answers the questions and must acknlowedge that they have read them before signing it. Once the checkbox is checked then the user can sign into the site.

The page will only display in the companies list companies which are on the approved list. Any company which is rejected will not appear on the list.

### Features for sign out page:
Sign out page will display a dropdown of visitors currently on site (not signed out). User selects there name and then signs out via the button. Simple form, simple design. Bootstrap buttons used for updating or returning to the previous page.


### Administrator page ( requires authentication via login form)
Administrator page uses bootstrap buttons for menu options and is very easy to navigate around. Administrator page allows users to add new questions, edit, delete, add new companies, edit, delete and edit or delete visitors. 


### Dashboard
Dashboard will display what users are currently on site. The dashboard can be accessed by anyone and does not need admin credentials.

## Features Left to Implement

1. Email Authentication
- Allow administrator to create another administration account if they want to allocate more than one account.

2. Email Notifications
- Once visitor selects who they are on site to visit then an email should be sent to that individual notifying them that a visitor is at reception with the details entered in the app.

3. Notifications
- Ability to add to contractors table fields for renewal dates for certificates and email a dedicated account when the certificates have been expired. If this is done then the administrator can change the contractor to rejected if the expiry date is elapsed.

4. Inductions
- Ability to ask the visitor if they have completed a site induction prior to entering. If they press no, then the system will complete the induction there and then. Once completed then the visitor signs this off along with there company representative on the app and this is updated in the database. A date is stored for a year/ or an appropriate time for renewal and the app will prompt when this is due.

5. Reports functionality
- Option for a reports section in the navbar where a user can go to access specific data such as the number of visitors in the last 30 days as an example. Reports can be fixed with parameters to enter for the report to query the data. 

6. Fire Register
- The app should allow a list of current users on site to quickly generate for printing in the event of site requiring a list for the fire register in the event of an evacuation.

7. Badge Printing
- It would be a good "nice to have" if once a visitor is signed into site then the app can connect to a printer and print a visitors badge.

8. Image capturing
- The ability to capture a image of the visitor via the device camera and store this into the database.

9. Answer Questions
- Once database is changed to SQL, set the ability to allow answers for questions to be strict or not. IF they are strict, then if selected they will not permit a user to access site. A report should be available showing the users details along with the questions and relevant answers.

10. Timer for dashboard
- Add a timer to the dashboard so the page automatically refreshes with the database queries and updates with the latest content. This will be useful for companies who would want to keep the dashboard on display(large TV in reception) as an example.

11. Dashboard information
- More information to display what companies are not approved, total number of visitors on site, number of visitors for the week etc.

# Information Architecture

### Database Choice

A SQL database structure i think would have been more suitable for this project however the requirements were to use mongoDB. I have experience with Firebird, and SQL server already so i'm looking forward to learning more about MongoDB and gain some experience with it.

To have easy access to relational data, inner objects were used inside the data structure so that they could be accessed and looped through for combo boxes and where else required.

### Data Storage Types

The types of data stored in MongoDB for this project are:
- ObjectId
- String
- Boolean
- DateTime


### Collections Data Structure

TraceVMS relies on the following structure

#### Administrator login

| Title | Key in db | form validation type | Data type |
--- | --- | --- | --- 
admin_id | _id | None | ObjectId 
Name | username | text | string
Password | password | text | string
role | role | text | string

#### Visitors On Site

|Title | Key in db| form validation type| data type |
--- | --- | --- | ---
visitorsID | _id | none | ObjectId
Name | name | text| string
Company | company | text | string
Visiting | visiting | text |string
entered_bakery| entered_Bakery| boolean | bool
sign_in_timestamp|sign_in_timestamp| timestamp |timestamp

#### Contractors

|Title| Key in db | form validation type | data type |
--- | --- | --- | ---
contractorID | _id | none | ObjectId
Name| Name| text|string 
Address | Address| text | string
Approved| isApproved| checkbox | boolean

#### Questions

|Title| Key in db| form validation type| data type |
--- | --- | --- | ---
questionID | _id| none | Objectid
Question| question | text | string
Answer_First | Answer_First| text | string
Answer_Second | Answer_Second| text | string

# Technologies Used

### Tools

- [Visual Studio Code](https://code.visualstudio.com/) is the IDE used for developing this project. 
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) is the database for this project
- [GitHub](https://github.com/) to store and share all project code remotely. 
- [Balsamiq](https://balsamiq.com/) used to create the wireframes for my project.

### Libraries

- [JQuery](https://jquery.com) to simplify DOM manipulation.
- [Bootstrap](https://www.bootstrapcdn.com/) to simplify the structure of the website and make the website responsive easily.
- [PyMongo](https://api.mongodb.com/python/current/) to make communication between Python and MongoDB possible.
- [Flask](https://flask.palletsprojects.com/en/1.0.x/) to construct and render pages.
- [Jinja](http://jinja.pocoo.org/docs/2.10/) to simplify displaying data from the backend of this project smoothly and effectively in html.
- [Google Fonts](https://fonts.google.com/) to style the website fonts.

### Languages
The project uses HTML,CSS, Javascript and python programming languages.

# Testing

1. Automatic testing was not done for this project.
2. HTML,CSS,Javascript and Python was validated using online vaidators. These were:

-[W3C Markup Validation Service](https://validator.w3.org/) for HTML and CSS
-[Esprima JS Syntax Validator](https://esprima.org/demo/validate.html) for Javascript
-[PEP8 Online](http://pep8online.com/) for python code

No issues were found apart from HTML validator flagging errors for the use of Jina in the HTML file.

Any features added were tested after implementation for this project. Any bugs that were identified were fixed during development. 


# Deployment

## How to run this project locally

To run this project on your own IDE follow the instructions below:

Ensure you have the following tools: 
- An IDE such as [Visual Studio Code](https://code.visualstudio.com/)

The following **must be installed** on your machine:
- [PIP](https://pip.pypa.io/en/stable/installing/)
- [Python 3](https://www.python.org/downloads/)
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)
- An account at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) or MongoDB running locally on your machine. 
    - How to set up your Mongo Atlas account [here](https://docs.atlas.mongodb.com/).

### Instructions
1. Save a copy of the github repository located at https://github.com/tdignan87/traceVMS by clicking the "download zip" button at the top of the page and extracting the zip file to your chosen folder. If you have Git installed on your system, you can clone the repository with the following command.
```
git clone https://github.com/tdignan87/traceVMS

2. If possible open a terminal session in the unzip folder or cd to the correct location.

3. A virtual environment is recommended for the Python interpreter, I recommend using Pythons built in virtual environment. Enter the command:
```
python -m .venv venv
```  
_NOTE: Your Python command may differ, such as python3 or py_

4. Activate the .venv with the command:
```
.venv\Scripts\activate 
```
_Again this **command may differ depending on your operating system**, please check the [Python Documentation on virtual environments](https://docs.python.org/3/library/venv.html) for further instructions._

4. If needed, Upgrade pip locally with
```
pip install --upgrade pip.
```

5. Install all required modules with the command 
```
pip -r requirements.txt.
```

6. In your local IDE create a file called `.flaskenv`.

7. Inside the .flaskenv file, create a SECRET_KEY variable and a MONGO_URI to link to your own database. Please make sure to call your database `vms`, with 4 collections called `av_questions`, `contractors`, `users` and `visitors`. 

8. You can now run the application with the command
```
python app.py
```

9. You can visit the website at `http://127.0.0.1:5000

```
## Heroku Deployment

To deploy traceVMS to heroku, take the following steps:

1. Create a `requirements.txt` file using the terminal command `pip freeze > requirements.txt`.

2. Create a `Procfile` with the terminal command `echo web: python app.py > Procfile`.

3. `git add` and `git commit` the new requirements and Procfile and then `git push` the project to GitHub.

3. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the "New" button in your dashboard. Give it a name and set the region to Europe.

4. From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.

5. Confirm the linking of the heroku app to the correct GitHub repository.

6. In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

7. Set the following config vars:

| Key | Value |
 --- | ---
DEBUG | FALSE
IP | 0.0.0.0
MONGO_URI | `mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority`
PORT | 5000
SECRET_KEY | `<your_secret_key>`

- To get you MONGO_URI read the MongoDB Atlas documentation [here](https://docs.atlas.mongodb.com/)

8. In the heroku dashboard, click "Deploy".

9. In the "Manual Deployment" section of this page, made sure the master branch is selected and then click "Deploy Branch".

10. The site is now successfully deployed.

# Credits

### Content

The sub main logo was sourced at:
 - [securly](https://www.securly.com/visitor)

 The company main logo i had developed by Tom Holmes an independent graphics designer:

- [Tom Holmes](http://www.tom-holmes.co.uk/?LMCL=zjuU4x)

 All of the content on the page was written by me with reference to BRC standard Food_8_Interpretation_English. This was provided to be my Ewelina Kwitek the Quality Manager at Paterson Arran.
- [BRC](https://www.brc.org.uk/)

## Acknowledgements

 - Big thanks to my mentor [Simen Daehlin](https://github.com/Eventyret) for his invaluable support as always.
 - Thank you to my fellow student [Cecilia Binck](https://www.linkedin.com/in/cecilia-binck-657b6977/)  for testing my UI and giving pointers and advice.
 - Thank you to [Ewelina Kwitek](https://www.linkedin.com/in/ewelina-kwitek-55950b2b/) for providing me with the BRC standard and giving advice as to what content the project should have to suit users in the food industry.
 
# Contact
To contact me feel free to email me at tdignan87@gmail.com

## Disclamer
The content of this website is for educational purposes only.






