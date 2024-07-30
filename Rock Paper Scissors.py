import random

should_break = False
while True:
    value = input(f"'r' for rock, 'p' for paper, 's' for scissors: ").strip().lower()
    print()
    Rnd = random.choice(['r', 'p', 's'])

    # Check for invalid input
    if value not in ['r','p','s']:
        print("wrong input. Please Try again!")

    # Draw
    if value == Rnd:
        print(f'I chose {Rnd}')
        print('draw')
        print()

        # Try again and exit loop
        choice =  input(f"Type 'T' to Try again or 'E' to Exit ").strip().lower()
        if choice == 'e':
            should_break = True
            break
        elif choice not in ['t','e']:
            print("wrong input. Please Try again!")
            print()
            choice = input(f"Type 'T' to Try again or 'E' to Exit ").strip().lower()
        else:
            continue

        if should_break == True:
            break


# Player wins
    if (value =='r' and Rnd == 's') or (value == 'p' and Rnd == 'r') or (value == 's' and Rnd == 'p'):
        print(f'I chose {Rnd}')
        print('You win!')
        print()

        # Try again and exit loop
        choice = input(f"Type 'T' to Try again or 'E' to Exit ").strip().lower()
        if choice == 'e':
            should_break = True
            break
        elif choice not in ['t', 'e']:
            print("wrong input. Please Try again!")
            print()
            choice = input(f"Type 'T' to Try again or 'E' to Exit ").strip().lower()
        else:
            continue

        if should_break == True:
            break

    if (Rnd== 'r' and value == 's') or (Rnd== 'p' and value == 'r') or (Rnd== 's' and value == 'p'):
        print(f'I chose {Rnd}')
        print('I win!')
        print()

        # Try again and exit loop
        choice = input(f"Type 'T' to Try again or 'E' to Exit ").strip().lower()
        if choice == 'e':
            should_break = True
            break
        elif choice not in ['t', 'e']:
            print("wrong input. Please Try again!")
            print()
            choice = input(f"Type 'T' to Try again or 'E' to Exit ").strip().lower()
        else:
            continue

        if should_break == True:
            break