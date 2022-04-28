import sys 
import socket 
import array as arr
 
BUFFER_SIZE = 2048 

 
def client(server_ip, server_port): 
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
            sys.stdout.write("Invalid Username, cannot contain spaces1")
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
            sent = s.sendall(playerName.encode("utf-8", "surrogateescape")) 
            if sent == 0: 
                raise RuntimeError("socket connection broken") 
            #recieve board state
            serverInput = s.recv(BUFFER_SIZE)
            serverInput = serverInput.decode("utf-8", "surrogateescape")
            sys.stdout.write(serverInput + "\n")
            gameState = [char for char in serverInput]
            if gameState[10] != '0':
                #initializing board
                board = gameState[:9]

            while True:
                #displaying board
                sys.stdout.write((board[0] + ' | '+ board[1] + ' | ' + board[2] + '\n')
                    + (board[3] + ' | '+ board[4] + ' | ' + board[5] + '\n')
                    + (board[6] + ' | '+ board[7] + ' | ' + board[8] + '\n'))

                #sending turn to server
                sys.stdout.write('Take your turn(input location 1-9): ')
                location = sys.stdin.read(1)
                turn = playerName + ' ' + location
                sent = s.sendall(turn)
                if sent == 0: 
                    raise RuntimeError("socket connection broken")

                #reciving gamestate from server
                serverInput = s.recv(BUFFER_SIZE)
                gameState = serverInput.split()
                
                #updating board
                if gameState[1] == '1':
                    count = 0
                    for space in gameState[0]:
                        board[count] = space
                        count + 1                        
                if gameState[1] == '2':
                    sys.stdout.write('Invalid move, try again.\n')
                #are you winning son?
                if gameState[1] == '3':
                    sys.stdout.write('You Win!')
                    break
                if gameState[1] == '4':
                    sys.stdout.write('You Lose!')
                    break
                if gameState[1] == '5':
                    sys.stdout.write('Its a Tie!')
                    break

        sys.stdout.write("Would you like to play again? (Y/N)")
        #Take out used for debugging
        readin = sys.stdin.buffer.readline(1)
        cont = readin == "Y"


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
