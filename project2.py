import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.title('Iris Flower Type Prediction App')
st.write("""
## Welcome to the Iris Flower Type Prediction App!

This app predicts the **type of Iris flower** based on user inputs.
""")

st.image('https://cdn.pixabay.com/photo/2017/08/30/01/05/milky-way-2695569_960_720.jpg', use_column_width=True)

st.sidebar.header('Enter Your Parameters')

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal Length (cm)', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal Width (cm)', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal Length (cm)', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal Width (cm)', 0.1, 2.5, 0.2)
    data = {
        'sepal_length': sepal_length,
        'sepal_width': sepal_width,
        'petal_length': petal_length,
        'petal_width': petal_width
    }
    features = pd.DataFrame(data, index=[0])
    return features

user_input = user_input_features()

st.subheader('User Input Parameters')
st.write(user_input)

iris = datasets.load_iris()
X = iris.data
Y = iris.target

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(user_input)
prediction_proba = clf.predict_proba(user_input)

st.subheader('Prediction')
st.write(f"The predicted Iris flower type is: {iris.target_names[prediction][0]}")

st.subheader('Prediction Probability')
st.write(pd.DataFrame(prediction_proba, columns=iris.target_names))
