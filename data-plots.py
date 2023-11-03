#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset into a DataFrame
df = pd.read_csv('dataset.csv')

# Filter the DataFrame by the label column
df_benign = df[df['label'] == 0]
df_malware = df[df['label'] == 1]

# Create a figure with two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Create a bubble plot for benign files
ax1.scatter(df_benign.index, range(len(df_benign)), s=100, alpha=0.5, c='blue')
ax1.set_xlabel('benign features')
ax1.set_ylabel('malware features')
ax1.set_title('Bubble Plot for Benign Files')
ax1.grid(True)

# Create a bubble plot for malware files
ax2.scatter(df_malware.index, range(len(df_malware)), s=100, alpha=0.5, c='red')
ax2.set_xlabel('malware features')
ax2.set_ylabel('benign features')
ax2.set_title('Bubble Plot for Malware Files')
ax2.grid(True)

# Display the plots
plt.show()
