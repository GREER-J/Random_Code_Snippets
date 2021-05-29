'''
This is a spelling test for the weekly words at Goulburn.
This program will do several things:
1. Present the user with a word
2. Ask the user to spell that word
3. Mark the users spelling
4. Score the user
'''

#import
import time



#Spelling words
words = ['affidavit', 'grievous', 'sergeant', 'amphetamine', 'psychiatric', 'felonious', 'magistrate', 'parliament',
         'recognisance', 'syringe', 'prejudice', 'questioning', 'interrupted', 'identified', 'appropriate', 'rapport',
         'listening', 'liaison', 'accommodation', 'negotiator', 'modification', 'superintendent', 'receipt', 'registrar',
         'nemesis', 'commissioner', 'ombudsman', 'subpoena', 'accountability', 'complainant', 'demographics', 'emergency',
         'illicit', 'juvenile', 'marijuana', 'prosecutors', 'analysis', 'behaviour', 'concise', 'confidentiality', 'hallucinogen',
         'intoxicated', 'miscellaneous', 'psychotic', 'solicitor', 'consequence', 'aggravated', 'courteous', 'indictable',
         'jewellery', 'misdemeanour', 'pedestrian', 'receive', 'summarily', 'achieved', 'alignment', 'commitment', 'deceased',
         'explanation', 'licensing', 'inadmissible', 'negligent', 'surveillance', 'vehicle', 'accident', 'committee', 'effectively',
         'intervention', 'occurrence', 'procedure', 'personnel', 'rehabilitation', 'submitted', 'thorough', 'affirmative',
         'apprehension', 'committed', 'corroborate', 'evidence', 'information', 'initiative', 'operations', 'supervisor',
         'administration', 'appraisal', 'communication', 'counselling', 'defendant', 'incident', 'informant', 'liquor',
         'positive', 'suicide', 'diplomatic', 'parallel', 'millilitres', 'concentration', 'sobriety', 'influence', 'gradient']



def check(word, user):
  return bool(word == user)


def choose(number):
  return words[number]


def ask(word):
  print("\n\nYour word is ", word)
  time.sleep(.5)
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
  user = input("Your guess: ")
  user = user.lower()
  return user



def quiz(word):
  tries = 3
  while tries > 0:
    user = ask(word)
    if check(word, user) == True:
      print("\n\nWell done, you got it right!")
      time.sleep(2.5)
      break
    else:
      tries -= 1
      time.sleep(2.5)
      print("\n\n Sorry try again, you have", tries, "tries left!")
      continue


for number in range(len(words)):
  word = choose(number)
  correct = 0
  quiz(word)
