# ⚡ Fluorescence Raman normalisation ⚡

![picture](https://github.com/jojorichard/Fluorescence_Raman_normalisation/assets/160879372/22fd9a95-884a-421d-abfe-041311cd3af8)
![Capture d'écran 2024-05-10 203345](https://github.com/jojorichard/Fluorescence_Raman_normalisation/assets/160879372/6c230a04-e5e5-43e0-9218-f44ae51f7aee)

**J'ai juste recopier l'exemple du prof, faudra voir si on ajoute / enlève des trucs ou pas !!!**

**J'ai mis en _ _ _évidence_ _ _ comme ça ce qu'il faudra encore modifier / adapter**

💫 💦 💥 💯 🗯️ 🧭 🚨 💡 📄

## 🎯 Content in a nutshell
The
## 🔥Usage
The
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
(ch200) $ pip install jupyterlab
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
## 📫☎️ Reaching us 👩‍💻👨‍💻
Justine Serra : justine.serratosio@gmail.com

Coralie Reuse : coralie.reuse23@gmail.com

Jonas Richard : jonas.richard@hotmail.fr
## ✒️ License
This code is published under the ![MIT LICENSE](https://github.com/jojorichard/Fluorescence_Raman_normalisation/blob/main/LICENSE)
