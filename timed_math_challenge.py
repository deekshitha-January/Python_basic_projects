import random
import time

OPERATORS = ["+", "-", "*", "/"]

MIN_OPERAND = 3
MAX_OPERAND = 12

TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)

    operator = random.choice(OPERATORS)

    expr = str(left) + " " +operator+  " " +str(right)
    answer = eval(expr)

    # print(expr)
    # print(answer)
    return expr, answer
wrong =0
correct =0
input("Press enter to start")
print("-----------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr , answer = generate_problem()
    while True:
        guess = input("Problem #"+str(i+1)+": "+expr+" = ")
        if(guess == str(answer)):
            print("Congracts")
            correct = correct+1
            
        else:
            print("Failed")
            wrong = wrong + 1
        break
        # wrong+=1

end_time = time.time()
    
total_time= end_time - start_time
print("------------")
print("Nice work, you finished in", total_time, "seconds!")
print("Correct answers = ", correct, "---- wrong answers = ", wrong)

    

         
             



