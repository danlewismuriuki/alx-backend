# Flask Application with Localization

## Overview

This project demonstrates how to build a Flask web application that supports multiple languages using Flask-Babel. The application can infer the correct locale based on various factors and localizes timestamps according to the user's locale.

## Learning Objectives

By working through this project, you will learn:

1. **How to Parametrize Flask Templates to Display Different Languages**
   - Understand how to use Flask-Babel to internationalize and localize Flask templates.
   - Learn how to create language-specific content and switch between languages dynamically.
   - Gain experience in configuring Flask-Babel to handle multiple languages in a web application.

2. **How to Infer the Correct Locale**
   - Learn how to detect and set the correct locale for the user based on URL parameters, user settings, or HTTP request headers.
   - Understand the role of the `localeselector` function in determining the user's preferred language.

3. **How to Localize Timestamps**
   - Learn how to format and display dates and times according to the user's locale.
   - Understand the importance of timezone handling in a multilingual application.
   - Explore how to use Flask-Babel and Python’s `pytz` library to ensure accurate and localized time representations.

## Project Structure

- **3-app.py**: The main Flask application file where localization is implemented.
- **templates/3-index.html**: The HTML template for rendering the index page in different languages.
- **requirements.txt**: Lists all Python dependencies required to run the application.

## How to Run the Project

1. **Set Up the Virtual Environment**:
   ```bash
   python3 -m venv env
   source env/bin/activate

