# InfSecProject

#setup

To setup the project you need first to install python 3. Add the python folder and the folder python/scripts to the PATH variable in Windows. 
Then make sure that python is correctly installed by executing the python command in cmd or powershell. In case the windows store is opened follow this guide: 
https://stackoverflow.com/questions/58754860/cmd-opens-window-store-when-i-type-python

You also need to download postgresql and a management tool for it like pgAdmin4. Install both programs and when asked for a password during the postgres install, you 
can either choose your own password and then change every occurance of the password "Kubsti4146" in the file databasemanagement.py to your password. Otherwise you can 
just enter "Kubsti4146" as your password. Leave as port the standard port or change it in the file to 5432. Run the command 
pg_ctl.exe restart -D "<postgredirectory>\data" in the bin file in your postgresql installation folder.

Then you need to start pgAdmin and add a connection to the postgreserver and create the database "secureforum" for the stable branch and "testforum" for the master
branch. Execute the sql query specified in the forum.sql file.

After having installed python and the database server, execute the command pip3 install flask. Repeat the same for argon2-cffi, flask-wtf, psycopg2. 
If other packages are missing, the  program will tell you so by creating an error message and just download the packages needed.

After having installed everything, go to the InfSecProject directory and execute the command py run.py for the stable branch and flask run in the env folder for 
the master branch. Connect to 127.0.0.1:5000 in your browser and now you can have fun with the website;)
