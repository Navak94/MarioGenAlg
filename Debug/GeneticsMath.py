from numpy import random

AllelePAT=[""]


def lowprob():
   
    AllelePAT.clear()
    Prob = random.randint(4)
    AllelePAT.append("0")
    AllelePAT.append("0")
    AllelePAT.append("0")
    AllelePAT.append("1")
    print(AllelePAT[Prob]) 
    AllelePAT.clear()
  

def midprob():
    AllelePAT.clear()
    Prob = random.randint(4)
    AllelePAT.append("0")
    AllelePAT.append("0")
    AllelePAT.append("1")
    AllelePAT.append("1")
    print(AllelePAT[Prob]) 
    AllelePAT.clear()


def highprob():
    AllelePAT.clear()
    Prob = random.randint(4)
    AllelePAT.append("0")
    AllelePAT.append("1")
    AllelePAT.append("1")
    AllelePAT.append("1")
    print(AllelePAT[Prob])
    AllelePAT.clear()
    
if __name__ == "__main__":
   for x in range (0, 100):
       lowprob()
       midprob()
       highprob()
       print("ROUND ", x  )
    
