# Importing Other party libraries
import string
import re

def tagpreprocess(filepath):

    # Importing text
    try:
        with open(filepath, 'r') as f:
            header_line = next(f)  # Skipping the header line
            tag_string = f.read()
            print("File read!")
    except IOError:
        print("Could not open input file containing questions' tags data.")
        return 404

    # Processing Text
    table = str.maketrans({key: None for key in string.whitespace + "\\\'\"["})  # Making a trans;ate table
    processed_tag_string = tag_string.translate(table)  # Stripping off whitespace charatcers, [, ', ", \
    tag_list = processed_tag_string.split(']')  # Splitting string with "]" as the delimiter
    query_re = re.compile("^\d+,\d+,", re.IGNORECASE)  # Compiling input string into a pattern object
    list_of_lists = []
    for i, ele in enumerate(tag_list):
        regexed_ele = query_re.sub("", tag_list[i], count=1)
        if regexed_ele != "":
            list_of_lists.append(regexed_ele.split(","))
    return list_of_lists
