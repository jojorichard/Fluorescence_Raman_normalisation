import numpy as np    
import pandas as pd

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
    Area = Area(files_directory)
    Raman_normalisation(files_directory, Area)
