def df_filter(df, string):
    new = df.filter(regex=string)
    return new

# Example
data = [{'2018_inc': 10, '2019_inc': 12, '2018_rev':23}, {'2018_inc':10, '2019_inc': 20, '2018_rev': 30}]
df = pd.DataFrame(data)
y_2018 = df_filter(df, '2018') # getting all columns with 2018 in their names
