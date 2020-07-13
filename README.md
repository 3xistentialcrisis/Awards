# Award Us
## Author  
  
>[Wanjiku Karanja](https://github.com/3xistentialcrisis)  
  
# Description  
This a django application which allows a user to post a project he/she has created and get it reviewed by his/her peers. 
  
##  Live Link  
 Click [View Site](https://awardus.herokuapp.com/)  to visit the site
  
## Screenshots 
###### Home page
 
<img src="https://raw.githubusercontent.com/3xistentialcrisis/Awards/master/static/images/home.png" width="900px" height="440px">
 
###### Sign Up
 <img src="https://raw.githubusercontent.com/3xistentialcrisis/Awards/master/static/images/signup.png" width="900px" height="440px">

###### Login
 <img src="https://raw.githubusercontent.com/3xistentialcrisis/Awards/master/static/images/login.png" width="900px" height="440px">

###### Login
 <img src="https://raw.githubusercontent.com/3xistentialcrisis/Awards/master/static/images/upload.png" width="900px" height="440px">

## User Story  
This app enables user to:

* View posted projects and their details
* Post a project to be rated/reviewed
* Rate/ review other users' projects
* Search for projects 
* View projects overall score
* View my profile page

  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
 https://github.com/3xistentialcrisis/Awards/.git 
```
##### Navigate into the folder and install requirements  
 ```bash 
cd Awards pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
python3 -m venv virtual 
```  
```bash 
source virtual/bin/activate 
```

##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrations 
 ```bash 
python manage.py makemigrations awards
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python3 manage.py runserver 
``` 

##### Testing the application  
 ```bash 
 python3 manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
## API Endpoints
*  https://awardus.herokuapp.com/api/users/
*  https://awardus.herokuapp.com/api/profile/
*  https://awardus.herokuapp.com/api/posts/

## Technology used  
  
* [Python 3.8](https://www.python.org/)  
* [Django 1.11.17](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
* [Postgres](https://www.postgresql.org/)
* [Pip](https://pypi.org/project/pip/)
* Html and CSS (Bootstrap)
  
## Known Bugs  
There are no known bugs at the time of deployment of this application 
  
## CodeBeat
[![codebeat badge](https://codebeat.co/badges/61881488-2da3-4522-be01-0226f8d1a6c6)](https://codebeat.co/projects/github-com-3xistentialcrisis-awards-master) 

## License 
[![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](https://github.com/3xistentialcrisis/awards/blob/master/LICENSE)

## Contact Information   
If you have any question or contributions, please email the administrator at [administrator@awardsus.com] 
