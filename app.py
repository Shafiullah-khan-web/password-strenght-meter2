import streamlit as st

import re
import string
score = 0
def check_password_strenght(password):
  global score
  # len check
  if len(password) >= 8:
    score += 1
  else:
    print("password should be atleast 8 characters long.")

  #upper and lowercase check
  if re.search(r"[A-Z]",password) and  re.search(r"[a-z]",password):
    score += 1
  else:
    print("include both  upercase and lowercase letters.")

  # digit check
  if re.search(r"\d",password):
    score += 1
  else:
    print("add atleast one number (0-9).")

  # special chracter check
  if re.search(r"[!$%^*&]",password):
    score += 1
  else:
    print("include atleast one special chracter (!$%^&*).")

  # strenght rating
  if score == 4:
    print("strong password!")
  elif score == 3:
    print("moderate password - consider adding more security features.")
  else:
    print("weak password - improve it using the suggestion above.")

 # get user input
password = input("enter your password ")



# check password strenght
check_password_strenght(password)
