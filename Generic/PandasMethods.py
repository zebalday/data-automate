# Import the Pandas library
import pandas as pd

# Create a sample DataFrame for demonstration
data = {'Name': ['John', 'Maria', 'Peter', 'Laura', 'Anna'],
        'Age': [25, 30, 22, 28, 24],
        'City': ['Santiago', 'Buenos Aires', 'Lima', 'Bogotá', 'São Paulo'],
        'Salary': [50000, 60000, 45000, 55000, 52000]}
df = pd.DataFrame(data)


# Selecting data from DataFrame

# Select specific columns
selected_columns = df[['Name', 'Age']]

# Select rows based on a condition
filtered_rows = df[df['Age'] > 25]

# Select rows using multiple conditions
filtered_rows_multiple_conditions = df[(df['Age'] > 25) & (df['Salary'] > 50000)]

# Sorting DataFrame
sorted_df = df.sort_values(by='Age', ascending=False)

# Resetting the index
df_reset_index = sorted_df.reset_index(drop=True)

# Adding new calculated columns
df['Age_squared'] = df['Age'] ** 2

# Renaming columns
df_renamed_columns = df.rename(columns={'Name': 'Full_Name', 'Salary': 'Monthly_Salary'})

# Removing duplicates
df_without_duplicates = df.drop_duplicates()


# Grouping data and performing aggregate functions

# Group by a column and calculate the mean of each group
grouped_data_mean = df.groupby('City')['Salary'].mean()

# Group by multiple columns and calculate the sum of each group
grouped_data_sum = df.groupby(['City', 'Age'])['Salary'].sum()


# Merging DataFrames

# Create a second DataFrame for merging
data2 = {'City': ['Santiago', 'Buenos Aires', 'Lima', 'Quito'],
         'Population': [6000000, 3000000, 9000000, 2800000]}
df2 = pd.DataFrame(data2)

# Merge DataFrames based on a common column
merged_df = pd.merge(df, df2, on='City', how='left')


# Handling missing data

# Check for missing values
missing_values = df.isnull().sum()

# Fill missing values with a default value
df_filled_na = df.fillna(0)

# Drop rows with missing values
df_dropped_na = df.dropna()


# Applying functions to DataFrame

# Apply a function to a specific column
df['Age_plus_5'] = df['Age'].apply(lambda x: x + 5)

# Apply a function element-wise to the entire DataFrame
df_modified = df.applymap(lambda x: x.lower() if type(x) == str else x)

# Aggregating data with pivot tables

# Create a pivot table to summarize data
pivot_table = pd.pivot_table(df, index='City', values='Salary', aggfunc='mean')

# Concatenating DataFrames

# Concatenate DataFrames vertically
df_concatenated = pd.concat([df, df2], ignore_index=True)


# Reshaping DataFrames

# Melt DataFrame to transform it from wide to long format
melted_df = pd.melt(df, id_vars='Name', value_vars=['Age', 'City'], var_name='Attribute', value_name='Value')

# Pivot DataFrame to transform it from long to wide format
pivoted_df = melted_df.pivot(index='Name', columns='Attribute', values='Value')


# Handling string data in DataFrame

# Convert strings to uppercase
df['City_uppercase'] = df['City'].str.upper()

# Split strings in a column and create new columns
df[['City', 'Country']] = df['City'].str.split(', ', expand=True)

# Handling date and time data

# Convert a string column to datetime type
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')

# Extract year, month, day from a datetime column
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day


# Aggregating data using groupby and resampling

# Group by a column and calculate the mean of each group
grouped_data_mean = df.groupby('City')['Salary'].mean()

# Resample data to a different time frequency and calculate the mean
df_resampled = df.set_index('Date').resample('M')['Salary'].mean()

# Apply rolling window functions
df['Salary_rolling_mean'] = df['Salary'].rolling(window=3).mean()

# Handling categorical data

# Convert a column to categorical data type
df['Category'] = df['Category'].astype('category')

# Create dummy variables for categorical data
df_with_dummies = pd.get_dummies(df, columns=['Category'])


# Exporting data to different file formats

# Export DataFrame to a CSV file
df.to_csv('data.csv', index=False)

# Export DataFrame to an Excel file
df.to_excel('data.xlsx', index=False)

# Export DataFrame to a JSON file
df.to_json('data.json', orient='records')
