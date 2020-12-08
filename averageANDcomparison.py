
#Extracting the average result of each nutrient
#Comparing the results with daily needs of the average person
#Extracting the average result of % Daily Value 

import pandas as pd

data = pd.read_csv("menu.csv")
#rows = data.shape[0]

calories = 0
fat = 0
saturatedFat = 0
transFat = 0
cholesterol = 0
sodium = 0
carbohydrates = 0
dietaryFiber = 0
sugars = 0
protein = 0


print("Results when only the foods/eatable items used: ")
print()
rows = 0
for x in data.index:
    if(data.loc[x,'Category'] != 'Beverages' and
       data.loc[x,'Category'] != 'Coffee & Tea' and
       data.loc[x,'Category'] != 'Smoothies & Shakes'):
        calories = calories + float(data.loc[x,'Calories'])
        fat = fat + float(data.loc[x,'Total Fat'])
        saturatedFat = saturatedFat + float(data.loc[x,'Saturated Fat'])
        transFat = transFat + float(data.loc[x,'Trans Fat'])
        cholesterol = cholesterol + float(data.loc[x,'Cholesterol'])
        sodium = sodium + float(data.loc[x,'Sodium'])
        carbohydrates = carbohydrates + float(data.loc[x,'Carbohydrates'])
        dietaryFiber = dietaryFiber + float(data.loc[x,'Dietary Fiber'])
        sugars = sugars + float(data.loc[x,'Sugars'])
        protein = protein + float(data.loc[x,'Protein'])
        rows = rows + 1

caloriesAVG = round(calories/rows,2)
fatAVG = round(fat/rows,2)
saturatedFatAVG = round(saturatedFat/rows,2)
transFatAVG = round(transFat/rows,2)
cholesterolAVG = round(cholesterol/rows,2)
sodiumAVG = round(sodium/rows,2)
carbohydratesAVG = round(carbohydrates/rows,2)
dietaryFiberAVG = round(dietaryFiber/rows,2)
sugarsAVG = round(sugars/rows,2)
proteinAVG = round(protein/rows,2)


###We suppose that normally there are 3 big meals per day, so we divide each of the recommended calories by 3.

#An average person's daily need of calories
#Source: https://www.nhs.uk/common-health-questions/food-and-diet/what-should-my-daily-intake-of-calories-be/
# For men - 2000 calories. For women - 2500 calories.
# The average is (2000 + 2500) / 2 calories per day.
healthyAverageCalories = (2000+2500)/2
print("Average calories in McDonald's - " + str(caloriesAVG) + " calories. Recommended - " + str(round(healthyAverageCalories/3,2)) + " calories.")


#An average person's daily need of fat
# Source: calculated from the dataset
healthyAverageFat = (data.loc[0,'Total Fat'] * 100) / data.loc[0,'Total Fat (% Daily Value)']
print("Average fat in McDonald's - " + str(fatAVG) + " grams. Recommended - " + str(round(healthyAverageFat/3,2)) + " grams.")


#An average person's daily need of saturated fat
# Source: calculated from the dataset
healthyAverageSaturatedFat = (data.loc[0,'Saturated Fat'] * 100) / data.loc[0,'Saturated Fat (% Daily Value)']
print("Average saturated fat in McDonald's - " + str(saturatedFatAVG) + " grams. Recommended - " + str(round(healthyAverageSaturatedFat/3,2)) + " grams.")


#An average person's daily need of trans fat
# Source: https://medlineplus.gov/ency/patientinstructions/000786.htm
# You should limit trans fat to less than 1% of your daily calories.
#For someone with a 2,000 calorie a day diet, this is about 20 calories or 2 grams per day.
healthyAverageTransFat = (healthyAverageCalories * 2) / 2000
print("Average trans fat in McDonald's - " + str(transFatAVG) + " grams. Recommended - " + str(round(healthyAverageTransFat/3,2)) + " grams.")


#An average person's daily need of cholesterol
# Source: calculated from the dataset
healthyAverageCholesterol = (data.loc[0,'Cholesterol'] * 100) / data.loc[0,'Cholesterol (% Daily Value)']
print("Average cholesterol in McDonald's - " + str(cholesterolAVG) + " mg. Recommended - " + str(round(healthyAverageCholesterol/3,2)) + " mg.")


