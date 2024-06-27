import json

def load_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Specify the paths to your files
file_path1 = r'G:\omidh\Downloads\following.json'
file_path2 = r'G:\omidh\Downloads\followers_1.json'

# Load the data from the files
data1 = load_json_file(file_path1)
data2 = load_json_file(file_path2)

def create_sets(data1, data2):
    set1 = set()
    set2 = set()

    # Navigate through data1 and add values to set1
    for index in range(len(data1['relationships_following'])):
        set1.add(data1['relationships_following'][index]['string_list_data'][0]['value'])
    for index in range(len(data2)):
        set2.add(data2[index]['string_list_data'][0]['value'])
    return set1, set2

# Use the function with your data
set1, set2 = create_sets(data1, data2)

def difference(set1,set2):
    return set1 - set2

# Get the difference between the two sets
fuckers = difference(set1, set2)
