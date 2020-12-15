def get_date_int(df, date_column):
	year = df[date_column].dt.year
	month = df[date_column].dt.month
	week = df[date_column].dt.week
	return year, month, week

def calc_cohorts(df, signup_date, last_active):
	"""
	signup_date: name of the column with the signup date
	last_active: name of the column with the last login
	"""
	sign_year, sign_month, sign_week = get_date_int(df, signup_date)
	lastlogin_year, lastlogin_month, lastlogin_week = get_date_int(df, last_active)
	years_diff = lastlogin_year - sign_year
	months_diff = lastlogin_month - sign_month
	weeks_diff = lastlogin_week - sign_week
	df['cohort_W'] = years_diff * 52 + weeks_diff + 1
	df['cohort_M'] = years_diff * 12 + months_diff + 1
