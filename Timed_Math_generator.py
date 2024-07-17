import random
import time
OPERATOR=["+","-","*"]
MIN_OPERAND=3
MAX_OPERAND=12
TOTLA_PROBLEMS=10

def generate_problem():
    left=random.randint(MIN_OPERAND, MAX_OPERAND)
    right=random.randint(MIN_OPERAND, MAX_OPERAND)
    operator=random.choice(OPERATOR)
    
    expr=str(left)+" "+operator+" "+str(right)
    ans=eval(expr)
    return expr,ans

wrong=0
input("press enter to start!")
print("----------------------")
start_time=time.time()
for i in range(TOTLA_PROBLEMS):
    expr,ans=generate_problem()
    while True:
        guess=input("Problem #"+str(i+1)+": "+expr+"= ")
        if guess == str(ans):
            break
        wrong+=1
end_time=time.time()
total_time=round(end_time-start_time)

print("----------------------")
print("nice work! You finshed in",total_time,"seconds!")
