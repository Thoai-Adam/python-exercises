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

# Total number of users
total_users = len(result6)
print("Total number of users:", total_users)

# Number of active users
active_users = sum(user["isActive"] for user in result6)
print("Number of active users:", active_users)

# Number of inactive users
inactive_users = total_users - active_users
print("Number of inactive users:", inactive_users)

# Grand total of balances for all users
total_balance = sum(float(user["balance"].replace("$", "").replace(",", "")) for user in result6)
print("Grand total of balances for all users:", total_balance)

"""total_balance = 10000  # Example total balance
total_users = 50  # Example total number of users

average_balance = total_balance / total_users
rounded_average_balance = round(average_balance, 2)

print("Average balance per user:", rounded_average_balance)"""

# Average balance per user
average_balance = total_balance / total_users
print("Average balance per user:", (average_balance))

# User with the lowest balance
lowest_balance_user = min(result6, key=lambda user: float(user["balance"].replace("$", "").replace(",", "")))
print("User with the lowest balance:", lowest_balance_user["name"])

#could be written as
"""balance_list = []
for profile in profiles:
        profile_balance = float(profile['balance'].strip('$').replace(',',''))
        balance_list.append(profile_balance)
min(balance_list)
for profile in profiles:
        if float(profile['balance'].strip('$').replace(',','')) == min(balance_list):
                print(profile['name'], min(balance_list))"""


# User with the highest balance
highest_balance_user = max(result6, key=lambda user: float(user["balance"].replace("$", "").replace(",", "")))
print("User with the highest balance:", highest_balance_user["name"])

# Most common favorite fruit, 
favorite_fruits = [user["favoriteFruit"] for user in result6]
most_common_fruit = max(set(favorite_fruits), key=favorite_fruits.count)
print("Most common favorite fruit:", most_common_fruit)

# Least common favorite fruit
least_common_fruit = min(set(favorite_fruits), key=favorite_fruits.count)
print("Least common favorite fruit:", least_common_fruit)

total_messages = 0
for profile in result6:
    #print(profile['greeting'])
    message = profile['greeting'].split(' ')
    for word in message: 
        if word.isdigit():
            total_messages += int(word)
print('The number of unread messages are',total_messages)


