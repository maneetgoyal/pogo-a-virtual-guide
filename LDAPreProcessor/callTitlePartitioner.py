import titlepartitioner as tp

# Instantiating the titlepar
assistant_and_advisor = tp.SuperPartitioner\
    (ldamodel_path=r"G:\References\MS1\Fall2017\CSE6242\Project\Pogo\PogoGit\LDA4PassModel\fi",
     dictionary_path="G:\References\MS1\Fall2017\CSE6242\Project\Pogo\TagsCorpusAndDictionary\dict_final.dict",
     corpus_path=r"G:\References\MS1\Fall2017\CSE6242\Project\Pogo\TagsCorpusAndDictionary\corpus_final.mm")

# Calling class methods
tp.SuperPartitioner.extend_stopwords()

# for i in range(9, 11):
placeholder_0 = assistant_and_advisor.assign_bucket(input_string="how do i prevent sql injection in php",
                                                    input_tags='["php", "mysql", "sql", "security", "sql-injection"]')
