import customtkinter
class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, master, message, Restart):
        super().__init__(master)
        self.geometry("400x300")
        self.message = message

        self.label = customtkinter.CTkLabel(self, text=message)
        self.label.pack(padx=20, pady=20)

        self.RestartButton = customtkinter.CTkButton(
                self,
                text="Restart",
                width=150, height=40,
                font=("Arial", 16, "bold"),
                command=Restart
            )
        self.RestartButton.pack(pady=15)
        self.QuitButton = customtkinter.CTkButton(self, text = "Quit",width=150, height=40,
                        font=("Arial", 16, "bold"),command = self.Quit)
        self.QuitButton.pack(pady=15)
    def Quit(self):
        app.destroy()

class TicTacToe(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.buttons = [] 
        self.title("Tic Tac Toe")
        self.geometry("500x600")
        self.xState = [0] * 9
        self.zState = [0] * 9
        self.turn = 1
        self.game_over = False
        self.toplevel_window = None

        frame1 = customtkinter.CTkFrame(self)
        frame1.pack(pady=10)
        frame2 = customtkinter.CTkFrame(self)
        frame2.pack(pady=10)

        title = customtkinter.CTkLabel(frame1, text="Tic Tac Toe",
                                        font=("Arial", 24, "bold"))
        title.pack(pady=5)

        self.statusLabel = customtkinter.CTkLabel(frame1, text="Turn: X",
                                                    font=("Arial", 18))
        self.statusLabel.pack(pady=5)

        for i in range(0,9):

            b = customtkinter.CTkButton(frame2, text=i, width=100, height=100,
                                                font=("Arial", 30, "bold"),
                                                text_color_disabled="white",
                                                command=lambda idx = i: self.ButtonClicked(idx))
            b.grid(row=i//3, column=i%3)
            self.buttons.append(b)
     
        self.RestartButton = customtkinter.CTkButton(
            self,
            text="Restart",
            width=150, height=40,
            font=("Arial", 16, "bold"),
            command=self.Restart,
        )
        self.RestartButton.pack(pady=15)

    def CheckWin(self):
            wins = [[0,1,2],[3,4,5],[6,7,8],
                [0,3,6],[1,4,7],[2,5,8],
                [0,4,8],[2,4,6]]
            for w in wins:
                  if self.xState[w[0]] + self.xState[w[1]] + self.xState[w[2]] == 3:
                   return "X"
                  if self.zState[w[0]] + self.zState[w[1]] + self.zState[w[2]] == 3:
                    return "O"
            if sum(self.xState) + sum(self.zState) == 9:
             return "Draw"
            return None
    def ButtonClicked(self, index):
        if self.game_over:
            return
        if self.xState[index] or self.zState[index]:
            return

        if self.turn == 1:
            self.xState[index] = 1
            self.buttons[index].configure(text="X", fg_color="dark blue", state="disabled")
            self.turn = 0
        else:
            self.zState[index] = 1
            self.buttons[index].configure(text="O", fg_color="dark blue", state="disabled")
            self.turn = 1

        result = self.CheckWin()          

        if result in ("X", "O", "Draw"):
            self.game_over = True
            for b in self.buttons:
                b.configure( fg_color = '#0a172b')
                if b.cget("state") == "normal":
                    b.configure(state="disabled",)
            if result == "Draw":
                message = 'DRAW'
                self.statusLabel.configure(text="It's a draw!", font=("Arial", 30, "bold"))

                if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                  
                   self.toplevel_window = ToplevelWindow(self,message,self.Restart)  # create window if its None or destroyed
                else:
                  
                   self.toplevel_window.focus()  # if window exists focus it
            else:
                message = f"{result} wins!"
                self.statusLabel.configure(text=f"{result} wins!", font=("Arial", 30, "bold"))

                if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                 
                   self.toplevel_window = ToplevelWindow(self,message, self.Restart)  # create window if its None or destroyed

                else:
                 
                   self.toplevel_window.focus()  # if window exists focus it
        else:
            who = "X" if self.turn == 1 else "O"
            self.statusLabel.configure(text=f"{who}'s Turn")   # <-- no self.frame1
    def Restart(self):
            self.xState = [0,0,0,0,0,0,0,0,0]
            self.zState = [0,0,0,0,0,0,0,0,0]
            self.turn = 1
            self.game_over = False

            if self.toplevel_window is not None and self.toplevel_window.winfo_exists():
               self.toplevel_window.destroy()
               self.toplevel_window = None

            for i, button in enumerate(self.buttons):
              button.configure(text=str(i), state="normal", fg_color=("#3B8ED0", "#1F6AA5"))

            self.statusLabel.configure(text="Turn: X")

app = TicTacToe()
app.mainloop()