#An average person's daily need of sodium
# Source: calculated from the dataset
healthyAverageSodium = (data.loc[0,'Sodium'] * 100) / data.loc[0,'Sodium (% Daily Value)']
print("Average sodium in McDonald's - " + str(sodiumAVG) + " mg. Recommended - " + str(round(healthyAverageSodium/3,2)) + " mg.")


#An average person's daily need of carbohydrates
# Source: calculated from the dataset
healthyAverageCarbohydrates = (data.loc[0,'Carbohydrates'] * 100) / data.loc[0,'Carbohydrates (% Daily Value)']
print("Average carbohydrates in McDonald's - " + str(carbohydratesAVG) + " grams. Recommended - " + str(round(healthyAverageCarbohydrates/3,2)) + " grams.")


#An average person's daily need of dietary fibers
# Source: calculated from the dataset
healthyAverageDietaryFiber = (data.loc[0,'Dietary Fiber'] * 100) / data.loc[0,'Dietary Fiber (% Daily Value)']
print("Average dietary fibers in McDonald's - " + str(dietaryFiberAVG) + " grams. Recommended - " + str(round(healthyAverageDietaryFiber/3,2)) + " grams.")


#An average person's daily need of sugars
# Source: https://www.healthline.com/nutrition/how-much-sugar-per-day#TOC_TITLE_HDR_4
# Men: 37.5 grams. Women: 25 grams.
healthyAverageSugars = (37.5 + 25) / 2
print("Average sugars in McDonald's - " + str(sugarsAVG) + " grams. Recommended - " + str(round(healthyAverageSugars/3,2)) + " grams.")


#An average person's daily need of protein
# Source: https://www.healthline.com/nutrition/how-much-protein-per-day
# Men: 56 grams. Women: 46 grams.
healthyAverageProtein = (56+46) / 2
print("Average proteins in McDonald's - " + str(proteinAVG) + " grams. Recommended - " + str(round(healthyAverageProtein/3,2)) + " grams.")



print()
print()
print()
print()
print()
print()
calories = 0
fat = 0
saturatedFat = 0
transFat = 0
cholesterol = 0
sodium = 0
carbohydrates = 0
dietaryFiber = 0
sugars = 0
protein = 0
print("Results when only the beverages/drinkable items used: ")
print()
rows = 0
for x in data.index:
    if(data.loc[x,'Category'] == 'Beverages' or
       data.loc[x,'Category'] == 'Coffee & Tea' or
       data.loc[x,'Category'] == 'Smoothies & Shakes'):
        calories = calories + float(data.loc[x,'Calories'])
        fat = fat + float(data.loc[x,'Total Fat'])
        saturatedFat = saturatedFat + float(data.loc[x,'Saturated Fat'])
        transFat = transFat + float(data.loc[x,'Trans Fat'])
        cholesterol = cholesterol + float(data.loc[x,'Cholesterol'])
        sodium = sodium + float(data.loc[x,'Sodium'])
        carbohydrates = carbohydrates + float(data.loc[x,'Carbohydrates'])
        dietaryFiber = dietaryFiber + float(data.loc[x,'Dietary Fiber'])
        sugars = sugars + float(data.loc[x,'Sugars'])
        protein = protein + float(data.loc[x,'Protein'])
        rows = rows + 1

caloriesAVG = round(calories/rows,2)
fatAVG = round(fat/rows,2)
saturatedFatAVG = round(saturatedFat/rows,2)
transFatAVG = round(transFat/rows,2)
cholesterolAVG = round(cholesterol/rows,2)
sodiumAVG = round(sodium/rows,2)
carbohydratesAVG = round(carbohydrates/rows,2)
dietaryFiberAVG = round(dietaryFiber/rows,2)
sugarsAVG = round(sugars/rows,2)
proteinAVG = round(protein/rows,2)


###We suppose that normally there are 3 big meals per day, so we divide each of the recommended calories by 3.

#An average person's daily need of calories
#Source: https://www.nhs.uk/common-health-questions/food-and-diet/what-should-my-daily-intake-of-calories-be/
# For men - 2000 calories. For women - 2500 calories.
# The average is (2000 + 2500) / 2 calories per day.
healthyAverageCalories = (2000+2500)/2
print("Average calories in McDonald's - " + str(caloriesAVG) + " calories. Recommended - " + str(round(healthyAverageCalories/3,2)) + " calories.")


