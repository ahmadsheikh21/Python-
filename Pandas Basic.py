# This will Convert the Dictonary into Data frame
import pandas as pd
Webtraffic = {'Day':[1,2,3,4,5,6,7], "Visitors": [100,300,500, 800,1200,430,5543], 'BounceRate':[35,33,55,64,21,56,32]}
df = pd.DataFrame(Webtraffic)
print(df)