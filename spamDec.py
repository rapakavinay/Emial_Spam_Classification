import streamlit as st
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from win32com.client import Dispatch

# Load the trained model and CountVectorizer from pickle
model = pickle.load(open('spam.pkl', 'rb'))
cv = pickle.load(open('vectorizer.pkl', 'rb'))  # Make sure to create and save this in your standard app if not yet done

# Define a function to use the computer's speech capabilities
def speak(text):
    speaker = Dispatch("SAPI.SpVoice")
    speaker.Speak(text)

def main():
    st.title("Email Spam Classification Application")
    st.write("Built with Streamlit & Python")
    activities = ["Classification", "About"]
    choice = st.sidebar.selectbox("Select Activities", activities)
    if choice == "Classification":
        st.subheader("Classification")
        msg = st.text_input("Enter a text")
        if st.button("Process"):
            data = [msg]
            vec = cv.transform(data).toarray()
            result = model.predict(vec)
            if result[0] == 0:
                st.success("This is Not A Spam Email")
                speak("This is Not A Spam Email")
            else:
                st.error("This is A Spam Email")
                speak("This is A Spam Email")

if __name__ == '__main__':
    main()
