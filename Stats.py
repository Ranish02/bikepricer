import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#@st.cache
def load_data():
    df = pd.read_csv('Used_Bikes.csv')
    df = df[['kms_driven', 'owner', 'age', 'power', 'brand', 'price']]
    df = df.dropna()
    return df


df = load_data()


def show_explore_page():
    st.title("Explore  Used Bike prices")

    st.write(
        """
    ### Dataset from www.droom.in
    """
    )

    data = df["brand"].value_counts()

    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=0, )
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig1)

    st.write(
        """
    #### Mean Price Based On Bike companies
    """
    )

    data = df.groupby(["brand"])["price"].mean().sort_values(ascending=True);
    st.bar_chart(data)

    st.write(
        """
    #### Mean Price Based On Bike Age
    """
    )

    data = df.groupby(["age"])["price"].mean().sort_values(ascending=True)
    st.line_chart(data)

    st.write(
        """
    #### Mean Price Based On Power (cc)
    """
    )

    data = df.groupby(["power"])["price"].mean().sort_values(ascending=True)
    st.bar_chart(data)

