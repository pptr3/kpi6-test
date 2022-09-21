To run the project, you need to habe Flask and Flask-mysqldb installed. 

`pip install flask`

`pip install flask-mysqldb`

Then, you need to have also MySql installed. Go on MySql website and install it depending on your operating system. During the installation, you will be asked to set a password. You have to set `root` as a password to be able to run the project.

Run MySql server using the commmand:

`mysql -u root -p`

Then, to create the database, step in in the folder `kpi6-test` and run: create database rip; 
`mysql -u root -p
 create database rip;
source dp.sql`

Now we can run the flask application. Open a new terminal and go into the folder `kpi6-test` again and run:

`python app.py`

then the server starts. To see this amazing application, open a browser and type:

`localhost:5000`

Cheers.



