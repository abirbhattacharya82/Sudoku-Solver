def find_space(board):
    for i in range(0,9):
        for j in range(0,9):
            if board[i][j]==0:
                return (i,j)
    return None
def check(board,num,r,c):
    for i in range(0,9):
        if board[r][i]==num and c!=i:
            return False
    for i in range(0,9):
        if board[i][c]==num and r!=i:
            return False
    x=r//3
    y=c//3
    for i in range(x*3,x*3+3):
        for j in range(y*3,y*3+3):
            if board[i][j]==num and r!=i and c!=j:
                return False
    return True
def enter_datas(board):
    for i in range(1,10):
        print("Enter the Datas in Row ",i)
        x=[int(i) for i in input().split()]
        board.append(x)
def show(board):
    for i in range(0,9):
        for j in range(0,9):
            if j==2 or j==5:
                print(board[i][j]," | ",end="")
            else:
                print(board[i][j],end=" ")
        if i==2 or i==5:
            print("\n-----------------------\n")
        else:
            print("\n")
def solve(board):
    x=find_space(board)
    if not x:
        return True
    else:
        r,c=x
    for i in range(1,10):
        if check(board,i,r,c):
            board[r][c]=i
            if solve(board):
                return True
            board[r][c]=0
    return False
board=[]
enter_datas(board)
show(board)
solve(board)
print("\n\n")
show(board)





'''
Enter the Datas in a Row
7 8 0 4 0 0 1 2 0
Enter the Datas in a Row
6 0 0 0 7 5 0 0 9
Enter the Datas in a Row
0 0 0 6 0 1 0 7 8
Enter the Datas in a Row
0 0 7 0 4 0 2 6 0
Enter the Datas in a Row
0 0 1 0 5 0 9 3 0
Enter the Datas in a Row
9 0 4 0 6 0 0 0 5
Enter the Datas in a Row
0 7 0 3 0 0 0 1 2
Enter the Datas in a Row
1 2 0 0 0 7 4 0 0
Enter the Datas in a Row
0 4 9 2 0 6 0 0 7
'''