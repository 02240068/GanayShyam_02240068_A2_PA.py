import random

choice="""
select a game : 

1. Number Guessing Game
2. Rock Paper Scissors game
3. Trivia Persuit Game
4. Pokemon Card Binder Manager
5. Checking overall Score"""

def number_guessing_game():
    num = random.randint(1,100) #getting random number
    guess = 0
    print("wlecome to number guessing game")
    guessing_score=100
    while True:
        user_guess = int(input("please choose a number from 1-100: "))
       
        if user_guess < 1 or user_guess > 100:
            print("Guess should be between 1-100")
            continue
        
        if user_guess == num:
            print(f"\ncongratulations!!! your guess {num} is correct")
            break
        else:
            guess += 1
            guessing_score -= 5
            if user_guess < num:
                print("guess higher")
            else:
                print("guess lower")
            
            if guessing_score <= 0:
                print("you loose")
                break
        
            
            
    print(f"number of guess = {guess}")
    print(f"your score is {guessing_score}")
# number_guessing_game()
    
def rock_paper_scissor():
    rock_paper_scissor_score = 0
    computer_score = 0
    num_of_rounds = 0
    choice = ["rock", "paper", "scissors"]
    print("welcome to the game")
    while True:
        user_choice = input("choose (rock/paper/scissors/quit): ").lower().strip()
        
        if user_choice == "quit":
            print(f"you played {num_of_rounds} of rounds")
            print(f"your score is {rock_paper_scissor_score} \ncomputers score is {computer_score}")
            
            if rock_paper_scissor_score > computer_score:
                print("victory")
            elif computer_score > rock_paper_scissor_score:
                print("defeat")
            else:
                print("it's a draw")
            break
        
        if user_choice not in choice:
            print("invalid choice!!! please choose again")
            continue
        computer_choice = random.choice(choice)
        num_of_rounds += 1
        print(f"computer chose {computer_choice}")
        print(f"you chose {user_choice}")
        
        if user_choice == computer_choice:
            print("It's a tie!")
            rock_paper_scissor_score += 10
            computer_score += 10
            
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
            rock_paper_scissor_score += 10
        else:
            print("computer won!")
            computer_score += 10 
# rock_paper_scissor()

def trivia_pursuit():
    # Define questions with questions, choices, and correct answers
    questions = [
        {
            "question": "Who unified Bhutan in the 17th century?",
            "options": ["Ugyen Wangchuck", "Jigme Dorji Wangchuck", "Zhabdrung Ngawang Namgyal", "Padmasambhava"],
            "answer": "C"
        },
        {
            "question": "What is the value of 12 × 8?",
            "options": ["96", "84", "108", "88"],
            "answer": "A"
        },
        {
            "question": "What is the SI unit of force?",
            "options": ["Joule", "Watt", "Newton", "Pascal"],
            "answer": "C"
        },
        {
            "question": "When did Bhutan begin its policy of planned economic development with its first Five-Year Plan?",
            "options": ["1950", "1961", "1972", "1985"],
            "answer": "B"
        },
        {
            "question": "What is the sum of the interior angles of a triangle?",
            "options": ["360°", "180°", "90°", "270°"],
            "answer": "B"
        }
    ]
        
    
    # Initialize score
    TriviaScore = 0
    attempted_questions = 0
    total_questions = len(questions)
    
    # Welcome message
    
    print("WELCOME TO TRIVIA PURSUIT QUIZ GAME!")
    
   
    print(f"There are {total_questions} questions in total.")
    print("Type 'quit' at any time to end the game.")
    
    # Shuffle questions
    random.shuffle(questions)
    
    # Main game loop
   
    for i, q in enumerate(questions):
      
        print(f"Question {i+1}/{total_questions}: {q['question']}")
        
        # Display choices
        for j, choice in enumerate(q['options']):
            print(f"{chr(65+j)}. {choice}")
        
        # Get user answer
        while True:
            user_answer = input("\nYour answer (A/B/C/D or 'quit'): ").strip().upper()
            if user_answer in ['A', 'B', 'C', 'D', 'QUIT']:
                break
            print("Invalid input! Please enter A, B, C, D, or 'quit'.")
        
        # Check if user wants to quit
        if user_answer == 'QUIT':
            print("\nYou've chosen to quit the game.")
            break
        
        # Increment attempted questions counter
        attempted_questions += 1
        
        # Check answer
        if user_answer == q['answer']:
            print("\n your answer is correct")
            TriviaScore += 1
        else:
            correct_letter = q['answer']
            correct_answer = q['choices'][ord(correct_letter) - 65]
            print(f"\n✗ INCORRECT! The correct answer is {correct_letter}: {correct_answer}")
    
    # Final results
    print("\n" + "="*60)
    print("GAME OVER!")
    print("="*60)
    print(f"\nQuestions attempted: {attempted_questions}/{total_questions}")
    print(f"Final Score: {TriviaScore}/{total_questions}")
    
   


