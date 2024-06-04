import streamlit as st
import pandas as pd
import altair as alt
import streamlit.components.v1 as com

st.balloons()
st.title("Welcome! "
        "Here is my analysis about the steam games, "
        "from 2008 to 2023")
st.markdown("Did **YOU** know, that there are over **70.000** games in steam!")
st.header("About the Data")

st.write("Our data has been engineered to become easy to read and understand, "
        "you click this link below to lookup to the original data.")
st.link_button("Data","https://www.kaggle.com/datasets/mexwell/steamgames")

data = pd.read_csv('games_.csv')

name_to_search = st.text_input('Search your game here:')
if name_to_search.strip() == '':
    st.dataframe(data)
else:
    filtered_df = data[data['Name'].str.contains(name_to_search, case=False, na=False)]
    if not filtered_df.empty:
        st.write('Is this what you looking for? ')
        st.dataframe(filtered_df)
    else:
        st.write('No results found.')

st.subheader("Highest user games!", divider='blue')

x = data.groupby(['Name']).agg(users=('Peak CCU','sum')).sort_values('users',ascending=False).head(10).reset_index()

st.altair_chart(alt.Chart(x)
    .mark_bar(orient='horizontal')
    .encode(
        x='users',
        y=alt.Y('Name').sort('-x'),
    ),
    use_container_width=True)


st.subheader("About The Author", divider='blue')
st.write('Fadllun Amir Alfitri, is an Electrical Engineering Bachelor from University of Muhammadiyah Malang. ' 
        'Dedicated in Data Analytic and Data Science. '
        'Since IT has become more contribute in many company and had a high demand, '
        'Fadllun decided to learn about computer science and coding, '
        'leading to data science hopping as a career starter in the world of IT')

st.write("## Thank you for visiting!")
st.image('thump up cat.png',width=500)