#An average person's daily need of fat
# Source: calculated from the dataset
healthyAverageFat = (data.loc[0,'Total Fat'] * 100) / data.loc[0,'Total Fat (% Daily Value)']
print("Average fat in McDonald's - " + str(fatAVG) + " grams. Recommended - " + str(round(healthyAverageFat/3,2)) + " grams.")


#An average person's daily need of saturated fat
# Source: calculated from the dataset
healthyAverageSaturatedFat = (data.loc[0,'Saturated Fat'] * 100) / data.loc[0,'Saturated Fat (% Daily Value)']
print("Average saturated fat in McDonald's - " + str(saturatedFatAVG) + " grams. Recommended - " + str(round(healthyAverageSaturatedFat/3,2)) + " grams.")


#An average person's daily need of trans fat
# Source: https://medlineplus.gov/ency/patientinstructions/000786.htm
# You should limit trans fat to less than 1% of your daily calories.
#For someone with a 2,000 calorie a day diet, this is about 20 calories or 2 grams per day.
healthyAverageTransFat = (healthyAverageCalories * 2) / 2000
print("Average trans fat in McDonald's - " + str(transFatAVG) + " grams. Recommended - " + str(round(healthyAverageTransFat/3,2)) + " grams.")


#An average person's daily need of cholesterol
# Source: calculated from the dataset
healthyAverageCholesterol = (data.loc[0,'Cholesterol'] * 100) / data.loc[0,'Cholesterol (% Daily Value)']
print("Average cholesterol in McDonald's - " + str(cholesterolAVG) + " mg. Recommended - " + str(round(healthyAverageCholesterol/3,2)) + " mg.")


#An average person's daily need of sodium
# Source: calculated from the dataset
healthyAverageSodium = (data.loc[0,'Sodium'] * 100) / data.loc[0,'Sodium (% Daily Value)']
print("Average sodium in McDonald's - " + str(sodiumAVG) + " mg. Recommended - " + str(round(healthyAverageSodium/3,2)) + " mg.")


#An average person's daily need of carbohydrates
# Source: calculated from the dataset
healthyAverageCarbohydrates = (data.loc[0,'Carbohydrates'] * 100) / data.loc[0,'Carbohydrates (% Daily Value)']
print("Average carbohydrates in McDonald's - " + str(carbohydratesAVG) + " grams. Recommended - " + str(round(healthyAverageCarbohydrates/3,2)) + " grams.")


#An average person's daily need of dietary fibers
# Source: calculated from the dataset
healthyAverageDietaryFiber = (data.loc[0,'Dietary Fiber'] * 100) / data.loc[0,'Dietary Fiber (% Daily Value)']
print("Average dietary fibers in McDonald's - " + str(dietaryFiberAVG) + " grams. Recommended - " + str(round(healthyAverageDietaryFiber/3,2)) + " grams.")


#An average person's daily need of sugars
# Source: https://www.healthline.com/nutrition/how-much-sugar-per-day#TOC_TITLE_HDR_4
# Men: 37.5 grams. Women: 25 grams.
healthyAverageSugars = (37.5 + 25) / 2
print("Average sugars in McDonald's - " + str(sugarsAVG) + " grams. Recommended - " + str(round(healthyAverageSugars/3,2)) + " grams.")


#An average person's daily need of protein
# Source: https://www.healthline.com/nutrition/how-much-protein-per-day
# Men: 56 grams. Women: 46 grams.
healthyAverageProtein = (56+46) / 2
print("Average proteins in McDonald's - " + str(proteinAVG) + " grams. Recommended - " + str(round(healthyAverageProtein/3,2)) + " grams.")



