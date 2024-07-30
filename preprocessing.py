import pandas as pd
import numpy as np
from pandas import (
    DataFrame,
    Series
    )


""" 
This is a collection of popular data science methods used in the data 
preprocessing & processing stage.
"""


# --------------------------------------------------------------------

def getNullInfo(
        df : DataFrame,
        to_df : bool = False        
    ) -> DataFrame:
    
    """
    Informative method
    ------------------
    Shows column names, null values amount per column, null values
    percentage relative to total dataframe records.

    Parameters
    ----------
    df : pandas.DataFrame object.
    to_df : Boolean.
        Wheter to return pandas.DataFrame with the null values 
        information.

    """

    data = {
        'Colnames' : df.columns,
        'Null values' : [],
        'Null percentage' : []
    }

    null_total = 0

    for col in df.columns:
        null_values = df[col].isnull().sum()
        null_percentage = (100 * null_values) / df.shape[0]
        null_total += null_values

        data['Null values'].append(null_values)
        data['Null percentage'].append(round(null_percentage, 3))

    overall_null_percentage = round((null_total * 100 ) / (df.shape[0] * df.shape[1]), 3)

    null_df = DataFrame(data) 

    if to_df:
        return null_df

    print(null_df)
    print(f"\n Overall the total dataframe null percentage is {overall_null_percentage}")


# --------------------------------------------------------------------

def rmNullColumns(
        df: DataFrame, 
        th: float = 10.0
    ) -> DataFrame:
    
    """ 
    Preprocessing method
    --------------------
    Remove columns from provided pandas.DataFrame object when they
    exceed null-values threshold (default 10% of DataFrame records).

    Parameters
    ----------
    df : pandas.DataFrame object.
    th : float.
        Represents the percentage of the dataset records that need 
        to be exceeded to remove the column.

    Returns
    -------
    Copy of the provided DataFrame with deleted columns.
    """

    data = {
        'columns': df.columns,
        'null-values': df.isnull().sum().values        
    }

    new_df = DataFrame(data)
    new_df['exceeds'] = new_df['null-values'] > ((df.shape[0] * th) / 100)
    columns_to_delete = new_df[new_df['exceeds'] == True]['columns'].values
    
    df = df.drop(columns=columns_to_delete, inplace=False)

    return df


# --------------------------------------------------------------------

def rmNullRecords(
        df : DataFrame,
        limit : float = 20.0
    ):
    
    """
    Preprocessing method
    --------------------
    Drops every record that has null values on its colums. Similar to
    pandas.DataFrame.dropna(), but adds percentage limit feature.

    Parameters
    ----------
    df : pandas.DataFrame object.
    limit : float.
        Represents the max tolerated percentage till wich null values
        will be removed. If amount of null values exceeds limit a
        warning will be raised. 
    
    Returns
    -------
    Copy of the provided DataFrame with deleted rows.
    """

    indexes = []

    for col in df.columns:
        null_indexes = df[col][df[col].isnull()].index.to_list()
        indexes += null_indexes
    
    indexes = set(indexes)
    null_values_percentage = (len(indexes) * 100) / df.shape[0]
    limit_value = (limit * df.shape[0]) / 100


    if len(indexes) > limit_value:
        print(f"WARNING - The amount of null values {len(indexes)} ({null_values_percentage})% exceeds current limit ({limit}%)")
        op = input("Proceed anyway? (y/n): ")
        
        if op in ("y","Y"):
            df = df.drop(indexes)
            return df

        else: 
            return df
    
    df = df.drop(indexes)
    return df


# --------------------------------------------------------------------

def rplcNullToMean(
        df : DataFrame,        
    ) -> DataFrame:
    
    for col in df.columns:
        if df[col].dtype in ('int64', 'float64'):
            mean = df[col].mean()
            indexes = df[col][df[col].isnull()].index.tolist()
            df.loc[indexes, col] = mean

    return df        


# --------------------------------------------------------------------

def rplcNullToMedian(
        df : DataFrame,        
    ) -> DataFrame:
    
    for col in df.columns:
        if df[col].dtype in ('int64', 'float64'):
            median = df[col].median()
            indexes = df[col][df[col].isnull()].index.tolist()
            df.loc[indexes, col] = median

    return df        


# --------------------------------------------------------------------

def rplcNullToMode(
        df : DataFrame,        
    ) -> DataFrame:
    
    for col in df.columns:
        if df[col].dtype in ('int64', 'float64'):
            mode = df[col].mode()
            indexes = df[col][df[col].isnull()].index.tolist()
            df.loc[indexes, col] = mode

    return df        


# --------------------------------------------------------------------

def getOutlierIndexes(
        sr : Series,
        z : int = 2,
    ) -> tuple:

    mean = sr.mean()
    std = sr.std()
    indexes = []

    for record in sr:
        z_index = (record - mean) / std

        if abs(z_index) > z:
            index_values = sr.loc[sr == record].index.tolist()
            indexes += index_values
    
    indexes = tuple(set(indexes))
    
    return indexes


# --------------------------------------------------------------------

def rmOutliers(
        df: DataFrame, 
        z: int = 2, 
        limit: float = 20.0
    ) -> DataFrame:

    """ 
    Preprocessing method
    --------------------
    Remove records from a provided pandas.DataFrame object
    when it has an outlier on a numeric column & tolerated
    deleting threshold is not exceeded (default 20% of 
    DataFrame records).

    Parameters
    ----------
    df : pandas.DataFrame object.
    z : integer.
        Represents the z-index value to detect outliers on numeric
        columns. Recomended values [2-4]
    limit : float.
        Represents the max tolerated percentage till wich outliers
        will be removed. If amount of outliers exceeds limit a
        warning will be raised.
    
    Returns
    -------
    Copy of the provided DataFrame with deleted rows.
    """

    indexes = []

    for col in df.columns:

        if df[col].dtype in ('int64', 'float64'):
            mean = df[col].mean()
            std = df[col].std()

            for record in df[col]:
                z_index = (record - mean) / std

                if abs(z_index) > z:            
                    values_index = (df[col][df[col] == record].index.tolist())
                    indexes += values_index

    indexes = set(indexes)
    outliers_percentage = (len(indexes) * 100) / df.shape[0]
    limit_value = (df.shape[0] * limit) / 100

    if len(indexes) > limit_value:
        print(f"WARNING - The amount of outliers {len(indexes)} ({outliers_percentage})% exceeds current limit ({limit}%)")
        op = input("Proceed anyway? (y/n): ")
        
        if op in ("y","Y"):
            df = df.drop(indexes)
            return df

        else: 
            return df
    
    df = df.drop(indexes)

    return df


# --------------------------------------------------------------------

def rplcOutlierToMean(
        df : DataFrame,
        z : int = 2    
    ) -> DataFrame:


    for col in df.columns:

        if df[col].dtype in ('int64', 'float64'):
            mean = df[col].mean()
            df[col] = df[col].astype('float64')

            indexes = getOutlierIndexes(df[col], z = z)
            df.loc[indexes, col] = mean
    
    return df


# --------------------------------------------------------------------
