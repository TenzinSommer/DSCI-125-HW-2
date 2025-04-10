import pandas as pd
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt


rdf = pd.read_csv('hw2_step2_reddit_posts.csv')
gdf = pd.read_csv('hw2_step1_games.csv')
#print(rdf.groupby(by='team_performance')).mean(rdf['sentiment'])


# stuff for generating bar graph that compares fan sentiment and team performance
# testdf = rdf[['team', 'sentiment']].copy()

# yaxis = testdf.groupby('team').mean()
# yaxis = yaxis['sentiment']
# xaxis = yaxis.keys()
# print(xaxis, '\n', yaxis)

# plt.bar(xaxis, yaxis)
# plt.xlabel('Team')
# plt.ylabel('Fan Sentiment')
# plt.title('Fan Sentiment by Team')
# plt.show()
# plt.close()


# stuff for generating scatterplot of fan sentiment game by game, team by team

# newdf = rdf
# print(rdf)
print(gdf)



#print(testdf.groupby('team_performance').mean())


# words = []
# for doc in rdf['tokens']:
# 	words.extend(doc)

# wordcloud_text = ' '.join(words)
# wordcloud = WordCloud(width=800, height=800,
# 					  background_color='white',
# 					  min_font_size=20
# 					  ).generate(wordcloud_text)
# plt.figure(figsize=(4,4),facecolor= None)
# plt.imshow(wordcloud)
# plt.axis('off')
# plt.show()


