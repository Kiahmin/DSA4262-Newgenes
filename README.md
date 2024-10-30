# DSA4262 Genomics Project: Prediction of m6A RNA modifications from direct RNA-Seq data

This repository contains the codes that are created by Team Newgenes for the purposes of detecting m6A RNA modifications from direct RNA-Seq data. 

## Table of Content: 

- [Folder Structure](#folder-structure)
- [Software Requirements](#software-requirements)
- [Setting Up](#setting-up)
  - [Machine Setup](#machine-setup)
  - [Cloning Repository](#cloning-repository)
  - [Install Software / Packages](#install-software--packages)
- [Running Model](#running-model)
- [Team Members](#team-members)

## Folder Structure

```
.
├── archive/
│   ├── 
│   ├── 
│   ├── random_forest
│   └── SVM  
├── data/
│   ├── 
│   └── 
├── model/
└── requirements.txt
```
* `archive` - Contains all the previous codes / models that were previously tested.
*  `data` - Contains sample data file
*  `model` - Contains the final model and this should be used for testing the training and prediction process. 
*  `requirements.txt` - Contains the necessary Python libraries that must be installed on the machine for the model to function properly.

## Software Requirements 

## Setting Up

Please follow the steps below carefully to ensure the model runs smoothly.

### Machine Setup

Ubuntu Machine 

### Cloning Repository

To clone the repository to your device, enter the following command in the terminal:

```bash
git clone https://github.com/Kiahmin/DSA4262-Newgenes.git
```
Once cloning is complete, you should see a folder `DSA4262-Newgenes` created. 

### Install Software / Packages

Once the repository has been successfully cloned, run the following commands to install the required software and packages. 

1. **Installing `pip`**

```bash
sudo apt install python3-pip
```
Note that when prompted for confirmation, please enter "*y*"

2. **Installing packages required**

Ensure that you are within the `DSA4262-Newgenes` folder before executing the following command.

```bash
pip3 install -r requirements.txt
```

Once the packages are installed, you are ready to start running the training/predictions for the model!

### Running Model

### Team Members