print()
print()
print()
print()
print()
print()
calories = 0
fat = 0
saturatedFat = 0
transFat = 0
cholesterol = 0
sodium = 0
carbohydrates = 0
dietaryFiber = 0
sugars = 0
protein = 0
print("Results when all the menu items used: ")
print()
rows = data.shape[0]
for x in data.index:
    calories = calories + float(data.loc[x,'Calories'])
    fat = fat + float(data.loc[x,'Total Fat'])
    saturatedFat = saturatedFat + float(data.loc[x,'Saturated Fat'])
    transFat = transFat + float(data.loc[x,'Trans Fat'])
    cholesterol = cholesterol + float(data.loc[x,'Cholesterol'])
    sodium = sodium + float(data.loc[x,'Sodium'])
    carbohydrates = carbohydrates + float(data.loc[x,'Carbohydrates'])
    dietaryFiber = dietaryFiber + float(data.loc[x,'Dietary Fiber'])
    sugars = sugars + float(data.loc[x,'Sugars'])
    protein = protein + float(data.loc[x,'Protein'])


caloriesAVG = round(calories/rows,2)
fatAVG = round(fat/rows,2)
saturatedFatAVG = round(saturatedFat/rows,2)
transFatAVG = round(transFat/rows,2)
cholesterolAVG = round(cholesterol/rows,2)
sodiumAVG = round(sodium/rows,2)
carbohydratesAVG = round(carbohydrates/rows,2)
dietaryFiberAVG = round(dietaryFiber/rows,2)
sugarsAVG = round(sugars/rows,2)
proteinAVG = round(protein/rows,2)


###We suppose that normally there are 3 big meals per day, so we divide each of the recommended calories by 3.

#An average person's daily need of calories
#Source: https://www.nhs.uk/common-health-questions/food-and-diet/what-should-my-daily-intake-of-calories-be/
# For men - 2000 calories. For women - 2500 calories.
# The average is (2000 + 2500) / 2 calories per day.
healthyAverageCalories = (2000+2500)/2
print("Average calories in McDonald's - " + str(caloriesAVG) + " calories. Recommended - " + str(round(healthyAverageCalories/3,2)) + " calories.")


#An average person's daily need of fat
# Source: calculated from the dataset
healthyAverageFat = (data.loc[0,'Total Fat'] * 100) / data.loc[0,'Total Fat (% Daily Value)']
print("Average fat in McDonald's - " + str(fatAVG) + " grams. Recommended - " + str(round(healthyAverageFat/3,2)) + " grams.")


#An average person's daily need of saturated fat
# Source: calculated from the dataset
healthyAverageSaturatedFat = (data.loc[0,'Saturated Fat'] * 100) / data.loc[0,'Saturated Fat (% Daily Value)']
print("Average saturated fat in McDonald's - " + str(saturatedFatAVG) + " grams. Recommended - " + str(round(healthyAverageSaturatedFat/3,2)) + " grams.")


#An average person's daily need of trans fat
# Source: https://medlineplus.gov/ency/patientinstructions/000786.htm
# You should limit trans fat to less than 1% of your daily calories.
#For someone with a 2,000 calorie a day diet, this is about 20 calories or 2 grams per day.
healthyAverageTransFat = (healthyAverageCalories * 2) / 2000
print("Average trans fat in McDonald's - " + str(transFatAVG) + " grams. Recommended - " + str(round(healthyAverageTransFat/3,2)) + " grams.")


#An average person's daily need of cholesterol
# Source: calculated from the dataset
healthyAverageCholesterol = (data.loc[0,'Cholesterol'] * 100) / data.loc[0,'Cholesterol (% Daily Value)']
print("Average cholesterol in McDonald's - " + str(cholesterolAVG) + " mg. Recommended - " + str(round(healthyAverageCholesterol/3,2)) + " mg.")


#An average person's daily need of sodium
# Source: calculated from the dataset
healthyAverageSodium = (data.loc[0,'Sodium'] * 100) / data.loc[0,'Sodium (% Daily Value)']
print("Average sodium in McDonald's - " + str(sodiumAVG) + " mg. Recommended - " + str(round(healthyAverageSodium/3,2)) + " mg.")


#An average person's daily need of carbohydrates
# Source: calculated from the dataset
healthyAverageCarbohydrates = (data.loc[0,'Carbohydrates'] * 100) / data.loc[0,'Carbohydrates (% Daily Value)']
print("Average carbohydrates in McDonald's - " + str(carbohydratesAVG) + " grams. Recommended - " + str(round(healthyAverageCarbohydrates/3,2)) + " grams.")


