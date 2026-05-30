# Overview of the System

For my Software Engineering project, I developed a database-driven Progressive Web Application (PWA) called GuessTG.Database. The purpose of this application is to allow users to record, store and view their GuessThe.Game results through a secure and easy-to-use online platform. Throughout the development of this project, I applied a range of software engineering concepts including database design, authentication, web development, user interface design, security practices and Progressive Web Application technologies.

The project was designed to simulate a real-world web application where multiple users can create accounts, log in securely and contribute data that is permanently stored within a database. Rather than simply creating a static website, I wanted to develop a dynamic application that could process user input, communicate with a database and provide personalised functionality depending on whether a user was logged in or not.

This project demonstrates how modern web applications combine frontend technologies such as HTML, CSS and JavaScript with backend technologies such as Python Flask and SQLite to create a complete software solution.

# Purpose of this Project

The main purpose of GuessTG.Database is to provide a centralised system where users can record and track their GuessThe.Game performance over time. Before developing this application, there was no simple way for users to store their game results in a structured format. Results were often forgotten, stored in screenshots or written down manually.

To solve this problem, I developed a system that allows users to:

- Create an account
- Log into the application
- Submit their GuessThe.Game results
- View previous submissions
- Track performance history
- Access the application through a web browser or installed PWA

The project was also created to demonstrate my understanding of full-stack web development and database integration

# Technologies used for this project

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
