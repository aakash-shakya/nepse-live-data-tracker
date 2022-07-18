from datetime import datetime


def generate_excel_file(filename, arr):
    
    with open (filename + str(datetime.now()) +'.xlsx', 'w') as f:
        for i in arr:
            for j in i:
                f.write(j.text)
                f.write('\t')
            f.write('\n')
    f.close()