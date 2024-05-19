
import os
import json
import csv
from tqdm import tqdm


base_path = "C:/work/SweetData-master/SweetData-master/Codeforces-Submissions"
cpp_data = []
java_data = []

all_files = [os.path.join(root, file) for root, _, files in os.walk(base_path) for file in files if file.endswith(('.cpp', '.java'))]

for file_path in tqdm(all_files, desc='Processing files'):
    json_path = file_path.rsplit('.', 1)[0] + '.json'
    
    try:
        with open(json_path, 'r') as json_file:
            metadata = json.load(json_file)
            tags = metadata.get('Tags', [])
            
            try:
                with open(file_path, 'r', encoding='utf-8') as code_file:
                    code = code_file.read()
            except UnicodeDecodeError:
                with open(file_path, 'r') as code_file:
                    code = code_file.read()
            
            row = {'Code': code, 'Tags': ','.join(tags)}
            
            if file_path.endswith('.cpp'):
                cpp_data.append(row)
            else:
                java_data.append(row)
    except FileNotFoundError:
        # If the JSON file does not exist, skip this file
        continue

# CSV file names
cpp_csv_file = "C:/Users/Alex/Downloads/cpp_solutions.csv"
java_csv_file = "C:/Users/Alex/Downloads/java_solutions.csv"

with open(cpp_csv_file, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Code', 'Tags']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for data in cpp_data:
        writer.writerow(data)

with open(java_csv_file, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Code', 'Tags']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for data in java_data:
        writer.writerow(data)
