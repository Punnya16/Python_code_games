import random

movie = ['the avengers', 'the dark knight', 'wonder woman', 'x men', 'green lantern', 'venom', 'thor', 'iron man', 'civil war', 'aqua man', 'man of steel', ' black panther', 'justice league', 'spider man', 'doctor strange', 'logan', 'the incredible hulk', 'captain marvel', 'the wolverine']



def create_blanks(movie):
    l = len(movie)
    letter = list(movie)    #decompose the string into separate alphabets
    temp = []   #empty list
    for i in range(l):
        if letter[i] == ' ':
            temp.append(' ')
        else:
            temp.append('*')
    q = ''.join(str(x) for x in temp)  #putting temp content in blanks string
    return q


def is_present(letter, movie):
    counter = movie.count(letter)    #how many times the letter occurs
    if counter == 0:
        return False    #letter not present
    else:
        return True     #letter present


def remove_blank(q, movie, letter):
    reference_list = list(movie)
    q_list = list(q)
    temp = []
    l = len(movie)
    for i in range(l):
        if reference_list[i] == ' ' or reference_list[i] == letter:
            temp.append(reference_list[i])
        else:
            if q_list[i] == '*':
                temp.append('*')
            else:
                temp.append(reference_list[i])
    q_new = ''.join(str(x) for x in temp)
    return q_new


def play():
    player_one = input("Player 1: Enter your name ->")
    player_two = input("Player 2: Enter your name ->")

    player_one_points = 0
    player_two_points = 0

    turn = 0    #to specify whose turn it is

    ready = True    #to check if players are ready for the game or not

    while ready:
        #check turn,if it is even then player1 plays else player2
        if turn % 2 == 0:
            #player 1 plays
            print("Turn for ", player_one)
            selected_movie = random.choice(movie)

            q = create_blanks(selected_movie)
            print(q)

            modified_q = q  #for the first run

            no_answer = True    #to check if answer is said or not

            while no_answer:
                #continue the game till answer is not given
                letter = input("Guess the letter! ")
                if is_present(letter, selected_movie):
                    #remove blanks
                    modified_q = remove_blank(modified_q, selected_movie, letter)
                    print(modified_q)
                    d = int(input("Press 1 to Guess the Movie || Press 2 to guess just another letter: "))
                    if d == 1:
                        ans = str(input("Your Guessed Movie: "))
                        if ans == selected_movie:
                            player_one_points = player_one_points + 1
                            print("You are Correct!")
                            no_answer = False   #as the player has answered
                            print(player_one, "Your score: ", player_one_points)
                        else:
                            print("Wrong answer. Please Try again! ")
                    else:
                        print("Another letter :)", end=" ")
            c = int(input("Press 1 to Continue || Press 0 to Quit "))
            if c == 0:
                print(player_one, "Your score: ", player_one_points)
                print(player_two, "Your score: ", player_two_points)
                turn += 1

        else:

            #player 2 plays

            print("Turn for ", player_two)
            selected_movie = str(random.choice(movie))

            q = create_blanks(selected_movie)
            print(q)

            modified_q = q  # for the first run

            no_answer = True  # to check if answer is said or not

            while no_answer:
                # continue the game till answer is not given
                letter = input("Guess the letter! ")
                if is_present(letter, selected_movie):
                    # remove blanks
                    modified_q = remove_blank(modified_q, selected_movie, letter)
                    print(modified_q)
                    d = int(input("Press 1 to Guess the Movie || Press 2 to guess just another letter "))
                    if d == 1:
                        ans = input("Your Guessed Movie: ")
                        if ans == selected_movie:
                            player_two_points = player_two_points + 1
                            print("You are Correct!")
                            no_answer = False  # as the player has answered
                            print(player_two, "Your score: ", player_two_points)
                        else:
                            print("Wrong answer. Please Try again! ")
                    else:
                        print("Another letter :)", end=" ")

            c = int(input("Press 1 to Continue || Press 0 to Quit "))
            if c == 0:
                print(player_one, "Your score: ", player_one_points)
                print(player_two, "Your score: ", player_two_points)
                print("Thank you for playing! Have a good day.")
                ready = False
        turn += 1   #giving turn to other player








print("\t\t-- WELCOME TO THE SUPERHERO MOVIES GUESSING GAME --\n")
play()