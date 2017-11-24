# Importing Other party libraries
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
import logging
logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# Needed for preprocessing tags
import ast
import spacy
import string
import gensim
# Needed for loading and querying model
import numpy as np
from gensim.models import LdaModel
from gensim.corpora import Dictionary
from gensim import corpora
import stopwords
# Import Pandas
import pandas as pd

def word_checker(w1, dict_stop_words, table, num_table):
         # POS Filter
        if w1.is_stop or w1.is_punct or w1.like_num or w1.like_url or w1.like_email:
            # wl must not be stop word, punctuation mark, a numeric (1, billion), a URL or e-mail ID.
            return False
        if (w1.pos_ == "VERB") or (w1.pos_ == "ADV") or (w1.pos_ == "SYM") or (w1.lemma_ == '-PRON-'):
            # wl must not be verb, adverb, symbol or pronoun (after lemmatizing)
            return False

        # Custom Filter
        under_radar = w1.lemma_.translate(table)
        if under_radar in dict_stop_words or under_radar == "":
            # lemmatized form w/o punctuation marks (except ".") and whitespace charatcters must not be a stop word & empty
            return False
        if under_radar.translate(num_table) == "":
            # the lemmatized form after stripping whitespace characters and punctuation marks must not contain only numbers
            return False

        return True

class Partitioner:

    def __init__(self, ldamodel_path, dictionary_path, corpus_path):
        # LDA Attributes
        self.ldamodel = LdaModel.load(ldamodel_path)
        self.dictionary = Dictionary.load(dictionary_path)
        self.corpus = corpora.MmCorpus(corpus_path)

    def get_lda(self):
        return list(self.ldamodel)

    def get_dictionary(self):
        return self.dictionary

    def get_corpus(self):
        return self.corpus

   

    def assign_bucket(self, input_string, input_tags):
        # df = pd.read_csv(input_filepath)
        # English is now our NLP language pipeline
        nlp = spacy.load('en_core_web_sm', disable=[
                         'parser', 'ner', 'textcat'])

    # Adding stop words to Spacy's stop-word list
        my_stop_words = stopwords.getstopwordlist()
        for stop_word in my_stop_words:
            lexeme = nlp.vocab[stop_word]
            lexeme.is_stop = True
        print("Stop words added!")

        # Creating a Dictionary of stopwords
        dict_stop_words = {}
        for stop_word in my_stop_words:
            dict_stop_words[stop_word] = 1

        # Iterating through each word in the text and assigning certain properties to it
        # ..say whether it's a stop word/number/verb/noun

        # Text to List # Processing is similar to what was done by Linares-Vasquez et al.

        # Variables used for corpus
        # texts = []
        # article = []
        article = []
        texts = []
        doc = nlp(input_string)

        all_puncts = string.punctuation.replace( ".", "") + string.whitespace
        table = str.maketrans({key: None for key in all_puncts})
        num_table = str.maketrans({key: None for key in string.digits})


        for word in doc:
            if word_checker(word, dict_stop_words, table, num_table): 
                article.append(word.lemma_.translate(table))
        texts.append(article)
        
            # input_list = ast.literal_eval(row['tags'])
        input_list = ast.literal_eval(input_tags)
        input_corpus = self.dictionary.doc2bow(input_list)
        output_topics = sorted(list(self.ldamodel[input_corpus]), key=lambda tup: tup[1], reverse=True)
        print(output_topics)
        selected_topics = output_topics[0]
        #ldamodel_chosen based on topic from corpus
        ldamodel_chosen = LdaModel.load("./multicore_4pass/Bucket" + str(selected_topics[0]) + "LDA")
        dictionary_chosen = Dictionary.load("./bucket_processed/dict" + str(selected_topics[0]) + ".dict")
        # corpus_chosen = corpora.MmCorpus("./bucket_processed/corpus" + str(selected_topics[0][0]) + ".mm")
        for text in texts:
         input_corpus_chosen = dictionary_chosen.doc2bow(text) 

        # print(input_corpus_chosen)
        output_topics_chosen = sorted(list(ldamodel_chosen[input_corpus_chosen]), key=lambda tup: tup[1],reverse=True) 
        # print(output_topics_chosen)

        selected_topics_chosen = output_topics_chosen[0:3]
        print(len(selected_topics_chosen))    
        df = pd.DataFrame()
        # print()
        # print( t1 )
        for i in range(0,3):
            df.at[i,'Topics'] = ldamodel_chosen.print_topic(selected_topics_chosen[i][0], topn = 5)
       
        # df.at[i, 'Bucket1'] = selected_topics[0][0]
        # df.at[i, 'Bucket1Prob'] = selected_topics[0][1]
        # df.at[i, 'Bucket2'] = selected_topics[1][0]
        # df.at[i, 'Bucket2Prob'] = selected_topics[1][1]
        # if i % 50000 == 0:
        #     print(i)


        df.to_csv( "query_result.csv") #writes query output to csv
        return 0


class Advisor:

    def get_assistscore(self, input_filepath):
        return 0
