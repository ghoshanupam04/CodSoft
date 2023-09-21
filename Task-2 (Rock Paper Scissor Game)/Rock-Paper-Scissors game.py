import random
p1=input("OPTIONS: ROCK, PAPER, Scissor\n Your Choice: ").lower()
p2=random.choice(["ROCK","PAPER","Scissor"]).lower()
print("Opponent Choose: ",p2)
if p1=="rock" and p2=="paper":
    print("Opponent Win")
elif p1=="paper" and p2=="Scissor":
    print("Opponent Win")
elif p1=="Scissor" and p2=="rock":
    print("Opponent win")
elif p1==p2:
    print("Tie")
else:
    print("You Win")