while True:
    import random 
    computer_choices=["rock","paper","scissors"]
    user_choice=input("Select your choice : Rock, Paper Or Scissors? ").lower()
    if user_choice=="rock":
        print("Your Choice Is Rock")
        print("""
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
            """)
    if user_choice=="paper":
        print("Your Choice Is Paper")
        print("""
        _______
    ---'    ____)____
            ______)
            _______)
            _______)
    ---.__________)         
    """)
    if user_choice=="scissors":
        print("Your Choice Is Scissors")
        print("""
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    """)
    generate_comp=random.choice(computer_choices)
    if generate_comp=="rock":
        print("Your Choice Is Rock")
        print("""
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
            """)
    if generate_comp=="paper":
        print("Your Choice Is Paper")
        print("""
        _______
    ---'    ____)____
            ______)
            _______)
            _______)
    ---.__________)         
    """)
    if generate_comp=="scissors":
        print("Your Choice Is Scissors")
        print("""
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    """)
    if generate_comp == user_choice:
        print("Draw, Let's Start Again😋😋")
        
    elif generate_comp == "rock":
        if user_choice == "scissors":
            print("You Lost!👎🏼")
        elif user_choice == "paper":
            print("You won!💪🏼")
        break
    elif generate_comp == "scissors":
        if user_choice == "rock":
            print("You won!💪🏼")
        elif user_choice == "paper":
            print("You Lost!👎🏼")
        break
    elif generate_comp == "paper":
        if user_choice == "rock":
            print("You Lost!👎🏼")
        elif user_choice == "scissors":
            print("You won!💪🏼")
        break
