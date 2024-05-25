

from game_data import data
from random import randint
from art import logo, vs
from replit import clear

def get_random_account():
  """Get data from random account"""
  return data[randint(0, len(data) - 1)]

def Calculate(A, B):
  if A['follower_count'] > B['follower_count']:
    return 'A'
  else:
    return 'B'

print(logo)
A = get_random_account()
B = get_random_account()
score = 0
print(f"Compare A: {A['name']}, {A['description']}, {A['country']}")
print(vs)
print(f"Compare B: {B['name']}, {B['description']}, {B['country']}")
chosen = input("Who has more followers? Type 'A' or 'B': ")
while Calculate(A, B) == chosen:
  score += 1
  clear()
  print(logo)
  print(f"You're right! Current score: {score}")
  A = B
  B = get_random_account()
  print(f"Compare A: {A['name']}, {A['description']}, {A['country']}")
  print(vs)
  print(f"Compare B: {B['name']}, {B['description']}, {B['country']}")
  chosen = input("Who has more followers? Type 'A' or 'B': ")
print(f"Sorry, that's wrong. Final score: {score}")