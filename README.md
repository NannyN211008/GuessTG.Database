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

The database was one of the most important parts of the system. I used SQLite because it is simple to set up and works well with Flask.

The database contains two main tables:

Users table:

- user_id (primary key)
- username
- password_hash

Guesses table:

- guess_id (primary key)
- game_name
- score
- date
- user_id (foreign key)

The relationship between these tables is important because each guess is linked to a specific user. This avoids duplication of data and ensures that the system stays organised.

# Key Features of this project

The system includes several major features that make it functional and secure.

User authentication is required before accessing most pages. When a user logs in, a session is created which keeps them signed in while navigating the site. Routes are protected so users cannot bypass login by directly entering URLs.

Another major feature is the guess submission system. Users can enter their game results through a form, which is then sent to the backend and stored in the database.

Other features include:

- dynamic homepage that updates automatically with new guesses
- display of usernames alongside each result
- ordering results from newest to oldest
- responsive design for different screen sizes
- PWA installability

# Security Implementation of this project

Security was an important focus during development. Instead of storing passwords in plain text, I used password hashing through Werkzeug. This means passwords are converted into encrypted strings before being stored.

The login process works by:

1. user enters username and password
2. system retrieves stored hash from database
3. entered password is compared to hash
4. access is granted only if they match

In addition, session management is used to ensure only logged-in users can access restricted routes. This prevents unauthorised access even if someone tries to manually type in URLs.

# Development Process of this project

The project was developed in stages rather than all at once. I started with basic routing in Flask, then added database functionality, followed by user authentication, and finally PWA features.

A rough development order was:

- setting up Flask project structure
- creating SQLite database and tables
- building login and authentication system
- creating homepage and guess submission system
- improving UI and styling
- adding PWA features (manifest + service worker)
- testing and debugging

This step-by-step approach made it easier to identify errors early and avoid major system breakdowns.

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


