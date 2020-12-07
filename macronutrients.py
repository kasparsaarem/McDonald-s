#Searching for the best meal(s)/item(s) with
#balanced macro nutrients.

#1) Adding 5 features:
    #Protein (% Daily Value)
    #Proportion of carbohydrates
    #Proportion of protein
    #Proportion of fat
    #Saturated fat percentage in fat


#https://www.healthline.com/nutrition/how-much-protein-per-day
#2) Calculating the values of each feature added.
    #Protein (% Daily Value) - the values are calculated based
    # on the webpage below.
    # How Much Protein Should You Eat per Day?
        #56 grams per day for the average sedentary man
        #46 grams per day for the average sedentary woman
        #So the average is 51 grams per day


#3) Asking only for items of which carbohydrates, protein, 
    #fat and saturated fat percentage is between
    #the area described below:

        #Carbohydrates: 45-65%
        #Protein: 10-35%
        #Fat: 20-35% of which saturated fat less than 10%



import pandas as pd
data = pd.read_csv("menu.csv")


data['Protein (% Daily Value)'] = 'default'
for x in data.index:
    perDay = 51.0
    protein = float(data.loc[x,'Protein'])
    if(protein > 0):
        percentage = round((protein * 100) / perDay,1)
        data.loc[x,'Protein (% Daily Value)'] = percentage
    elif(protein == 0):
        data.loc[x,'Protein (% Daily Value)'] = 0


data['Proportion of Carbohydrates (%)'] = 'default'
for x in data.index:
    total = float(data.loc[x,'Total Fat']) + float(data.loc[x,'Carbohydrates']) + float(data.loc[x,'Protein'])
    carbohydrates = float(data.loc[x,'Carbohydrates'])
    if(carbohydrates > 0):
        proportion = round((carbohydrates * 100) / total,1)
        data.loc[x,'Proportion of Carbohydrates (%)'] = proportion
    elif(carbohydrates == 0):
        data.loc[x,'Proportion of Carbohydrates (%)'] = 0
        

data['Proportion of Protein (%)'] = 'default'
for x in data.index:
    total = float(data.loc[x,'Total Fat']) + float(data.loc[x,'Carbohydrates']) + float(data.loc[x,'Protein'])
    protein = float(data.loc[x,'Protein'])
    if(protein > 0):
        proportion = round((protein * 100) / total,1)
        data.loc[x,'Proportion of Protein (%)'] = proportion
    elif(protein == 0):
        data.loc[x,'Proportion of Protein (%)'] = 0


data['Proportion of Fat (%)'] = 'default'
for x in data.index:
    total = float(data.loc[x,'Total Fat']) + float(data.loc[x,'Carbohydrates']) + float(data.loc[x,'Protein'])
    fat = float(data.loc[x,'Total Fat'])
    if(fat > 0):
        proportion = round((fat * 100) / total,1)
        data.loc[x,'Proportion of Fat (%)'] = proportion
    elif(fat == 0):
        data.loc[x,'Proportion of Fat (%)'] = 0
       

data['Saturated Fat Percentage in Fat'] = 'default'
for x in data.index:
    fat = float(data.loc[x,'Total Fat'])
    saturated = float(data.loc[x,'Saturated Fat'])
    if(fat > 0):
        proportion = round((saturated * 100) / fat,1)
        data.loc[x,'Saturated Fat Percentage in Fat'] = proportion
    elif(fat == 0):
        data.loc[x,'Saturated Fat Percentage in Fat'] = 0
       
count = 1
for x in data.index:
    carbohydrates = data.loc[x,'Proportion of Carbohydrates (%)']
    protein = data.loc[x,'Proportion of Protein (%)']
    fat = data.loc[x,'Proportion of Fat (%)']
    
    #instead of saturated we use Saturated Fat (% Daily Value)
    #because when adding the condition that saturated < 10
    #then there are no results.
    
    #So it means that there are too much Saturated Fat in Fat.
    
    saturated = data.loc[x,'Saturated Fat Percentage in Fat']
    
    #Assuming that an average is three meals a day,
    #we look that the nutrient % Daily Value is not more than (100/3)
    if(45 <= carbohydrates <= 65 and 10 <= protein <= 35 and
       20 <= fat <= 35 and
       float(data.loc[x,'Carbohydrates (% Daily Value)']) <= (100/3)
       and float(data.loc[x,'Total Fat (% Daily Value)']) <= (100/3)
       and float(data.loc[x,'Saturated Fat (% Daily Value)']) <= (100/3)
       and float(data.loc[x,'Protein (% Daily Value)']) <= (100/3)):
        
        print(str(count) + ". " + data.loc[x,'Category'] + ": " + str(data.loc[x,'Item']))
        count = count + 1