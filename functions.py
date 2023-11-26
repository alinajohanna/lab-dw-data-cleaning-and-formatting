
import pandas as pd

def clean_col_name (df: pd.DataFrame) -> pd.DataFrame:
    '''
    Function to apply naming convention to column names.
    Convert all names to lower case strings and replace empty spaces with "_".
    Renames st to state.
    
    Input: df: pd.DataFrame
    Output: New DataFrame with replaced values
    '''
    # make a safety copy
    df2= df.copy()
    
    # convert all to lower case names
    df2.columns = df2.columns.str.lower()
    
    # replacing " " with "_" in column names
    df2.columns = map(lambda x: x.replace(" ","_"), df2.columns)
    
    # to replace the column name "ST" (by now its "st") with "state" the rename() method is applied
    df2 = df2.rename(columns={'st':'state'})
    return df2

def clean_gender (df: pd.DataFrame, column='gender') -> pd.DataFrame:
    '''
    Function cleans by default the "gender" column.
    All entries that are not equal to "F" or "M" will be converted.
    NaNs or Others will be replaced by "D" (Divers, like "not prefer to say").
    
    Input: df: pd.DataFrame
           column: string
    Output: New DataFrame with replaced values
    '''
    # make a safety copy
    df2= df.copy()
    
    # change gender to "F" or "M"
    df2[column] = df2[column].apply(lambda x: x[0].upper() if pd.notnull(x) and x[0].upper() in ['M','F'] else "D")
    
    # replace NaNs by "D"
    #df2 = df.loc[:,column] = df[column].fillna("D", axis=0)
    
    return df2

def clean_state (df: pd.DataFrame, column='state') -> pd.DataFrame:
    '''
    Function cleans by default the "state" column.
    All values that are have an abbreviation listed in state_dict will be converted.
    
    Input: df: pd.DataFrame
           column: string
    Output: New DataFrame with replaced states
    '''
    # make a safety copy
    df2= df.copy()
    
    # creating a dictionary that translates the abbrevations to their full state names
    state_dict = {'AZ':'Arizona','Cali':'California','WA':'Washington'}
    
    # replace each abbrevated state with its full state name on the basis of state_dict
    df2[column] = df2[column].replace(state_dict)
    return df2

def clean_education (df: pd.DataFrame, column='education') -> pd.DataFrame:
    '''
    Function cleans by default the "education" column.
    "Bachelors" will be converted to "Bachelor"
    
    Input: df: pd.DataFrame
           column: string
    Output: New DataFrame with replaced education
    '''
    # make a safety copy
    df2= df.copy()
    
    # replacing 'Bachelors' with 'Bachelor'
    df2[column] = df2[column].replace({'Bachelors':'Bachelor'})
    return df2

def clean_clv (df: pd.DataFrame, column='customer_lifetime_value') -> pd.DataFrame:
    '''
    Function cleans by default the "customer_lifetime_value" column.
    Replaces '%' with nothing ('') and formats it to float.
    
    Input: df: pd.DataFrame
           column: string
    Output: New DataFrame with replaced values
    '''
    # make a safety copy
    df2= df.copy()
    
    # replacing '%' with nothing ('')
    df2[column] = df2[column].apply(lambda x: x.replace('%','') if pd.notnull(x) else x)
    
    
    # changing the data type to float is not working here
    #df2[column] = df2[column].astype(float)
    return df2

def clean_car_class (df: pd.DataFrame, column='vehicle_class') -> pd.DataFrame:
    '''
    Function cleans by default the "vehicle_class" column.
    All values that are listed in car_classes_dict will be converted.
    
    Input: df: pd.DataFrame
           column: string
    Output: New DataFrame with replaced vehicle type
    '''
    # make a safety copy
    df2= df.copy()
    
    # creating a dictionary that converts the values to Luxury
    car_classes_dict = {'Sports Car':'Luxury','Luxury SUV':'Luxury','Luxury Car':'Luxury'}
    
    # replace values listed in car_classes_dict 
    df2[column] = df2[column].replace(car_classes_dict)
    return df2

def split_keep_middle (df: pd.DataFrame, column='number_of_open_complaints') -> pd.DataFrame:
    '''
    Function cleans by default the "number_of_open_complaints" column.
    Splits values by "/" and only keep second string as new variable.
    
    Input: df: pd.DataFrame
           column: string
    Output: New DataFrame with replaced NaNs
    '''
    # make a safety copy
    df2= df.copy()
    
    # splits values by "/" and only keep second string
    df2[column] = df2[column].str.split(pat="/").str[1]
    return df2

def drop_null_rows (df: pd.DataFrame) -> pd.DataFrame:
    '''
    Function deleted rows only containing nulls.
    
    Input: df: pd.DataFrame
    
    Output: New DataFrame with mean to replace nulls
    '''
    # make a safety copy
    df2= df.copy()
    
    # delete null rows
    df2 = df2.dropna(axis=0, how='all')
    return df2


def fill_with_mean (df: pd.DataFrame, column= 'customer_lifetime_value') -> pd.DataFrame:
    '''
    Function filles null values of a given column with mean of the column.
    
    Input: df: pd.DataFrame
           column: string
    Output: New DataFrame with mean to replace nulls
    '''
    # make a safety copy
    df2 = df.copy()
    
    # convert column to numeric
    df2[column] = df2[column].astype(float)
    
    # fill null values with the mean of the column
    df2.loc[:, column] = df2[column].fillna(df2[column].mean(), axis=0)
    return df2

def num_to_int (df: pd.DataFrame) -> pd.DataFrame:
    '''
    Function to convert numeric values to integers.
    
    Input: df: pd.DataFrame
           column: string
    Output: New DataFrame with mean to replace nulls
    '''
    # make a safety copy
    df2 = df.copy()
    
    # defining a list with all numeric variables
    num_var = ['customer_lifetime_value','income', 'monthly_premium_auto', 'number_of_open_complaints', 'total_claim_amount']
    # applying a lambda function that sets them all to be of type integer
    df2[num_var] = df2[num_var].apply(lambda x: x.astype(int))
    return df2

def clean_dataframe (df: pd.DataFrame, column= str) -> pd.DataFrame:
    '''
    Function takes a pd.DataFrame and applies the previous functions to column.
    
    Input: df: pd.DataFrame
           column: string
    Outputs: New DataFram
    '''

    df2 = df.copy()
    df2 = clean_col_name(df)
    df2 = drop_null_rows(df2)
    df2 = clean_gender(df2)
    df2 = clean_state(df2)
    df2 = clean_education(df2)
    df2 = clean_clv(df2)
    df2 = split_keep_middle(df2)
    df2 = fill_with_mean(df2)
    return df2
