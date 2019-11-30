import pandas as pd 
#Creat dictionary
data = {"Box":["Box 1", "Box 1","Box 1","Box 2","Box 2","Box 2"], 
        "Dimension": ["Length", "Width", "Height", "Length", "Width", "Height"],
        "Value": [6,4,2,5,3,4]}
#Output the Dataframe wanted 
df = pd.DataFrame(data, columns = ["Box","Dimension", "Value"])
#Convert messy dataframe to tidy dataframe
tidy = df.pivot_table ( index = ["Box"], columns = "Dimension", values = "Value").reset_index()
#Add column  for volume 
X = tidy["Volume"]= tidy.Length*tidy.Height*tidy.Width 
#Output the tidy data frame with the new Volume column
print (tidy)