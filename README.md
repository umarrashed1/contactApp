Note: All the steps are to be followed on a windows machine

step 1: install MySql 
step 2: Import the database 'contactsdb' into MySql:
        a. start the MySql shell and create a new database using the following command:
           create database contactsdb;
        b. run the following command from the command line to create a new databse:
           mysql -u username -p contactsdb < contactsdb.sql
        c. Type the root password
step 3: install python 3
step 4: install virtualenv using the following command
        pip install virtualenv
step 5: Navigate to the project folder and create a virtual environment using the following command:
        virtualenv env
step 6: activate the virtual environment using the following command:
        env\Scripts\activate
step 5: install all the requirements in requirements.txt using the following command:
        pip install -r requirements.txt
step 7: run the command python start.py from the project folder 
step 8: open a brower and goto http://localhost:5000/ to access the webapp
step 9: You can create a new user use the following credentials as email and password
        email: s@gmail.com
        password: qwerty