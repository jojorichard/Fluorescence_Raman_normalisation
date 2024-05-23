# Data's organisation to use the package
 
The package has been designed to work with a standardised form of DataFrame to enable the use of a wide range of file formats.

The data must be arranged in the following form:

| EmWl [nm]                                         | Initial excitation wavelength (integer)               | ... | Final excitation wavelength (integer)               |
| -------------------------------------------------- | -------------------------------------------------------------- | --- | -------------------------------------------------------------- |
| Initial emitted wavelength (integer)    | Initial fluorescence's intensity corresponding to the initial excitation/emission wavelength (integer)                  | ... | ...                                                            |
| ...                                                | ...                                                            | ... | ...                                                            |
| Final emitted wavelength (integer)       | ...                                                            | ... |  Final fluorescence's intensity corresponding to the final excitation/emission wavelength (integer)                   |



## Example of an excel file converted in standardised DataFrame
### Original excel file 
| EmWl [nm] | Int(250) | Int(260) | Int(270) | Int(280) | Int(290) | Int(300) |
| --------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 350       | 8.378    | 46.433   | 71.544   | 101.368  | 115.766  | 103.823  |
| 350.5     | 9.5323   | 47.8672  | 71.8733  | 99.4352  | 116.3693 | 104.4283 |
| 351       | 9.6695   | 48.3257  | 73.1534  | 99.7022  | 116.8489 | 105.4132 |
| 351.5     | 9.8104   | 48.9186  | 73.7622  | 100.3105 | 117.4956 | 106.5844 |
| 352       | 9.939    | 49.4724  | 74.7073  | 101.0268 | 118.1397 | 107.7044 |

### Standardised Dataframe
| EmWl [nm] | 250     | 260     | 270     | 280     | 290     | 300     |
| --------- | ------- | ------- | ------- | ------- | ------- | ------- |
| 350.0     | 8.3780  | 46.4330 | 71.5440 | 101.3680| 115.7660| 103.8230|
| 350.5     | 9.5323  | 47.8672 | 71.8733 | 99.4352 | 116.3693| 104.4283|
| 351.0     | 9.6695  | 48.3257 | 73.1534 | 99.7022 | 116.8489| 105.4132|
| 351.5     | 9.8104  | 48.9186 | 73.7622 | 100.3105| 117.4956| 106.5844|
| 352.0     | 9.9390  | 49.4724 | 74.7073 | 101.0268| 118.1397| 107.7044|

## Implement function to read a particular file
If your file isn't suported by the present package, you can create a function that reads the file and converts the data in standardised DataFrame, as shown above.
### 1) Find the filepath
You can call the following function in your function to upload your file and return the corresponding filepath. 
```
read_eem()
```
### 2) Conversion into a DataFrame
The use of panda is recommended to convert your file into a DataFrame. The following documentation states the files that can be read by panda: https://pandas.pydata.org/docs/reference/frame.html

### 3) Organise the data as shown above to return the usable DataFrame

## Small example
```
def read_newfile():

  file_path = read_eem() # Load the file path

  eem = pd.read_csv(file_path) # Load your file into a DataFrame for example if it is a CSV file

  # Organise the dataframe

  return eem
```

# Supported file formats

## Excel file in the following form 

| EmWl [nm] | Int(250) | Int(260) | Int(270) | Int(280) | Int(290) | Int(300) |
| --------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 350       | 8.378    | 46.433   | 71.544   | 101.368  | 115.766  | 103.823  |
| 350.5     | 9.5323   | 47.8672  | 71.8733  | 99.4352  | 116.3693 | 104.4283 |
| 351       | 9.6695   | 48.3257  | 73.1534  | 99.7022  | 116.8489 | 105.4132 |
| 351.5     | 9.8104   | 48.9186  | 73.7622  | 100.3105 | 117.4956 | 106.5844 |
| 352       | 9.939    | 49.4724  | 74.7073  | 101.0268 | 118.1397 | 107.7044 |

```
def read_excel(path = False):
    """
    Reads a specific spectrometer's excel file where the values are structured in the following form:

    	EmWl [nm] Int(250) Int(260)	Int(270)	Int(280)	Int(290)	Int(300)	Int(310)	Int(320)	Int(330)
         350.0 8.3780   46.4330	  71.5440	 101.3680	115.7660	103.8230	111.0970	121.6770	58.7180	
         350.5 9.5323	  47.8672   71.8733	 99.4352	 116.3693	104.4283	110.9135	123.3000	61.2646
         ...	   ...	     ...	    ...       ...	    ...	      ...	      ...	       ...	      ...
         600.0 2.8920	  19.2880	  53.0750	  59.5580	 42.0960  999.9990	290.3740	13.1150	 12.2750

    Int(XXX) contains the excitation wavelength with the measured intensity in the corresponding column EmWL [nm] contains the emission wavelengths

    It returns a standardised Dataframe in a form that can be treated by the other package's functions.

    Args:
    - The filepath
    In case of error in the read_eem function, the filepath can be entered manually.
    
    Returns: eem standardised Dataframe in a form that can be treated by the other pakage's functions.
    """
    
    try:
        file_path = read_eem()  # Call read_eem to upload and read the file
    except: # If an exception is raised, it reads the filepath manually entered 
        print('An error as occured in the read_eem function. Excecute read_excel(path) with the path file of your file')
        file_path = path
        
    eem = pd.read_excel(file_path)  # Read the Excel file into a DataFrame
    new_columns = [col if i == 0 else int(re.search(r'\d+', col).group()) for i, col in enumerate(eem.columns)]   # put the Dataframe in the standardised form for this package
    eem.columns = new_columns  
    return eem

```

## Add your future function here
