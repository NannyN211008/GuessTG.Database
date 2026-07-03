# GTGDB – Secure Progressive Web Application

Overview of the Project

GTGDB (Guess The Game Database) is a Progressive Web Application (PWA) that I developed as part of my Year 12 HSC Software Engineering assessment. The purpose of this project was to design and build a secure web application that allows users to record and manage their daily GuessThe.Game results in a database.

The application was originally provided as an insecure web application. Throughout this project, I analysed the system, identified security vulnerabilities using both Static Application Security Testing (SAST) and Dynamic Application Security Testing (DAST), and then implemented secure coding solutions to protect the application against common web attacks.

The project was developed using Python with the Flask framework, SQLite for the database, and HTML, CSS and JavaScript for the user interface. Progressive Web App features such as a service worker and web app manifest were also included so the application can be installed and used similarly to a native application.

The completed application allows users to:

Register a new account.
Log in securely.
Submit their GuessThe.Game results.
View previous guesses submitted by all users.
Store information permanently within a SQLite database.
Use the application as an installable Progressive Web App.

# Project Requirements

At the beginning of the project, I identified a set of functional and non-functional requirements to guide development.

Functional requirements included:

- users must be able to register and log in
- users must be able to submit guesses
- data must be stored in a database permanently
- users must be able to view past results
- system must restrict access to logged-in users only

Non-functional requirements were also important, especially around performance and usability:

- the system should load quickly on most devices
- the interface should be simple and easy to navigate
- data security must be maintained through password hashing
- the application should work offline where possible (PWA feature)

I also had some constraints, such as:

- limited time for development
- using only SQLite instead of a full-scale database server
- keeping the system lightweight so it can run on school devices

# System Design

The system follows a client-server architecture, where the frontend interacts with the backend through Flask routes. The backend then communicates with the SQLite database to retrieve or store information.

The structure of the system is split into:

- Frontend (client side): HTML templates, CSS styling, JavaScript interactions
- Backend (server side): Flask routes, session handling, logic processing
- Database layer: SQLite tables storing users and guesses

This separation helped keep the project organised and made debugging easier since each part of the system had a clear purpose.

# Database Design

SQLite was selected because it is lightweight, easy to configure and integrates well with Flask applications.

The database contains two tables.

Users
ID (Primary Key)
Username
Password Hash
Guesses
ID (Primary Key)
Date
Game
Score
User ID (Foreign Key)

The relationship between these tables ensures that every submitted guess belongs to a registered user. This reduces duplicated information while maintaining database integrity.

# Key Features of this project

The application contains several features that improve both functionality and security.

These include:

. Secure user registration.
. Secure login and logout.
. Password hashing using Werkzeug.
. Strong password validation.
. Password confirmation during registration.
. Secure session management.
. Protected application routes.
. Guess submission form.
. Homepage displaying all guesses.
. Automatic ordering of guesses from newest to oldest.
. Progressive Web App installation support.

# Security Implementation of this project

Throughout development I used both Static Application Security Testing (SAST) and Dynamic Application Security Testing (DAST).

SAST involved reviewing the application's source code to identify insecure coding practices before execution. This included analysing authentication logic, password handling, session management and database interactions.

DAST involved testing the running application by entering both valid and invalid data into forms to confirm that vulnerabilities could no longer be exploited after secure coding improvements had been implemented.

Every vulnerability was retested after being fixed to ensure that the application continued functioning correctly and that no additional vulnerabilities had been introduced.

# Development Process of this project

The application was developed gradually rather than attempting to build everything at once.

The overall development process included:

. planning the project requirements
. creating the Flask application
. designing the SQLite database
. implementing authentication
. creating database functionality
. developing the user interface
. implementing Progressive Web App features
. identifying vulnerabilities
. implementing secure coding improvements
. testing every security fix
. documenting the development process using Git and a DevOps journal

Using Git throughout development allowed every improvement to be tracked through commits and version history.

# Technologies Used in this Project
The technologies used throughout this project include:

. Python . Flask . SQLite . HTML5 . CSS3 . JavaScript . Git . GitHub . Visual Studio Code . Werkzeug Security Library


# Project Testing and Evaluation

Testing was done throughout development rather than only at the end. Each feature was tested individually before being combined into the full system.

Some issues I encountered included:

- database connection errors when querying tables
- incorrect SQL joins causing missing usernames
- login sessions not persisting correctly
- form data not being inserted properly

These were fixed through debugging and reviewing both backend logic and SQL queries. Testing helped ensure that the final system was stable and functional.

# Implementation of PWA

To improve the application beyond a normal website, I added Progressive Web App functionality.

This included:

- a manifest file that defines the app name, icons and display settings
- a service worker that caches files for offline use
- installable app behaviour on supported devices

This means users can install the application on their phone or computer and use it like a native app. It also improves performance because cached resources load faster.

# Project Conclusion

Overall, GuessTG.Database is a fully functional database-driven web application that demonstrates a range of software engineering concepts including authentication, database design, client-server architecture and PWA development.

Through building this project, I gained a better understanding of how real-world applications are structured and how different technologies work together. I also improved my skills in debugging, database management and full-stack development.

The final system successfully meets its requirements and provides a simple but effective way for users to track their GuessThe.Game results over time.


