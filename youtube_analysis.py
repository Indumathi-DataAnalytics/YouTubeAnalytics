# -*- coding: utf-8 -*-
"""
Created on Sun May 10 23:03:21 2026

@author: ELCOT

"""
import pandas as pd

data=pd.read_csv("INvideos.csv")


#view code
data['views']=pd.to_numeric(data['views'])

top_views=data.sort_values(by='views',ascending=False)
print(top_views[['title','views']].head())
#view plot code
import matplotlib.pyplot as plt
top5=top_views.head()
plt.bar(top5['title'],top5['views'])
plt.xticks(rotation=90)
plt.xlabel("Video Title")
plt.ylabel("Views")
plt.title("Top 5 Trending Vides")
plt.show()

#likes code
top_likes=data.sort_values(by='likes',ascending=False)
print(top_likes[['title','likes']].head())

#top likes plot
top5likes=top_likes.head()
plt.bar(top5likes['title'],top5likes['likes'])
plt.xticks(rotation=90)
plt.xlabel("Video Title")
plt.ylabel("likes")
plt.title("Top 5 Most Liked Videos")
plt.show()

#top trending channels code

top_channels=data['channel_title'].value_counts().head()
print(top_channels)
#top trending channels plot

top_channels.plot(kind='bar') 
plt.xlabel("Channnal Name")
plt.ylabel("Trending Court")
plt.title("Top Trending Channels")
plt.show()

#likes and views
plt.scatter(data['views'],data['likes'])
plt.xlabel("Views")
plt.ylabel("Likes")
plt.title("Views and Likes")
plt.show()

#category analysis
category_count=data['category_id'].value_counts().head(10)
print(category_count)

#category graph

category_count.plot(kind='bar')
plt.xlabel("Category ID")
plt.ylabel("Number of Trending Videos")
plt.title("Top Trending Categories")
plt.show()

#engagement rate
data['engagement_rate']=((data['likes']+data['comment_count'])/data['views'])*100
top_engagement=data.sort_values(by='engagement_rate',ascending=False)
print(top_engagement[['title','engagement_rate']].head())

#Engagement rate plot

top5eng=top_engagement.head()
plt.bar(top5eng['title'],top5eng['engagement_rate'])
plt.xticks(rotation=90)
plt.xlabel("Video Title")
plt.ylabel("Engagement Rate")
plt.title("Top Engagement Videos")
plt.show()

#multi comment
us_data=pd.read_csv("USvideos.csv")
india_avg_views=data['views'].mean()
us_avg_views=us_data['views'].mean() 
print("India Average  Views:",india_avg_views)
print("USA Average  Views:",us_avg_views)
  
#multi comment graph

countries=['India','USA']
avg_views=[india_avg_views,us_avg_views]
plt.bar(countries,avg_views)
plt.xlabel("Country")
plt.ylabel("Average Views")
plt.title("India vs USA Average Views")
plt.show()














