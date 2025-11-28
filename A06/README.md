# Graph plotter

This repository contains a script `graph.py` that creates a .png file containing a graph from values in graph.csv file with columns named x and y, where y is the cosine of x (y = cos(x)).

# Instructions to clone, set up, and run the script

## Clone the repository
```
git clone https://github.com/martinkovav/ci2.git
cd ci2/A06
```

## Create virtual environment
```
python3 -m venv venv
source venv/bin/activate
```
## Install required packages
```
pip3 install matplotlib
pip3 install pandas
pip3 install jupyter
```
## Run the script
```
python3 graph.py
```

This will create a .png file with y=cos(x) graph