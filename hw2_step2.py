import pandas as pd

import nltk
# nltk.download('wordnet')
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


def text2tokens(text):
	stop_words = set(stopwords.words('english'))
	ps = PorterStemmer()
	text = str(text)
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

posNegWords = pd.read_excel('posNegList.xlsx')
posWords = posNegWords['Positive Sense Word List']
posWords = posWords.dropna()
negWords = posNegWords['Negative Sense Word List']
negWords = negWords.dropna()



def findPosNegCount(list):
	posCount = 0
	negCount = 0
	
	for word in list:
		if word in posWords:
			posCount += 1
		elif word in negWords:
			negCount += 1
	
	return posCount - negCount
			
or_df = pd.read_csv('hw2_step1_or_posts.csv')

or_df['tokens'] = or_df['text'].apply(text2tokens)

or_df['posOrNeg'] = or_df['tokens'].apply(findPosNegCount)
print(or_df)
