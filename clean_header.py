def clean_header(df):
	"""
	This functions removes weird characters and spaces from column names, while keeping everything lower case
	"""
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
