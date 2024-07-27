from pandas import read_csv
from Pandas.preprocessing import (
    getNullInfo,
    rmOutliers, 
    rmNullColumns,
    rmNullRecords
    )

# Get DataFrame

path = 'D:\Progra\Programacion\Python\DataScience\Pandas\Datos\ds_salaries.csv'
df = read_csv(path)


# Show Null Values Info

getNullInfo(df)


# Remove Columns with null values higher than
# given percentage.

df = rmNullColumns(df, 20)


# Remove Records with null values from dataframe.
# Gives warning if amount record to be deleted
# exceed given percentage of dataframe total.

df = rmNullRecords(df, 20)


# Remove Records with outlier values from dataframe.
# Gives warning if amount record to be deleted
# exceed given percentage of dataframe total.

df = rmOutliers(df, limit=20)

