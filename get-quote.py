import random
print('Ditt favoritdjur är:')
def roligt():

  f = open("jenny.txt")
  djur = f.readlines()
  f.close()

  katt = len(djur) - 1
  jennysrandom = random.randint(0, katt)

  print(djur[jennysrandom])

if __name__== "__main__":
  roligt()
