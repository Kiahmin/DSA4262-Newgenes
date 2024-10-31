import pandas as pd
import torch
import torch.nn as nn
from sklearn.preprocessing import StandardScaler
import json
import gzip

# parse the features

def parse_features(feature_file_path):
    rows = []

    with gzip.open(feature_file_path, 'rt', encoding='utf-8') as file:
        for line in file:
            data = json.loads(line)

            for transcript_id, positions in data.items():
                for position, flanking_data in positions.items():
                    for flanking_nucleotide, features_list in flanking_data.items():
                        for features in features_list:
                            row = {
                                "transcript_id": transcript_id,
                                "position": int(position),
                                "flanking_nucleotide": flanking_nucleotide,
                                "dwelling_time_(-1)": features[0],
                                "std_dev_(-1)": features[1],
                                "mean_signal_(-1)": features[2],
                                "dwelling_time_central": features[3],
                                "std_dev_central": features[4],
                                "mean_signal_central": features[5],
                                "dwelling_time_(+1)": features[6],
                                "std_dev_(+1)": features[7],
                                "mean_signal_(+1)": features[8]
                            }
                            rows.append(row)  # Append each parsed entry to rows

    return pd.DataFrame(rows)


# add and scale features

def preprocessing(df):
    processed_df = df.copy()
    processed_df['relative_position'] = processed_df['position'] / processed_df.groupby('transcript_id')['position'].transform('max')
    processed_df['dwelling_time_diff'] = processed_df['dwelling_time_(+1)'] - processed_df['dwelling_time_(-1)']
    processed_df['std_dev_diff'] = processed_df['std_dev_(+1)'] - processed_df['std_dev_(-1)']
 
    scaler = StandardScaler()

    numeric_columns = ['dwelling_time_(-1)', 'std_dev_(-1)', 'mean_signal_(-1)',
                       'dwelling_time_central', 'std_dev_central', 'mean_signal_central',
                        'dwelling_time_(+1)', 'std_dev_(+1)', 'mean_signal_(+1)',
                        'relative_position', 'dwelling_time_diff', 'std_dev_diff']

    processed_df[numeric_columns] = scaler.fit_transform(processed_df[numeric_columns])

    return processed_df

# encode the nucleotides

def encode_nucleotide(df):
    df = df.copy()

    # split into 7 columns
    nucleotides = df['flanking_nucleotide'].apply(lambda x: pd.Series(list(x)))
    nucleotides.columns = ['nucleotide_' + str(i) for i in range(7)]

    # encode the nucleotides
    nucleotides = nucleotides.replace({'A': 1, 'C': 2, 'G': 3, 'T': 4})

    # scale the encoded nucleotides
    scaler = StandardScaler()
    nucleotides_scaled = scaler.fit_transform(nucleotides)

    # concatenate the encoded nucleotides with the original dataframe
    df = pd.concat([df.reset_index(drop=True), pd.DataFrame(nucleotides_scaled, columns=nucleotides.columns)], axis=1)

    # drop the original nucleotide column
    df = df.drop('flanking_nucleotide', axis=1)
    
    return df

class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1 = nn.Linear(19, 32)
        self.layer2 = nn.Linear(32, 1)
        self.relu = nn.ReLU()
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.relu(self.layer1(x))
        x = self.sigmoid(self.layer2(x))
        return x