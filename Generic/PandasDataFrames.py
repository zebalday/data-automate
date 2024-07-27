# Import the Pandas library
import pandas as pd
from pandas import DataFrame

# Create an empty DataFrame
df_empty = pd.DataFrame()

# Create a DataFrame from a dictionary
data = {'Name': ['John', 'Maria', 'Peter'],
        'Age': [25, 30, 22],
        'City': ['Santiago', 'Buenos Aires', 'Lima']}
df_from_dict = pd.DataFrame(data)

# Create a DataFrame from a list of lists
data_lists = [['John', 25, 'Santiago'],
              ['Maria', 30, 'Buenos Aires'],
              ['Peter', 22, 'Lima']]
columns = ['Name', 'Age', 'City']
df_from_lists = pd.DataFrame(data_lists, columns=columns)

# Create a DataFrame from a CSV file
# Let's assume we have a file named 'data.csv' with the same columns: Name, Age, City
df_from_csv = pd.read_csv('data.csv')

# Create a DataFrame from a SQL query
# Let's assume we have a connection to a database and a valid SQL query
query = "SELECT Name, Age, City FROM data_table WHERE Age > 20"
df_from_sql = pd.read_sql(query, my_connection)

# Create a DataFrame from an Excel file
# Let's assume we have a file named 'data.xlsx' with the same columns: Name, Age, City
df_from_excel = pd.read_excel('data.xlsx')

# Create a DataFrame with calculated columns based on other columns
df_calculated = df_from_dict.copy()
df_calculated['Age_squared'] = df_calculated['Age'] ** 2

# Create a DataFrame from a dictionary of Series
dict_of_series = {'Name': pd.Series(['John', 'Maria', 'Peter']),
                  'Age': pd.Series([25, 30, 22]),
                  'City': pd.Series(['Santiago', 'Buenos Aires', 'Lima'])}
df_from_series = pd.DataFrame(dict_of_series)

# Create a DataFrame from a dictionary of lists
dict_of_lists = {'Name': ['John', 'Maria', 'Peter'],
                 'Age': [25, 30, 22],
                 'City': ['Santiago', 'Buenos Aires', 'Lima']}
df_from_dict_of_lists = pd.DataFrame.from_dict(dict_of_lists)

# Create a DataFrame from a list of dictionaries
list_of_dicts = [{'Name': 'John', 'Age': 25, 'City': 'Santiago'},
                 {'Name': 'Maria', 'Age': 30, 'City': 'Buenos Aires'},
                 {'Name': 'Peter', 'Age': 22, 'City': 'Lima'}]
df_from_list_of_dicts = pd.DataFrame(list_of_dicts)

# Create a DataFrame with a custom index
data_with_index = {'Name': ['John', 'Maria', 'Peter'],
                   'Age': [25, 30, 22],
                   'City': ['Santiago', 'Buenos Aires', 'Lima']}
df_with_index = pd.DataFrame(data_with_index, index=['a', 'b', 'c'])


# Filter rows of the DataFrame based on a condition
df_filtered = df_from_dict[df_from_dict['Age'] > 25]

# Select specific columns from the DataFrame
selected_columns = ['Name', 'City']
df_selected = df_from_dict[selected_columns]

# Sort the DataFrame by a specific column
df_sorted = df_from_dict.sort_values(by='Age', ascending=False)

# Reset the DataFrame index
df_reset = df_sorted.reset_index(drop=True)

# Drop rows or columns from the DataFrame
df_without_city = df_from_dict.drop(columns=['City'])

# Add a new row to the DataFrame
new_row = {'Name': 'Laura', 'Age': 28, 'City': 'Bogotá'}
df_with_new_row = df_from_dict.append(new_row, ignore_index=True)

# Rename a column in the DataFrame
df_with_modified_name = df_from_dict.rename(columns={'Name': 'Full_Name'})

# Remove duplicates from the DataFrame
df_without_duplicates = df_from_dict.drop_duplicates()

# Add a new calculated column based on other columns
df_with_calculated_column = df_from_dict.copy()
df_with_calculated_column['Age_times_2'] = df_with_calculated_column['Age'] * 2


# Show the count of null values for every column in the dataframe
print(df_from_excel.isnull().sum())







