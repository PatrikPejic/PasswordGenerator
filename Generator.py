import random

NUMBER_OF_CHAR_TYPES = 3

letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'
'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

number_list = [i for i in range(10)]

special_character_list = ['!', '@', '#', '$', '%', '^', '&', '*', '-', '_', '=', '+',
 '<', '>', '/', '?', 'q', '~']

def select_random_char(): 
  char = ""
  char_type = random.randint(0, NUMBER_OF_CHAR_TYPES)
  if char_type == 0: 
    char = letter_list[random.randint(0, len(letter_list))]

  if char_type == 1: 
    char = letter_list[random.randint(0, len(letter_list))].upper()
  
  if char_type == 2: 
    char = number_list[random.randint(0, len(number_list))]

  if char_type == 3: 
    char = special_character_list[random.randint(0, len(special_character_list))]

  return char 
  
'''
def generate_password(password_length):
  password = "" 
  for i in range(password_length): 
    password += select_random_char()
  return password
'''