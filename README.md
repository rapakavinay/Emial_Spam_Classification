Spam Email Detection Application



Overview

This Spam Email Detection Application is designed to classify emails as spam or not spam using a machine learning model based on the Multinomial Naive Bayes algorithm. The project is divided into two parts: a desktop application built with Tkinter and a web application developed using Streamlit.


Installation
Prerequisites
Before running this application, ensure you have Python installed on your machine along with the following Python libraries:

pandas
numpy
scikit-learn
pickle
tkinter
win32com (for text-to-speech)
streamlit (for the web application)

File Structure
spam.csv: The dataset containing the spam and ham messages.
spam.pkl: The trained Multinomial Naive Bayes model.
vectorizer.pkl: The CountVectorizer object used for text processing.
app.py: The Python script for the Tkinter application.
streamlit_app.py: The Python script for the Streamlit web application.


Usage
Running the Tkinter Application
To run the Tkinter-based desktop application, execute the app.py script:

python app.py

This will open a GUI where you can input text messages to classify them as spam or not spam.


Running the Streamlit Web Application
To run the web application, execute the streamlit_app.py script:

streamlit run streamlit_app.py
Navigate to the local URL provided by Streamlit (usually http://localhost:8501) to access the web interface.


How It Works
The application uses a pre-trained Multinomial Naive Bayes model to classify messages. The text data is vectorized using a CountVectorizer to convert text data into a format that the machine learning model can process.

Tkinter Application: Allows the user to input a message via a GUI, classifies the message, and uses text-to-speech to announce the result.
Streamlit Application: Provides a web interface where users can enter messages, submit them, and view the classification results directly on the webpage along with text-to-speech output.






