#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 18:39:50 2020

@author: averysmith
"""
# Libraries
import pandas as pd
import nltk
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

## Load in Tweets
df = pd.read_csv('JoeExoticTweets.csv')

# Tokenize words
texts = ' '.join(df['Text'])
FindWordsText = nltk.word_tokenize(texts) # Seperate text into words and preprocessing
text = nltk.Text(FindWordsText) # Spit out finished, searchable version of text
words = text.tokens

# Clean up links as words
words_clean = [i for i in words if '//' not in i]
words_clean = [i for i in words_clean if '.com' not in i]
other_messy_words = ['https', ' https', 'https ', '.',':','\'','&',',']
words_clean = [i for i in words_clean if i not in other_messy_words]

print(len(words))
print(len(words_clean))

text_clean = pd.Series(words_clean)
text_clean.to_csv('JoeCleanWords.csv')

# Get text_clean in string again
texts_clean = ' '.join(words_clean)

# Redo NLTK
FindWordsText = nltk.word_tokenize(texts_clean) # Seperate text into words and preprocessing
text = nltk.Text(FindWordsText) # Spit out finished, searchable version of text
words = text.tokens


# Analyze word
def analyze_word_frequency(words,num_to_show,save_name,color):
    frequency_dist = nltk.FreqDist(words)
    word_dict = sorted((value, key) for (key,value) in frequency_dist.items())
    x, y = zip(*word_dict) # unpack a list of pairs into two tuples
    plt.figure(figsize=[6,14])
    plt.plot(x[-num_to_show:], y[-num_to_show:],lw=6,c=color)
    plt.yticks(fontname = "Arial Black", fontsize=20)
    plt.xlabel('Num Times Used',fontsize=14, fontname = "Arial Black")
    plt.xticks(fontsize=14, fontname = "Arial Black")
    plt.tight_layout()
    plt.savefig(save_name + ".png", format="png")
    plt.show()


# Analyze Frequency 
analyze_word_frequency(words,40,'joes_most_common','r')


# Remove stop words
stop_words = set(nltk.corpus.stopwords.words('english')) 
filtered_by_stopwords = [w for w in FindWordsText if not w in stop_words] 
extra_stopwords = ["…",'#','@','!','\'s','..',"’",'?','n\'t','.','I','...']
filtered_by_stopwords = [w for w in filtered_by_stopwords if not w in extra_stopwords] 


# Redo frequency analysis
analyze_word_frequency(filtered_by_stopwords,40,'joes_most_common_clean','b')



### Make Word Cloud

# Simple word cloud

# Create and generate a word cloud image:
wordcloud = WordCloud(background_color="white").generate(texts_clean)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
plt.figure(figsize=[12,12])
wordcloud.to_file("joes_simple_tweets.png")




# Make image word bubble
mask = np.array(Image.open("JoeExoticPic.jpg"))
wordcloud_colored = WordCloud( background_color="white",  mask=mask).generate(texts_clean)

# create coloring from image
image_colors = ImageColorGenerator(mask)
plt.figure(figsize=[12,12])
plt.imshow(wordcloud_colored.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")

# store to file
plt.savefig("joes_tweets_colored.png", format="png")




