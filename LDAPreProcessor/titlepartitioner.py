# Importing Other party libraries
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# Needed for preprocessing tags
import ast
import spacy
import string

from gensim.models import LdaModel
from gensim.corpora import Dictionary
from gensim import corpora
import stopwords

# Import Pandas
import pandas as pd

class SuperPartitioner:

    # Class Variables
    all_puncts = string.punctuation.replace(".", "") + string.whitespace
    table = str.maketrans({key: None for key in all_puncts})
    num_table = str.maketrans({key: None for key in string.digits})
    nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner', 'textcat'])
    my_stop_words = stopwords.getstopwordlist()
    dict_stop_words = {}

    @classmethod
    def extend_stopwords(cls):

        for stop_word in cls.my_stop_words:
            lexeme = cls.nlp.vocab[stop_word]
            lexeme.is_stop = True
        print("Stop words added!")

        for stop_word in __class__.my_stop_words:
            cls.dict_stop_words[stop_word] = 1
        print("dict_stop_words dictionary populated from stop words.")

    @classmethod
    def word_checker(cls, w1):

        # POS Filter
        if w1.is_stop or w1.is_punct or w1.like_num or w1.like_url or w1.like_email:
            # wl must not be stop word, punctuation mark, a numeric (1, billion), a URL or e-mail ID.
            return False
        if (w1.pos_ == "VERB") or (w1.pos_ == "ADV") or (w1.pos_ == "SYM") or (w1.lemma_ == '-PRON-'):
            # wl must not be verb, adverb, symbol or pronoun (after lemmatizing)
            return False

        # Custom Filter
        under_radar = w1.lemma_.translate(cls.table)
        if under_radar in __class__.dict_stop_words or under_radar == "":
            # lemmatized form w/o punctuation marks (except ".") and whitespace charatcters must not be a stop word & empty
            return False
        if under_radar.translate(cls.num_table) == "":
            # the lemmatized form after stripping whitespace characters and punctuation marks must not contain only numbers
            return False

        return True

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

        # Variables used for corpus
        article = []  # Will contain the filtered words from the input string
        doc = __class__.nlp(input_string)  # Tagging the Input String

        # Processing the input string
        for word in doc:
            if __class__.word_checker(word):
                article.append(word.lemma_.translate(__class__.table))

        input_list = ast.literal_eval(input_tags)  # Reading the input string containing tags as a list
        input_corpus = self.dictionary.doc2bow(input_list)  # Creating bag of words out of the input_list
        output_topics = sorted(list(self.ldamodel[input_corpus]), key=lambda tup: tup[1], reverse=True)  # Running lda
        # model on the input tags
        print(output_topics)  # Printing output topics from the 'tags' input
        selected_topics = output_topics[0]  # Picking the first topic out the output topics to direct the query to the
        # appropriate bucket based LDA model.

        # Loading the appropriate bucket based LDA model and dictionary
        ldamodel_chosen = LdaModel.load(r"G:\References\MS1\Fall2017\CSE6242\Project\Pogo\TrainedModels\AdvisorModels\bucket" + str(selected_topics[0]) + "LDA")
        dictionary_chosen = Dictionary.load(r"G:\References\MS1\Fall2017\CSE6242\Project\Pogo\BucketedDatabase\Buckets\QuestionTitlesCorpusandDictionary\dict" + str(selected_topics[0]) + ".dict")

        input_corpus_chosen = dictionary_chosen.doc2bow(article)  # Creating bag of words out of the article

        # Querying the bucket based ldamodel without string query
        output_topics_chosen = sorted(list(ldamodel_chosen[input_corpus_chosen]), key=lambda tup: tup[1], reverse=True)

        # Choosing the top 3 topics from the bucket mbased ldamodel's output
        selected_topics_chosen = output_topics_chosen[0:3]

        # Creating a data frame to store bugging topics
        # TODO Need to print it as string/retrun a string instead of storing it in CSV
        df = pd.DataFrame()
        for i in range(0, 3):
            df.at[i, 'Topics'] = ldamodel_chosen.print_topic(selected_topics_chosen[i][0], topn=5)  # Picking just the
            # top 5 words in each of the 3 selected topics
        df.to_csv("query_result.csv")  # writes query output to csv
        return 0


class Advisor:

    def get_assistscore(self, input_filepath):
        return 0
