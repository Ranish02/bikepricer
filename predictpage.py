import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('./stored_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data


data = load_model()

regressor = data["model"]
le_brand = data["le_brand"]
le_owner = data["le_owner"]


def show_predict_page():
    st.title("Bike Pricer- Used Bike Price Estimator")
    st.write("""### Estimate your used bike prices""")
    st.write(""" We need some information to estimate the bike price""")
    st.write(
        """ This app is based on a model trained using dataset from kaggle """)
    st.write(
        "Dataset source: [link](https://www.kaggle.com/datasets/saisaathvik/used-bikes-prices-in-india)")

    brand = (
        'TVS', 'Royal Enfield', 'Triumph', 'Yamaha',
        'Honda', 'Hero', 'Bajaj', 'Suzuki',
        'Benelli', 'KTM', 'Mahindra', 'Kawasaki', 'Ducati',
        'Hyosung', 'Harley-Davidson', 'Jawa',
        'BMW', 'Indian', 'Rajdoot', 'LML', 'Yezdi', 'MV', 'Ideal'
    )
    Power = (
        100, 107, 110, 125,
        135, 149, 150, 160, 175,
        180, 200, 220, 223, 250, 295,
        300, 302, 310, 320, 350, 390, 400,
        410, 500, 502, 535, 600, 650,
        675, 750, 765, 796, 797,
        800, 821, 850, 865, 883, 899,
        900, 959, 1000, 1050, 1090,
        1100, 1130, 1198, 1200,
        1262, 1299, 1300, 1700, 1800
    )
    owner = (
        'First Owner',
        'Second Owner',
        'Third Owner',
        'Fourth Owner Or More'
    )

    Brand = st.selectbox("Brand", brand)
    Power = st.selectbox("Power (cc)", Power)
    kms_driven = st.number_input(
        "Bike Driven (in Kilometer)", 0, None, 1000, None)
    Owner = st.selectbox("Owner", owner)
    age = st.number_input("Bike age (years)", 0, 50, 1)
    ok = st.button("Estimate")
    if ok:
        X = np.array([[kms_driven, Owner, age, Power, Brand]])
        X[:, 4] = le_brand.transform(X[:, 4])
        X[:, 1] = le_owner.transform(X[:, 1])
        X = X.astype(float)
        salary = regressor.predict(X)
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")
