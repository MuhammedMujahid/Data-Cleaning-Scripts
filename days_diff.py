def days_diff(df):
    df['CohortIndex_d'] = (df['last_active_date'] - df['signup_date']).dt.days
