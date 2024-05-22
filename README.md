# ⚡ Fluorescence spectroscopy analysis ⚡

This package is a tool for processing Excitation Emission Matrix (EEM). It includes several functions such as fluorescence normalisation based on the Raman peak of water. The ability to remove the first and second order Rayleigh scattering and the plotting of several graphs ranging from 2D graphs of excitation wavelengths against fluorescence to 3D contourplots or surfaceplots for data visualisation.
![Graphique](https://github.com/jojorichard/Fluorescence_Raman_normalisation/assets/160777950/dc2cf7c0-6011-45c3-bb12-784114e40ce0)


## :notebook_with_decorative_cover: Documentation
  - 
## ⚙️ Installation
Create a new environment, you may also give the environment a different name.
```
conda create -n fluo python=3.10 
```
```
conda activate fluo
```
If you need jupyter lab, install it

```
(fluo) $ pip install jupyterlab
```
## 🛠️ Development installation
Initialize Git (only for the first time).

Note: You should have create an empty repository on https://github.com:_ _ _pschwllr/fluo_ _ _.
```
git init
git add * 
git add .*
git commit -m "Initial commit" 
git branch -M main
git remote add origin git@github.com:_ _ _pschwllr/fluo_ _ _.git 
git push -u origin main
```
Then add and commit changes as usual.

To install the package, run
```
(fluo) $ pip install -e "._ _ _[test,doc]"_ _ _
```
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
## 📄 Testing
Models and results can be found _ _ _here_ _ _. -> mettre un lien qui renvoie à un document à télécharcher
## 💡Features


### 💫 File's upload 
The function uploads the file, find the pathfile and retrun it.
```
read_eem()
```   
The function (containing 6 sub-functions) opens a Tkinter window for selecting an Excel file, displays its contents in dataframe, 
and asks the user for confirmation on the data display.✅ ❌

It is important to note that if the file is not under the excel format, the function will only return the path without displaying its contents.

### 🔭 Normalised dataframe
The function converts the file into normalised dataframe and prints it.
```
read_excel()
```
The function converts the excel file into dataframe by taking the pathfile form the above function and converts it in normalised dataframe.

It is important to note that the present function only works  for excel files of a specific spectrometer.

For any other type of file, one could use the pathfile form the above function and converts it dataframe. 

### Caluclation of the Area
Take a dataframe and/or a blank and do the normalisation of the data
```
fluo_raman_norm(eem, blank = False):
```

### function's name
The function in one sentence
```
copy paste
```
Details
### function's name
The function in one sentence
```
copy paste
```
Details
### function's name
The function in one sentence
```
copy paste
```
Details

The description of the complementary features can be found under ![features description.](https://github.com/jojorichard/Fluorescence_Raman_normalisation/blob/main/Features_description.md)
## 📫 Reaching us 
Justine Serra : justine.serratosio@gmail.com

Coralie Reuse : coralie.reuse23@gmail.com

Jonas Richard : jonas.richard@hotmail.fr
## ✒️ License
This code is published under the ![MIT LICENSE](https://github.com/jojorichard/Fluorescence_Raman_normalisation/blob/main/LICENSE)
