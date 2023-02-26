<h2>The Application for testing</h2>
I chose my own web application called WatchFest as the application to test. It is a web application that serves as a blog aimed at presenting articles on series and movies. The user can register, which gives him/her certain privileges that a non-logged-in user does not have. A non-logged-in user can only read the articles, read something about the author, log in or register. A logged-in user can add articles, delete them, or edit them. They can also change their login details or delete their account if they no longer wish to be a registered user. 

<h2>Starting the test application</h2>
The application is not published, it runs at a local address. It needs to be downloaded from the repository : https://github.com/ErikUrban28/VAII . You need to have Docker installed to run the application. In the WatchFest/docker folder, there is a docker-compose.yml , which creates a Docker container called vaiicko_fw. This needs to be run. The database from the WatchFest/docker/sql folder, the db.sql file, must then be imported. The page can then be accessed by typing 'localhost' into the browser.

<h2>Starting the tests</h2>
The recommended way to run test cases is via the pytest library, which has a user-friendly way of outputting to the console. Simply type the following into the command line: 'pytest Scripts/' , without the quotes.	
Scripts can also be run via the command 'python $cesta_k_suboru.py$ , without the $.

<h2>Testing Evaluation</h2>
If the pytest library is used to execute , the tests are started one at a time and the result of each test is printed continuously. A '.' indicates a successfully passed test and an 'F' indicates a failed test. Also, the percentages are displayed on the right side, where reaching [100%] indicates the end of the execution of the automatic tests.
