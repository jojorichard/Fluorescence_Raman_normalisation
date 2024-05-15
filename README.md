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
## 💡Functions
### 📈 Function to plot a specific excited wavelength on a graph
This function plots fluorescence data on a standard graph and/or an interactive graph, depending on the users choices.
```
plot_fluorescence_graph():
```   
This function prompts the user to provide the file location, the sheet name on Excel, the names of the excitation and emission wavelength columns in an Excel file, and the excitation wavelength of interest in nanometers (nm) to label the curve on the graph. It then plots the fluorescence data on a standard graph and/or an interactive graph using Plotly.
### 📈 Function to plot several excited wavelength on a graph
This function plots a superposition of several excited wavelenghts on a standard graph and, if wanted, an interactive graph.   
 ```    
plot_superimposed_graphs():
``` 
This function prompts the user to input the number of graphs they want to superimpose. It then collects data for each graph, including file location, sheet name on Excel, column names for excitation and emission wavelengths, and the excited wavelengths of interest to label the graph. It plots a static graph and, if wanted, an interactive graph showing the superimposed curves.
### ↔️ Conversion coma to point (step)
The function converts the coma to a point if the step is given with a coma.
```
conversion_coma_point(step)
```   
The argument of the function is the step of the spectroscopy machine (given by the user).
The given step will be analysed and converted if necessary.

### 📝 List of the excited wavelengths considering the step of the spectroscopy machine
The function returns a list of the excited wavelengths depending on the step and its type (float or integer).
```
excited_wavelength_list(first, last, step)
```   
The arguments of the functions are the following and are asked beforehand to the user: the first and last excited wavelengths values measure and the step of the spectroscopy machine.
This function also takes into consideration the different types of values (only one decimal after the point, converts the float values ".0" in int) to ensure that the list contains the exact same values than in the excel file.
### ▶ Windows to upload the excel file (upload button)
Initialize the upload of the excel file by browsing through the user's computer through an window and upload button.
```
__init__(self, root)
```
The arguments of the function are defined as follows:
- self: A reference to the current instance of the class.
- root: An instance of the tkinter.Tk class representing the root tkinter window.

It is important to note that this function is the first one of the follwing class:
```
class ExcelFileUploaderAndConverter
```
### 💯 Excel upload and dataframe conversion
This function handles the file upload process triggered by the 'Upload' button click created by the above function and converts the content into dataframe.
```
_handle_upload(self)
```   
The argument of the function is self which is a reference to the current instance of the class (ExcelFileUploaderAndConverter).
The function also displays several message changing depending on the possible events of the uploading process.
It is important to note that this function is the second of the class (ExcelFileUploaderAndConverter).

### 🔭 Content display
The function displays the dataframe (converted from the uploaded excel file).
```
_process_excel_file(self)
```   
The argument of the function is self which is a reference to the current instance of the class (ExcelFileUploaderAndConverter).
It is the third function of the class (ExcelFileUploaderAndConverter).
Returns the dataframe.

### ✅ Successful upload
The function prints "successful upload" if the upload was well processed.
```
_display_success_message(self)
```   
The argument of the function is self which is a reference to the current instance of the class (ExcelFileUploaderAndConverter).
It is the fourth function of the class (ExcelFileUploaderAndConverter).
Returns the successful upload message. 
### ❌ Unsuccessful upload
The function prints "unsuccessful upload" if the upload was not well processed.
```
_display_error_message(self)
```
The argument of the function is self which is a reference to the current instance of the class (ExcelFileUploaderAndConverter).
It is the fifth function of the class (ExcelFileUploaderAndConverter).
Returns the unsuccessful upload message.
### 💫 Instantiation of the class
The main function to create the tkinter window and instantiate the ExcelFileUploaderAndConverter class.
```
def main()
```
This function takes onto consideration the response of the user. It starts the event loop which allows the tkinter application to become interactive, processing user input and updating the GUI in response to events. Once the event loop is started, the program will continue running until the user closes the main window or exits the application.
It is the sixth function of the class (ExcelFileUploaderAndConverter).

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

## 📫 Reaching us 
Justine Serra : justine.serratosio@gmail.com

Coralie Reuse : coralie.reuse23@gmail.com

Jonas Richard : jonas.richard@hotmail.fr
## ✒️ License
This code is published under the ![MIT LICENSE](https://github.com/jojorichard/Fluorescence_Raman_normalisation/blob/main/LICENSE)
