import sys 
import socket 
 
RECV_BUFFER_SIZE = 2048 
QUEUE_LENGTH = 10 
usernames = []
gameboards = []
playerSign = '1'

def main(): 
    """Parse command-line argument and call server function """ 
    if len(sys.argv) != 2: 
        sys.exit("Usage: python server.py [Server Port]") 
    server_port = int(sys.argv[1]) 
    server(server_port) 

if __name__ == "__main__": 
    main() 

def server(server_port): 
    # TODO: get clinet inputs
    # create an INET, STREAMing socket 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serversocket: 
        # bind the socket to the host and its port 
        serversocket.bind(('', server_port)) 
        # prepare for connection 
        serversocket.listen(QUEUE_LENGTH) 
        while True: 
            # accept connections from outside 
            (clientsocket, address) = serversocket.accept() 
            with clientsocket: 
                while True: 
                    # receive data and print it out 
                    data = clientsocket.recv(RECV_BUFFER_SIZE) 
                    if not data: break 
                    session(data)
                    #if OP code is 345 call delete session method
                    #maybe call persistant data

                    #sys.stdout.buffer.write(data) 
                #sys.stdout.flush() 
    pass 


def session(inputData):
    temp = inputData.split()
    placement = 0
    if temp.len() == 1:
        if temp[0] in usernames:
            placement = usernames.index(temp[0])
            return gameboards[placement] + " 1"
        else:
            usernames.append(temp[0])
            gameboards.append("000000000")
            placement = usernames.index(temp[0])
            return gameboards[placement] + " 1"
    else: 
        if temp.len() == 2:
            if temp[0] in usernames:
                placement = usernames.index(temp[0])
                game = list(gameboards[placement])
                if game[int(temp[1])-1] != 0:
                    return "000000000 2"
                game[int(temp[1])-1] = playerSign
                gameboards[placement] = "".join(game)
                #add in ai
                return gameboards[placement] + " 1"
            else:
                return "000000000 0"
        else:
            return "000000000 0"

    pass



def artificialIntelligence():
    #check if game is over
    #come up with move
    #make move
    pass

def deleteInstance(username):
    pass





def persistant():
    pass



 


