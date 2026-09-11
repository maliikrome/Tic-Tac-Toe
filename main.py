def sum(a,b,c):
    return a+b+c

def printBoard(xstate, zState):
    zero = 'X' if xState[0] else ('O' if zState[0] else 0)
    one = 'X' if xState[1] else ('O' if zState[1] else 1)
    two = 'X' if xState[2] else ('O' if zState[2] else 2)
    three = 'X' if xState[3] else ('O' if zState[3] else 3)
    four = 'X' if xState[4] else ('O' if zState[4] else 4)
    five = 'X' if xState[5] else ('O' if zState[5] else 5)
    six = 'X' if xState[6] else ('O' if zState[6] else 6)
    seven = 'X' if xState[7] else ('O' if zState[7] else 7)
    eight = 'X' if xState[8] else ('O' if zState[8] else 8)
    print(f"{zero} | {one} | {two} |")
    print(f"-----------")
    print(f"{three} | {four} | {five} |")
    print(f"-----------")
    print(f"{six} | {seven} | {eight}|")

def checkwin(xState, zState):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if(sum(xState[win[0]],xState[win[1]],xState[win[2]]) == 3):
            print("X wins")
            return 1
          
        if(sum(zState[win[0]],zState[win[1]],zState[win[2]]) == 3):
            print("O wins!")
            return 0
            
    return -1

if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1 # 1 for x and 0 for O
    print("welcome to tic tac toe ")
    while(True):
        sumup = 0
        print(xState, zState)
        printBoard(xState,zState)
        if(turn == 1):
            print("X's Chance")
            value = int(input("please enter a value: "))
            if(value in range(0,9)):
                if(zState[value] == 1 or xState[value] == 1):
                    print("place already filled, please try again")
                    continue    
            else:
                print("Invalid input, please enter a value between 0 and 8")
                continue
            xState[value] = 1
        else:
            print("O's Chance")
            value = int(input("please enter a value: "))
            if(value in range(0,9)):
                if(xState[value] == 1 or zState[value] == 1):
                    print("place already filled, please try again")
                    continue
                zState[value] = 1
            else:
                print("Invalid input, please enter a value between 0 and 8")
                continue
      
        cwin = checkwin(xState,zState)
        if(cwin != -1):
            print("game over")
            printBoard(xState, zState)
            break
        else:
            for x in range(0,9):
                    sumup = xState[x] + zState[x] + sumup
            if(sumup == 9):
                     print("its a draw")
                     printBoard(xState, zState)
                     break

                  


 
        turn = 1 - turn