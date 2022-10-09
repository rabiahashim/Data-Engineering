import pandas as pd
import numpy as np
from plotly.subplots import make_subplots
import plotly.express as px 
import streamlit as st
import datetime

# Fetch Data from Google sheet
def get_complains_data():
    complains_data_url='https://docs.google.com/spreadsheets/d/e/2PACX-1vQZiq18p_LgTk99DXGehERcTuXWmQEe3RpPWBRDElEeRLyQUfrHpKT6cOKoNCH9Og/pub?output=xls'
    df_complain=pd.read_excel(complains_data_url)
    df_complain.replace(np.nan,0,inplace=True)
    df_complain['Month_Year']=pd.to_datetime(df_complain['date_received']).dt.strftime('%m-%Y')
    return df_complain

df_complain=get_complains_data()
# Top KPIs TO DISPLAY 
#1 Total Number of Complaints
no_of_complains=df_complain['complaint_id'].count()
#2 Total Number of Complaints with Closed Status
no_of_complains_with_closed=df_complain[df_complain['company_response']=='Closed']['complaint_id'].count()
#3 % of Timely Responded Complaints
timely_responded_complains=df_complain[df_complain['timely']=='Yes']['complaint_id'].count()/(df_complain['complaint_id'].count())*100
#4 Total Number of Complaints with Progress Status
no_of_complains_with_progress=df_complain[df_complain['company_response']=='In progress']['complaint_id'].sum()

st.set_page_config(page_title="Consumer Financial Complaints Dashboard",layout="wide",page_icon=":sparkles:")
# To display title of website 
st.header("Consumer Financial Complaints Dashboard")
st.subheader("Display Data for “All States” or “Colorado” State (Based on Filter Selected)")

# KPI GRID Representation along with dropdown
with st.container():
    col1, col2, col3,col4,col5 = st.columns([1,1,1,1,1])
    col1.metric("Total Number of Complaints",no_of_complains)
    col2.metric("Total Number of Complaints with Closed Status",no_of_complains_with_closed)
    col3.metric("% of Timely Responded Complaints",timely_responded_complains, delta_color="off")
    col4.metric("Total Number of Complaints with in Progress Status",no_of_complains_with_progress)
    state=col5.selectbox( 'Select the State',options=df_complain['state'].unique())
    df_selection=df_complain.query("state == @state")

# if wants to display charts dynamically w.r.t to states than use this instead of original dataframe
df_selection.sort_values(by=['date_received'],inplace=True)

#Horizontal bar chart
no_of_complains_by_product=df_complain.groupby('product').sum()[['Count_of_Complaint_ID']].sort_values(by='Count_of_Complaint_ID')
fig_complains_by_product=px.bar(no_of_complains_by_product,x='Count_of_Complaint_ID',y=no_of_complains_by_product.index,
 orientation='h',
  title="<b> No of Complains by Product</b>",
    color_discrete_sequence=["#0083B8"] * len(no_of_complains_by_product),
    template="plotly_white",
)
fig_complains_by_product.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

# Line chart
no_of_complains_over_time=df_complain.groupby('Month_Year').sum()[['Count_of_Complaint_ID']].sort_values(by='Count_of_Complaint_ID')
fig_complains_over_time=px.line(no_of_complains_over_time,y='Count_of_Complaint_ID',x=no_of_complains_over_time.index,
  title="<b> No of Complains Over Time </b>",
    color_discrete_sequence=["#E694FF"] * len(no_of_complains_over_time),
    template="plotly_white",
)
fig_complains_over_time.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

# Pie Chart
no_of_complains_by_channel=df_complain.groupby('submitted_via').sum()[['Count_of_Complaint_ID']].sort_values(by='Count_of_Complaint_ID')
fig_complains_by_channel=px.pie(no_of_complains_by_channel,values='Count_of_Complaint_ID',names=no_of_complains_by_channel.index,
  title="<b> No of Complains Submitted via Channel </b>",
    color_discrete_sequence=["#0083B8","#000080","#008080","#00FFFF","#808080"] * len(no_of_complains_by_channel),
    template="plotly_white",
)
fig_complains_by_channel.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

import plotly.graph_objects as go
# Tree Map 
state=df_complain['state']
issue=df_complain['issue']
sub_issue=df_complain['sub_issue']
count_of_complains=df_complain['Count_of_Complaint_ID']
fig_tree=px.treemap(df_complain,path=['state','issue','sub_issue'],values=count_of_complains,
                color_continuous_scale=['red','green','yellow'],title= "<b> Number Over Issue and Sub Issue </b>")

fig_tree.update_layout(title_font_size=15,title_font_family='Arial')

with st.container():
	col1, col2= st.columns([1,1])
	
	#col1.subheader("No of Complains by Product")
	col1.plotly_chart(fig_complains_by_product, use_container_width=True)
	
	#col4.subheader("No of Complains Over Tenure")
	col2.plotly_chart(fig_complains_over_time, use_container_width=True)

with st.container():
	col3, col4= st.columns([1,1])
	
	col3.plotly_chart(fig_complains_by_channel, use_container_width=True)
	col4.plotly_chart(fig_tree,use_container_width=True)
    

# ---- HIDE STREAMLIT STYLE ----
hide_st_style =  """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
