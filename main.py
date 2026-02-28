import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.max_rows = 999

original_df = pd.read_csv("hospital.csv")
cleaned_df = pd.read_csv("hospital.csv")

# Clean up insurance data
cleaned_df.fillna({"insurance" : "N\\A"}, inplace = True)

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


print() #linebreak 

# ANALYSIS

# 1.1 - what is the average stay by admission type? 
average_stay = cleaned_df.groupby("admission_type")["length_of_stay"].mean()

print("\n== 1.1 - What is the average stay by admission type?  ==")
for admission, value in average_stay.items():
    print(f"{admission}:  {value:.6f} days")

# 1.2 - Which department has the highest readmission rate? 
readmission_rate = cleaned_df.groupby("department")["readmitted"].mean()
highest_department = readmission_rate.idxmax()
highest_value = readmission_rate.max()

print("\n== 1.2 - Which department has the highest readmission rate?  ==")
print(f" Department with highest re-admission rate:  {highest_department, highest_value}\n") 

#1.3 - How does insurance type affect total charges (list charges by type - is there any causality?) 
insurance_average = cleaned_df.groupby("insurance")["total_charges"].mean().sort_values(ascending=False)

print("\n== 1.3 - How does insurance type affect total charges? ==")
for insurance_type, value in insurance_average.items():
    print(f"{insurance_type}: ${value:.6f}")


# 1.4 - What percentage of patients in each age group require emergency admission?

# 0-19
underage = cleaned_df[cleaned_df['age'].between(0, 19)]
underage_emergency_rate = round((underage['admission_type'] == 'Emergency').mean() * 100, 2)

# 20-59
adult = cleaned_df[cleaned_df['age'].between(20, 59)]
adult_emergency_rate = round((adult['admission_type'] == 'Emergency').mean() * 100, 2)

# 60+
senior = cleaned_df[cleaned_df['age'].between(20, 59)]
senior_emergency_rate = round((senior['admission_type'] == 'Emergency').mean() * 100, 2)

print("\n== 1.4 - What percentage of patients in each age group require emergency admission? ==")
print(f"Underage emergency admission rate: {underage_emergency_rate}%")
print(f"Adult emergency admission rate: {adult_emergency_rate}%")
print(f"Senior emergency admission rate: {senior_emergency_rate}%\n")


# 1.5 - Is there a relationship between length of stay and total charges?
charge_per_day = []
for x in cleaned_df.index:
    charge_per_day.append(round(float(cleaned_df.loc[x, 'total_charges'] / cleaned_df.loc[x, 'length_of_stay']), 2))
charge_per_day = pd.DataFrame({'charge_per_day' : charge_per_day})
charge_per_day['total_charges'] = cleaned_df['total_charges']

largest_charge_per_day = charge_per_day['charge_per_day'].max()
lowest_charge_per_day = charge_per_day['charge_per_day'].min()

diff_charge_per_day = largest_charge_per_day - lowest_charge_per_day

print("\n== 1.5 - Is there a relationship between length of stay and total charges? ==")
print(f"Largest Charge per Day: {largest_charge_per_day}")
print(f"Lowest Charge per Day: {lowest_charge_per_day}")
print(f"Difference of Largest and Lowest Charge per Day: {largest_charge_per_day}")
print("\nThere are almost no relationship between length of stay and total charges from this data\nsince there is large difference between largest charge per day and lowest charge per day.\n")


# 1.6 - Which department treats the oldest patients on average?

oldpatient_treatment = cleaned_df.groupby("department")["age"].mean().sort_values(ascending = False)

print("\n== 1.6 -  Which department treats the oldest patients on average? ==")
for department_type, value in oldpatient_treatment.items():
    print(f"{department_type}: {value:.6f}")

print() #newline


# VISUALIZATION

# Age distribution by department
cleaned_df.plot(kind='bar')

# Price Increase per day for each department
cleaned_df.plot(x='length_of_stay', y='total_charges', kind='scatter')

#print(cleaned_df)
print(cleaned_df.info())
