# Name - Aditya Arya
# Date: 2025-10-06
# Project: Daily Calorie Tracker

print("Welcome to the Daily Calorie Tracker!")
print("This tool helps you log your meals and calories, compare against your daily limit, and save your session.\n")

meal_names = []
calorie_amounts = []

num_meals = int(input("How many meals do you want to enter today? "))

for i in range(num_meals):   
    meal = input(f"Enter {i+1} th meal name: ")
    calories = float(input(f"Enter calorie for {i+1} th meal: "))
    meal_names.append(meal)
    calorie_amounts.append(calories)    

total_calories = sum(calorie_amounts)
average_calories = total_calories / len(calorie_amounts)
daily_limit = float(input("\nEnter your daily calorie limit: "))

if total_calories > daily_limit:
    status_msg = f"Warning: You have exceeded your daily limit by {total_calories - daily_limit} calories."
else:
    status_msg = f"Great! You are within your daily limit. You have {daily_limit - total_calories} calories remaining."

print("\n\n--- Daily Calorie Summary ---")
print("Meal Name\tCalories")
print("-" * 30)

for meal, cal in zip(meal_names, calorie_amounts):
    print(f"{meal}\t\t{cal}")

print("-" * 30)
print(f"Total:\t\t{total_calories}")
print(f"Average:\t{average_calories}")
print(status_msg)

save = input("\nWould you like to save this session to a file? (yes/no): ").strip().lower()

import datetime

if save == 'yes':
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"calorie_log{timestamp}.txt"

    with open(filename, "w") as file:
        file.write("Daily Calorie Tracker Log\n")
        file.write(f"Date: {datetime.datetime.now()}\n\n")
        file.write("Meal Name\tCalories\n")
        file.write("-" * 30 + "\n")
        for meal, cal in zip(meal_names, calorie_amounts):
            file.write(f"{meal}\t\t{cal}\n")
        file.write("-" * 30 + "\n")
        file.write(f"Total:\t\t{total_calories}\n")
        file.write(f"Average:\t{average_calories}\n")
        file.write(status_msg + "\n")

    print(f"Session saved to {filename}")
else:
    print("Session not saved.")








