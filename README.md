# Royal_Awards

![RoyalAwards!](/static/img/Screenshot.png)

## Author

[Ian wanarua](https://github.com/Ianwanarua)

## Description

This is a django application where Users are allowed to see projects posted and are able to rate on them, they can also post projects for it to be rated also.

## Live Link

To view the site [Click here.](https://royalawards.herokuapp.com/)

## User Story

* A User can register in the application by feeding in his/her email,username and password.
* A User is able update their profile by adding a profile picture and also their Bio.
* A User can browse projects posted by different Users on the application. 
* User is able to rate on projects posted on the application.
* A user is able to post their projects on the application.

## Prerequisites

For this system to work on your pc you need the following; 

1. Python3.8
2. Django
3. Pip
4. Virtual Environment(virtual)
5. A text editor (Vscode)

## Development Installation

To get the code..

1. Clone the repository:
 `git clone  https://github.com/Ianwanarua/RoyalAwards.git`

2. Move to the folder and install requirements
 ` cd  RoyalAwards`

3. In the projects root directory, install the virtualenv library using pip and create a virtual environment. Run the following commands respectively:
    - **`pip install virtualenv`**
    - **`virtualenv virtual`**
    - **`source virtual/bin/activate`**
        * Note that you can exit the virtual environment by running the command **`deactivate`**
4. Download the all dependencies in the requirements.txt using **`pip install -r requirements.txt`**
5. Launch the application locally by running the command **`python manage.py runserver`** and copying the link given on the termnal on your browser.
    - To post photos, run the command  **`python manage.py createsuperuser`** to create an admin account in order to post. Access to the admin panel is by adding the path /admin to the address bar.

## Technology used

* Python3.8
* Django
* Heroku
* Html
* Css
* Javascript
* Bootstrap4
