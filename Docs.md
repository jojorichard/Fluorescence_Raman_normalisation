# ⚡Fluorescence spectroscopy analysis⚡

## 💡Main features

## 💡Complementary features

### 📈 Function to plot a specific excited wavelength on a graph
This function plots fluorescence data on a standard graph and/or an interactive graph, depending on the users choices.
```
plot_fluorescence_graph()
```   
This function prompts the user to provide the excitation wavelength of interest in nanometers (nm) to label the curve on the graph and to select the values of interest. It then plots the fluorescence data on a standard graph and/or an interactive graph using Plotly.
### 📈 Function to plot several excited wavelength on a graph
This function plots a superposition of several excited wavelenghts on a standard graph and, if wanted, an interactive graph.   
 ```    
plot_superimposed_graphs()
``` 
This function prompts the user to input the number of graphs they want to superimpose. It then collects data for each graph, including file location, sheet name on Excel, column names for excitation and emission wavelengths, and the excited wavelengths of interest to label the graph. It plots a static graph and, if wanted, an interactive graph showing the superimposed curves.

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

**▶ Windows to upload the excel file (upload button)**

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

**💯 Excel upload and dataframe conversion**

This function handles the file upload process triggered by the 'Upload' button click created by the above function and converts the content into dataframe.
```
_handle_upload(self)
```   
The argument of the function is self which is a reference to the current instance of the class (ExcelFileUploaderAndConverter).
The function also displays several message changing depending on the possible events of the uploading process.
It is important to note that this function is the second of the class (ExcelFileUploaderAndConverter).

**🔭 Content display**

The function displays the dataframe (converted from the uploaded excel file).
```
_process_excel_file(self)
```   
The argument of the function is self which is a reference to the current instance of the class (ExcelFileUploaderAndConverter).
It is the third function of the class (ExcelFileUploaderAndConverter).
Returns the dataframe.

**✅ Successful upload**

The function prints "successful upload" if the upload was well processed.
```
_display_success_message(self)
```   
The argument of the function is self which is a reference to the current instance of the class (ExcelFileUploaderAndConverter).
It is the fourth function of the class (ExcelFileUploaderAndConverter).
Returns the successful upload message. 

**❌ Unsuccessful upload**

The function prints "unsuccessful upload" if the upload was not well processed.
```
_display_error_message(self)
```
The argument of the function is self which is a reference to the current instance of the class (ExcelFileUploaderAndConverter).
It is the fifth function of the class (ExcelFileUploaderAndConverter).
Returns the unsuccessful upload message.
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
