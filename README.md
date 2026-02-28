# TEAM-2-Hospital-Patient-Records

### **Contributers**


Julian Shin, 7647613
Jongbeom Shim, 7820434

## **Installation**
Clone or Download ZIP this project to your local machine.

Open terminal, go to directory you want for this project
(If you downloaded as ZIP file, extract it).

Run `pip install -r requirement.txt` on terminal to download all dependencies that require for this project (You can use virtual environment to avoid conflict between global and local packages)

That's it for installation!

---

## **Purpose**

  This Hospital Data Analysis project analyzes patient data from hospitals used to identify patterns in admission rates, the impact of different insurances on patient charges, readmission rates, impact of gender on charges, and length of stay based on departments. 

  The goal for this project is to perform data exploration, data cleaning, statistical analysis, and to visualize the patterns that emerged while extracting the important information from this dataset. 

## **Repository Structure**

- README.md = Project Documentation 
- hospital.csv = Raw dataset
- main.py = Python script containing data analysis, cleaning, visualization
- requirements.txt = external requirements
  
## **Data Cleaning**
1. Handle missing values
> Insurance has 106 missing values(null values): instead of empty/None value we can insert "N\A”.
3. Address inconsistencies
> Gender has two different version for one gender (e.g. M and Male for males and F and Female for females): to standardize we use the whole word version.
4. Validate cleaned data
> Age column contains value -1, Instead of dropping all data values containing -1; change to mean age .

## **Data Analysis**
> You can check results on the console result
### 1. Elective is the longest average stay by admission type.
### 2. Pediatrics has the highest readmission rate by department.
### 3. Difference between most expensive insurance type and least expensive: $388.61
### 4. 
### 5.
### 6. Orthopedics department treats the oldest patients on average at a 51.88 average age at treatment.

## **Data Visualization**
> Check the result on console

## **Key Insights**

- Elective is the longest average stay by admission type.
- Pediatrics has the highest readmission rate by department.
- Charges differ from best insurance coverage to least insurance coverage by $388.61. Insurance does not majorly affect charges as each level of insurance is <$150 more expensive then the next lower level.
- There are almost no relationship between length of stay and total charges from this data since there is large difference between largest charge per day and lowest charge per day.
- Orthopedics department treats the oldest patients on average at a 51.88 average age at treatment.


