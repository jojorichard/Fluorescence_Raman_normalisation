import numpy as np    
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import io
import tkinter as tk
from tkinter import filedialog

#Initial condition
a=input("Are your values in nanometers? If yes, write Yes, if not write No:")
if a== "Yes" or a=="yes":
    pass
else:
    raise ValueError("Please make sure your values are in nanometers otherwise the program doesn't work :)")
    
#step
step=input("Please insert the measure step of your spectroscopy machine (no unit needed):")





def conversion_coma_point(step):
    """
    This fonction converts the coma in a point so that python recognises the number under the float form.
    
    Parameters: the step previously entered.
    
    Returns: the initial step if it is an integer or in the float form or the step converted in float.
    """
    if "," in step:
        step = step.replace(",", ".")
        return step
    else:
        return step

step=conversion_coma_point(step)

#Raise ValueError if step<0

if float(step) < 0:
    raise ValueError("The step must be positive.")


#First and last excited wavelength values

first=int(input("Please insert the first excited wavelength value(no unit needed):"))
last=int(input("Please insert the last excited wavelength value(no unit needed):"))

# Raise ValueError if first>last
if first>last:
    raise ValueError("Your first value should be smaller than your last.")





def excited_wavelength_list(first, last, step):
    """
    This fonction creates a list with excited wavelengths in terms of the step, from the first value and last 
    entered value. It consists of two main parts: the first if the step is an integer, the other if the step ia a float.
    
    Parameters: first(int) and last (int) excited wavelengths value.
    
    Returns: a list of excited wavelength value in the exact where the integer values are in the form int, and the 
    others are in the form float.
    """

    
    # Conversion first, last, end in float
    first = float(first)
    last = float(last)
    step = float(step)
    
    l_x = []
    

    if isinstance(step, int):
        # If the step is an integer
        l_x = list(range(int(first), int(last) + 1, int(step)))
    else:
        # If the step is a float
        current = first
        while current <= last:
            rounded_current = round(current, 1)# Round the values with one decimal 
            if rounded_current.is_integer():
                l_x.append(int(rounded_current))# If the wavelengths is an integer,remove the coma  
            else:
                l_x.append(rounded_current)
            current += step
    
    return l_x
#excel file dataframe, file stored under the variable "file_contents


class ExcelFileUploaderAndConverter:
    """
    A class to upload and convert Excel files using a tkinter GUI.
    
    Attributes:
    - root (tk.Tk): The root tkinter window.
    - file_contents (pandas.DataFrame): The content of the uploaded Excel file.
    - uploaded_file: (None): Information about the uploaded file.
    - file_label (tk.Label): A label widget for displaying instructions to select a file.
    - upload_button (tk.Button): A button widget to trigger the file upload process.
    - output_text (tk.Text): A text widget to display the content of the uploaded file.
    - success_message_label (tk.Label): A label widget to display success messages.
    - error_message_label (tk.Label): A label widget to display error messages.
    """

    def __init__(self, root):
        """
        Initializes the ExcelFileUploaderAndConverter instance.
    
        Parameters:
        - root (tk.Tk): The root tkinter window.
        """
        # Initialize the class with a tkinter root window
        self.root = root
        self.file_contents = None
        self.uploaded_file = None

        # Create a label widget to prompt the user to select an Excel file
        self.file_label = tk.Label(self.root, text="Select an Excel file:")
        self.file_label.pack()

        # Create a button widget for uploading files, with a command to call _handle_upload method
        self.upload_button = tk.Button(self.root, text="Upload", command=self._handle_upload)
        self.upload_button.pack()

        # Create a text widget to display the content of the uploaded Excel file
        self.output_text = tk.Text(self.root)
        self.output_text.pack()

        # Create label widgets for displaying success and error messages
        self.success_message_label = tk.Label(self.root, text="")
        self.success_message_label.pack()

        self.error_message_label = tk.Label(self.root, text="")
        self.error_message_label.pack()

    def _handle_upload(self):
        """
        Handles the file upload process triggered by the 'Upload' button click.
        """

        # Open a file dialog to select an Excel file
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
        if file_path:
            try:

                # Read the selected Excel file and store its content in self.file_contents
                self.file_contents = pd.read_excel(file_path)

                # Process the Excel file content
                self._process_excel_file()

                # Display success message
                self._display_success_message()
            except Exception as e:

                # Display error message if an error occurs during file processing
                self._display_error_message()
                self.output_text.insert(tk.END, f"An error occurred during uploading: {str(e)}\n")
        else:

            # Display a message if no file is selected
            self.output_text.insert(tk.END, "Please select an Excel file.\n")


    def _process_excel_file(self):
        """
        Processes the uploaded Excel file and displays its content in the output_text widget.
        """

        # Clear the output_text widget and display the content of the uploaded Excel file
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, str(self.file_contents))

    def _display_success_message(self):
        """
        Displays a success message in the success_message_label widget.
        """
        # Configure the success_message_label widget to display a success message
        self.success_message_label.config(text="Upload successful.", fg="green")

        # Clear the error message
        self.error_message_label.config(text="")
    

    def _display_error_message(self):
        """
        Displays an error message in the error_message_label widget.
        """

        # Configure the error_message_label widget to display an error message
        self.error_message_label.config(text="Upload unsuccessful, please try again.", fg="red")

        # Clear the success message
        self.success_message_label.config(text="")

