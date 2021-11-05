import time
from time import sleep
e = input("a, s, m, d, or fd (add f to a, s, m, d, for float d = ffd fd = fffd): ")
wt = "Please wait 5 seconds to restart."
def getn(a1, a2, s):
  if s == "a":
     a1 = int(a1)
     a2 = int(a2)
     b1 = a1 + a2
     c1 = str(b1)
     print("Answer: " + c1)
     time.sleep(1)
     print(wt)
     time.sleep(5)
  if s == "s":
      a1 = int(a1)
      a2 = int(a2)
      b1 = a1 - a2
      c1 = str(b1)
      print("Answer: " + c1)
      time.sleep(1)
      print(wt)
      time.sleep(5)
  if s == "m":
      a1 = int(a1)
      a2 = int(a2)
      b1 = a1 * a2
      c1 = str(b1)
      print("Answer: " + c1)
      time.sleep(1)
      print(wt)
      time.sleep(5)
  if s == "d":
      a1 = int(a1)
      a2 = int(a2)
      b1 = a1 / a2
      c1 = str(b1)
      print("Answer: " + c1)
      time.sleep(1)
      print(wt)
      time.sleep(5)
  if s == "fd":
        a1 = int(a1)
        a2 = int(a2)
        b1 = a1 // a2
        c1 = str(b1)
        print("Answer: " + c1)
        time.sleep(1)
        print(wt)
        time.sleep(5)
  if s == "fa":
   a1 = float(a1)
   a2 = float(a2)
   b1 = a1 + a2
   if b1.is_integer():
     b1 = int(b1)
   c1 = str(b1)
   print("Answer: " + c1)
  if s == "fs":
    a1 = float(a1)
    a2 = float(a2)
    b1 = a1 - a2
    if b1.is_integer():
     b1 = int(b1)
    c1 = str(b1)  
    print("Answer: " + c1)
  if s == "fm":
    a1 = float(a1)
    a2 = float(a2)
    b1 = a1 * a2
    if b1.is_integer():
     b1 = int(b1)
    c1 = str(b1)
    print("Answer: " + c1)
  if s == "ffd":
    a1 = float(a1)
    a2 = float(a2)
    b1 = a1 / a2
    if b1.is_integer():
     b1 = int(b1)
    c1 = str(b1)
    print("Answer: " + c1)
  if s == "fffd":
    a1 = float(a1)
    a2 = float(a2)
    b1 = a1 // a2
    if b1.is_integer():
     b1 = int(b1)
    c1 = str(b1)
    print("Answer: " + c1)
    
    
    
    
def run(t):
  ask = input("What is the 1st number? ")
  ask2 = input("What is the 2nd number? ")
  getn(ask, ask2, t)
run(e)
while True:
  run(input("a, s, m, d, or fd (add f to a, s, m, d, for float d = ffd fd = fffd): "))
