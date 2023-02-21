# Streamlit live coding script
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
from copy import deepcopy
from plotly.subplots import make_subplots

# First some MPG Data Exploration
# @st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    return df


mpg_df_raw = load_data(path="mpg.csv")
mpg_df = deepcopy(mpg_df_raw)

# Add title and header
st.title("Introduction to Streamlit")
st.header("MPG Data Exploration")

# Creat checkbox for showing the dataframe


df_type=st.checkbox("click", ["mpg_df"])

if df_type:
    st.dataframe(data=mpg_df)
# else:
#     print("")


# Widgets: checkbox (you can replace st.xx with st.sidebar.xx)
# if st.checkbox("Show Dataframe"):
#     st.subheader("This is my dataset:")
#     st.dataframe(data=mpg_df)
    # st.table(data=mpg_df)

# Scatter plot of displ vs. hwy for year =2008
# matplotlib
#plotly
plot_type=st.radio("Choose plot type", ["Matplotlib","Plotly"])


df=mpg_df[mpg_df['year']==2008]
# plt.scatter(x=df['hwy'], y=df['displ'])
# plt.show()

fig1 = make_subplots(rows=1, cols=1, 
                     subplot_titles=(" Tips"))
fig1.add_trace(
    go.Scatter(x=df['hwy'],
        y=df['displ'],
        mode='markers',
        marker=dict(size=5, color="MediumPurple")))
st.plotly_chart(fig1)

