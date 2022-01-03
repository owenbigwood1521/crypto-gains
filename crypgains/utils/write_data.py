
def write_data(df):
    print(f"Number of records found: {len(df)}")
    print(f"Minimum Date found: {df.dt.min()}")
    print(f"Maximum Date found: {df.dt.max()}")
    df.to_csv('prices.csv',index=False)