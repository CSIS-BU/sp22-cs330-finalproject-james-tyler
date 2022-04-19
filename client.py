import sys 
import socket 
import array as arr
 
BUFFER_SIZE = 2048 
 
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

            #assuming server okayed playername and allowed game start

            #initializing board
            a = arr.array('i', [0, 0, 0, 0, 0, 0, 0, 0, 0])

            while True:
                #displaying board
                sys.stdout.write('{a[1]} | {a[2]} | {a[3]}\n')
                     << ('{a[4]} | {a[5]} | {a[6]}\n')
                     << ('{a[7]} | {a[8]} | {a[9]}\n')
                sys.stdout.write('Take your turn(input location 1-9): ')
                location = sys.stdin
                turn = playerName + ' ' + location
                turn = sys.stdin.buffer.read(BUFFER_SIZE)


                

            if not playerName: break 
            sent = s.sendall(playerName) 
            if sent == 0: 
                raise RuntimeError("socket connection broken") 
    pass 
 
 
def main(): 
    """Parse command-line arguments and call client function """ 
    if len(sys.argv) != 3: 
        sys.exit("Usage: python3 client-python.py [Server IP] [Server Port] < [message]") 
    server_ip = sys.argv[1] 
    server_port = int(sys.argv[2]) 
    client(server_ip, server_port) 
 
if __name__ == "__main__": 
    main()