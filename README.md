# ⚡ Fluorescence spectroscopy analysis ⚡

This package is a tool for processing Excitation Emission Matrix (EEM). It includes several functions such as fluorescence normalisation based on the Raman peak of water. The ability to remove the first and second order Rayleigh scattering and the plotting of several graphs ranging from 2D graphs of excitation wavelengths against fluorescence to 3D contourplots or surfaceplots for data visualisation.

![Graphique](https://github.com/jojorichard/Fluorescence_Raman_normalisation/assets/160777950/dc2cf7c0-6011-45c3-bb12-784114e40ce0)


## :notebook_with_decorative_cover: Documentation
  - ![Description of all the features](https://github.com/jojorichard/Fluorescence_Raman_normalisation/blob/main/documentation%20/Features_description.md)
  - ![Implementation of a new file format](https://github.com/jojorichard/Fluorescence_Raman_normalisation/blob/main/documentation%20/Implementation_of_a_new_file_format.md)
  - ![How to use the package](https://github.com/jojorichard/Fluorescence_Raman_normalisation/blob/main/documentation%20/How_to_use_the_package.md)
  - ![Notebook](https://github.com/jojorichard/Fluorescence_Raman_normalisation/blob/main/notebook/project_report.ipynb)
    
## ⚙️ Installation
```
pip install git+https://github.com/jojorichard/EEM.git
```

## 🛠️ Development installation
Clone this repository locally from GitHub:
```
git clone https://github.com/jojorichard/Fluorescence_Raman_normalisation.git .
```
Then add and commit changes as usual. 
Contributions from third parties or the implementation of the reading of a file format not yet supported are of course welcome. To see how to implement support for the new format, refer to "Implementation of a new file format" in the documentation section.

## 🔎 Run test and coverage
```
(conda_env) $ pip install tox
(conda_env) $ tox
```
## 🔌 Generate coverage badge
Works after running tox
```
(conda_env) $ pip install "genbadge[coverage]"
(conda_env) $ genbadge coverage -i coverage.xml
```


## 📫 Reaching us 
Justine Serra : justine.serratosio@gmail.com

Coralie Reuse : coralie.reuse23@gmail.com

Jonas Richard : jonas.richard@hotmail.fr
## ✒️ License
This code is published under the ![MIT LICENSE](https://github.com/jojorichard/Fluorescence_Raman_normalisation/blob/main/LICENSE)
