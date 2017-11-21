# Importing Other party libraries
import warnings
import pandas as pd
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
import gensim
import spacy
import string
from gensim import corpora
from gensim.corpora import Dictionary
# Importing personal libraries
import stopwords

# Function word-check
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

def bucket_preprocess(filepath):

    # Importing text
    try:
        df = pd.read_csv(filepath)
    except PermissionError:
        print("Permission to open the file denied")
        

    # Specifying language model
    nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner', 'textcat'])  # English is now our NLP language pipeline

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

    # Varibales used for corpus
    texts = []
    article = []
    doc_count = 0


    # Variables used for removing punctuation
    all_puncts = string.punctuation.replace(".", "") + string.whitespace
    table = str.maketrans({key: None for key in all_puncts})
    num_table = str.maketrans({key: None for key in string.digits})
    for ind, ele in enumerate(df['TITLE']):
        doc = nlp(ele)
        
        for w in doc:  # again iterating thru each word in doc
                if word_checker(w, dict_stop_words, table, num_table): 
                    article.append(w.lemma_.translate(table))  # appending lemmatized version of the word without whitespace
                # characters and punctuation marks (allowing only fullstop)
        
        texts.append(article)
        article = []
        doc_count = doc_count + 1
        
        if (doc_count % 10000) == 0:
            doc_count = 0
            print(str(doc_count), "done!")

    # Bigrams New, York will be made into New_York
    bigram = gensim.models.Phrases(texts)  # Important for our application
    texts = [bigram[line] for line in texts]
    print("Texts bigramed!")
    # print(texts)
    
    dictionary = Dictionary(texts)

    dictionary.save("./bucket_processed/dict_sample.dict")

    corpus = [dictionary.doc2bow(text) for text in texts]

    corpora.MmCorpus.serialize("./bucket_processed/corpus_sample.mm", corpus)
    print(dictionary)
    print(corpus)


bucket_preprocess("./Buckets/sample_bucket.csv")
