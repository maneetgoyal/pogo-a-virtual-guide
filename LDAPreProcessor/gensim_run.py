import string
# Suppressing warnings
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
import re
import gensim
from gensim import corpora
from gensim.corpora import Dictionary
from gensim.models import CoherenceModel, LdaModel, LsiModel, HdpModel, LdaMulticore
from gensim.models.wrappers import LdaMallet
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
# import pyLDAvis.gensim

if __name__ == '__main__':
    for i in range (0,4): #change range to your range of files
    dictionary = Dictionary.load("./tag_processed/dict" + str(i) + ".dict") #change file structure according to your folders
    corpus = corpora.MmCorpus("./tag_processed/corpus" + str(i) + ".mm")


    ldamodel = LdaMulticore(corpus=corpus, num_topics=20, id2word=dictionary, workers = 3, passes = 4) #if you don't have 4 cores, change LdaMulticore to LdaModel and remove the "workers = 3" parameter, 
    # you can run LdaMulticore on 2 cores however it's not advised

    ldamodel.show_topics()

    ldamodel.save("./multicore_4pass/bucket"+ str(i) + "LDA") # change file structure according to your folders

    # pyLDAvis.save_html(pyLDAvis.gensim.prepare(ldamodel, corpus, dictionary), "demo2.html")