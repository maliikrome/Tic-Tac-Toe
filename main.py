class tic_tac_toe(customtkinter.CTk):
    def __init__(self):
        super().__init__()
                
        self.title("Tic Tac Toe")
        self.geometry("500x600")
        self.xState = [0] * 9
        self.zState = [0] * 9
        self.turn = 1
        self.game_over = False

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

        self.button0 = customtkinter.CTkButton(frame2, text="0", width=100, height=100,
                                               font=("Arial", 30, "bold"),
                                               text_color_disabled="white",
                                               command=lambda: self.buttonclicked(0))
        self.button0.grid(row=0, column=0)

        self.button1 = customtkinter.CTkButton(frame2, text="1", width=100, height=100,
                                               font=("Arial", 30, "bold"),
                                               text_color_disabled="white",
                                               command=lambda: self.buttonclicked(1))
        self.button1.grid(row=0, column=1)

        self.button2 = customtkinter.CTkButton(frame2, text="2", width=100, height=100,
                                               font=("Arial", 30, "bold"),
                                               text_color_disabled="white",
                                               command=lambda: self.buttonclicked(2))
        self.button2.grid(row=0, column=2)

        self.button3 = customtkinter.CTkButton(frame2, text="3", width=100, height=100,
                                               font=("Arial", 30, "bold"),
                                               text_color_disabled="white",
                                               command=lambda: self.buttonclicked(3))
        self.button3.grid(row=1, column=0)

        self.button4 = customtkinter.CTkButton(frame2, text="4", width=100, height=100,
                                               font=("Arial", 30, "bold"),
                                               text_color_disabled="white",
                                               command=lambda: self.buttonclicked(4))
        self.button4.grid(row=1, column=1)

        self.button5 = customtkinter.CTkButton(frame2, text="5", width=100, height=100,
                                               font=("Arial", 30, "bold"),
                                               text_color_disabled="white",
                                               command=lambda: self.buttonclicked(5))
        self.button5.grid(row=1, column=2)

        self.button6 = customtkinter.CTkButton(frame2, text="6", width=100, height=100,
                                               font=("Arial", 30, "bold"),
                                               text_color_disabled="white",
                                               command=lambda: self.buttonclicked(6))
        self.button6.grid(row=2, column=0)

        self.button7 = customtkinter.CTkButton(frame2, text="7", width=100, height=100,
                                               font=("Arial", 30, "bold"),
                                               text_color_disabled="white",
                                               command=lambda: self.buttonclicked(7))
        self.button7.grid(row=2, column=1)

        self.button8 = customtkinter.CTkButton(frame2, text="8", width=100, height=100,
                                               font=("Arial", 30, "bold"),
                                               text_color_disabled="white",
                                               command=lambda: self.buttonclicked(8))
        self.button8.grid(row=2, column=2)

        self.buttons = [self.button0, self.button1, self.button2,
                        self.button3, self.button4, self.button5,
                        self.button6, self.button7, self.button8]
        self.restartButton = customtkinter.CTkButton(
            self,
            text="Restart",
            width=150, height=40,
            font=("Arial", 16, "bold"),
            command=self.restart,
        )
        self.restartButton.pack(pady=15)

    def checkwin(self):
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
    def buttonclicked(self, index):
            if self.game_over:
                return
            if self.xState[index] or self.zState[index]:
                return

            if self.turn == 1:
                self.xState[index] = 1
                self.buttons[index].configure(text="X", fg_color="dark blue",
                                            state="disabled")
                self.turn = 0
            else:
                self.zState[index] = 1
                self.buttons[index].configure(text="O", fg_color="dark blue",
                                            state="disabled")
                self.turn = 1

            result = self.checkwin()

            if result in ("X", "O", "Draw"):
                self.game_over = True
                for b in self.buttons:
                    b.configure(state="disabled")
                if result == "Draw":
                    self.statusLabel.configure(text="It's a draw!")
                else:
                    self.statusLabel.configure(text=f"{result} wins!")
            else:
                who = "X's" if self.turn == 1 else "O's"
                self.statusLabel.configure(text=f"{who} Turn")

    def restart(self):
            self.xState = [0,0,0,0,0,0,0,0,0]
            self.zState = [0,0,0,0,0,0,0,0,0]
            self.turn = 1
            self.game_over = False

            for i, b in enumerate(self.buttons):
                b.configure(text=str(i), state="normal",
                            fg_color=("#3B8ED0", "#1F6AA5"))

            self.statusLabel.configure(text="Turn: X")
app = tic_tac_toe()
app.mainloop()
