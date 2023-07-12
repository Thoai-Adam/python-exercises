import function_exercises
import json



from itertools import product, combinations, permutations

result0 = function_exercises.calculate_tip(1,3)
print(result0)

result1 = function_exercises.is_vowel('o')
print(result1)

result2 = function_exercises.get_letter_grade(70)
print(result2)

letters = 'abc'
numbers = [1,2,3]
result3 = list(product(letters, numbers))
print(len(result3))

letters = "abcd"
result4 = list(combinations(letters, 2))
print(len(result4))

letters = "abcd"
result5 = list(permutations(letters, 2))
print(len(result5))

result6 = json.load(open('profiles.json'))
print(result6)

data = [
    {"name": "John Doe", "isActive": True, "balance": "$1,234.56", "favoriteFruit": "apple", "unreadMessages": 3},
    {"name": "Jane Smith", "isActive": False, "balance": "$2,345.67", "favoriteFruit": "banana", "unreadMessages": 0},
    # Add more user data dictionaries here...
]

# Total number of users
total_users = len(data)
print("Total number of users:", total_users)

# Number of active users
active_users = sum(user["isActive"] for user in data)
print("Number of active users:", active_users)

# Number of inactive users
inactive_users = total_users - active_users
print("Number of inactive users:", inactive_users)

# Grand total of balances for all users
total_balance = sum(float(user["balance"].replace("$", "").replace(",", "")) for user in data)
print("Grand total of balances for all users:", total_balance)

# Average balance per user
average_balance = total_balance / total_users
print("Average balance per user:", average_balance)

# User with the lowest balance
lowest_balance_user = min(data, key=lambda user: float(user["balance"].replace("$", "").replace(",", "")))
print("User with the lowest balance:", lowest_balance_user["name"])

# User with the highest balance
highest_balance_user = max(data, key=lambda user: float(user["balance"].replace("$", "").replace(",", "")))
print("User with the highest balance:", highest_balance_user["name"])

# Most common favorite fruit
favorite_fruits = [user["favoriteFruit"] for user in data]
most_common_fruit = max(set(favorite_fruits), key=favorite_fruits.count)
print("Most common favorite fruit:", most_common_fruit)

# Least common favorite fruit
least_common_fruit = min(set(favorite_fruits), key=favorite_fruits.count)
print("Least common favorite fruit:", least_common_fruit)

# Total number of unread messages for all users
total_unread_messages = sum(user["unreadMessages"] for user in data)
print("Total number of unread messages for all users:", total_unread_messages)
