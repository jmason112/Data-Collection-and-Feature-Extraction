#!/usr/bin/env python3

import csv

def read_feature_list_txt(file_path):
    with open(file_path, 'r') as txt_file:
        features = [line.strip() for line in txt_file]
    return features

def encode_features_csv(input_csv, feature_list, output_csv):
    with open(input_csv, 'r') as in_csv, open(output_csv, 'w', newline='') as out_csv:
        csv_reader = csv.reader(in_csv)
        csv_writer = csv.writer(out_csv)

        # Write header
        header = ['md5hash'] + feature_list + ['label']
        csv_writer.writerow(header)

        # Process each line in features.csv
        for row in csv_reader:
            md5hash = row[0]
            features = [feature.strip() for feature in row[1:-1] if feature]
            label = row[-1]

            encoded_features = [1 if feature in features else 0 for feature in feature_list]
            new_row = [md5hash] + encoded_features + [label]
            csv_writer.writerow(new_row)
            print(f'Processed {md5hash}')

features_csv_path = 'features.csv'
feature_list_txt_path = 'feature-list.txt'
dataset_csv_path = 'dataset.csv'

feature_list = read_feature_list_txt(feature_list_txt_path)
encode_features_csv(features_csv_path, feature_list, dataset_csv_path)
