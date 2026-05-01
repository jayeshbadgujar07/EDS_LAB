'''A dictionary of lists has been provided to you in the editor. Create a DataFrame from the dictionary of lists and perform the listed operations, then display the DataFrame before and after each manipulation.

Create the DataFrame:

Convert the dictionary to a Pandas DataFrame.


Add a new row:

Take inputs from the user for the new row data (name, age).
Add the new row to the DataFrame.
Display the DataFrame after adding the new row.


Modify a row:

Modify a specific row by changing the age. Take the row index and new age value from the user.
Display the DataFrame after modifying the row.


Delete a row:

Take the row index to be deleted from the user.
Remove the specified row.
Display the DataFrame after deleting the row.


Add a new column:

Add a column Gender with values taken from the user.
Display the DataFrame after adding the new column.


Modify a column:

Convert names to uppercase.
Display the DataFrame after modifying the column.


Delete a column:

Remove the Age column.
Display the DataFrame after deleting the column.
'''

import pandas as pd

# Provided dictionary of lists
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Adding a new row
name = input("New name: ")
age = int(input("New age: "))
new_row = {"Name": name,"Age":age}
df = df.append(new_row,ignore_index = True)
# Display the DataFrame after adding a new row
print("After adding a row:\n",df)

# Modifying a row
ind = int(input("Index of row to modify: "))
age = int(input("New age: "))
df.loc[ind, "Age"]= age
# Display the DataFrame after modifying a row
print("After modifying a row:")
print(df)

# Deleting a row
ind = int(input("Index of row to delete: "))
df = df.drop(index = ind).reset_index(drop = True)
# Display the DataFrame after deleting a row
print("After deleting a row:")
print(df)

# Adding a new column
gender = input("Enter genders separated by space: ").split()
df["Gender"]= gender

# Display the DataFrame after adding a new column
print("After adding a new column:")
print(df)

# Modifying a column
column=[]

for i in df["Name"]:
	column.append(i.upper())

df["Name"] = column
# Display the DataFrame after modifying a column
print("After modifying a column:")
print(df)

# Deleting a column
df = df.drop(columns=["Age"])
# Display the DataFrame after deleting a column
print("After deleting a column:")
print(df)
