import titlepartitioner as bp



my_partitioner = bp.Partitioner(ldamodel_path="./tag_processed/fi", dictionary_path="tag_processed/dict_final.dict",
                                corpus_path="tag_processed/corpus_final.mm")


# for i in range(9, 11):
placeholder_0 = my_partitioner.assign_bucket(input_string="learn d3 visualization", input_tags = '["d3", "javascript", "viz"]')
    # print("{} is done!".format(i))