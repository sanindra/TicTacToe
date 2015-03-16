def print_board(board):

	print "Present status of the board \n"

	for i in range(3):
		print " ",
		for j in range(3):
			if board[i*3+j] == 1:
				print 'X',
			elif board[i*3+j] == 0:
				print 'O',	
			elif board[i*3+j] != -1:
				print board[i*3+j]-1,
			else:
				print ' ',
			
			if j != 2:
				print " | ",
		print
		
		if i != 2:
			print "-----------------"
		else: 
			print 
def user_input(turn):

	moved = False

	while not moved:
		try:
			inp = raw_input("Please enter the location " + turn + "(1-9)?")
			inp = int(inp)
			if  inp>=1 and inp<=9:
				return inp-1
			else:
				print "Not a valid move"
		except Exception as e:
			print ("not a valid integer.")


def win_condition(board):
	condi = ((1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7))
	for i in condi:
		try:
			if board[i[0]-1] == board[i[1]-1] and board[i[1]-1] == board[i[2]-1]:
				return board[i[0]-1]
		except:
			pass
	return -1

def quits(msg):
	print msg
	quit()

def main():

            board = []
            for i in range(1,10):
                    board.append(-1)

            print_board([2,3,4,5,6,7,8,9,10])
            winner = False
            move = 0

            while not winner:
                if not move ==0:
                        print_board(board)
                
                if move % 2 ==0:
                    turn = 'X'
                else:
                    turn = 'O'

                inp = user_input(turn)
                #print inp
                while board[inp] != -1:
                    print "Cell not empty, try again \n"
                    inp = user_input(turn)
                if turn =='X':
                        board[inp] =1
                else:
                        board[inp] =0
                    
                move = move +1
                if move>4:
                        wins = win_condition(board)
                        #print wins
                        if wins != -1:
                                
                                if wins ==1:
                                        out = "X"
                                        
                                else:
                                        
                                        out = "O"
                                out += " wins"
                                quits(out)
                        elif move==9:
                                quits("Drawn Match")
                                


if __name__ == "__main__":
	main()
