# Importing Other party libraries
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# Needed for preprocessing tags
import ast

# Needed for loading and querying model
import numpy as np
from gensim.models import LdaModel
from gensim.corpora import Dictionary
from gensim import corpora

# Import Pandas
import pandas as pd

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

    def assign_bucket(self, input_filepath):
        df = pd.read_csv(input_filepath)
        for i, row in df.iterrows():
            input_list = ast.literal_eval(row['tags'])
            input_corpus = self.dictionary.doc2bow(input_list)
            output_topics = sorted(list(self.ldamodel[input_corpus]), key=lambda tup: tup[1], reverse=True)
            selected_topics = output_topics[0:2]
            df.at[i, 'Bucket1'] = selected_topics[0][0]
            df.at[i, 'Bucket1Prob'] = selected_topics[0][1]
            df.at[i, 'Bucket2'] = selected_topics[1][0]
            df.at[i, 'Bucket2Prob'] = selected_topics[1][1]
            if i%50000 == 0:
                print(i)
        df.to_csv(input_filepath[0:-4] + "_result" + ".csv", index=False)
        return 0


class Advisor:

    def get_assistscore(self, input_filepath):
        return 0
