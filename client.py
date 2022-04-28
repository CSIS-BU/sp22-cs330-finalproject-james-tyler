import sys 
import socket 
import array as arr
 
BUFFER_SIZE = 2048 

 
def client(server_ip, server_port): 
    move = ""
    board = []
    """TODO: Open socket and send message from sys.stdin""" 
    #keep playing marker
    cont = True
    sys.stdout.write('Input playername to begin:\n')
    playerName = "1"
    while playerName == "1":
        playerName = sys.stdin.readline()
        playerName = playerName.split(" ",1)[0]



        if ' ' in playerName: 
            sys.stdout.write("Invalid Username, cannot contain spaces")
            playerName = "1"
        else:
            break
    #while game is wanted to be played
    while cont:
    # create an INET, STREAMing socket 
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
            # now connect to server 
            s.connect((server_ip, server_port)) 
            #initializing game by sending playername to server
            sent = s.sendall((playerName + move).encode("utf-8", "surrogateescape")) 
            move = ""
            if sent == 0: 
                raise RuntimeError("socket connection broken") 
            #recieve board state
            serverInput = s.recv(BUFFER_SIZE)
            serverInput = serverInput.decode("utf-8", "surrogateescape")
            sys.stdout.write(serverInput + "\n")
            gameState = [char for char in serverInput]

            if gameState[10] != "0":
                #initializing board
                board = gameState[:9]
            #displaying board
            sys.stdout.write((board[0] + ' | '+ board[1] + ' | ' + board[2] + '\n')
                + (board[3] + ' | '+ board[4] + ' | ' + board[5] + '\n')
                + (board[6] + ' | '+ board[7] + ' | ' + board[8] + '\n'))

            #check game status                   
            if gameState[10] == '2':
                sys.stdout.write('Invalid move, try again.\n')
            #are you winning son?
            if gameState[10] == '3':
                sys.stdout.write('You Win!')
                sys.stdout.write("Would you like to play again? (Y/N)")
                cont = sys.stdin.buffer.readline(1) == "Y"
                break
            if gameState[10] == '4':
                sys.stdout.write('You Lose!')
                sys.stdout.write("Would you like to play again? (Y/N)")
                cont = sys.stdin.buffer.readline(1) == "Y"
                break
            if gameState[10] == '5':
                sys.stdout.write('Its a Tie!')
                sys.stdout.write("Would you like to play again? (Y/N)")
                cont = sys.stdin.buffer.readline(1) == "Y"
                break



            #sending turn to server
            if gameState[10] not in [3,4,5]:
                sys.stdout.write('Take your turn(input location 1-9): ')
                sys.stdout.flush()
                location = sys.stdin.read(1)
                #server will check for validity
                move = ' ' + location
        
        
        


    pass

def main(): 
    """Parse command-line arguments and call client function """ 
    if len(sys.argv) != 3: 
        sys.exit("Usage: python3 client-python.py [Server IP] [Server Port]") 
    server_ip = sys.argv[1] 
    server_port = int(sys.argv[2]) 
    client(server_ip, server_port) 
 
if __name__ == "__main__": 
    main()
