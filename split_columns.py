def split_columns(df, orig, one, two, separator):
	"""
	orig: string name of the column we want to split
	one: string name of the first new column
	two: string name of the second new column
	separator: string - this is the character(s) that will define where to split
	"""
	df[[one,two]] = df[orig].str.split(separator,expand=True)