#An average person's daily need of dietary fibers
# Source: calculated from the dataset
healthyAverageDietaryFiber = (data.loc[0,'Dietary Fiber'] * 100) / data.loc[0,'Dietary Fiber (% Daily Value)']
print("Average dietary fibers in McDonald's - " + str(dietaryFiberAVG) + " grams. Recommended - " + str(round(healthyAverageDietaryFiber/3,2)) + " grams.")


#An average person's daily need of sugars
# Source: https://www.healthline.com/nutrition/how-much-sugar-per-day#TOC_TITLE_HDR_4
# Men: 37.5 grams. Women: 25 grams.
healthyAverageSugars = (37.5 + 25) / 2
print("Average sugars in McDonald's - " + str(sugarsAVG) + " grams. Recommended - " + str(round(healthyAverageSugars/3,2)) + " grams.")


#An average person's daily need of protein
# Source: https://www.healthline.com/nutrition/how-much-protein-per-day
# Men: 56 grams. Women: 46 grams.
healthyAverageProtein = (56+46) / 2
print("Average proteins in McDonald's - " + str(proteinAVG) + " grams. Recommended - " + str(round(healthyAverageProtein/3,2)) + " grams.")


print()
print()
print()
print()
print()




#Extracting the average result of % Daily Value

#Adding 4 helpful features to the dataset:
    #Calories (% Daily Value)
    #Trans Fat (% Daily Value)
    #Protein (% Daily Value)
    #Sugars (% Daily Value)

data['Calories (% Daily Value)'] = 'default'
for x in data.index:
    perDay = healthyAverageCalories
    calories = float(data.loc[x,'Calories'])
    if(calories > 0):
        percentage = round((calories * 100) / perDay,1)
        data.loc[x,'Calories (% Daily Value)'] = percentage
    elif(calories == 0):
        data.loc[x,'Calories (% Daily Value)'] = 0


data['Trans Fat (% Daily Value)'] = 'default'
for x in data.index:
    perDay = healthyAverageTransFat
    transFat = float(data.loc[x,'Trans Fat'])
    if(transFat > 0):
        percentage = round((transFat * 100) / perDay,1)
        data.loc[x,'Trans Fat (% Daily Value)'] = percentage
    elif(transFat == 0):
        data.loc[x,'Trans Fat (% Daily Value)'] = 0


data['Protein (% Daily Value)'] = 'default'
for x in data.index:
    perDay = healthyAverageProtein
    protein = float(data.loc[x,'Protein'])
    if(protein > 0):
        percentage = round((protein * 100) / perDay,1)
        data.loc[x,'Protein (% Daily Value)'] = percentage
    elif(protein == 0):
        data.loc[x,'Protein (% Daily Value)'] = 0


data['Sugars (% Daily Value)'] = 'default'
for x in data.index:
    perDay = healthyAverageSugars
    sugars = float(data.loc[x,'Sugars'])
    if(sugars > 0):
        percentage = round((sugars * 100) / perDay,1)
        data.loc[x,'Sugars (% Daily Value)'] = percentage
    elif(sugars == 0):
        data.loc[x,'Sugars (% Daily Value)'] = 0

print()
print("Results when only the foods/eatable items used: ")
print()
caloriesPercent = 0
fatPercent = 0
saturatedFatPercent = 0
transFatPercent = 0
cholesterolPercent = 0
sodiumPercent = 0
carbohydratesPercent = 0
dietaryFiberPercent = 0
sugarsPercent = 0
proteinPercent = 0
vitaminAPercent = 0
vitaminCPercent = 0
calciumPercent = 0
ironPercent = 0

