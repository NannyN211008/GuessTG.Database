# Overview of the System

GuessTG.Database is a Progressive Web Application I developed to allow users to store and track their GuessThe.Game results in a structured database system. The main idea behind the project was to create something that goes beyond a basic website and instead functions like a real-world application with login systems, data storage, and offline capabilities.

The application uses Python (Flask) for the backend, SQLite for the database, and HTML/CSS/JavaScript for the frontend. It also includes PWA features such as a service worker and manifest file so it can be installed like a mobile app.

The system allows users to:

- create an account
- log in securely
- submit game guesses/results
- view previous submissions
- track performance over time

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






