# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
#print("\nPath: \n\n", path)
#print("\nData: \n\n", data)
#print("\nType of data: \n\n", type(data))

census = np.concatenate((data, new_record))
print("\nArray Size : \n\n", len(census))
print("\nCensus: \n\n", census.shape)

## Step 2 ## 
print("\nStep 2 starts here: \n\n")
age = census[:,0]
print("\nAge: \n\n", age)
max_age = age.max()
min_age = age.min()
age_mean = round(age.mean(),2)
age_std = round(age.std(),2)
print("\nMax Age : \n\n", max_age,
       "\nMinimum Age : \n\n", min_age, 
       "\nMean Age : \n\n", age_mean,
       "\nStandard Age : \n\n", age_std
)

## Step 3 ## 
print("\nStep 3 starts here: \n\n")

race = census[:,2]
print("\nRace : \n\n", len(race))
##race_0 = [ r for r in race if race[r] == 0 ]  
## race[race[:,0] == 0]
#val0 = 0/val1 = 1/val2 = 2/val3 = 3/val4 = 4
#race_x = [] 
#for val in range(len(race)):    
#race_0 = race[race[val] == val1]
#race_x = np.append(race_x,race_0)

race_0 = [x for x in race if x == 0]
race_1 = [x for x in race if x == 1]
race_2 = [x for x in race if x == 2]
race_3 = [x for x in race if x == 3]
race_4 = [x for x in race if x == 4]

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

print("Length of race_0 : ", len_0, "\n\n",
"Length of race_1 : ", len_1, "\n\n",
"Length of race_2 : ", len_2, "\n\n",
"Length of race_3 : ", len_3, "\n\n",
"Length of race_4 : ", len_4
)
## print("\race_0 : \n\n", (race[val] == 0))    
length = np.array([len_0, len_1, len_2, len_3, len_4])
## min_val = [x for x in length if x == np.min(length)]
m_race = [x for x in range(len(length)) if length[x] == np.min(length)]
minority_race =  m_race[0]
print("Minority Race : ", minority_race)

## Step 4 ## 

print("\nStep 4 starts here: \n\n")

senior_citizens = [x for x in age if x > 60]
senior_citizens_index = [x for x in range(len(age)) if age[x] > 60]

print("Senior Citizens : ", senior_citizens)
print("Senior Citizens Index : ", senior_citizens_index)
senior_citizens_len = len(senior_citizens)
print("Total Senior Citizens : ", senior_citizens_len)

working_hours = census[:,6]
print("Working Hours : ", working_hours.dtype)

print("senior_citizens_index : ", working_hours[senior_citizens_index[0]])

##sr_age_group = np.concatenate(age, working_hours)
##print("sr_age_group : ", sr_age_group)

## working_hours_sr1 = [x for x in senior_citizens_index if working_hours[x] != 0 ]
## working_hours_sr = [x for x in working_hours if np.where() == senior_citizens_index[x] ]
## print("working_hours lengh : ", len(working_hours_sr))
## print("working_hours_sr : ", working_hours_sr)

#working_hours_sr1 = []
working_hours_sr = []

for x in senior_citizens_index:
    working_hours_sr.append(working_hours[x])   

# working_hours_sr1 = working_hours[senior_citizens_index[x]]
# working_hours_sr = working_hours_sr.append(working_hours_sr1)

print("working_hours_sr : ", working_hours_sr)

working_hours_sum = np.sum(working_hours_sr)
print("working_hours_sum : ", working_hours_sum)

avg_working_hours = working_hours_sum / senior_citizens_len
print("avg_working_hours : ", round(avg_working_hours,2))

## Step 5 ## 
print("\nStep 5 starts here: \n\n")

education = census[:,1]

high = [x for x in education if x > 10]
high_index = [x for x in range(len(education)) if education[x] > 10]

low = [x for x in education if x <= 10 ]
low_index = [x for x in range(len(education)) if education[x] <= 10]

income = census[:,7]

high_income = []
low_income = []

for x in high_index:
    high_income.append(income[x])   

for x in low_index:
    low_income.append(income[x])   

avg_pay_high = round(np.mean(high_income),2)
avg_pay_low = round(np.mean(low_income),2)

print("\nAvg_pay_high : ", avg_pay_high)
print("\nAvg_pay_low : ", avg_pay_low)




