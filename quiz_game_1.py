
print("Welcome to my computer quiz game !!")

interested = input("Are you interested in playing the game ? ")

if interested != "yes":
    quit()

print("Let's start the game :) ")   

name = input("What is your name? ") 

smart = print("So " +name+ " Let's see how smart are you")

choose = print("There are 4 dificulty levels choose yours")
print("difficulty level 1")
print("difficulty level 2")
print("difficulty level 3")
print("difficulty level 4")

print("If you want to choose the level please write the number clearly like this : 1 ")



while(True):
    difficulty_level = input("Choose your difficulty level: ")
    
    if difficulty_level == "1":
        question = input("1. Which animal is known as the 'Ship of the Desert? ")

        if question == "camel":
            print("WOAH GENIUS IT'S THE CORRECT ANSWER!!")
        else:
            print("Better luck next time, incorrect answer")


        question_two = input("2. How many days are there in a week? ")

        if question_two == "7":
            print("BRAVO! CORRECT")

        else: 
            print("incorrect")

        question_three = input("3. How many hours are there in a day? ")      
        if question_three == "24":
            print ("CORRECT")
        else:
            print("incorrect")

        question_four = input("4. How many letters are there in the English alphabet? ")   
        if question_four == "26":
            print("CORRECT")
        else:
            print("incorrect") 

        question_five = input("5. How many days are there in a year? ")          
        if question_five == "365":
            print("CORRECT")
        else:
            print("incorrect")

        question_exit = input("Bahar jana hai ya nahi??  Ans-> y/n") 
        if question_exit == 'n':
            continue;
        else:
            exit()

    elif difficulty_level == "2":
        d_2_question = input("1. How many states are there in India? ") 
        if d_2_question == "28":
            print("IT'S CORRECT ANSWER")
        else:
            print("incorrect")

        d_2_questiontwo = input("2. Who was the first man to step on the moon? ")    
        if d_2_questiontwo == "neil armstrong":
            print("CONGRATS! IT'S CORRECT")
        else:
            print("incorrect")

        d_2_questionthree = input("3. Who was the first man to step on the moon? ") 
        if d_2_questionthree == "butterfly":
            print("CONGRATS! IT'S CORRECT")
        else:
            print("incorrect") 

        d_2_questionfour = input("4. Which city is the capital of India? ")
        if d_2_questionfour == "delhi":
            print("CONGRATS! IT'S CORRECT")
        else:
            print("incorrect")

        d_2_questionfive = input("5. Name the current prime minister of India ")
        if d_2_questionfive == "narendra modi":
            print("CONGRATS! IT'S CORRECT")
        else:
            print("incorrect")

        question_exit = input("Bahar jana hai ya nahi??  Ans-> y/n \n") 
        if question_exit == 'n':
            continue;
        else:
            exit()

    elif difficulty_level == "3":
        d_3_questions = input("1. Who was the first woman Prime Minister of India? ")
        if d_3_questions == "indira gandhi":
            print("CONGRATS! IT'S CORRECT")
        else:
            print("incorrect")

        d_3_questiontwo = input("2. Who is known as the father of India? ")
        if d_3_questiontwo == "Gandhi":
            print("CONGRATS! IT'S CORRECT")
        else:
            print("incorrect")

        d_3_questionthree = input("3. What is the national animal of India? ") 
        if d_3_questionthree == "tiger":
            print("CONGRATS! IT'S CORRECT")
        else:
            print("incorrect")         
            
        d_3_questionfour = input("4. What is the national bird of India? ")
        if d_3_questionfour == "peacock":
            print("CONGRATS! IT'S CORRECT")
        else:
            print("incorrect")

        d_3_questionfive = input("5. Who is the father of Indian Constitution? ")
        if d_3_questionfive == "dr ambedkar":
            print("CONGRATS! IT'S CORRECT")
        else:
            print("incorrect")    

        question_exit = input("Bahar jana hai ya nahi??  Ans-> y/n \n") 
        if question_exit == 'n':
            continue;
        else:
            exit()


    elif difficulty_level == "4":
        d_4_question = input("1. India lies in which continent? ")
        if d_4_question == "asia":
            print("CONGRATS! IT'S CORRECT")
        else:
            print("incorrect")
        
        d_4_questiontwo = input("2. Which country does pyramids exists? ")
        if d_4_questiontwo == "egypt":
            print("CONGRATS! IT'S CORRECT")
        else:
            print("incorrect")

        d_4_questionthree = input("3. Which is the largest river in the world? ")
        if d_4_questionthree == "nile":
            print("CONGRATS! IT'S CORRECT")
        else:
            print("incorrect")
        
        d_4_questionfour = input("4. Name the first 3 planets in our solar system ")
        if d_4_questionfour == "mercury, venus, earth":
            print("CONGRATS! IT'S CORRECT")
        else:
            print("incorrect")

        d_4_questionfive = input("How many planets does solar system have? ")
        if d_4_questionfive == "8":
            print("CONGRATS! IT'S CORRECT")
        else:
            print("incorrect")  


        question_exit = input("Bahar jana hai ya nahi??  Ans-> y/n \n") 
        if question_exit == 'n':
            continue;
        else:
            exit()