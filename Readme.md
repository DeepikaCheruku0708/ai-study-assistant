# AI Study Assistant

## Overview

AI Study Assistant is a Generative AI-based web application developed using Python, Streamlit, and Google's Gemini API. The application helps students quickly generate study notes, key points, and interview questions for any topic.

This project was built as a learning project to understand Python programming, Prompt Engineering, API integration, and GitHub project management.

---

## Features

* Generate study notes for any topic
* Get simplified explanations for beginners
* Generate important key points
* Generate interview questions
* User-friendly web interface
* Powered by Google's Gemini AI model

---

## Technologies Used

* Python
* Streamlit
* Google Gemini API
* python-dotenv
* Git
* GitHub

---

## Project Structure

AI-Study-Assistant/

├── app.py

├── README.md

├── requirements.txt

├── .gitignore

└── .env (local only, not uploaded to GitHub)

---

## Installation

### Clone the Repository

git clone https://github.com/DeepikaCheruku0708/ai-study-assistant.git


### Navigate to Project Folder

cd ai-study-assistant


### Install Required Packages


pip install -r requirements.txt


---

## Environment Setup

Create a `.env` file in the project folder.

Add your Gemini API key:

GEMINI_API_KEY=YOUR_API_KEY_HERE


Note: Do not upload the `.env` file to GitHub.


## Run the Application

streamlit run app.py


The application will open in your browser at:

http://localhost:8501


## How It Works

1. User enters a topic.
2. A prompt is generated dynamically.
3. Gemini AI processes the prompt.
4. The application displays:

   * Explanation
   * Key Points
   * Interview Questions


## Learning Outcomes

Through this project, I learned:

* Python basics
* Streamlit web application development
* API integration
* Prompt Engineering
* Environment variable management
* Git and GitHub workflows
* Building AI-powered applications

---



## Author

Deepika Cheruku

---

## Disclaimer

This project is developed for educational and learning purposes. API keys and sensitive credentials are excluded from the repository using `.gitignore`.
