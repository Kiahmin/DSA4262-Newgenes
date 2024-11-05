# Neural Network Model
## Table of Content: 

- [Folder Structure](#folder-structure)
- [Setup for Model Testing](#setup-for-model-testing)
- [Requirements](#requirements)
  
## Folder Structure 

```
├── train
│   ├── neural_network
├── test
│   ├── function 
│   ├── main
└── data
```

- `train`: Contains files related to model training.
  - `neural_network`: Jupyter notebook with code for training the model and generating plots.

- `test`: Contains scripts for testing and evaluation.
  - `function`: Contains custom functions for model training and evaluation.
  - `main`: The main script to run and test the model.

- *`data`*: Directory with sample data files, including datasets or input files required to run the model.

## Setup for Model Testing

1. Navigate to directory:
   ```bash
   cd model/test

2. Generate predictions:
   ```bash
   python3 main.py

3. Check results(optional):
   ```bash
   cd ../data
   cat sample_predictions.csv

## Requirements
Refer <a href="../requirements.txt/" target="_blank">here</a>
