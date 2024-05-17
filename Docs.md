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

### 🔭 Normalised dataframe
The function converts the file into normalised dataframe and prints it.
```
read_excel()
```
The function converts the excel file into dataframe by taking the pathfile form the above function and converts it in normalised dataframe.
It is important to note that the present function only works  for excel files.
For any other type of file, one could use the pathfile form the above function and converts it dataframe. 


**🔭 Content display**

The function displays the dataframe (converted from the uploaded excel file).
```
_process_excel_file()
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