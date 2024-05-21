# ⚡ Fluorescence spectroscopy analysis ⚡

![spectre 3D](https://github.com/jojorichard/Fluorescence_Raman_normalisation/assets/160879372/894e23a3-ff94-4a60-85b4-d2d7a1648a05)

**J'ai juste recopié l'exemple du prof, faudra voir si on ajoute / enlève des trucs ou pas !!!**

**J'ai mis en _ _ _évidence_ _ _ comme ça ce qu'il faudra encore modifier / adapter**

💫 💦 💥 💯 🗯️ 🧭 🚨 ☎️ 👩‍💻 👨‍💻
📝📉📊📌📍✂️📏 ▶

## 🎯 Content in a nutshell
This project has for aim to analyse the fluorescence of water thanks to fluorescence spectroscopy. This special type of spectroscopy is based on the different excited wavelengths emitted by the solution. The results will be analysed thanks to the different Raman cross section of water which will vary depending on the content of the solution. 

The following program will normalize the values thanks to the Raman cross section of water which will serve as a neutral measure. The normalisation area will be calculated for the excited wavelengths of choice and the graphs will be plotted and provided if wanted. 

This code will optimize the fluorescence values analysis by directly providing the normalisation area and graphs. 
## 🔥Usage
Concretley, your file (Excel for now) will be entered in the program by sliding it in to avoid lecture complications. Few questions will be asked throughout the process as to make it interactive and include personal preferences, from which the answers are required. For instance, the first and last measured excited wavelength or the step of the apparatus must necessarily and precisely be filled. Later, on the graphs will be plotted at one’s preference.  
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

It is important to note that the present function only works  for excel files.

For any other type of file, one could use the pathfile form the above function and converts it dataframe. 

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
