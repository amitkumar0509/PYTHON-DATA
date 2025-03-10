# importing pandas as pd
import pandas as pd

# dictionary of lists
dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
		'degree': ["MBA", "BCA", "M.Tech", "MBA"],
		'score':[90, 40, 80, 98]}

df = pd.DataFrame(dict)

print(df)