def main():
    """
    The main function to create the tkinter window and instantiate the ExcelFileUploaderAndConverter class.
    """

    # Create the main tkinter window
    root = tk.Tk()
    root.title("Excel File Uploader and Converter")

    # Instantiate the ExcelFileUploaderAndConverter class with the root window
    uploader = ExcelFileUploaderAndConverter(root)

    # Run the tkinter event loop
    uploader.root.mainloop()

if __name__ == "__main__":
    # Call the main function when the script is executed
    main()





def Area(files_directory):
    '''
    Calculate the Area of the water Raman peak for each exitation wavelenght.

    Args: 
    - files_directory the files directory of the spectroscopy matrice

    Returns: Arp the Area of the water Raman peak calculated using the trap
    '''
    df = pd.read_excel(files_directory)
    raman = df.loc[(df['EmWl [nm]'] >= 371) & (df['EmWl [nm]'] <= 428)]
    dif = np.diff(raman['EmWl [nm]'])
    l_ex = (excited_wavelength_list(250,600,10))  # Ajouter partie qui demande les bornes et le pas
    collumn = {}
    Arp = pd.DataFrame(columns=[f'Int({i})' for i in l_ex], index=[0])
    print(df)
    print(Arp)

    for i in l_ex:
        fluo_avg = (raman["Int(" + str(i) + ")"][:-1] + raman["Int(" + str(i) + ")"][1:]) / 2
        A = np.sum(dif[0] * fluo_avg)
        print(f'The Area of the water Raman peak at {i} nm is: {A}')
        Arp[f'Int({i})'] = A
    return Arp

def Raman_normalisation(files_directory, Area):
    '''
    Normalise all the fluorecence values in each exitation waveleght with the area of the Raman peak computed in the Area function
    
    Args: files_directory the files directory of the spectroscopy matrice, Area a dataframe containing the wavelenght exitation in each collumn and the associaced Raman Area
    
    Returns: A new files containing the normalised matrice
    '''

    df = pd.read_excel(files_directory)
    columns_of_interest = df.columns[df.columns.str.startswith('Int')]  
    normalised = df.copy()
    normalised[columns_of_interest] = normalised[columns_of_interest].div(Area.iloc[0])
    normalised.to_excel('normalised_Raman.xlsx', index=False)
    return normalised    




def fluo_raman_norm(files_directory):
    A = Area(files_directory)
    Raman_normalisation(files_directory, A)