rows = 0
for x in data.index:
    if(data.loc[x,'Category'] != 'Beverages' and
       data.loc[x,'Category'] != 'Coffee & Tea' and
       data.loc[x,'Category'] != 'Smoothies & Shakes'):
        calories = calories + float(data.loc[x,'Calories'])
        caloriesPercent = caloriesPercent + float(data.loc[x,'Calories (% Daily Value)'])
        fatPercent = fatPercent + float(data.loc[x,'Total Fat (% Daily Value)'])
        saturatedFatPercent = saturatedFatPercent + float(data.loc[x,'Saturated Fat (% Daily Value)'])
        transFatPercent = transFatPercent + float(data.loc[x,'Trans Fat (% Daily Value)'])
        cholesterolPercent = cholesterolPercent + float(data.loc[x,'Cholesterol (% Daily Value)'])
        sodiumPercent = sodiumPercent + float(data.loc[x,'Sodium (% Daily Value)'])
        carbohydratesPercent = carbohydratesPercent + float(data.loc[x,'Carbohydrates (% Daily Value)'])
        dietaryFiberPercent = dietaryFiberPercent + float(data.loc[x,'Dietary Fiber (% Daily Value)'])
        sugarsPercent = sugarsPercent + float(data.loc[x,'Sugars (% Daily Value)'])
        proteinPercent = proteinPercent + float(data.loc[x,'Protein (% Daily Value)'])
        vitaminAPercent = vitaminAPercent + float(data.loc[x,'Vitamin A (% Daily Value)'])
        vitaminCPercent = vitaminCPercent + float(data.loc[x,'Vitamin C (% Daily Value)'])
        calciumPercent = calciumPercent + float(data.loc[x,'Calcium (% Daily Value)'])
        ironPercent = ironPercent + float(data.loc[x,'Iron (% Daily Value)'])
        rows = rows + 1


caloriesPercentAVG = round(caloriesPercent / rows, 2)
fatPercentAVG = round(fatPercent / rows, 2)
saturatedFatPercentAVG = round(saturatedFatPercent / rows, 2)
transFatPercentAVG = round(transFatPercent / rows, 2)
cholesterolPercentAVG = round(cholesterolPercent / rows, 2)
sodiumPercentAVG = round(sodiumPercent / rows, 2)
carbohydratesPercentAVG = round(carbohydratesPercent / rows, 2)
dietaryFiberPercentAVG = round(dietaryFiberPercent / rows, 2)
sugarsPercentAVG = round(sugarsPercent / rows, 2)
proteinPercentAVG = round(proteinPercent / rows, 2)
vitaminAPercentAVG = round(vitaminAPercent / rows, 2)
vitaminCPercentAVG = round(vitaminCPercent / rows, 2)
calciumPercentAVG = round(calciumPercent / rows, 2)
ironPercentAVG = round(ironPercent / rows, 2)


print("Calories average (% Daily Value) - " + str(caloriesPercentAVG) + "%.")
print("Fat average (% Daily Value) - " + str(fatPercentAVG) + "%.")
print("Saturated Fat average (% Daily Value) - " + str(saturatedFatPercentAVG) + "%.")
print("Trans Fat average (% Daily Value) - " + str(transFatPercentAVG) + "%.")
print("Cholesterol average (% Daily Value) - " + str(cholesterolPercentAVG) + "%.")
print("Sodium average (% Daily Value) - " + str(sodiumPercentAVG) + "%.")
print("Carbohydrates average (% Daily Value) - " + str(carbohydratesPercentAVG) + "%.")
print("Dietary Fibre average (% Daily Value) - " + str(dietaryFiberPercentAVG) + "%.")
print("Sugars average (% Daily Value) - " + str(sugarsPercentAVG) + "%.")
print("Protein average (% Daily Value) - " + str(proteinPercentAVG) + "%.")
print("Vitamin A average (% Daily Value) - " + str(vitaminAPercentAVG) + "%.")
print("Vitamin C average (% Daily Value) - " + str(vitaminCPercentAVG) + "%.")
print("Calcium average (% Daily Value) - " + str(calciumPercentAVG) + "%.")
print("Iron average (% Daily Value) - " + str(ironPercentAVG) + "%.")





print()
print()
print()
print()
print()
print()

print("Results when only the beverages/drinkable items used: ")
print()
caloriesPercent = 0
fatPercent = 0
saturatedFatPercent = 0
transFatPercent = 0
cholesterolPercent = 0
sodiumPercent = 0
carbohydratesPercent = 0
dietaryFiberPercent = 0
sugarsPercent = 0
proteinPercent = 0
vitaminAPercent = 0
vitaminCPercent = 0
calciumPercent = 0
ironPercent = 0

