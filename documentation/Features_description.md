# ⚡Fluorescence spectroscopy analysis⚡

## :warning: WARNING :warning:
The dataframe containing the EEM matrice needs to be specifically standardised to ensure the proper package's functioning. Please refer to the "Implementation of a new file format.md" to see the form required. 

## 💡Main features 💡

### 🔭 Read and standardise the spectrometer's Excel file
The function reads a raw Excel file and rearrange the data in a DataFrame that can be read by the other function.
```
read_excel(path = False)
```
The function converts the excel file into dataframe by taking the pathfile form the read_eem function and converts it in a standardised dataframe.
If there is an error while excecuting the read_eem function it is possible to input the path file manually by specifing it as follow  path ='user/username/example.xlsx'
It is important to note that the present function only works  for excel files of a specific spectrometer.

For any other type of file, one could use the pathfile form the above function and converts it dataframe please refer to "Implementation of a new file format.md". 

### 🧾Normalisation of an EEM matrice
Take a dataframe of an EEM matrice and optionally a blank and normalise the EEM matrice according to the Area of the Raman peak of water computed for 350 nm exitation waveleght and emission from 371 nm to 428 nm according to the following paper:
    Lawaetz, A. J., & Stedmon, C. A. (2009). Fluorescence Intensity Calibration Using the Raman Scatter Peak of Water. Applied Spectroscopy, 63(8), 936-940. 
    https://journals.sagepub.com/doi/10.1366/000370209788964548
```
fluo_raman_norm(eem, blank = False)
```
The function calls two other function. Area and Raman_normalisation described in the next section.

### ✂️Remove Rayleigh scattering of first and/or second order
Take a dataframe of an EEM matrice and remove the Rayleigh scattering for a beter visualisation in the graph.
The Rayleigh scatteing are removed according the following paper:	Anal. Methods, 2013,5, 6557-6566, https://pubs.rsc.org/en/content/articlelanding/2013/ay/c3ay41160e
```
remove_rayleigh_scattering(eem, order=1, width=10)
```
The order can be specified by calling the function with order = 1 or order = 2, order = 'both'.
The width of the band that is removed can me specified by calling the function with width = values. Default width set to 10

## 💡Complementary features 💡

### 📈 Function to plot a specific excited wavelength on a graph
This function plots fluorescence data on a standard graph and/or an interactive graph, depending on the users choices.
```
plot_fluorescence_graph(eem)
```   
This function prompts the user to provide the excitation wavelength of interest in nanometers (nm) to label the curve on the graph and to select the values of interest. It then plots the fluorescence data on a standard graph and/or an interactive graph using Plotly.
### 📈 Function to plot several excited wavelength on a graph
This function plots a superposition of several excited wavelenghts on a standard graph and, if wanted, an interactive graph.   
 ```    
plot_superimposed_graphs()
``` 
This function prompts the user to upload the values for each curve. It then collects the excited wavelengths of interest to label the graph. It plots a static graph and, if wanted, an interactive graph showing the superimposed curves.

### 💫 File's upload 
The function uploads the file, find the pathfile and retrun it.
```
read_eem()
```   
The function (containing 6 sub-functions) opens a Tkinter window for selecting an Excel file, displays its contents in dataframe, 
and asks the user for confirmation on the data display.✅ ❌
It is important to note that if the file is not under the excel format, the function will only return the path without displaying its contents.

**▶ Window to upload the excel file and dataframe display**

The function handles the file upload process and displays the contents converted in dataframe if it's an Excel file.

```
_handle_upload()
```
The function returns the pathfile (str) or None if no file is selected.

It is important to note that the function returns the pathfile of any file regardless of its type; only a excel file's contents (converted in dataframe) is displayed. 

**🔬 Content display and confirmation on the data display**

The function displays the dataframe (converted from the uploaded excel file) and asks the user's confirmation on the correct or incorrect dataframe display.
```
_process_excel_file()
```
This function is called in the _handle_upload() function above. It asks the user's confirmation (yes/no) before continuing reading the code.

