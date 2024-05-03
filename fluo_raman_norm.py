import numpy as np
import pandas as pd
371 428
def Area(files_directory):
    '''
    Calculate the Area of the water Raman peak for each exitation wavelenght.

    Args: 
    - files_directory the files directory of the spectroscopy matrice

    Returns: Arp the Area of the water Raman peak calculated using the trap
    '''
    df = pd.read_csv(files_directory)
    dif = np.diff(df['EmWl [nm]'])

    for i in l_ex:

        fluo_avg = (df[f'Int{str(l_ex)}))'][:-1] + df[f'Int{str(l_ex)}))'][1:]) / 2
        Arp = np.sum(dif * lem_avg)
        print(f'The Area of the water Raman peak is: {Arp}')
    return Arp


def Raman_normalisation():









  def excited_wavelength_list(first, last, step):
    # Convertir start, end et step en float
    first = float(first)
    last = float(last)
    step = float(step)
    
    # Créer une liste vide pour stocker les nombres
    l_x = []
    
    # Générer la liste de nombres en fonction des types de start, end et step
    if isinstance(step, int):
        # Si step est un entier, générer une liste de nombres entiers
        l_x = list(range(int(first), int(last) + 1, int(step)))
    else:
        # Si step est un float, générer une liste de nombres à virgule flottante
        current = first
        while current <= last:
            rounded_current = round(current, 1)
            if rounded_current.is_integer():
                l_x.append(int(rounded_current))
            else:
                l_x.append(rounded_current)
            current += step
    
    return l_x
