print("Today's date ? ")
date = input()
print("Breakfast Calories ? ")
brkfst = int(input())
print("Lunch Calorie ? ")
lunch = int(input())
print("Dinner Calorie ? ")
dinner = int(input())
print("Snack Calorie ? ")
snack = int(input())
sum = brkfst + lunch + dinner + snack
print("Calorie content for " + date + " : " + str(sum))