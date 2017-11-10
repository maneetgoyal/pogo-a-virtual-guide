# Importing Libraries
import pandas as pd
from bs4 import BeautifulSoup

# Extracts text out <p>...</p>
def parastripper(inputstring):
    soup = BeautifulSoup(inputstring, "lxml")
    outputstring = soup.get_text()
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
            df = pd.DataFrame({'id': data['id'], 'title': data['title'], 'body': data['body']})
            df.to_csv(outputpath)
        except PermissionError:
            print("Permission to open the output file denied")
    except PermissionError:
        print("Permission to open input the file denied")


parastripping("questions0.csv", "out0.csv")
