import customtkinter

root = customtkinter.CTk()
root.title("tic tac toe")
root.geometry("500x600")


xState = [0,0,0,0,0,0,0,0,0]
zState = [0,0,0,0,0,0,0,0,0]
turn = 1
game_over = False

frame1 = customtkinter.CTkFrame(root)
frame1.pack(pady=10)

titleLabel = customtkinter.CTkLabel(frame1, text="Tic Tac Toe", font=("Arial", 24, "bold"))
titleLabel.pack(pady=5)

statusLabel = customtkinter.CTkLabel(frame1, text="Turn: X", font=("Arial", 18))
statusLabel.pack(pady=5)
frame2 = customtkinter.CTkFrame(root)
frame2.pack(pady=10)


def checkwin(xState, zState):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if xState[win[0]] + xState[win[1]] + xState[win[2]] == 3:
            return "X"
        if zState[win[0]] + zState[win[1]] + zState[win[2]] == 3:
            return "O"
    if sum(xState) + sum(zState) == 9:
        return "Draw"
    return None


def buttonclicked(index):
    global turn, game_over

    if game_over:
        return
    if xState[index] or zState[index]:
        return

    if turn == 1:
        xState[index] = 1
        buttons[index].configure(text="X", fg_color="dark blue", state="disabled")
        turn = 0
    else:
        zState[index] = 1
        buttons[index].configure(text="O", fg_color="dark blue", state="disabled")
        turn = 1

    result = checkwin(xState, zState)

    if result in ("X", "O", "Draw"):
        game_over = True
        for b in buttons:
            b.configure(state="disabled")
        if result == "Draw":
            statusLabel.configure(text="It's a draw!")
        else:
            statusLabel.configure(text=f"{result} wins!")
    else:
        temp = "X's" if turn == 1 else "O's"
        statusLabel.configure(text=f"{temp} Turn")



button0 = customtkinter.CTkButton(frame2, text="0", width=100, height=100, font=("Arial", 30, "bold"), text_color_disabled="white", command=lambda: buttonclicked(0))
button0.grid(row=0, column=0)


button1 = customtkinter.CTkButton(frame2, text="1", width=100, height=100, font=("Arial", 30, "bold"), text_color_disabled="white", command=lambda: buttonclicked(1))
button1.grid(row=0, column=1)

button2 = customtkinter.CTkButton(frame2, text="2", width=100, height=100, font=("Arial", 30, "bold"), text_color_disabled="white", command=lambda: buttonclicked(2))
button2.grid(row=0, column=2)

button3 = customtkinter.CTkButton(frame2, text="3", width=100, height=100, font=("Arial", 30, "bold"), text_color_disabled="white", command=lambda: buttonclicked(3))
button3.grid(row=1, column=0)


button4 = customtkinter.CTkButton(frame2, text="4", width=100, height=100, font=("Arial", 30, "bold"), text_color_disabled="white", command=lambda: buttonclicked(4))
button4.grid(row=1, column=1)

button5 = customtkinter.CTkButton(frame2, text="5", width=100, height=100, font=("Arial", 30, "bold"), text_color_disabled="white", command=lambda: buttonclicked(5))
button5.grid(row=1, column=2)

button6 = customtkinter.CTkButton(frame2, text="6", width=100, height=100, font=("Arial", 30, "bold"), text_color_disabled="white", command=lambda: buttonclicked(6))
button6.grid(row=2, column=0)

button7 = customtkinter.CTkButton(frame2, text="7", width=100, height=100, font=("Arial", 30, "bold"), text_color_disabled="white", command=lambda: buttonclicked(7))
button7.grid(row=2, column=1)

button8 = customtkinter.CTkButton(frame2, text="8", width=100, height=100, font=("Arial", 30, "bold"), text_color_disabled="white", command=lambda: buttonclicked(8))
button8.grid(row=2, column=2)

buttons = [button0, button1, button2, button3, button4, button5, button6, button7, button8]

def restart():
    global xState, zState, turn, game_over

    xState = [0,0,0,0,0,0,0,0,0]
    zState = [0,0,0,0,0,0,0,0,0]
    turn = 1
    game_over = False

    for i, b in enumerate(buttons):
        b.configure(text=str(i), state="normal", fg_color = "dark blue")

    statusLabel.configure(text="Turn: X")


restartButton = customtkinter.CTkButton(root, text="Restart", width=150, height=40, font=("Arial", 16, "bold"), command=restart)
restartButton.pack(pady=15)


root.mainloop()