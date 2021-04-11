# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 01:45:14 2021

@author: Syed Muhammmad Hamza
"""

import requests
from bs4 import BeautifulSoup
from pprint import pprint
import pandas as pd
import time

url = "https://api.pushshift.io/reddit/search/submission"
url_comments = "https://api.pushshift.io/reddit/search/comment"

#Personality_Types=['ISTJ','infj','intj','enfj','istp','ESFJ','infp','ESFP','ENFP','estp','ESTJ','entj','INTP','isfj','entp','isfp']
#Personality_Types=['ESFJ','ESFP','estp','ESTJ']
#Personality_Types=['intj','ENFP','entp']
#Personality_Types=['ISTJ','isfj']
Personality_Types=['ESTJ']
def get_comments(subreddit, n_iter):
    
    df_list = []
    current_time = 1617467670
    
    for _ in range(n_iter):
        res = requests.get(
            url_comments,
            #url,
            params={
                "subreddit": subreddit,
                "size": 500,
                "before": current_time
            }
        )
        time.sleep(3)
        df = pd.DataFrame(res.json()['data'])
        #df = df.loc[:, ["subreddit", "body", "created_utc"]]
        filtered_columns =["subreddit", "body", "created_utc"]
        df = df.reindex(columns = filtered_columns)
        df_list.append(df)
        current_time = df.created_utc.min()
        
    return pd.concat(df_list, axis=0)

def get_posts(subreddit, n_iter):
    
    df_list = []
    current_time = 1617467670
    
    for _ in range(n_iter):
        res = requests.get(
            #url_comments,
            url,
            params={
                "subreddit": subreddit,
                "size": 500,
                "before": current_time
            }
        )
        time.sleep(3)
        df = pd.DataFrame(res.json()['data'])
        #df = df.loc[:, ["title","subreddit","selftext","created_utc","media_only","is_video"]]
        filtered_columns =["title","subreddit","selftext","created_utc","media_only","is_video"]
        df = df.reindex(columns = filtered_columns)
        
        df_list.append(df)
        current_time = df.created_utc.min()
    return pd.concat(df_list, axis=0)

for personality in Personality_Types:
    comments='df_comments_'+ personality
    comments=get_comments(personality, 3)
    comments[comments['body'].duplicated() == False]
    df1=comments
    
    posts='df_posts_'+ personality
    posts=get_posts(personality, 8)
    posts[posts['selftext'].duplicated() == False]
    #posts['selftext']=posts['title']+posts['selftext']
    posts = posts.loc[:, ["subreddit", "selftext", "created_utc"]]
    posts =posts.rename(columns={'selftext': 'body'})
    df2=posts

    df=pd.concat([df1, df2],ignore_index=True)
    
    path='Dataset/'+personality+'.csv'
    df.to_csv(path, index=False)
    



