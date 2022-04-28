import sys 
import socket 
import random 

RECV_BUFFER_SIZE = 2048 
QUEUE_LENGTH = 10 
usernames = []
gameboards = []
playerSign = '1'
compSign = '2'

#removes current game from data set
def deleteInstance(username):
    placement = usernames.index(username)
    del usernames[placement]
    del gameboards[placement]
    return

#return 1 not yet a winner, 3 player winner, 4 computer winner, 5 tie
def winner(username):
    board = list(gameboards[usernames.index(username)])
    win = [playerSign,playerSign,playerSign]
    lose = [compSign,compSign,compSign]
    #player win horizontal, virtical, diag
    if board[0:2] == win or board[3:5] == win or board[6:8] == win:
        return 3
    if board[0:7:3] == win or board[1:8:3] == win or board[2:9:3] == win:
        return 3
    if board[0:9:4] == win or board[2:7:3] == win:
        return 3
    #computer wins 
    if board[0:2] == lose or board[3:5] == lose or board[6:8] == lose:
        return 4
    if board[0:7:3] == lose or board[1:8:3] == lose or board[2:9:3] == lose:
        return 4
    if board[0:9:4] == lose or board[2:7:3] == lose:
        return 4
    #moves left
    if 0 in board:
        return 1
        #draw
    return 5

    #return 0 if moves left, else return 1
def artificialIntelligence(username):
    board = list(gameboards[usernames.index(username)])
    #check if game is over
    if not 0 in board or winner(username) != 1:
        return 1
    #come up with move
    moves = board.count(0)
    move = random.randomrange(1,moves+1)
    indexMove = [i for i, n in enumerate(board) if n == 0][move-1]
    #make move
    board[indexMove] = compSign
    gameboards[usernames.index(username)] = "".join(board)
    return 0
    
def session(inputData):
    temp = inputData.split(" ")
    placement = 0
    if len(temp) == 1:
        if temp[0] in usernames:
            placement = usernames.index(temp[0])
            return gameboards[placement] + " 1"
        else:
            usernames.append(temp[0])
            gameboards.append("000000000")
            placement = usernames.index(temp[0])
            return gameboards[placement] + " 1"
    else: 
        if len(temp) == 2:
            temp1 = 0
            try:
                temp1 = int(temp[1])
            except:
                return "000000000 0"
            if temp[0] in usernames and temp1 in {1,2,3,4,5,6,7,8,9}:
                placement = usernames.index(temp[0])
                game = list(gameboards[placement])
                if game[int(temp[1])-1] != 0:
                    return "000000000 2"
                game[int(temp[1])-1] = playerSign
                gameboards[placement] = "".join(game)
                #add in ai
                if status == 1:
                # return board and game ending condition
                   return gameboards[placement] + " " + winner(temp[0])
                status = artificialIntelligence(temp[0])
                if status == 1:
                # return board and game ending condition
                   return gameboards[placement] + " " + winner(temp[0])
                return gameboards[placement] + " 1"
            else:
                return "000000000 0"
        else:
            return "000000000 0"

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
            sys.stdout.write("client!\n")
            with clientsocket: 
                while True: 
                    # receive data and print it out 
                    data = clientsocket.recv(RECV_BUFFER_SIZE)
                    if not data: break 
                    data = data.decode("utf-8", "surrogateescape")
                    sys.stdout.write(data + "\n")
                    output = session(data)
                    #if OP code is 345 call delete session method
                    if list(output)[10] in [3,4,5]:
                        deleteInstance(data.split()[0])
                    #send data back
                    clientsocket.send(output.encode("utf-8", "surrogateescape"))
                    #maybe call persistant data
            clientsocket.close()
    pass 

#possibly stores high scores between clients
def persistant():
    pass


def main(): 
    """Parse command-line argument and call server function """ 
    if len(sys.argv) != 2: 
        sys.exit("Usage: python server.py [Server Port]") 
    server_port = int(sys.argv[1]) 
    server(server_port) 

if __name__ == "__main__": 
    main() 
