# notebooks
Computational analysis of LibCrowds data
# notebooks

> Computational analysis of LibCrowds data

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/LibCrowds/notebooks/master?urlpath=lab)

The Jupyter notebooks contained in this repository explore the data created
via the LibCrowds platform.

## Visit the lab

To work with interactive versions of the notebooks, visit the following URL:

https://mybinder.org/v2/gh/libcrowds/notebooks/master?urlpath=lab

The notebooks are located in the `/notebooks` folder.

## Contents

1. [An Introduction to Analysing In the Spotlight Data Using Python](https://nbviewer.jupyter.org/github/LibCrowds/notebooks/blob/master/notebooks/intro_to_analysing_its_data_using_python.ipynb)

## Build setup

``` bash
# install core dependencies
pip install -r requirements.txt

# install Jupyter extensions
jupyter labextension install @jupyterlab/plotly-extension

# run
jupyter lab
```