def plot_fluorescence_graph():
    """
    Function to plot fluorescence data on a standard graph and/or an interactive graph.

    This function prompts the user to provide the file location, the sheet name, 
    the names of the excitation and emission wavelength columns in an Excel file, 
    and the wavelength of interest in nanometers (nm). It then plots the fluorescence 
    data on a standard graph and an interactive graph using Plotly.

    Returns:
    None
    """
    # Wavelenth of interest
    chemin = input("What is the exact file location : ")
    df = pd.read_excel(chemin, sheet_name=None)
    Feuil = input("What is the exact name of the sheet on Excel  : ")
    X = input("What is the exact name of the emission wavelength column on Excel : ")
    wavelength = input("What is the excitation wavelength of interest in nm : ")
    Y = input("What is the exact name of the excitation wavelength column of interest on Excel : ")

    EmWl = df[Feuil][X]
    Int = df[Feuil][Y]

    # Ask the user if he wants to display the standard graph
    while True:
        choice1 = input("Would you like to plot a standard graph ? (yes/no) : ").lower()
        if choice1 == "yes":
            # Size of the graph
            plt.figure(figsize=(40,30))

            # Plotting of the point cloud
            plt.plot(EmWl, Int, label=f'λ = {wavelength}', color='black')
            plt.legend(fontsize=30)

            # Formating of the axis and title of the graph
            plt.title("Raman spectrum", fontsize=70)
            plt.xlabel(r'Excitation wavelength [nm]', fontsize=50)
            plt.ylabel(r'Fluorescence', fontsize=50)

            # Graduation of the axis
            plt.xticks(fontsize=30)
            plt.yticks(fontsize=30)
            plt.show()
            plt.savefig('Raman_spectrum.svg')
            break
        elif choice1 == "no":
            break
        elif choice1 != "no":
            print("Please answer by 'yes' or 'no'.")

    # Creation of an interactive graphic with zoom
    fig = go.Figure()

    # Adding of a scatter plot to the interactive graphic
    fig.add_trace(go.Scatter(x=EmWl, y=Int, marker=dict(color='black'), mode='lines', name='Data'))

    # Configuration of the layout of the interactive graphic
    fig.update_layout(
        title='Interactive graphics with zoom',
        xaxis_title='Fluorescence', 
        yaxis_title='Excitation wavelength [nm]',
        title_font=dict(size=25),  # Size of the title 
        title_x=0.5,  # To center the title
        xaxis=dict(
            title='Fluorescence',
            title_font=dict(size=20),  # Size of the label of the x axis
            rangeselector=dict(
                buttons=list([
                    dict(step="all") ])),
            rangeslider=dict(visible=True), 
            type="linear"),
        yaxis=dict(title='Excitation wavelength [nm]', 
                   title_font=dict(size=20)),  # Size of the label of the y axis
        hovermode='closest',
        height=700,  # Height in pixels
        width=900 )   # Width in pixels

    # Ask the user if he wants to display the interactive graph
    while True:
        choice2 = input("Would you like to plot an interactive graph ? (yes/no) : ").lower()
        if choice2 == "yes":
            fig.show()
            break
        elif choice2 == "no":
            break
        elif choice2 != "no":
            print("Please answer by 'yes' or 'no'.")
            