rows = 0
for x in data.index:
    if(data.loc[x,'Category'] == 'Beverages' or
       data.loc[x,'Category'] == 'Coffee & Tea' or
       data.loc[x,'Category'] == 'Smoothies & Shakes'):
        calories = calories + float(data.loc[x,'Calories'])
        caloriesPercent = caloriesPercent + float(data.loc[x,'Calories (% Daily Value)'])
        fatPercent = fatPercent + float(data.loc[x,'Total Fat (% Daily Value)'])
        saturatedFatPercent = saturatedFatPercent + float(data.loc[x,'Saturated Fat (% Daily Value)'])
        transFatPercent = transFatPercent + float(data.loc[x,'Trans Fat (% Daily Value)'])
        cholesterolPercent = cholesterolPercent + float(data.loc[x,'Cholesterol (% Daily Value)'])
        sodiumPercent = sodiumPercent + float(data.loc[x,'Sodium (% Daily Value)'])
        carbohydratesPercent = carbohydratesPercent + float(data.loc[x,'Carbohydrates (% Daily Value)'])
        dietaryFiberPercent = dietaryFiberPercent + float(data.loc[x,'Dietary Fiber (% Daily Value)'])
        sugarsPercent = sugarsPercent + float(data.loc[x,'Sugars (% Daily Value)'])
        proteinPercent = proteinPercent + float(data.loc[x,'Protein (% Daily Value)'])
        vitaminAPercent = vitaminAPercent + float(data.loc[x,'Vitamin A (% Daily Value)'])
        vitaminCPercent = vitaminCPercent + float(data.loc[x,'Vitamin C (% Daily Value)'])
        calciumPercent = calciumPercent + float(data.loc[x,'Calcium (% Daily Value)'])
        ironPercent = ironPercent + float(data.loc[x,'Iron (% Daily Value)'])
        rows = rows + 1


caloriesPercentAVG = round(caloriesPercent / rows, 2)
fatPercentAVG = round(fatPercent / rows, 2)
saturatedFatPercentAVG = round(saturatedFatPercent / rows, 2)
transFatPercentAVG = round(transFatPercent / rows, 2)
cholesterolPercentAVG = round(cholesterolPercent / rows, 2)
sodiumPercentAVG = round(sodiumPercent / rows, 2)
carbohydratesPercentAVG = round(carbohydratesPercent / rows, 2)
dietaryFiberPercentAVG = round(dietaryFiberPercent / rows, 2)
sugarsPercentAVG = round(sugarsPercent / rows, 2)
proteinPercentAVG = round(proteinPercent / rows, 2)
vitaminAPercentAVG = round(vitaminAPercent / rows, 2)
vitaminCPercentAVG = round(vitaminCPercent / rows, 2)
calciumPercentAVG = round(calciumPercent / rows, 2)
ironPercentAVG = round(ironPercent / rows, 2)


print("Calories average (% Daily Value) - " + str(caloriesPercentAVG) + "%.")
print("Fat average (% Daily Value) - " + str(fatPercentAVG) + "%.")
print("Saturated Fat average (% Daily Value) - " + str(saturatedFatPercentAVG) + "%.")
print("Trans Fat average (% Daily Value) - " + str(transFatPercentAVG) + "%.")
print("Cholesterol average (% Daily Value) - " + str(cholesterolPercentAVG) + "%.")
print("Sodium average (% Daily Value) - " + str(sodiumPercentAVG) + "%.")
print("Carbohydrates average (% Daily Value) - " + str(carbohydratesPercentAVG) + "%.")
print("Dietary Fibre average (% Daily Value) - " + str(dietaryFiberPercentAVG) + "%.")
print("Sugars average (% Daily Value) - " + str(sugarsPercentAVG) + "%.")
print("Protein average (% Daily Value) - " + str(proteinPercentAVG) + "%.")
print("Vitamin A average (% Daily Value) - " + str(vitaminAPercentAVG) + "%.")
print("Vitamin C average (% Daily Value) - " + str(vitaminCPercentAVG) + "%.")
print("Calcium average (% Daily Value) - " + str(calciumPercentAVG) + "%.")
print("Iron average (% Daily Value) - " + str(ironPercentAVG) + "%.")






print()
print()
print()
print()
print()
print()

