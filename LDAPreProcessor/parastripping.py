# Importing Libraries
import pandas as pd
from bs4 import BeautifulSoup

# Extracts text out <p>...</p>
def parastripper(inputstring):
    soup = BeautifulSoup(inputstring, "lxml")  # Creating soup
    outputstring = " ".join([row.text for row in soup.find_all("p")])  # Getting only the content present with <p> tags
    outputstring = outputstring + " mgoyal35"  # "mgoyal35" denotes line end. This word will be used in text preprocess.
    # joining each of that data by a white space.
    return outputstring

# Combines title and body text and saves at outputpath
def parastripping(csvpath, outputpath):
    # Open Data File
    try:
        data = pd.read_csv(csvpath)
        # Spliiting tags' string
        for ind, ele in enumerate(data['title']):
            data.set_value(ind, 'title', ele)
            data.set_value(ind, 'body', parastripper(data['body'][ind]))  # Updating data frame with array of tags
        # Open Output File
        try:
            df = pd.DataFrame({'id': data['id'], 'title': data['title'], 'zbody': data['body']})
            df.to_csv(outputpath)
        except PermissionError:
            print("Permission to open the file denied")
    except PermissionError:
        print("Permission to open the file denied")


for i in ["0", "1", "2", "3", "4", "5", "6", "7", "8"]:
    parastripping(r"G:\References\MS1\Fall2017\CSE6242\Project\Pogo\TagsGraph\InputCSV\questions" + i + ".csv", r"Stripped\output" + i + ".csv")
    print(i, "th file done!")

