import sys 
import socket 
import array as arr
 
BUFFER_SIZE = 2048 

def main(): 
    """Parse command-line arguments and call client function """ 
    if len(sys.argv) != 2: 
        sys.exit("Usage: python3 client-python.py [Server IP] [Server Port] < [message]") 
    server_ip = sys.argv[1] 
    server_port = int(sys.argv[2]) 
    client(server_ip, server_port) 
 
if __name__ == "__main__": 
    main()
 
def client(server_ip, server_port): 
    """TODO: Open socket and send message from sys.stdin""" 
    # create an INET, STREAMing socket 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
        # now connect to server 
        s.connect((server_ip, server_port)) 
         
        while True:
            #initializing game by sending playername to server
            sys.stdout.write('Input playername to begin:\n')
            playerName = sys.stdin.buffer.read(BUFFER_SIZE)
            if not playerName: break 

            sent = s.sendall(playerName) 
            if sent == 0: 
                raise RuntimeError("socket connection broken") 

            #assuming server okayed playername and allowed game start
            serverInput = s.recv(BUFFER_SIZE)
            gameState = serverInput.split()
            if gameState[1] == '1':
                #initializing board
                initializeBoard()

            while True:
                #displaying board
                sys.stdout.write('{a[1]} | {a[2]} | {a[3]}\n')
                    + ('{a[4]} | {a[5]} | {a[6]}\n')
                    + ('{a[7]} | {a[8]} | {a[9]}\n')

                #sending turn to server
                sys.stdout.write('Take your turn(input location 1-9): ')
                location = sys.stdin
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


    pass

def initializeBoard():
    board = ['0', '0', '0', '0', '0', '0', '0', '0', '0']