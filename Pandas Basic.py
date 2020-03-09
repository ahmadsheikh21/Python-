# This will Convert the Dictonary into Data frame
import pandas as pd
WebtrafficW1  = ({"Day":[1,2,3,4,5,6,7], "Visitors": [100,300,500, 800,1200,430,5543], 'BounceRate':[35,33,55,64,21,56,32]})

WebtrafficW2  = ({"Day": [1,2,3,4,5,6,7], "Visitors": [1300,4300,6500, 2800,14200,5430,55543], 'BounceRate':[5,34,25,34,41,56,52]})
df1 = pd.DataFrame(WebtrafficW1)
df2 = pd.DataFrame(WebtrafficW2)
print(df1)
print(df2)

# ******This will set day as an index*******
df1.set_index("Day" , inplace=True)
print(df1)

print(df1.head(2))
# this will show the first two rows

print(df1.tail(2))
# this will show the last two rows

# ******Mergeing*******

WebtrafficWeek1  =pd.DataFrame ({"Visitors": [100,300,500, 800,1200,430,5543], 'BounceRate':[35,33,55,64,21,56,32]},
                    index = [ 1,2,3,4,5,6,7])

WebtrafficWeek2  = pd.DataFrame({"Visitors":[1003,3002,500, 800,1200,430,5543], 'BounceRate':[35,33,55,64,21,56,32]},
                                index = [8,9,10,11,12,13,14])

merge= pd.merge(WebtrafficWeek1,WebtrafficWeek2)
print(merge)



