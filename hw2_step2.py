import pandas as pd

import nltk
# nltk.download('stopwords')
# nltk.download('punkt_tab')

from nltk.corpus import stopwords
from gensim.corpora import Dictionary
from gensim.models import TfidfModel

from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer


# Data Modeling 
# pick two topics to compare
# develop a way to identify which topic a post is talking about 
# check occurences of different topics of conversation over time
#   could these different conversation topics appear during a game period more often?
# 

def text2tokens(text):
	stop_words = set(stopwords.words('english'))
	ps = PorterStemmer()
	text = text.lower()
	textList = word_tokenize(text)
	textList = [word for word in textList if word not in stop_words and len(word) >= 3]

	textList = [ps.stem(word) for word in textList]
	return textList
    

def gen_bow(df, column):
	df['tokens'] = df[column].apply(text2tokens)
	dct = Dictionary(df['tokens'])
	dct.filter_extremes(no_below=5, no_above=0.5)
	df['bow'] = df['tokens'].apply(dct.doc2bow)
	worddict = {}

	for i in range(len(df)):
		for token in df.at[i,'bow']:
			if token in list(worddict.keys()):
				worddict[token] += 1
			else: 
				worddict[token] = 1

	df.drop('tokens', axis=1, inplace=True)	
	return df, worddict


# print(text2tokens("In this offering, one only has to view the current Westminster Kennel Club's annual offering to see the parallels."))

orioles_df = pd.read_json('orioles.json')
# orioles_df = gen_bow(orioles_df, '')
orioles_df.columns