print("Results when all the menu items used: ")
print()
caloriesPercent = 0
fatPercent = 0
saturatedFatPercent = 0
transFatPercent = 0
cholesterolPercent = 0
sodiumPercent = 0
carbohydratesPercent = 0
dietaryFiberPercent = 0
sugarsPercent = 0
proteinPercent = 0
vitaminAPercent = 0
vitaminCPercent = 0
calciumPercent = 0
ironPercent = 0

rows = data.shape[0]
for x in data.index:
    calories = calories + float(data.loc[x,'Calories'])
    caloriesPercent = caloriesPercent + float(data.loc[x,'Calories (% Daily Value)'])
    fatPercent = fatPercent + float(data.loc[x,'Total Fat (% Daily Value)'])
    saturatedFatPercent = saturatedFatPercent + float(data.loc[x,'Saturated Fat (% Daily Value)'])
    transFatPercent = transFatPercent + float(data.loc[x,'Trans Fat (% Daily Value)'])
    cholesterolPercent = cholesterolPercent + float(data.loc[x,'Cholesterol (% Daily Value)'])
    sodiumPercent = sodiumPercent + float(data.loc[x,'Sodium (% Daily Value)'])
    carbohydratesPercent = carbohydratesPercent + float(data.loc[x,'Carbohydrates (% Daily Value)'])
    dietaryFiberPercent = dietaryFiberPercent + float(data.loc[x,'Dietary Fiber (% Daily Value)'])
    sugarsPercent = sugarsPercent + float(data.loc[x,'Sugars (% Daily Value)'])
    proteinPercent = proteinPercent + float(data.loc[x,'Protein (% Daily Value)'])
    vitaminAPercent = vitaminAPercent + float(data.loc[x,'Vitamin A (% Daily Value)'])
    vitaminCPercent = vitaminCPercent + float(data.loc[x,'Vitamin C (% Daily Value)'])
    calciumPercent = calciumPercent + float(data.loc[x,'Calcium (% Daily Value)'])
    ironPercent = ironPercent + float(data.loc[x,'Iron (% Daily Value)'])


caloriesPercentAVG = round(caloriesPercent / rows, 2)
fatPercentAVG = round(fatPercent / rows, 2)
saturatedFatPercentAVG = round(saturatedFatPercent / rows, 2)
transFatPercentAVG = round(transFatPercent / rows, 2)
cholesterolPercentAVG = round(cholesterolPercent / rows, 2)
sodiumPercentAVG = round(sodiumPercent / rows, 2)
carbohydratesPercentAVG = round(carbohydratesPercent / rows, 2)
dietaryFiberPercentAVG = round(dietaryFiberPercent / rows, 2)
sugarsPercentAVG = round(sugarsPercent / rows, 2)
proteinPercentAVG = round(proteinPercent / rows, 2)
vitaminAPercentAVG = round(vitaminAPercent / rows, 2)
vitaminCPercentAVG = round(vitaminCPercent / rows, 2)
calciumPercentAVG = round(calciumPercent / rows, 2)
ironPercentAVG = round(ironPercent / rows, 2)


print("Calories average (% Daily Value) - " + str(caloriesPercentAVG) + "%.")
print("Fat average (% Daily Value) - " + str(fatPercentAVG) + "%.")
print("Saturated Fat average (% Daily Value) - " + str(saturatedFatPercentAVG) + "%.")
print("Trans Fat average (% Daily Value) - " + str(transFatPercentAVG) + "%.")
print("Cholesterol average (% Daily Value) - " + str(cholesterolPercentAVG) + "%.")
print("Sodium average (% Daily Value) - " + str(sodiumPercentAVG) + "%.")
print("Carbohydrates average (% Daily Value) - " + str(carbohydratesPercentAVG) + "%.")
print("Dietary Fibre average (% Daily Value) - " + str(dietaryFiberPercentAVG) + "%.")
print("Sugars average (% Daily Value) - " + str(sugarsPercentAVG) + "%.")
print("Protein average (% Daily Value) - " + str(proteinPercentAVG) + "%.")
print("Vitamin A average (% Daily Value) - " + str(vitaminAPercentAVG) + "%.")
print("Vitamin C average (% Daily Value) - " + str(vitaminCPercentAVG) + "%.")
print("Calcium average (% Daily Value) - " + str(calciumPercentAVG) + "%.")
print("Iron average (% Daily Value) - " + str(ironPercentAVG) + "%.")