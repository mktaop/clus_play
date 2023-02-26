#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 16:54:55 2023

@author: avi_patel
"""

import streamlit as st
import numpy as np
import joblib
import pickle
from tensorflow import keras
from sklearn.cluster import KMeans

with open("clus1model.pkl", "rb") as f:
     model = pickle.load(f)
#model = joblib.load('clus1model.joblib')

page_title="Enter Info to see what cluster you belong to!"
page_icon=":large_blue_diamond:"
layout="centered"
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_icon + " " + page_title+ " "+ page_icon)


f = st.selectbox('Which of the following does your current age fall into:',
                 ('<18', '18-25', '26-34','36-45','46-55','56-65','>65'))
if f =='<18':
    f1=1.1
elif f=='18-25':
    f1=1.2
elif f=='26-35':
    f1=1.3
elif f=='36-45':
    f1=1.4
elif f=='46-55':
    f1=1.5
elif f=='56-65':
    f1=1.6
else:
    f1=1.7


f = st.selectbox('Which of the following regions do you currently reside (US only):',
                 ('Northeast', 'Southeast', 'South','North','Northwest','West'))
if f =='Northeast':
    f2=2.1
elif f=='Southeast':
    f2=2.2
elif f=='South':
    f2=2.3
elif f=='North':
    f2=2.4
elif f=='Northwest':
    f2=2.5
else:
    f2=2.6


f = st.selectbox('What is your highest level of education:',
                 ('No HS', 'HS or Equivalent', 'Third Choice','2yr Degree','4yr Degree',
                  'Graduate Degree','Ph.D'))
if f =='No HS':
    f3=3.1
elif f=='HS or Equivalent':
    f3=3.2
elif f=='Third Choice':
    f3=3.3
elif f=='2yr Degree':
    f3=3.4
elif f=='4yr Degree':
    f3=3.5
elif f=='Graduate Degree':
    f3=3.6
else:
    f3=3.7

f = st.selectbox('Which of the genders below do you classify yourself with:',
                 ('Male', 'Female', 'Transgender','Other'))
if f =='Male':
    f4=4.1
elif f=='Female':
    f4=4.2
elif f=='Transgender':
    f4=4.3
else:
    f4=4.4

f = st.selectbox('Which of the following best describes your current employment:',
                 ('Not Employed', 'Retired', 'Employed full time','Employed part time','Gig worker full time',
                  'Gig worker part time','Employed and Gig worker'))
if f =='Not Employed':
    f5=5.1
elif f=='Retired':
    f5=5.2
elif f=='Employed full time':
    f5=5.3
elif f=='Employed part time':
    f5=5.4
elif f=='Gig worker full time':
    f5=5.5
elif f=='Gig worker part time':
    f5=5.6
else:
    f5=5.7

f = st.selectbox('What is your monthly income, regardless of your employment status:',
                 ('<$1,000', '$1,000-$2,499', '$2,500-$4,999','>=$5,000'))
if f =='<$1,000':
    f6=6.1
elif f=='$1,000-$2,499':
    f6=6.2
elif f=='$2,500-$4,999':
    f6=6.3
else:
    f6=6.4

f = st.selectbox('What best describes your savings (regardless of the product) situation:',
                 ('No savings at all', 'Some amount of savings', 'Moderate amount of savings',
                  'Appropriate amount of savings'))
if f =='No savings at all':
    f7=7.1
elif f=='Some amount of savings':
    f7=7.2
elif f=='Moderate amount of savings':
    f7=7.3
else:
    f7=7.4

f = st.selectbox('Would you like to save more than you currently are:',
                 ('Yes','No'))
if f =='Yes':
    f8=8.1
else:
    f8=8.4

f = st.selectbox('What is your current level of debt:',
                 ('No debt', 'Minimum amount of debt', 'Moderate amount of debt','Too much debt'))
if f =='No debt':
    f9=9.1
elif f=='Minimum amount of debt':
    f9=9.2
elif f=='Moderate amount of debt':
    f9=9.3
else:
    f9=9.4

f = st.selectbox('How would you describe your current physical health status:',
                 ('Very healthy','Moderately healthy','Somewhat healthy','Not healthy'))
if f =='Very healthy':
    f10=10.1
elif f=='Moderately healthy':
    f10=10.2
elif f=='Somewhat healthy':
    f10=10.3
else:
    f10=10.4

if st.button("Submit"):
    features=np.array([f1, f2, f3, f4, f5, f6, f7, f8,f9,f10])
    features2=features.reshape(1, -1)
    clus=model.predict(features2)
    clusval=clus[0]
    
    text1='You belong to Cluster Number: ' + str(clusval)
    st.subheader(text1)
    if clus==0:
        st.write('Which means XYZ and 123')
    elif clus==1:
        st.write('Which means ABC and 456')
    else:
        st.write('Which means GHI and 789')
    st.write()


