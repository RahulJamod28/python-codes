# practices
# Q 5      
# resorved word mtlb kon kon se 

# import random
from random import randint

class Train: 

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")
    
    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket is fare in train no : {self.trainNo} from {fro} to {to} is {randint(224, 5454)}")

t = Train(12399)
t.book("Indore", "Kukshi")
t.getStatus()
t.getFare("Indore", "Kukshi")

# Q 6
# same as 5
