import numpy as np    
import pandas as pd

#Initial condition
a=input("Are your values in nanometers? If yes, write Yes, if not write No:")
if a== "Yes" or a=="yes":
    pass
else:
    raise ValueError("Please make sure your values are in nanometers otherwise the program doesn't work :)")
    
#step
step=input("Please insert the measure step of your spectroscopy machine (no unit needed):")



"""
This fonction converts the coma in a point so that python recognises the number under the float form.

Parameters: the step previously entered.

Returns: the initial step if it is an integer or in the float form or the step converted in float.
"""

def conversion_coma_point(step):
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



"""
This fonction creates a list with excited wavelengths in terms of the step, from the first value and last 
entered value. It consists of two main parts: the first if the step is an integer, the other if the step ia a float.

Parameters: first(int) and last (int) excited wavelengths value.

Returns: a list of excited wavelength value in the exact where the integer values are in the form int, and the 
others are in the form float.
"""

def excited_wavelength_list(first, last, step):
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
    l_ex = (exicted_wavelength_list(250,600,10))  # Ajouter partie qui demande les bornes et le pas
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
    normalised[columns_of_interest] = normalised[columns_of_interest].div(A.iloc[0])
    normalised.to_excel('normalised_Raman.xlsx', index=False)
    return normalised    




def fluo_raman_norm(files_directory):
    A = Area(files_directory)
    Raman_normalisation(files_directory, A)
