questions = [["\nwhich of the following is the favourite dish of Maanjar?","Milk","Chicken","Paneer masala" ,"B & C both","d"], 
             ["\nwhich of the following is the useless person in the family?","Saurabh","Shruti", "Jaadi","None","c"], 
             ["\nwhich of the following is good at making poha?","Shruti","Jaadi","Mummy" ,"Saurabh","a"],
             ["\nwhich of the following is the favourite dish of saurabh?","Cauliflower","Rajma", "Chole", "Potato","d"],
             ["\nwhich of the following is the mom's favourite icecream flavour?","Vanilla","Pista","Chocolate" ,"Strawberry","b"],
    ]

levels = [1000,2000,3000,5000,10000]

i=0
money = 0
for i in range(0,len(questions)):
    question = questions[i]
    print(f"\nQuestion for rs. {levels[i]} ")
    print(f"{question[0]}")
    print(f"a. {question[1]}           b. {question[2]}")
    print(f"c. {question[3]}           d. {question[4]}")
    reply = input("Enter your answer : ")

    if (reply == question[-1]):
        print(f"Coorect answer, you have won rs. {levels[i]}")
        if(i==4):
            money = 10000
    else:
        print(f"Wrong answer! Cash Prize you won : {levels[i-1]}")
        break

