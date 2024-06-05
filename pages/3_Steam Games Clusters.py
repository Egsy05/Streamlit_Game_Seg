import streamlit as st
import pandas as pd

data = pd.read_csv("games_labels.csv")
data['Review'] = data['Positive']-data['Negative']
data['Profit'] = data['Peak CCU']*data['Price']
st.header("This is the clusters for All games in Steam from 2008 to 2023", divider='blue')
cluster_value = data['Labels'].sort_values().unique()
select_clusters = st.multiselect("Select Cluster",cluster_value)
if select_clusters:
    filter_table = data[data['Labels'].isin(select_clusters)]
    st.write(filter_table)
else:
    filter_table = data
    st.write(filter_table)


st.scatter_chart(filter_table, x='Profit', y='Peak CCU', color='Labels',size='Review')
