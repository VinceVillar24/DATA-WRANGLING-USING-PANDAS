import pandas as pd
math  = {"Student": ["Ice Bear", "Panda", "Grizzly"],
     "Math": [ 80,95,79]}
#Create individual dictionaries
electronics = {"Student": ["Ice Bear", "Panda", "Grizzly"],
     "Electronics": [ 85,81,83]}
GEAS = {"Student": ["Ice Bear", "Panda", "Grizzly"],
     "GEAS": [ 90,79,93]}
ESAT = {"Student": ["Ice Bear", "Panda", "Grizzly"],
     "ESAT": [ 93,89,88]}
#Create the individual dataframes
a =  pd.DataFrame(math, columns = ["Student", "Math"])
b =  pd.DataFrame(electronics, columns = ["Student", "Electronics"])
c =  pd.DataFrame(GEAS, columns = ["Student", "GEAS"])
d =  pd.DataFrame(ESAT, columns = ["Student", "ESAT"])
#Merge dataframes 
X = pd.merge(a,b)
Y = pd.merge(X,c)
Z = pd.merge(Y,d)
#Output merged dataframe 
print(Z)