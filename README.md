# Overview of the System

GuessTG.Database is a database-driven Progressive Web Application (PWA) designed to allow users to record, store, and view GuessThe.Game results in a structured and interactive way. The system demonstrates core software engineering concepts including authentication, database management, client-server communication, routing, and offline capability through PWA technology.

The application is built using a modern web stack consisting of:

- Flask (Python) – backend web framework handling routing and logic
- SQLite – lightweight relational database for persistent data storage
- HTML/CSS/JavaScript – frontend structure, styling, and interactivity
- Service Workers + Manifest File – enabling Progressive Web App functionality

The system is designed to simulate a real-world web application where users can securely log in, submit data, and interact with dynamically updated content.

Purpose of the Application

The main purpose of GuessTG.Database is to provide a centralised platform for tracking game guesses and results, allowing users to:

- Record individual game attempts (guesses)
- Store results in a structured database
- View all previous guesses in a ranked or time-ordered format
- Authenticate users before accessing or modifying data
- Experience a mobile-friendly, installable web application (PWA)
