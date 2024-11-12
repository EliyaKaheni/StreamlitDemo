import streamlit as st
import joblib
import tensorflow as tf
import numpy as np
from PIL import Image

def FashionMNIST():
    model = tf.keras.models.load_model('fashion_mnist_model.keras')

    cloths = {
        0: 'T-shirt/top',
        1: 'Trouser',
        2: 'Pullover',
        3: 'Dress',
        4: 'Coat',
        5: 'Sandal',
        6: 'Shirt',
        7: 'Sneaker',
        8: 'Bag',
        9: 'Ankle boot'
    }

    st.title("Fashion MNIST Model")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert('L')
        image = image.resize((28, 28))  

        st.image(image, width=100)

        image_array = np.array(image) / 255.0 
        image_array = image_array.reshape(1, 28, 28) 

        prediction = model.predict(image_array)
        predicted_label = np.argmax(prediction)

        st.write(f"Predicted label: {cloths[predicted_label]}")

def NLP():
    st.header('Sentiment Analysis')

    model = joblib.load('sentiment_model.joblib')
    
    text = st.text_area('Please enter your text')
    
    if text:  
        ans = model.predict([text])
        
        if ans[0] == 1: 
            st.header('A positive text')
            image = Image.open('positive_feedback.jpg')
            st.image(image=image, width=200)
        else:
            st.header('A negative text')
            image = Image.open('negative_feedback.jpg')
            st.image(image=image, width=200)

st.title('Welcome to our multi-media AI project')
page = ''
if not page:
    st.write('You can select [Vision] or [NLP] project from the sidebar')

page = st.sidebar.selectbox('Page:', options=['NLP', 'Vision'])
if page=='NLP':
    NLP()
else:
    FashionMNIST()