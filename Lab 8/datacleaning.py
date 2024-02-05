import pandas as pd;

file_path = 'C:/Users/Tonkhaow/Desktop/Data-Analysis/Lab 8/GP_Dataset_Preprocess.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# # Calculate the percentage of 0 values in each row from columns AC to AV
# percentage_blanks = df.iloc[:, 32:57].eq("").mean(axis=1)

# # Remove rows where more than 50% of the data is 0
# df_filtered = df[percentage_blanks <= 0.5]

# Replace True with 1 and False with 0
df.replace({True: 1, False: 0}, inplace=True)

# Replace blank values with NaN
df.replace("", float("nan"), inplace=True)

# Iterate over columns with "S/I/R" + nameOfMedicine format
for col in df.columns:
    if col.startswith("S/I/R_"):
        medicine_name = col.split("S/I/R_")[1]
        s_col = "S_" + medicine_name
        i_col = "I_" + medicine_name
        r_col = "R_" + medicine_name
        df[[s_col, i_col, r_col]] = df[col].apply(lambda x: pd.Series([1 if x == letter else 0 for letter in ['S', 'I', 'R']]))


# Drop the original columns with "S/I/R" + nameOfMedicine format
df.drop(columns=df.columns[df.columns.str.startswith("S/I/R")], inplace=True)

# Save the filtered DataFrame to a new CSV file
output_file_path = 'GN_Dataset_Processed.csv'
df.to_csv(output_file_path, index=False)

# Display the resulting DataFrame
print(df)
