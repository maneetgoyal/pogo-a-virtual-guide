import spacy
import re

def getstopwordlist():
    # Spacy's Stop word list
    from spacy.lang.en.stop_words import STOP_WORDS
    count_Spacy = len(STOP_WORDS)

    # Stop words from Link Assistant
    # https://www.link-assistant.com/seo-stop-words.html Oct 29 2017
    try:
        listo = open("stopwords.txt").read()
        listo = re.split("\s+", listo)  # '/s' Matches Unicode whitespace characters; '+' for global search
    except IOError:
        print("Text File couldn't be opened")

    link_assistant_set = set()
    link_assistant_set.update(listo)

    # Desired List
    union_set = link_assistant_set.union(STOP_WORDS)  # 'set' of 683 words # include empty '' also
    #diff_set = link_assistant_set.difference(STOP_WORDS)
    try:
        union_set.remove('')
    except KeyError:
        print("'' wasn't there in the union set.")

    return union_set
