
# Text Summarizer Web App

Welcome to the Text Summarizer web app project! This repository houses the code for a Flask-based web application designed for text summarization using the T5 transformer model. Below is an overview of the project and instructions on how to use and run the application.
### Input
![Screenshot 2024-01-28 at 1 13 46 PM](https://github.com/ananyamanjunath/Text-Summarizer/assets/109954683/1de18e26-811d-4df0-b0fc-057abb602414)
### Output (English)
![Screenshot 2024-01-28 at 1 13 38 PM](https://github.com/ananyamanjunath/Text-Summarizer/assets/109954683/89e7a444-ac25-4ea7-9f4a-c75cd0ef483f)
### Input
![Screenshot 2024-01-28 at 1 13 54 PM](https://github.com/ananyamanjunath/Text-Summarizer/assets/109954683/a7df899c-d442-4e40-ae18-659651ca4fea)
### Output (Hindi)
![Screenshot 2024-01-28 at 1 14 07 PM](https://github.com/ananyamanjunath/Text-Summarizer/assets/109954683/a7cf9ee8-3239-41b1-ac4f-25593a206adf)

## Overview

The main file, `app.py`, serves as the core of the web application, integrating Flask, the T5 transformer model, and the Google Translate API. Users can input text and choose the language for summarization, receiving concise summaries in their preferred language. The project also includes HTML templates for the main and result pages, along with a CSS file for styling.

## Installation

To run the web app, ensure you have the required dependencies installed. You can install them using the following command:

```bash
pip install Flask transformers googletrans
```

## Usage

1.  Clone this repository:

```bash
git clone https://github.com/ananyamanjunath/Text-Summarizer.git
cd Text-Summarizer

```

2.  Run the Flask application:

```bash
python app.py
```

3.  Open your web browser and go to http://localhost:5000/ to access the Text Summarizer web app.
    
4.  Choose the language for summarization, enter your text in the provided text area, submit the form, and view the summarization result.
    

## Acknowledgments

This web app leverages Flask for web development, the T5 transformer model for text summarization, and the Google Translate API for language translation. Feel free to explore and customize the code to suit your requirements.

Please note that the web app is currently set to run in debug mode. Ensure that it meets your security and deployment standards before deploying it in a production environment.
