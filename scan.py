#!/usr/bin/env python3

import os
import hashlib
import re

def md5_hash(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
        md5 = hashlib.md5(data).hexdigest()
    return md5

def extract_features(output):
    features = []
    lines = output.splitlines()
    for i, line in enumerate(lines):
        if line.startswith('namespace'):
            feature = lines[i - 1].strip()
            features.append(feature)
    return ', '.join(features)

def scan_files(folders):
    total_files = 0
    processed_files = 0

    for folder_path in folders:
        for root, _, files in os.walk(folder_path):
            total_files += len(files)

    with open('features.csv', 'w') as csv_file:
        for folder_path in folders:
            for root, _, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    try:
                        md5 = md5_hash(file_path)
                        output = os.popen(f'./capa {file_path} -v').read()
                        features = extract_features(output)
                        csv_file.write(f'{md5}, {features}\n')
                        processed_files += 1
                        print(f'Processed file {processed_files}/{total_files}')
                    except Exception as e:
                        print(f'Error processing file: {file_path}')
                        print(e)

folder_path_benignware = '/home/osboxes/Downloads/malware_data_science/ch8/data/benignware/'
folder_path_malware = '/home/osboxes/Downloads/malware_data_science/ch8/data/malware/'

scan_files([folder_path_benignware, folder_path_malware])





