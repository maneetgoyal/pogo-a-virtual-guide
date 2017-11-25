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
    for i in range(14, 15):  # change range to your range of files
        dictionary = Dictionary.load(r"G:\References\MS1\Fall2017\CSE6242\Project\Pogo\BucketedDatabase\Buckets\CorpusandDictionary\dict" + str(i) + ".dict")  # change file structure according to your folders
        corpus = corpora.MmCorpus(r"G:\References\MS1\Fall2017\CSE6242\Project\Pogo\BucketedDatabase\Buckets\CorpusandDictionary\corpus" + str(i) + ".mm")

        ldamodel = LdaModel(corpus=corpus, num_topics=5, id2word=dictionary, passes=10)
        # if you don't have 4 cores, change LdaMulticore to LdaModel and remove the "workers = 3" parameter,
        # you can run LdaMulticore on 2 cores however it's not advised

        ldamodel.show_topics()

        ldamodel.save("ldamodel" + str(i))  # change file structure according to your folders
