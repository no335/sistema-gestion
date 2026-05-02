import json

database = {}

def read():
    global database
    with open('data/data.json', 'r') as data_file:
        database = json.loads(data_file.read())

def write():
    with open('data/data2.json', 'w') as data_file:
        out_data = json.dump(database, data_file)

def from_csv():

    

read()
