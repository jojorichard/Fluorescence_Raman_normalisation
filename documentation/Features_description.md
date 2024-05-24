# ⚡Fluorescence spectroscopy analysis⚡

## :warning: WARNING :warning:
The dataframe containing the EEM matrice needs to be specifically standardised to ensure the proper package's functioning. Please refer to the [Implementation](https://github.com/jojorichard/Fluorescence_Raman_normalisation/blob/main/documentation/Implementation_of_a_new_file_format.md) to see the required form. 

## 💡Main features 💡

### 🔭 Read and standardise the spectrometer's Excel file

This function reads a raw Excel file and arrange the data in a DataFrame that can be read by the other functions.
```
read_excel(path = False)
```
This function converts the excel file into a standardised DataFrame by taking the filepath from the read_eem function.
If there is an error while excecuting the read_eem function, it is possible to manually enter the filepath (specified form: path ='user/username/example.xlsx')
It is important to note that the present function only works for excel files of a specific form.

For any other type of file, one could use the pathfile from the read_eem function and create a new function to convert file into a standardised DataFrame. Please refer to [Implementation](https://github.com/jojorichard/Fluorescence_Raman_normalisation/blob/main/documentation/Implementation_of_a_new_file_format.md). 

### 🧾EEM matrice normalisation

This function normalises the EEM matrix according to the area of the Raman peak of water computed for 350 nm exitation waveleght and emission from 371 nm to 428 nm according to the following paper:
    Lawaetz, A. J., & Stedmon, C. A. (2009). Fluorescence Intensity Calibration Using the Raman Scatter Peak of Water. Applied Spectroscopy, 63(8), 936-940. 
    https://journals.sagepub.com/doi/10.1366/000370209788964548
```
fluo_raman_norm(eem, blank = False)
```
This function has for arguments the EEM matrix converted into a DataFrame. 
It can, optionally consider the blank measure.

This function calls two other functions : Area and Raman_normalisation (described below).

### ✂️Remove Rayleigh scattering of first and/or second order

This function has for argument the standardised DataFrame removes the Rayleigh scattering.
The Rayleigh scatteing are removed according the following paper:	Anal. Methods, 2013,5, 6557-6566, https://pubs.rsc.org/en/content/articlelanding/2013/ay/c3ay41160e
```
remove_rayleigh_scattering(eem, order=1, width=10)
```
The order can be specified by calling the function with order = 1 or order = 2, order = 'both'.

The width of the removed band can me specified by calling the function with width = values. Default width set to 10.

This step allows for a better data visualisation.

## 💡Complementary features 💡

### 📈 Function to plot a specific excited wavelength (graph)
This function plots fluorescence data on a standard graph and/or an interactive graph, depending on the users choices.
```
plot_fluorescence_graph(eem)
```   
This function prompts the user to provide the excitation wavelength of interest in nanometers (nm) to label the curve on the graph and to select the values of interest. Then, it plots the fluorescence data on a standard graph and/or an interactive graph using Plotly.
### 📈 Function to plot several excited wavelength (graph)
This function plots a superposition of several excited wavelenghts on a standard graph and, if wanted, an interactive graph.   
 ```    
plot_superimposed_graphs(eem, eem1 = False, eem2 = False, eem3 = False, eem4 = False, eem5 = False, eem6 = False)
``` 
This function prompts the user to enter the values for each curve. It then collects the excited wavelengths of interest to label the graph. It plots a static graph and, if wanted, an interactive graph showing the superimposed curves.

### 💫 File's upload 
This function uploads the file, find the filepath and retrun it.
```
read_eem()
```   
The function (containing 6 sub-functions) opens a Tkinter window for selecting an Excel file, displays its contents in DataFrame, 
and asks the user for confirmation on the data display.✅ ❌

It is important to note that if the file is not under the excel format, the function will only return the path without displaying its contents.

**▶ Window to upload the excel file and dataframe display**

This function handles the file upload process and displays the contents converted in DataFrame if it's an Excel file.

```
_handle_upload()
```
The function returns the filepath (str) or None if no file is selected.

It is important to note that the function returns the filepath of any file regardless of its type; only a excel file's contents (converted in DataFrame) is displayed. 

**🔬 Content display and confirmation on the data display**

The function displays the DataFrame (converted from the uploaded excel file) and asks the user's confirmation on the correct or incorrect dataframe display.
```
_process_excel_file()
```
This function is called in the _handle_upload() function above. It asks the user's confirmation (yes/no) before continuing the code.

It is important to note that a ValueError is raised if the user's answer is "no" as the code left will not work appropriately.

This function is called in _handle_upload() function.

**✅ Successful upload**

The function prints "successful upload" in the GUI upon successful upload.
```
_display_success_message()
```   
The message is written in green at the botton of the upload window.

This function is called in _handle_upload() function.

**✅ Successful upload for non-excel files**

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

The function prints the filepath to the console once the file is uploaded.
```
print_file_path()
```   
It is important to check whether the correct filepath was printed to ensure a smooth continuation.


### 🧮Calculation of the area of water's Raman peak

This functions calculates the area of the water's Raman peak computed for 350 nm excitation wavelenght, and emission from 371 nm to 428 nm, according to the following paper:
    Lawaetz, A. J., & Stedmon, C. A. (2009). Fluorescence Intensity Calibration Using the Raman Scatter Peak of Water. Applied Spectroscopy, 63(8), 936-940.
    https://journals.sagepub.com/doi/10.1366/000370209788964548
```
Area(eem, blank = False)
```
This functions has for arguments: EEM matrice converted into a DataFrame and the blank.
If the blank (water) is in another file, it can be uploaded and converted into a DataFrame and specified as follow: blank = DataFrame

The integral is computed using the trapezoidal rule.

### 📐Raman normalisation

This functions normalises the EEM matrice by dividing the values by the area.
```
Raman_normalisation(eem, Area)
```
This functions has for arguments: EEM matrix converted into a DataFrame and the area of the water raman peak

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

