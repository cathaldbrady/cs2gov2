
Getting started:

1) download python (v.3.6.3)
 - make sure python is added to your path

2) open command prompt and run:
 - pip install -r requirements.txt
 - This will install all packages related to the application.


To run the project:

1) Open command prompt

2) Go to directory with app.py script 

3) run -> python app.py

4) Open browser and enter http://127.0.0.1:8080/ OR the local host URL given in the terminal after the project is ran if it differs from this one.  

5) Done

*The mlab and gmail credentials used to setup database if you wish to use the same account again*

mlab login username: cs2go
mlab login password: projectpassword123
Database username: cs2gouser
Database password: userpw312

gmail: cs2goproject@gmail.com
gmail password: projectpassword123
***********************************************************

*Hidden URL for admin account creation*
http://127.0.0.1:8080/teachers/create_admin

*Secret Key required for admin creation*
some_super_secret_text_here


Explaination of the file structure of the project: 

App.py is the main python file for the project. App.py is the file you want to run in order to launch cs2go.

The project has been broken up into smaller sub folders. The folders cover different areas of CS2Go. Example folders are students, teachers, forums.

ALL code both front and backend relating to "students" will be found in the students folder. ALL code both front and backed relating to the teacher discussion forum will be found in the forum folder etc.The same logic applies for all folders.

Within each folder there is a templates folder, views.py file and a forms.py file. 

Housed in the templates folder is all HTML files that are related to that folder for example in the students->templates folder, HTML files such as student-create.html, student-profile.html etc will be found. 

The views.py file holds all the python functions (routes) that are related to that folder. 

For example in the students->views.py file you will find python functions responsibily for the creation of new student accounts, functions for approving or disapproving students from joining a class, function responsible for displaying the student homepage etc.

The forms.py file holds all the WTForms python classes that were developed for each form in cs2go. Taking students folder as example again, all WTForms python classes for forms in relation to students will be found in students->forms.py. StudentForm class for new student account form, StudentPersonalQs for the personal student quiz etc.

The files that are uploaded to cs2go are stored in the uploads folder, the machine that is hosting cs2go will also act as the server for holding the files that are uploaded to CS2Go. File details are stored in the MongoDB database but the files themselves are not.

The Models.py file contains all the MongoEngine models developed for the entire application.

Static file contains all CSS, JS files and images that are used throughout the project.