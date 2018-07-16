# LibCrowds Notebooks

> Computational analysis of LibCrowds data.

The Jupyter notebooks contained in this repository explore the data created
via the LibCrowds platform. To work with interactive versions of the notebooks,
visit the following URL:

https://mybinder.org/v2/gh/libcrowds/notebooks/master?urlpath=lab

The notebooks are located in the `/notebooks` folder.

## Contents

1. [An Introduction to Analysing In the Spotlight Data Using Python](https://nbviewer.jupyter.org/github/LibCrowds/notebooks/blob/master/notebooks/intro_to_analysing_its_data_using_python.ipynb)
2. [An Introduction to Visualising In the Spotlight Data Using Python](https://nbviewer.jupyter.org/github/LibCrowds/notebooks/blob/master/notebooks/intro_to_visualising_its_data_using_python.ipynb)

#### Appendicies
[Appendix A: Loading PYBOSSA Tasks into a Dataframe](https://nbviewer.jupyter.org/github/LibCrowds/notebooks/blob/master/notebooks/loading_pybossa_tasks_into_a_dataframe.ipynb)

## Build setup

``` bash
# install core dependencies
pip install -r requirements.txt

# install Jupyter extensions
jupyter labextension install @jupyterlab/plotly-extension

# raise memory limit
export NODE_OPTIONS=--max-old-space-size=4096

# install Jupyter extensions
jupyter labextension install @jupyter-widgets/jupyterlab-manager
jupyter labextension install plotlywidget

# run
jupyter lab
```
