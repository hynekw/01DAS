# Link to final presentation

https://docs.google.com/presentation/d/13RU0OLRF9Snh1sXFqnJ6UbEsItsiuAtU2b1oVJt_7eA/edit#slide=id.g29e5d65a1c6_0_84


# Possible lecture outline

This covers a bit more than was showcased during the lecture.

## Introduction (5 minutes)
- Why it's important to know how to deploy simple web app to display model results.
    - (story about stakeholders not understanding value until they see it)
    - experience with need to build internal app ~once a year as a demo or annotation tool..

## Overview of the Project (5 minutes)
- Present an overview of the app (simple QA chatbot with knowledge base).
    - App provides simple text input with button to ask a question.
    - In response the app displays the answer from LLM and ability to ask new question.
    - No chat history or ability to ask follow up questions.
- Introduce the technologies and tools we'll be using (Flask, Bootstrap, Huggingface transformers lib)

## Setting Up the Development Environment (5 minutes)
- Walk through the installation of necessary tools and libraries and creating requirements.txt file
- Demonstrate how to create a virtual environment for the project.
    ```sh
    which python
    python --version
    python -m venv .venv
    pip install flask
    pip install sentence-transformers
    pip freeze > requirements.txt
    ```

## Understanding the architecture (5 minutes)
- Outline architecture: FE, BE, DB, Model.
- MVC model - why it's useful.

## Building the Backend (10 minutes)
- Show how to create a Flask web application.
    - https://flask.palletsprojects.com/en/3.0.x/quickstart/#a-minimal-application
- Implement a simple API endpoint to receive user input.

## Integrating the Model with the Web App (5 minutes)
- Create a route for receiving user input and returning predictions.
- Update the Flask app to incorporate the machine learning model to answer question.
- Provide model with most similar documents from the knowledge base.

## Using OpenAI API instead (5 minutes)
- Show a way to get response from OpenAI API instead of using local model.
- Handle basic issues with exceptions and time outs.

## Building the Frontend (10 minutes)
- Introduce the concept of the frontend and its role in web development.
- Create a basic HTML form for user input.
- Handle form submission and display predictions.

## Testing and Debugging (5 minutes)
- Emphasize the importance of testing the web app thoroughly. Showcase debug mode.
- Show how to test the app's functionality and handle common issues.

## Discuss Streamlit as alternative (5 minutes)
- Explore how it could be implemented there as an alternative.
