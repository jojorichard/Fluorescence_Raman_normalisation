#How to put your data when using the package
To enable the use of a wide range of file types. The package has been designed to work with a standardised form of DataFrame.

The data must be arranged in the following form:

| EmWl [nm]                                         | integrer of initial value of exitation wavelenght               | ... | final of initial value of exitation wavelenght               |
| -------------------------------------------------- | -------------------------------------------------------------- | --- | -------------------------------------------------------------- |
| integrer of initial value of emmited wavelenght    | integrer of intensity of fluorescence corresponding at initial value of exitation/emmision wavelenght                  | ... | ...                                                            |
| ...                                                | ...                                                            | ... | ...                                                            |
| integrer of final value of emmited wavelenght      | ...                                                            | ... | integrer of intensity of fluorescence corresponding at final value of exitation/emmision wavelenght                    |



## Example of an excel file converted in a standardised DataFrame
### Original excel files 
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
