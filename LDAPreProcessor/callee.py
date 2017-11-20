import bucketpartitioner as bp

my_partitioner = bp.Partitioner(ldamodel_path="LDA4Pass/fi", dictionary_path="CorpusAndDictionary/dict_final.dict",
                                corpus_path="CorpusAndDictionary/corpus_final.mm")

for i in range(9, 11):
    placeholder_0 = my_partitioner.assign_bucket(input_filepath=("TagsData/output" + str(i) + ".csv"))
    print("{} is done!".format(i))
