import pandas as pd

serie = pd.read_html('https://meta.wikimedia.org/wiki/List_of_Wikipedias/Table')
#Len of list
print(len(serie))
#Print the table
print(serie[8])