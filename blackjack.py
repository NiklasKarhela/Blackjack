import random
import time

cards = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11]
phand = []
dhand = []


def getcard(a):
  
  #taking a random card from the deck
  place = int(random.random()*len(cards))
  if place == 0:
    place = 1
    
  place = place - 1 #So that it take the correct number from list
  card = cards[place]
  
  #taking out the cards from the deck
  #aces
  if card == 1 or card == 11:
    pop1 = cards.index(1)
    pop2 = cards.index(11)
    cards.pop(pop1)
    cards.pop(pop2)

  #other
  else:
    cards.pop(place)
  
  #placing caard in hand
  if a == 0:
    phand.append(card)
  else:
    dhand.append(card)
  
def hit():
  getcard(0)
  print(phand)
  print("Player has: " + str(sum(phand)))
  
  #odds
  under = 21 - sum(phand)
  
  
  if sum(phand) < 21:
    hitting = input("Do you want to hit (yes/no)? ")
    
    if hitting == "yes":
      hit()
    else:
      dealer()
  elif sum(phand) == 21:
    print("Look at that 21!")
    dealer()
  
  elif 11 in phand:
    for x in range(len(phand)):
      if sum(phand) <= 21:
        choose = input("Do you want to hit(yes/no)? ")
        if choose == "yes":
          hit()
          break
        else:
          dealer()
          break
      elif 11 in phand:
        print("Changing 11 to 1")
        eleven_spot = phand.index(11)
        phand.pop(eleven_spot)
        phand.append(1)
        print(phand)
        print(sum(phand))
        
        choose = input("Do you want to hit(yes/no)? ")
        if choose == "yes":
          hit()
          break
        else:
          dealer()
          break
    
    
  else:
    print("Player busted")
    print("Dealer won")


def dealer():
  n = 1
  dealerhand = str(dhand[0]) +", " + str(dhand[1])
  
  dealerhand2 = str(dhand[0]) +" and " + str(dhand[1])
  if sum(dhand) <= 21 and sum(dhand)>16:
      print(dhand)
      print("Dealer has: " + str(sum(dhand)))
      
      
      if sum(dhand)<sum(phand):
        print("Player won")
      elif sum(dhand)==sum(phand):
        print("Player and dealer drawed")
      else:
        print("dealer won")
  
  while sum(dhand) <= 16:
    getcard(1)
    print(dhand)
    time.sleep(2)
    
    if sum(dhand) > 21 and 11 in dhand:
      for x in range(len(dhand)):
        if 11 in dhand:
          print("Changing 11 to 1")
          eleven_spot = dhand.index(11)
          dhand.pop(eleven_spot)
          dhand.append(1)
          print(dhand)
    
    if sum(dhand) <= 21 and sum(dhand)>16:
      print("Dealer has: " + str(sum(dhand)))
      
      
      if sum(phand) > sum(dhand):
        print("Player won")
      else:
        print("Dealer won")
        
    elif sum(dhand)>21:
      print(sum(dhand))
      print("dealer busted")
      print("Player won")
      
      
def deal():
  getcard(0)
  getcard(1)
  getcard(0)
  getcard(1)
  
  #if both cards are 11 for player and dealer
  if phand[0] == 11 and phand[1] == 11:
    phand.pop(1)
    phand.append(1)
  if dhand[0] == 11 and dhand[1] == 11:
    dhand.pop(1)
    dhand.append(1)
  if sum(phand) == 21:
    print("Look at that 21!")
    dealer()
  

  
game = 1
while game == 1:
  deal()
  plen = len(phand)-1
  dlen = len(dhand)-1
  print("Player has: " + str(phand[plen-1]) + " and " + str(phand[plen]))
  print("Dealer has: " + str(dhand[dlen-1]) + " and ?")
  
  hitting = input("Do you want to hit (yes/no)? ")
  if hitting == "yes":
    hit()
  else:
    dealer()
  
  
  break
  