def pokemon_binder_manager():
    pokemon_binder = {}
    max_pokedex = 1025
    cards_per_page = 64
    rows = 8
    columns = 8
    score = 0
    def get_card_position(pokedex_number):
        "Given a pokedex_number, calculate its page, row, and column."
        
        "Page numbering starts at 1."
        "Card positions are filled left-to-right, top-to-bottom."
        index = pokedex_number - 1  # zero-based index
        page = index // cards_per_page + 1
        position_in_page = index % cards_per_page
        row = position_in_page // rows
        col = position_in_page % columns
        return page, row, col
    def add_card():
    
        pokedex = int(input("Enter Pokedex Number (1-1025): "))
        if not (1 <= pokedex <= max_pokedex):
            print("Invalid Pokedex number! Must be between 1 and 1025.\n")
            return
        
        if pokedex in pokemon_binder:
            page, row, col = pokemon_binder[pokedex]
            print(f"Card already in binder - Page: {page}, Row: {row}, Column: {col}, Status: Pre-existing\n")
        else:
            page, row, col = get_card_position(pokedex)
            pokemon_binder[pokedex] = (page, row, col)
            print(f"Page: {page}\nPosition: Row {row+1}, Column {col+1}\n Status: Added Pokedex #{pokedex} to binder\n")


    #reset function
    def reset():
        print("WARNING: you want to delete all the cards?")
        choice = input("Type 'confirm' to reset or 'exit' to return to Main Menu: ").lower().strip()
        if choice == "confirm":
            nonlocal pokemon_binder
            pokemon_binder.clear()
            print("The binder reset was successfull! All cards have been removed.\n")
        elif choice == "exit":
            print("Returning to main menu...\n")
            print("Welcome to Pokemon Card Binder Manager!\n")
            print("Main Menu:")
            print("1. Add a Pokemon Card")
            print("2. Reset Binder ")
            print("3. View Binder Placements")
            print("4. Exit \n")
        else:
            print("Invalid choice.\n")

    def status():
        print(f"Current Binder Contents: \n{"-"*20}\n")
        count = len(pokemon_binder)
        if count!=0:
            for i in pokemon_binder:
                print(f"Pokedex #{i}\n    Page: {pokemon_binder[i][0]}\n    Position: Row {pokemon_binder[i][1]}, Column {pokemon_binder[i][2]}\n")
            print("-"*20)

        else: print("The binder is empty.")

        completion = (count / max_pokedex) * 100
        print(f"Total Cards in Binder: {count}")
        print(f"% Completion: {completion:.2f}%")
        if count == max_pokedex:
            print("You have Caught them all!!")
        print("")
        nonlocal score
        pokeScore= completion

    def exit():
        print("Thank you for using Pokemon Card Binder Manager!")
    
        # exit()
    # --- Main Menu Loop ---
    print("Welcome to Pokemon Card Binder Manager!\n")
    print("Main Menu:")
    print("1. Add a Pokemon Card")
    print("2. Reset Binder ")
    print("3. View Binder Placements")
    print("4. Exit \n")
    while True:
        
        mode = int(input("Select option (1-4): "))

        if mode == 1:
            add_card()
            
        elif mode == 2:
            reset()
        elif mode == 3:
            status()
        elif mode == 4:
            exit()
            break
        else:
            print("Invalid mode selected. Please choose 1-4.\n")


def displayScore():
    global guessing_score, pokeScore, rock_paper_scissor_score, TriviaScore
    
    pass

while(True):
    print(choice)
    fun=int(input("Enter your choice: "))
    if fun==1: number_guessing_game()
    elif fun==2: rock_paper_scissor()
    elif fun==3: trivia_pursuit()
    elif fun==4:pokemon_binder_manager()
    elif fun==5: displayScore()
    elif fun==6: break    
