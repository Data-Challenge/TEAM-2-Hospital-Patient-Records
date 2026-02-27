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
        cleaned_df.loc[x, "gender"] = "Female


print() #linebreak 

# ANALYSIS

# 1.1 - what is the average stay by admission type? 
average_stay = cleaned_df.groupby("admission_type")["length_of_stay"].mean()
print(f"Average stay length by admission type {average_stay}%" )

print() #linebreak

# 1.2 - Which department has the highest readmission rate? 
readmission_rate = cleaned_df.groupby("department")["readmitted"].mean()
highest_department = readmission_rate.idxmax()
highest_value = readmission_rate.max()
print(f" Department with highest re-admission rate:  {highest_department, highest_value}%") 

print() #linebreak

#1.3 - How does insurance type affect total charges (list charges by type - is there any causality?) 
insurance_average = cleaned_df.groupby("insurance")["total_charges"].mean()
print(f"highest total charge by insurance type: {insurance_average}%") 

print() #linebreak

# 1.4 - What percentage of patients in each age group require emergency admission?
# 0-19
underage = cleaned_df[cleaned_df['age'].between(0, 19)]
underage_emergency_rate = round((underage['admission_type'] == 'Emergency').mean() * 100, 2)
print(f"Underage emergency admission rate: {underage_emergency_rate}%")

# 20-59
adult = cleaned_df[cleaned_df['age'].between(20, 59)]
adult_emergency_rate = round((adult['admission_type'] == 'Emergency').mean() * 100, 2)
print(f"Adult emergency admission rate: {adult_emergency_rate}%")

# 60+
senior = cleaned_df[cleaned_df['age'].between(20, 59)]
senior_emergency_rate = round((senior['admission_type'] == 'Emergency').mean() * 100, 2)
print(f"Senior emergency admission rate: {senior_emergency_rate}%")


print() #linebreak 

# 1.5 - Is there a relationship between length of stay and total charges?

print() #linebreak 

# 1.6 - Which department treats the oldest patients on average?

oldpatient_treatment = cleaned_df.groupby("department")["age"].mean().sort_values(ascending = False)
print(f"Department treating the average oldest patients: {oldpatient_treatment}%")

print() #linebreak 


#print(cleaned_df)
print(cleaned_df.info())
