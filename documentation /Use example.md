# How to use the package
## Full example

## Step by Step
### 1) load the EEM matrice to be processed
#### exemple with an excel files
```
eem = read_excel()
```
![Tuto read_excel](https://github.com/jojorichard/Fluorescence_Raman_normalisation/assets/160777950/d7f3a432-950c-47df-8ac7-7d7728fcd84e)

 ### 2) Normalise the EEM matrice
 #### If the blank is the loaded eem
 ```
 eem_norm = fluo_raman_norm(eem)
```
#### If the blank is in another file
 ```
 blank = read_excel()
 eem_norm = fluo_raman_norm(eem, blank = blank)
 ```
 The normalised EEM matrice is saved in an excel file called "normalised_Ramnan.xlsx" of the follwing form and it's DataFrame is returned
 
 | EmWl [nm] | 250        | 255        | 260        | 265        | 270        | 275        | 280        | 285        | 290        | 295        | 300        |
| --------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- |
| 350       | 0.0008789  | 0.0023753  | 0.0028547  | 0.004495   | 0.0065382  | 0.0060588  | 0.0084375  | 0.0080449  | 0.0088119  | 0.0091292  | 0.0088656  |
| 350.5     | 0.0010234  | 0.0022913  | 0.002919   | 0.0044307  | 0.0058528  | 0.0064289  | 0.0076323  | 0.009171   | 0.0087779  | 0.0084182  | 0.0080242  |
| 351       | 0.0011219  | 0.0022533  | 0.0030072  | 0.0044122  | 0.0055507  | 0.0064891  | 0.0079348  | 0.0089342  | 0.0090996  | 0.0080688  | 0.007986   |
| 351.5     | 0.0011135  | 0.0022734  | 0.0030723  | 0.0044049  | 0.0056659  | 0.0065027  | 0.0079862  | 0.0089206  | 0.0089053  | 0.0079954  | 0.0079835  |
| 352       | 0.0011124  | 0.0022865  | 0.0031589  | 0.0043866  | 0.0056515  | 0.0065596  | 0.0079579  | 0.0087859  | 0.00886    | 0.007912   | 0.0078569  |

### 3) Optional Remove Rayleigh scattering. (Recommanded before plotting)
#### Of first order
```
remove_rayleigh_scattering(eem_norm, order=1)
```
#### Of second order
```
remove_rayleigh_scattering(eem_norm, order=2)
```
#### Of both order 
```
remove_rayleigh_scattering(eem_norm, order='both')
```

### Example of graph without removing the Rayleigh scattering
![Contour_avec_rayleight](https://github.com/jojorichard/Fluorescence_Raman_normalisation/assets/160777950/dc6b63a2-0a5b-4a90-995b-48cda94bc0d0)

### Example of graph with removing  Rayleigh scattering of first order
![Contour_sans_rayleight_1](https://github.com/jojorichard/Fluorescence_Raman_normalisation/assets/160777950/1d498a4b-be16-43b3-9f55-55557b6fa396)

### Example of graph with removing  Rayleigh scattering of second order
![newplot (1)](https://github.com/jojorichard/Fluorescence_Raman_normalisation/assets/160777950/66179bdb-a3d9-4f35-8f8c-ea9bbaf27ef8)

### Example of graph with removing  Rayleigh scattering with width = 50 (default = 10)
![Width_50](https://github.com/jojorichard/Fluorescence_Raman_normalisation/assets/160777950/879d659d-1a0c-4d46-9943-2ee854212e7c)

### Example of graph with removing  Rayleigh scattering with width = 5 (default = 10)
![newplot (2)](https://github.com/jojorichard/Fluorescence_Raman_normalisation/assets/160777950/08e896af-6f23-4d1a-84f0-63ee67b6ffa7)





