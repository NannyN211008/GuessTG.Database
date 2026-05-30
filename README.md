# Overview of the System

GuessTG.Database is a Progressive Web Application I developed to allow users to store and track their GuessThe.Game results in a structured database system. The main idea behind the project was to create something that goes beyond a basic website and instead functions like a real-world application with login systems, data storage, and offline capabilities.

The application uses Python (Flask) for the backend, SQLite for the database, and HTML/CSS/JavaScript for the frontend. It also includes PWA features such as a service worker and manifest file so it can be installed like a mobile app.

The system allows users to:

. create an account
. log in securely
. submit game guesses/results
. view previous submissions
. track performance over time

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

A range of technologies were used throughout the development process.

Python

- Python was selected as the primary programming language because it is relatively easy to learn while still being powerful enough to develop database-driven web applications. Python was used to process user requests, communicate with the database and control the behaviour of the application.

Flask Framework

- The Flask framework was used to simplify web development. Flask provides routing functionality, template rendering and session management which made it suitable for this project.

- Using Flask allowed me to create multiple pages and manage interactions between the user interface and database efficiently.

SQLite Database

- SQLite was chosen because it is lightweight, reliable and does not require a separate database server. This made it ideal for a school software engineering project.

The database stores:

. User account information
. Usernames
. Password hashes
. Guess submissions
. Scores
. Dates of submission

All data remains stored even when the application is closed, demonstrating persistent data storage.

HTML

- HTML was used to create the structure of every page within the application including forms, tables, navigation menus and content sections.

CSS

- CSS was used to improve the visual appearance of the application. Styling was applied to create a clean and professional user interface while ensuring readability and usability.

JavaScript

- JavaScript was used to support interactive functionality and Progressive Web App features.

Progressive Web App Technologies

The application includes:

. Manifest file
. Service worker
. Application icons
. Offline caching
