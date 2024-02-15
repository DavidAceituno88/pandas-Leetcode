import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    person = person.merge(address[['personId','city','state']] ,on ='personId',how='left')
    df = person[['firstName','lastName','city','state']]
    return df
