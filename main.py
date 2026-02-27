import pandas as pd

pd.options.display.max_rows = 999

original_df = pd.read_csv("hospital.csv")
cleaned_df = pd.read_csv("hospital.csv")

# Clean up insurance data
cleaned_df.fillna({"insurance" : "N\A"}, inplace = True)

# Clean up age data
avg_age = int(cleaned_df["age"].mean())
for x in cleaned_df.index:
    if cleaned_df.loc[x, "age"] < 0:
        cleaned_df.loc[x, "age"] = avg_age

# Clean up gender data
for x in cleaned_df.index:
    if cleaned_df.loc[x, "gender"] == "M":
        cleaned_df.loc[x, "gender"] = "Male"
    if cleaned_df.loc[x, "gender"] == "F":
        cleaned_df.loc[x, "gender"] = "Female"

print(cleaned_df)
print(cleaned_df.info())


#ANALYSIS

#1.1 - what is the average stay by admission type? 
cleaned_df.groupby("admission_type")["length_of_stay"].mean()

#1.2 - Which department has the highest readmission rate? 
readmission_rate = cleaned_df.groupby("department")["readmitted"].mean()
highest_department = readmission_rate.idxmax()
highest_value = readmission_rate.max()

#1.3 - How does insurance type affect total charges (list charges by type - is there any causality?) 
cleaned_df.groupby("insurance")["total_charges"].mean()
