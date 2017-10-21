# Importing Libraries
import pandas as pd
import itertools as it
import ast

# Function to read through a CSV file and create an edge list
def edgelist(csvpath, outputpath):
    # Open Data File
    try:
        data = pd.read_csv(csvpath)
        # Spliiting tags' string
        for ind, ele in enumerate(data['tags']):
            data.set_value(ind, 'tags', ele.split("|"))  # Updating data frame with array of tags
        # Open Output File
        try:
            df = pd.DataFrame({'id': data['id'], 'tags': data['tags']})
            df.to_csv(outputpath)
        except PermissionError:
            print("Permission to open the file denied")
    except PermissionError:
        print("Permission to open the file denied")

# Function to read through a node array and create an edge list
def edgecreate(edgearrayfile, edgesoutput):
    # Open Data File
    try:
        data = pd.read_csv(edgearrayfile)
        out = []
        for ele in (data['tags']):
            if len(ast.literal_eval(ele)) > 1:  # ast.literal_eval(ele) evaluates ele as a python command. '[a,b,c,d]'
                # will be interpreted as a list not as string using this command
                out = out + list(it.combinations(ast.literal_eval(ele), 2))
            else:
                tups = (ast.literal_eval(ele)[0], ast.literal_eval(ele)[0])
                out.append(tups)
            if len(out) > 1000:  # Limiting the array length to 1000 and then writing to our .txt file. .csv not chosen
                # because all rows weren't shown in the csv. May be I was exceeding some csv rows limit.
                # Open Output File
                try:
                    with open(edgesoutput, "a") as f:
                        for tuppy in out:
                            f.write(",".join(tuppy)+"\n")  # ",".join(tuppy) joins the tuple elements as a string
                            # delimited by ','
                except PermissionError:
                    print("Permission to open the file denied")
                out = []
    except PermissionError:
        print("Permission to open the file denied")

# Fetching edge lists from all input csv files
def batchitup():
    for i in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        edgelist("InputCSV/questions" + i + ".csv", "IntermediateOutput/output" + i + ".csv")
        print(i + "'s Part 1 is done!")
        edgecreate("IntermediateOutput/output" + i + ".csv", "EdgeLists/edgelist" + i + ".txt")
        print(i + "'s Part 2 is done!")

# Hit the gas!
batchitup()

# ----- READ IT ---------
# Before running this file. Download all your 8-9 Input csv files in an InputCSV named folder in the current directory.
# Correct the file type of tables downloaded from Google Cloud. questions.csv0000000009 will become questions9.csv
# Create an IntermediateOutput named folder in the current directory.
# Create an EdgeLists named folder in the current directory.
# Modify line 52 so that it contains the right file numbers (in str format only).
# Run the function.
# Once all the output files are obtained in EdgeLists folder. Run the command
# contained in textmerger.txt from command line (Windows only), with EdgeLists
# as the current directory.
