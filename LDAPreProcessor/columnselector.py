import pandas as pd

def columnselector(csvpath, outputpath):
    # Open Data File
    try:
        data = pd.read_csv(csvpath)
        print("Data Loaded!")
        df = pd.DataFrame({'id': data['id'], 'answer_count': data['answer_count'],
                           'comment_count': data['comment_count'], 'creation_date': data['creation_date'],
                           'last_activity_date': data['last_activity_date'], 'last_edit_date': data['last_edit_date'],
                           'view_count': data['view_count'], 'accepted_answer_id': data['accepted_answer_id'],
                           'score': data['score']})
        try:
            df.to_csv(outputpath, index=False)
        except PermissionError:
            print("Output File Permission Error")
    except PermissionError:
        print("Input File Permission Error.")


for i in range(9):
    columnselector(r"G:\References\MS1\Fall2017\CSE6242\Project\Pogo\TagsGraph\InputCSVFraction\questions"+str(i)+".csv"
                   , r"DesiredColumnsOnly\output"+str(i)+".csv")
    print("{}th file done!".format(i))
