#Define a function named is_vowel. 
def is_vowel(value):
#It should return True if the passed string is a vowel, I was lazy so i only include 2 letters
    vowels = ['a', 'e']
#i use the strip to eliminate any spacing and lower to to include lower and capitalize words
    if value.strip().lower() in vowels:
        return True
#False otherwise
    else:
        return False
#def is_vowel(input):
#    if input in ('aeiou'):
#        return True
#    else:
#        return False

#testing time

def calculate_tip(tip_percentage, bill_total):
    if 0 <= tip_percentage <= 1:
        tip_amount = tip_percentage * bill_total
        return tip_amount
    else:
        return None
    
def get_letter_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'