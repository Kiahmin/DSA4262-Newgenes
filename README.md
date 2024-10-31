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

Python version $\geq 3.8$
   
## Setting Up

Please follow the steps below carefully to ensure the model runs smoothly.

### Machine Setup

1. Launch a *new* ubuntu instance with a minimum of *t3.large* to ensure the model runs efficiently and avoids code  termination.

2. Open terminal window on your local machine.

3. If your `.pem` key file is in a different directory, navigate to that location using `cd`:

```bash
cd /path/to/your-key-file
```
4. (if any) Set appropriate permissions to ensure security with SSH:

```bash
chmod 400 your-key-file.pem
```
5. Use the SSH command to connect, replacing `<username>`, `your-key-file.pem` and `<InstanceIPAddress>` with your instance details:

```bash
ssh -i your-key-file.pem <username>@<InstanceIPAddress>
```
* For Ubuntu instance, `<username>` is typically `ubuntu`.

Example:

```bash
ssh -i my-key-file.pem ubuntu@54.123.45.67
```

### Cloning Repository

To clone the repository, enter the following command in the terminal:

```bash
git clone https://github.com/Kiahmin/DSA4262-Newgenes.git
```
After cloning, you should see a new folder named `DSA4262-Newgenes` in your directory. Verify its creation by running the `ls` command. 

### Install Software / Packages

Once the repository has been successfully cloned, run the following commands to install the required software and packages. 

1. **Installing `pip`** (if Python is not already installed on your instance)

```bash
sudo apt install python3-pip
```
Note that when prompted for confirmation, please enter "*y*"

2. **Installing packages required**

Make sure you are inside the `DSA4262-Newgenes` folder by running:

```bash
cd DSA4262-Newgenes
```
Then, install the required packages by running:

* If you are on Windows, use:

```bash
pip install -r requirements.txt
```

* If you are on macOS or Linux, use:

```bash
pip3 install -r requirements.txt
```

Once the packages are installed, you are all set to start running the training/predictions for the model!

### Running Model

Ensure that you have completed all the steps above before attempting to run the model.

The instructions for running the model can be found <a href="./model/" target="_blank">here</a>

### Team Members
1. Felicia Mah Min Yi
2. Goh Xin Yi
3. How Kiah Min
4. Lim Kai Sin
5. Yong Zhi Yi








