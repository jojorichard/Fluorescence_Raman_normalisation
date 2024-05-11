# ⚡ Fluorescence spectroscopy analysis ⚡

![picture](https://github.com/jojorichard/Fluorescence_Raman_normalisation/assets/160879372/22fd9a95-884a-421d-abfe-041311cd3af8)
![Capture d'écran 2024-05-10 203345](https://github.com/jojorichard/Fluorescence_Raman_normalisation/assets/160879372/6c230a04-e5e5-43e0-9218-f44ae51f7aee)
![spectre 3D](https://github.com/jojorichard/Fluorescence_Raman_normalisation/assets/160879372/894e23a3-ff94-4a60-85b4-d2d7a1648a05)

**J'ai juste recopié l'exemple du prof, faudra voir si on ajoute / enlève des trucs ou pas !!!**

**J'ai mis en _ _ _évidence_ _ _ comme ça ce qu'il faudra encore modifier / adapter**

💫 💦 💥 💯 🗯️ 🧭 🚨 💡 ☎️ 👩‍💻 👨‍💻

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
## 📫 Reaching us 
Justine Serra : justine.serratosio@gmail.com

Coralie Reuse : coralie.reuse23@gmail.com

Jonas Richard : jonas.richard@hotmail.fr
## ✒️ License
This code is published under the ![MIT LICENSE](https://github.com/jojorichard/Fluorescence_Raman_normalisation/blob/main/LICENSE)
