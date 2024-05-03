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