It is important to note that a ValueError is raised if the user's answer is "no" as the code left will not work appropriately.

This function is called in _handle_upload() function.

**✅ Successful upload**

The function prints "successful upload" in the GUI upon successful upload.
```
_display_success_message()
```   
The message is written in green at the botton of the upload window.

This function is called in _handle_upload() function.

**✅ Successful upload for non excel files**

The function displays "successful upload" in the GUI upon successful for non-Excel files in the GUI.
```
_display_success_message_no_conversion()
```   
The message is written in green at the botton of the upload window.

This function is called in _handle_upload() function.

**❌ Unsuccessful upload**

The function displays in the GUI "unsuccessful upload" upon failed uplaod. 
```
_display_error_message()
```
The message is written in red at the botton of the upload window.

This function is called in _handle_upload() function.

**🎥 Filepath print**

The function prints the filepath to the console oncce the file is uploaded.
```
print_file_path()
```   
It is important to check whether the correct filepath was printed to ensure a smooth continuation.


### 🧮Calculation of the area of water's Raman peak
Take a dataframe of an EEM matrice or a blank and calculate the Area of the water Raman peak computed for 350 nm exitation waveleght and emission from 371 nm to 428 nm according to the following paper:
    Lawaetz, A. J., & Stedmon, C. A. (2009). Fluorescence Intensity Calibration Using the Raman Scatter Peak of Water. Applied Spectroscopy, 63(8), 936-940.
    https://journals.sagepub.com/doi/10.1366/000370209788964548
```
Area(eem, blank = False)
```
If the blank (water) is on a other file the file can be load in a dataframe and specified as follow blank = DataFrame
The integral is computed using the trapezoidal rule.

### 📐Raman normalisation
Take a dataframe of an EEM matrice and the Area of the water raman peak calculated with the Area function and normalise the EEM matrice by dividing the values with the area.
```
Raman_normalisation(eem, Area)
```

### 📉Plot contour graph
Take a dataframe of an EEM matrice and plot a contour graph
```
plot_3D_contour(eem, levels = 25, Normalisation = True)
```
 Plot an 3D contour graph with the folowing axes:
        - x: the emmited wavelenght in nm
        - y: the exitation wavelenght in nm
        - z: the intensity in a.u or R.u depending if the data are normalised or not

The number of levels showed in the graph can be changed by specify a number with levels = number. The default values of levels is set to 25. Note that a high levels value may affect the legibility of the graph. 
The Normalisation argument can be specified to be False if the function is called with an non normalised EEM matrice. It allows to label correctly the fluorescence axes.

### 📉Plot an interactive contour graph 
Take a dataframe of an EEM matrice and plot an interactive contour graph
```
plot_3D_contour_inter(eem, levels = 30, Normalisation = True)
```
 Plot an 3D contour graph with the folowing axes:
        - x: the emmited wavelenght in nm
        - y: the exitation wavelenght in nm
        - z: the intensity in a.u or R.u depending if the data are normalised or not

The number of levels showed in the graph can be changed by specify a number with levels = number. The default values of levels is set to 25. Note that a high levels value may affect the legibility of the graph. 
The Normalisation argument can be specified to be False if the function is called with an non normalised EEM matrice. It allows to label correctly the fluorescence axes.

### 📉Plot an interactive surface graph
Take a dataframe of an EEM matrice and plot an interactive contour graph
```
plot_3D_surface_inter(eem, Normalisation = True)
```
 Plot an 3D surface interactive graph with the folowing axes:
        - x: the emmited wavelenght in nm
        - y: the exitation wavelenght in nm
        - z: the intensity in a.u or R.u depending if the data are normalised or not

The Normalisation argument can be specified to be False if the function is called with an non normalised EEM matrice. It allows to label correctly the fluorescence axes.
