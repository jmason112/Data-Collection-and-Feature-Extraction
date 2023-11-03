#!/usr/bin/env python3

def read_features_csv(file_path):
    unique_features = set()
    progress_counter = 0

    with open(file_path, 'r') as csv_file:
        for line in csv_file:
            features = line.strip().split(',')[1:-1]
            for feature in features:
                # Check if the feature is already in the unique_features set
                if not any(existing_feature[:10] == feature[:10] for existing_feature in unique_features):
                    # Combine similar features
                    for existing_feature in unique_features.copy():
                        if existing_feature[:10] == feature[:10]:
                            unique_features.remove(existing_feature)
                            feature = existing_feature.split()[0] + ' ' + feature.split()[-1]
                            break
                    unique_features.add(feature.strip())
            progress_counter += 1
            print(f'Processed {progress_counter} lines')


    # Delete repeated lines that match other lines before the "(" symbol by comparing only the first 10 characters
    unique_lines = []
    for feature in unique_features:
        if not any(existing_line[:10] == feature[:10] for existing_line in unique_lines):
            unique_lines.append(feature)

    return unique_lines

def write_feature_list_txt(file_path, unique_features):
    with open(file_path, 'w') as txt_file:
        for feature in sorted(unique_features):
            txt_file.write(f'{feature}\n')

features_csv_path = 'features.csv'
feature_list_txt_path = 'feature-list.txt'

unique_features = read_features_csv(features_csv_path)
write_feature_list_txt(feature_list_txt_path, unique_features)