def plot_superimposed_graphs():
    """
    Function to plot a superposition of graphs on a standard graph and, if wanted, an interactive graph.

    This function prompts the user to input the number of graphs they want to superimpose. 
    It then collects data for each graph, including file location, sheet name, column names 
    for excitation and emission wavelengths, and the wavelength of interest. It plots both 
    a static and an interactive graph showing the superimposed curves.

    Returns:
    None
    """

    while True:
        try:
            number_of_graph = int(input("How many graphs would you like to superimpose :"))
            if number_of_graph > 7:
                print("A maximum of 7 different graphs can be superimposed !")
            elif number_of_graph < 2:
                print("The number of graph should be at least 2 !")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

            
    # Extraction of the values of interest

    
    # Creation of lists to store the values
    chemins = []
    Feuils = []
    Xs = []
    wavelengths = []
    Ys = []

    # Loop to collect variables for each graph
    while True:
        q1 = input("Are all the values in the same file ? (yes/no) ")
        if q1 == "yes":
            chemin = input("What is the exact file location : ")
            for i in range(1, int(number_of_graph) + 1):
                Feuil = input(f"What is exact name of the sheet on Excel for curve {i}: ")
                X = input(f"What is the exact name of the emission wavelength column on Excel for curve {i}: ")
                wavelength = input(f"What is the excitation wavelength of interest for curve {i} in nm: ")
                Y = input(f"What is the exact name of the excitation wavelength column of interest on Excel for curve {i}: ")
                # Adding the variables to the corresponding list
                chemins.append(chemin)
                Feuils.append(Feuil)
                Xs.append(X)
                wavelengths.append(wavelength)
                Ys.append(Y)
            break
        elif q1 == "no":
            for i in range(1, int(number_of_graph) + 1):
                chemin = input(f"What is the exact file location for curve {i}: ")
                Feuil = input(f"What is exact name of the sheet on Excel for curve {i}: ")
                X = input(f"What is the exact name of the excitation wavelength column on Excel for curve {i}: ")
                wavelength = input(f"What is the wavelength of interest for curve {i} in nm: ")
                Y = input(f"What is the exact name of the emission wavelength column of interest on Excel for curve {i}: ")
                # Adding the variables to the corresponding list
                chemins.append(chemin)
                Feuils.append(Feuil)
                Xs.append(X)
                wavelengths.append(wavelength)
                Ys.append(Y)
            break
        elif q1 != "no":
            print("Please answer by 'yes' or 'no'.")
    
            
    # General shape of the graph

    
    # Size of the graph, formating of the axis and title of the graph
    plt.figure(figsize=(40,30))
    plt.title("Raman spectrum", fontsize=70)
    plt.xlabel(r'Excitation wavelength [nm]',  fontsize=50)
    plt.ylabel(r'Fluorescence', fontsize=50)

    # Graduation of the axis
    plt.xticks(fontsize=30)
    plt.yticks(fontsize=30)

    
    # Plot of the superimposed point cloud 


    colors = ["black", "blue", "red", "green", "magenta", "yellow", "cyan"]
    for i in range(number_of_graph):
        df = pd.read_excel(chemins[i], sheet_name=None)
        EmWl = df[Feuils[i]][Xs[i]]
        Int = df[Feuils[i]][Ys[i]]
        color = colors[i]
        wavelength = wavelengths[i]
        plt.plot(EmWl, Int, label = f'λ = {wavelength}',color = color)
        plt.legend(fontsize = 40)

        
    # Plot of the interactive graph

    # Creation of an interactive graphic with zoom
    fig = go.Figure() 

    # Add each curve from data in Excel files
    for i, chemins in enumerate(chemins):
        # Load the value from an Excel file
        df = pd.read_excel(chemins) 

        # Select columns corresponding to x and y values
        x_col_name = Xs[i]
        y_col_name = Ys[i]  
        x_data = df[x_col_name]
        y_data = df[y_col_name]
    
        # Add curve to figure
        color = colors[i]
        wavelength = wavelengths[i]
        fig.add_trace(go.Scatter(x=x_data, y=y_data, marker=dict(color= color), mode='lines', name=f'λ = {wavelength}'))

    # Configuration des boutons pour afficher/supprimer les courbes
    buttons = []

    # Add a button for each curve
    for i in range(len(Xs)):
        wavelength = wavelengths[i]
        button = dict(
        label=f'λ = {wavelength}',
        method="update",
        args=[{"visible": [True if j == i else False for j in range(len(Xs))]}, {"title": f'λ = {wavelength}'}])
        buttons.append(button)

    # Add a button to display all curves
    button_all = dict(
        label="All",
        method="update",
        args=[{"visible": [True for _ in range(len(Xs))]}, {"title": "All"}])
    buttons.append(button_all)

    # Add a button to hide all curves
    button_none = dict(
        label="None",
        method="update",
        args=[{"visible": [False for _ in range(len(Xs))]}, {"title": "None"}])
    buttons.append(button_none)

    # Configuration of the layout of the interactive graphic
    fig.update_layout(
        updatemenus=[
            dict(
                type="buttons",
                buttons=buttons,
                direction="left",
                pad={"r": 10, "t": 10},
                showactive=True,
                x=0.02,
                xanchor="left",
                y=1.1,
                yanchor="top",
                font=dict(size=14))], # Font size
        title='Interactive graphics with zoom',
        xaxis_title='Fluorescence', 
        yaxis_title='Excitation wavelength [nm]',
        title_font=dict(size=25),  # Size of the title 
        title_x=0.5,  # To center the title
        xaxis=dict(
            title='Fluorescence',
            title_font=dict(size=20),  # Size of the label of the x axis
            type="linear"),
        yaxis=dict(title='Excitation wavelength [nm]', 
                   title_font=dict(size=20)),  # Size of the label of the y axis
        hovermode='closest',
        height=650,  # Height in pixels
        width=850 )   # Width in pixels
    
    # Ask the user if he wants to display the interactive graph
    while True:
        choice2 = input("Would you like to plot an interactive graph ? (yes/no) : ").lower()
        if choice2 == "yes":
            fig.show()
            break
        elif choice2 == "no":
            break
        elif choice2 != "no":
            print("Please answer by 'yes' or 'no'.")

            
    # Displaying and saving the graph

    
    plt.savefig('Raman_spectrum.svg')  
    plt.show()



