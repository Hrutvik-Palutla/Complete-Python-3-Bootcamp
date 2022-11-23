print("Tic-Tac-Toe")
print("To play this game using Python, follow the following instructions:")
print("1. Both players must be playing on the same computer. Choose a X Player, who goes first.")
print("2. To put a mark, select a coordinate. The columns are a, b & c and the rows are 1, 2 & 3. So, for example, a2 refers the first column and the second row.")
print("Let the fun begin!")
board_positions_list = ["a1","b1","c1","a2","b2","c2","a3","b3","c3"]
#The dictionary below has no practical role to play. However, if in the future you wanna make this code more efficient, use it.
#Currently, values do update for the dictionary below.
entered_values_dictionary = {"a1":" ","b1":" ","c1":" ","a2":" ","b2":" ","c2":" ","a3":" ","b3":" ","c3":" "}
a1 = " "
b1 = " "
c1 = " "
a2 = " "
b2 = " "
c2 = " "
a3 = " "
b3 = " "
c3 = " "
def board_printer():
    global a1,b1,c1,a2,b2,c2,a3,b3,c3
    print (
        f"    a   b   c \n\n1   {a1} | {b1} | {c1} \n   -----------\n2   {a2} | {b2} | {c2} \n   -----------\n3   {a3} | {b3} | {c3} \n"
    )
def xplayer_game():
    global board_positions_list
    x_choice = input("[X Player] Enter a square by using the coordinates (ex. a1, c2): ")
    while x_choice.lower() not in board_positions_list:
        print("You seemed to have entered an unrecognizable position, or a position that's already been taken.")
        x_choice = input("[X Player] Enter a square by using the coordinates (ex. a1, c2): ")
    board_positions_list.remove(f"{x_choice}")
    if x_choice == "a1":
        global a1
        a1 = "X"
        entered_values_dictionary["a1"] = "X"
    elif x_choice == "b1":
        global b1
        b1 = "X"
        entered_values_dictionary["b1"] = "X"
    elif x_choice == "c1":
        global c1
        c1 = "X"
        entered_values_dictionary["c1"] = "X"
    elif x_choice == "a2":
        global a2
        a2 = "X"
        entered_values_dictionary["a2"] = "X"
    elif x_choice == "b2":
        global b2
        b2 = "X"
        entered_values_dictionary["b2"] = "X"
    elif x_choice == "c2":
        global c2
        c2 = "X"
        entered_values_dictionary["c2"] = "X"
    elif x_choice == "a3":
        global a3
        a3 = "X"
        entered_values_dictionary["a3"] = "X"
    elif x_choice == "b3":
        global b3
        b3 = "X"
        entered_values_dictionary["b3"] = "X"
    else:
        global c3
        c3 = "X"
        entered_values_dictionary["c3"] = "X"
def oplayer_game():
    global board_positions_list
    o_choice = input("[O Player] Enter a square by using the coordinates (ex. a1, c2): ")
    while o_choice.lower() not in board_positions_list:
        print("You seemed to have entered an unrecognizable position, or a position that's already been taken.")
        o_choice = input("[O Player] Enter a square by using the coordinates (ex. a1, c2): ")
    board_positions_list.remove(f"{o_choice}")
    if o_choice == "a1":
        global a1
        a1 = "O"
        entered_values_dictionary["a1"] = "O"
    elif o_choice == "b1":
        global b1
        b1 = "O"
        entered_values_dictionary["b1"] = "O"
    elif o_choice == "c1":
        global c1
        c1 = "O"
        entered_values_dictionary["c1"] = "O"
    elif o_choice == "a2":
        global a2
        a2 = "O"
        entered_values_dictionary["a2"] = "O"
    elif o_choice == "b2":
        global b2
        b2 = "O"
        entered_values_dictionary["b2"] = "O"
    elif o_choice == "c2":
        global c2
        c2 = "O"
        entered_values_dictionary["c2"] = "O"
    elif o_choice == "a3":
        global a3
        a3 = "O"
        entered_values_dictionary["a3"] = "O"
    elif o_choice == "b3":
        global b3
        b3 = "O"
        entered_values_dictionary["b3"] = "O"
    else:
        global c3
        c3 = "O"
        entered_values_dictionary["c3"] = "O"
def winner_check():
    global a1,b1,c1,a2,b2,c2,a3,b3,c3
    winner_positions_list = [(a1,b1,c1),(a2,b2,c2),(a3,b3,c3),(a1,b2,c3),(a3,b2,c1),(a1,a2,a3),(b1,b2,b3),(c1,c2,c3)]
    for square1,square2,square3 in winner_positions_list:
        if square1 == "X" and square2 == "X" and square3 == "X":
            print("X PLAYER HAS WON! CONGRATULATIONS!")
            #print(f"The line is through {square1},{square2} and {square3}.")
            print("Care to play again? Rerun the file!")
            exit()
        elif square1 == "O" and square2 == "O" and square3 == "O":
            print("O PLAYER HAS WON! CONGRATULATIONS!")
            #print(f"The line is through {square1},{square2} and {square3}.")
            print("Care to play again? Rerun the file!")
            exit()
def game():
    board_printer()
    xplayer_game()
    board_printer()
    winner_check()
    oplayer_game()
    board_printer()
    winner_check()
    xplayer_game()
    board_printer()
    winner_check()
    oplayer_game()
    board_printer()
    winner_check()
    xplayer_game()
    board_printer()
    winner_check()
    oplayer_game()
    board_printer()
    winner_check()
    xplayer_game()
    board_printer()
    winner_check()
    oplayer_game()
    board_printer()
    winner_check()
    xplayer_game()
    board_printer()
    winner_check()
    print("X PLAYER AND O PLAYER HAVE TIED!")
    print("Care to play again? Rerun the file!")
game()