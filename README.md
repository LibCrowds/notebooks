# LibCrowds Notebooks

> Computational analysis of LibCrowds data.

The Jupyter notebooks contained in this repository explore the data created
via the LibCrowds platform. To work with interactive versions of the notebooks,
visit the following URL:

https://mybinder.org/v2/gh/libcrowds/notebooks/master?urlpath=lab

The notebooks are located in the `/notebooks` folder.

## Contents

1. [An Introduction to the LibCrowds Annotations Data Model](https://nbviewer.jupyter.org/github/LibCrowds/notebooks/blob/master/notebooks/intro_to_the_libcrowds_data_model.ipynb)

2. [An Introduction to Analysing In the Spotlight Data Using Python](https://nbviewer.jupyter.org/github/LibCrowds/notebooks/blob/master/notebooks/intro_to_analysing_its_data_using_python.ipynb)

3. [An Introduction to Visualising In the Spotlight Data Using Python](https://nbviewer.jupyter.org/github/LibCrowds/notebooks/blob/master/notebooks/intro_to_visualising_its_data_using_python.ipynb)

4. [Visualising In the Spotlight Data Over Time](https://nbviewer.jupyter.org/github/LibCrowds/notebooks/blob/master/notebooks/visualising_its_data_over_time.ipynb)

## Build setup

``` bash
# install dependencies
pip install -r requirements.txt

# raise memory limit
export NODE_OPTIONS=--max-old-space-size=4096

# install Jupyter extensions
jupyter labextension install @jupyter-widgets/jupyterlab-manager
jupyter labextension install plotlywidget

# run
jupyter lab
```
