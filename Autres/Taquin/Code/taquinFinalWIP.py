#!/bin/python3
# native imports
import random
import os
import time
import tracemalloc
from collections import deque

# additionnal/optional imports

# try to import pip to try and install others external libraries if they're not installed already
pipInstalled=True # checks if pip is installed
try:
    import pip
except ImportError:
    pipInstalled=False

# try to import tkinter, if fail try to install it, if fail disables the graphical version
available=True # checks if the graphical version is available
try:
    from tkinter import *
except ImportError:
    print('''it appears that you don't have tkinter installed on your device
we will now try installing it''')
    try: 
        if (os.name == 'nt'):
            if(pipInstalled):
                pip.main(['install', '--user', "tk"])
        else:
            test = int(input("admin permissions required, proceed with installation of tkinter ? 0=no 1=yes: "))==1
            if test :
                os.system("sudo apt-get install python3-tk")
        from tkinter import *
    except:
        print('''installation has failed 
defaulting to terminal version 
if you want to experience the graphical version please install Tkinter''')
        available=False

# try to import pynput, if fail try to install it, if fail disables the terminal version with keyboard listners
onlyClassicTerm=False # checks if the classic version is the only the only terminal version available
try:
    from pynput.keyboard import Key, Listener
except ImportError:
    if pipInstalled:
        try:
            print('''it appears that you don't have pynput installed on your device
we will now try installing it''')
            pip.main(['install', '--user', "pynput"])
            from pynput.keyboard import Key, Listener
        except:
            if(available):
                print('''installation has failed 
since you have Tkinter installed you will have the choice between graphical mode or terminal(classic)''')
            else:
                print('''installation has failed 
defaulting to classic mode 
if you want to be able to play using our keyboard we recommend installing pynput with the command \'pip install pynput\'''')
            onlyClassicTerm=True

# try to import PIL (pillow), if fail try to install it, if fail disables images in the graphical version
images=True # checks if images are available
try:
    from PIL import Image, ImageTk
except ImportError:
    if pipInstalled:
        try:
            if (os.name == 'nt'):
                if(pipInstalled):
                    pip.main(['install', '--user', "Pillow"])
            else:
                test = int(input("admin permissions required, proceed with installation of pillow ? 0=no 1=yes: "))==1
                if test :
                    os.system("sudo apt-get install python3-pil python3-pil.imagetk")
            from PIL import Image, ImageTk
        except:
            print('''installation has failed 
if you want to be able to play with images in the graphical version we recommend installing pillow with the command \'pip install pillow\'''')
            images=False


# since in terminal mode we want to clear the terminal for a better readability we check what os are we running to use the appropriate clear command 
clear="clear"
if os.name == 'nt':
    clear="cls"

# definition of global variables
FONT=('Ubuntu', 27) # font used for the numbers in the tiles
won=False #is the current game complete
master=None # the window of graphical mode
cnv=None # the canvas upon which the elements of the graphical mode are drawn
solved=0 # the hashed of the solved game for easier tests
lTile=[] # lists of the tiles ids for the grafical version
lValues=[] # lists of the value of each tile (same order as lTiles) for finding which tiles to move when a move is applied on the board
board=[] # the game board
size=0 # the size of the board (for a board of dimension k*k size=k)
winbox=(0,0) # will store the id of the final tile and it's number once the game is finished so that they can be deleted when the game is reset
solution=[] # when an search algorithm is called it will store the path found in this variable
mode=0 # the mode in which the game will be executed
image=None
imageWon=None
imageTiles=[]
# this function will take a random picture of a supported format (png,ppm,jpg,bmp) from the ones stored in the "images" directory
def getImage():
    global images
    files=os.listdir("./images")
    imageList=[]
    for i in range(len(files)):
        if (files[i].endswith(".png") or files[i].endswith(".ppm") or files[i].endswith(".jpg") or files[i].endswith(".bmp")):
            imageList.append(files[i])
    if len(imageList)==0:
        print("there are no compatible images in the 'images' folder proceeding without images")
        images=False
        res = None
    else:
        j = random.randint(0,len(imageList)-1)
        res=Image.open("./images/"+imageList[j])
    return res

# this function initialize the board
def init(k=-1): 
    global solved,size
    temp=[]
    if k<3:
        size = int(input("taille de la grille (k*k) (k = 3 pour pouvoirt tester les IA efficacement) minimum 3: ")) # asking for the size of the board
        while size <3: # checking if size is valid
            size = int(input("taille de la grille (k*k) (k = 3 pour pouvoirt tester les IA efficacement) minimum 3: "))
    else:
        size=k
    for i in range(size*size):
        temp.append(i+1)
    temp[-1]=0
    solved=hash(temp) # setting the hash of the solution
    return temp # returning the board

# return the position of the empty space in the board
def freeSpace(board): 
    return board.index(0)

# movement functions: these functions move the empty space in the direction specified in their name and returns 0 if the move is successfull else 1
def moveUp(board, k):
    t =freeSpace(board)
    if(t-k>=0):
        board[t]=board[t-k]
        board[t-k]=0
        return 0
    return 1

def moveDown(board, k):
    t =freeSpace(board)
    if(t+k<k*k):
        board[t]=board[t+k]
        board[t+k]=0
        return 0
    return 1

def moveLeft(board, k):
    t =freeSpace(board)
    if(t%k-1>=0):
        board[t]=board[t-1]
        board[t-1]=0
        return 0
    return 1

def moveRight(board, k):
    t =freeSpace(board)
    if(t%k+1<k):
        board[t]=board[t+1]
        board[t+1]=0
        return 0
    return 1

# this function tells if a board is in a solved state for that we hash the current board and compare it to the hash of the soluton
def hasWon(board):
    return hash(board)==solved

# this functions couts the number of "real" inversion of a board this is used to test if a board is solvable
def countInversions(board):
    inversions = 0
    testBoard=[]
    for i in board:
        testBoard.append(i)
    testBoard.remove(0)
    n = len(testBoard)
    for i in range(n):
        for j in range(i + 1, n):
            if testBoard[i] > testBoard[j]:
                inversions += 1
    return inversions

# this function shuffles the board
def shuffle(board, k):
    global solution
    solution=[]
    t = k**2 # number of operation to do to shuffle the board
    len = k*k
    while t>0 or countInversions(board)% 2 != 0: # while there's still operations to do or the board isn't in a solvable state
        t-=1
        rand=random.randrange(len)
        rand2=random.randrange(len)
        tmp = board[rand]
        board[rand]=board[rand2]
        board[rand2]=tmp
    t=0
    while t!= 1: # we put the empty space at the bottom
        t=moveDown(board,k)
    t=0
    while t!= 1: # we put the empty space to the right
        t=moveRight(board,k)

#this function to displays the board on the terminal
def printBoardAscii(board,k):
    for i in range(k):
        for j in range(k):
            print("[",board[i*k+j],"\t]",end="")
        print()

# this function dictates what happens when the game is completed in the graphical version
def win(size):
    global winbox,imageWon
    x,y=100*(size-1), 100*(size-1)
    A, B, C=(x, y), (x+100, y+100), (x+50, y+50)
    if (images):
        imWidth,imHeight=image.size
        stepx=imWidth/size
        stepy=imHeight/size
        tileImage = image.crop((stepx*(size-1),stepy*(size-1),stepx*size,stepy*size)).resize((100,100))
        tileImageTk=ImageTk.PhotoImage(tileImage)
        imageWon=(tileImageTk,tileImage)
        imageItem=cnv.create_image(A, image=imageWon[0],anchor=NW)
        winbox=(cnv.create_rectangle(A, B,),cnv.create_text(C, text=str(size*size), fill="black", font=FONT),imageItem)
    else:
        winbox=(cnv.create_rectangle(A, B, fill="gray"),cnv.create_text(C, text=str(size*size), fill="black", font=FONT))

# a placeholder function that's used in case clicks event aren't treated properly to not cause a "value move has no value" error see line 264
def moveNull(board,k):
    return None

# a placeholder function that's used in case clicks event aren't treated properly to not cause a "value anim has no value" error see line 265
def animNull(n, empty, board, step): 
    return None

# this function and the three following allow for the smooth displacement of the tiles in the graphical version thanks to recursion with cnv.after() 
# n is the number of tiles to move , empty the index of the free space, board the game boardbefore any move (needed for the recursion as it happens in parallel to the rest of the program), step is the number of step in the animation and the max depth of the recursion, list is the list of tles to move for the recursion
def animUp(n, empty, board, step, list=[]):
    step-=1
    if(n!=0):
        toMove=[]
        for i in range(n):
            ind = lValues.index(board[empty-((i+1)*size)])
            toMove.append(lTile[ind])
    else:
        n=len(list)
        toMove=list.copy()
    for i in range(n):
        cnv.move(toMove[i][0],0,10)
        cnv.move(toMove[i][1],0,10)
        if(images):
            cnv.move(toMove[i][2],0,10)
    if(step!=0):
        cnv.after(5,animUp,0,empty,board,step,toMove)

def animDown(n, empty, board, step, list=[]):
    step-=1
    if(n!=0):
        toMove=[]
        for i in range(n):
            ind = lValues.index(board[empty+((i+1)*size)])
            toMove.append(lTile[ind])
    else:
        n=len(list)
        toMove=list.copy()
    for i in range(n):
        cnv.move(toMove[i][0],0,-10)
        cnv.move(toMove[i][1],0,-10)
        if(images):
            cnv.move(toMove[i][2],0,-10)
    if(step!=0):
        cnv.after(5,animDown,0,empty,board,step,toMove)

def animLeft(n, empty, board, step, list=[]):
    step-=1
    if(n!=0):
        toMove=[]
        for i in range(n):
            ind = lValues.index(board[empty-(i+1)])
            toMove.append(lTile[ind])
    else:
        n=len(list)
        toMove=list.copy()
    for i in range(n):
        cnv.move(toMove[i][0],10,0)
        cnv.move(toMove[i][1],10,0)
        if(images):
            cnv.move(toMove[i][2],10,0)
    if(step!=0):
        cnv.after(5,animLeft,0,empty,board,step,toMove)

def animRight(n, empty, board, step, list=[]):
    step-=1
    if(n!=0):
        toMove=[]
        for i in range(n):
            ind = lValues.index(board[empty+(i+1)])
            toMove.append(lTile[ind])
    else:
        n=len(list)
        toMove=list.copy()
    for i in range(n):
        cnv.move(toMove[i][0],-10,0)
        cnv.move(toMove[i][1],-10,0)
        if(images):
            cnv.move(toMove[i][2],-10,0)
    if(step!=0):
        cnv.after(5,animRight,0,empty,board,step,toMove)

# this function manage the click events
def click(event):
    global board,size,cnv,lTile,lValues,won
    if event.x<size*100 and event.y<size*100: # if the click event is within the boundary of the game
        if not won: # the game has finished and wasn't reset we ignore the click
            i=event.y//100
            j=event.x//100
            empty = freeSpace(board)
            ind = i*size+j
            if (ind != empty):
                move=moveNull
                anim=animNull
                x, y, =0, 0, 
                nb=0
                if (ind%size==empty%size) : # if click was in the same collumn as the free space
                    nb=abs(int((empty-ind)/size))
                    if(ind>empty):
                        y=-100
                        move=moveDown
                        anim=animDown
                    elif (ind<empty):
                        y=100
                        move=moveUp
                        anim=animUp
                elif (ind//size==empty//size): # if click was in the same ligne as the free space
                    nb=abs(empty-ind)
                    if(ind>empty):
                        x=-100
                        move=moveRight
                        anim=animRight
                    elif (ind<empty):
                        x=100
                        move=moveLeft
                        anim=animLeft
                anim(nb,empty,board,10)
                for i in range(nb):
                    move(board,size)
                if hasWon(board): # if the player finished the game: 
                    print("You win !")
                    win(size)
                    won = True

# this function reset the display to be coherent with the board after the initialization or a reset 
def drawgrid():
    global board,size,master,cnv,lTile,lValues,images,image,imageTiles
    lValues=[]
    imageTiles=[]
    for i in range(len(lTile)):
        cnv.delete(lTile[i][0])
        cnv.delete(lTile[i][1])
    lTile=[]
    if images:
        image = getImage()
        imWidth,imHeight=image.size
        stepx=imWidth/size
        stepy=imHeight/size
    for i in range(size):
        for j in range(size):
            if(board[i*size+j]!=0):
                x,y=100*j, 100*i
                A, B, C=(x, y), (x+100, y+100), (x+50, y+50)
                if(images):
                    textColor="black"
                    val=board[i*size+j]
                    tileI=(val-1)//size
                    tileJ=(val-1)%size
                    tileImage = image.crop((stepx*tileJ,stepy*tileI,stepx*(tileJ+1),stepy*(tileI+1))).resize((100,100))
                    tileImageTk=ImageTk.PhotoImage(tileImage)
                    imageTiles.append((tileImageTk,tileImage))
                    imageItem=cnv.create_image(A, image=imageTiles[size*i+j][0],anchor=NW)
                    cnv.tag_raise(imageItem)
                    lTile.append((cnv.create_rectangle(A, B),cnv.create_text(C, text=board[i*size+j], fill=textColor, font=FONT),imageItem))
                else:
                    lTile.append((cnv.create_rectangle(A, B, fill="gray"),cnv.create_text(C, text=board[i*size+j], fill="black", font=FONT)))
                lValues.append(board[i*size+j])
    cnv.create_rectangle((size*100,size*100),(size*100,0),fill="black")
    master.attributes('-topmost', 1) # this makes the graphical window pop up to the front of the screen after being initialized
    master.attributes('-topmost', 0)

# resets the game
def reset(graphic=True):
    global board,size,won,cnv
    shuffle(board, size) 
    if(graphic):
        drawgrid()
        cnv.delete(winbox[0])
        cnv.delete(winbox[1])
        if(images):
            cnv.delete(winbox[2])
            imageWon=None
        won=False

# returns the possible future states of a board along with the move required to attain said states
# it also take into consideration potential previous moves to avoid returning states previously analized
def getChildStates(board, k, prev):
    childStates = []
    tmp=board.copy()
    if prev!='D' and moveUp(tmp, k) == 0:
        childStates.append((tmp, "U"))
    tmp=board.copy()
    if prev!='U' and moveDown(tmp, k) == 0:
        childStates.append((tmp, "D"))
    tmp=board.copy()
    if prev!='R' and moveLeft(tmp, k) == 0:
        childStates.append((tmp, "L"))
    tmp=board.copy()
    if prev!='L' and moveRight(tmp, k) == 0:
        childStates.append((tmp, "R"))
    return childStates

# this functions execute a Breadth First Search on the current board to find a solution to the board
def BFS(benchmark = False):
    global board,size,solution
    tracemalloc.reset_peak()
    tracemalloc.start()
    temps=time.time() # this will be used to check how much time the BFS took to find the solution
    initial=board.copy() # we duplicate the game board to not influence the game during our search
    todo = deque([(tuple(initial), [])]) # creates a queue with deque for better performance
    visited = set() # this set will contain the states already visited for optimization
    while todo:
        current, path = todo.popleft()
        hashed=hash(current)
        if hashed in visited:
            continue
        visited.add(hashed)
        if hasWon(list(current)):
            if not benchmark:
                print("solution found in ",len(path),"steps")
                print("path to do: ",path)
                print("time elapsed BFS: ",time.time()-temps)
            solution = path
            res =(time.time()-temps,len(path),tracemalloc.get_traced_memory()[1])
            tracemalloc.stop()
            return  res
        prev = path[-1] if len(path) > 0 else "S"
        for childState, move in getChildStates(list(current),size,prev):
            todo.append((tuple(childState), path + [move]))

# this functions execute a Depth First Search on the current board to find a solution to the board
def DFS(benchmark = False):
    global board,size,solution
    tracemalloc.reset_peak()
    tracemalloc.start()
    temps=time.time() # this will be used to check how much time the BFS took to find the solution
    initial=board.copy() # we duplicate the game board to not influence the game during our search
    todo = deque([(tuple(initial), [])]) # creates a stack with deque for better performance
    visited = set() # this set will contain the states already visited for optimization
    path=[]
    found=False 
    while todo:
        current, path = todo.pop()
        if(len(path)>45):
            continue
        hashed=hash(current)
        if hashed in visited:
            continue
        visited.add(hashed)
        if hasWon(list(current)):
            if not benchmark:
                print("solution found in ",len(path),"steps")
                print("path to do: ",path)
                print("time elapsed DFS: ",time.time()-temps)
            solution = path
            found=True
            res =(time.time()-temps,len(path),tracemalloc.get_traced_memory()[1])
            tracemalloc.stop()
            return  res
        prev = path[-1] if len(path) > 0 else "S"
        for childState, move in getChildStates(list(current),size,prev):
            todo.append((tuple(childState), path + [move]))
    if(not found):
        if(not benchmark):
            print("DFS pas de solution trouvée")
        res=(0.2,50,tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
        return res

# this function returns the index of the state with the minimal cost value for the A* search
def findMinH(list):
    ind=-1
    min=0
    for i in range(len(list)):
        t=list[i][2]+len(list[i][1]) # the cost is calculated by adding the distance (number of moves) to the heuristic (manhattan distance) 
        if ind<0 or min > t:
            min=t
            ind=i
    return ind

# this function does a hash of the baord for a better optimization
def hash(board):
    res=0
    for i in range(len(board)):
        res+=(10**i)*board[i]
    return res

# this function implements a A* search algorithm
def aStar(benchmark = False):
    global board,size,solution
    tracemalloc.reset_peak()
    tracemalloc.start()
    temps=time.time() # this will be used to check how much time the BFS took to find the solution
    initial=board.copy() # we duplicate the game board to not influence the game during our search
    start=(initial,[],manhattanDist(initial,size)) # this is the first value we analyze it is commprised of the current board, list that contains the path to follow to attain this board from the current one (empty because it's the first step), and it's manhattan distance
    todo=[start]
    while todo:
        ind = findMinH(todo)
        current,path,h = todo.pop(ind)
        if(hasWon(current)):
            if not benchmark:
                print("solution found in ",len(path),"steps")
                print("path to do: ",path)
                print("time elapsed A*: ",time.time()-temps)
            solution = path
            res =(time.time()-temps,len(path),tracemalloc.get_traced_memory()[1])
            tracemalloc.stop()
            return  res
        prev = path[-1] if len(path) > 0 else "S"
        for childState,move in getChildStates(current,size,prev):
            todo.append((childState,path+[move],manhattanDist(childState,size)))

# this function calculates the manhattan distance of a given board
def manhattanDist(board,k):
    global solved
    dist=0
    for i in range(len(board)):
        if board[i] != 0:
            goalY, goalX = divmod(board[i] - 1, k)
            currY, currX = divmod(i, k)
            dist += abs(goalY - currY) + abs(goalX - currX)
    return dist

# this function is called when the user presses the "solve" button it will solve the game if the user as previously done a search
def solve():
    global board,solution,size
    empty=freeSpace(board)
    anim=animNull
    move=moveNull
    moveDir=solution.pop(0)
    if(moveDir=='U'):
        anim=animUp
        move=moveUp
    elif(moveDir=='D'):
        anim=animDown
        move=moveDown
    elif(moveDir=='L'):
        anim=animLeft
        move=moveLeft
    elif(moveDir=='R'):
        anim=animRight
        move=moveRight
    anim(1,empty,board,10)
    move(board,size)
    time.sleep(0.1)
    if(hasWon(board)):
        win(size)
        solution=[]
    elif(len(solution)>0):
        cnv.after(20,solve) # recursion to go through the whole solution path

# this function allows the graphical version to display the differen states of the board while it's getting solved
def solveTerminalButton():
    solveTerminal(board.copy())

# this is the setup of the graphical version
def graphical():
    global board,size,master,cnv,lTile,lValues,available
    # creating the window an canvas
    master=Tk()
    master.title("Taquin")
    master.resizable(False, False)
    master.geometry(str((size*100)+150)+"x"+str(size*100))
    cnv=Canvas(master, width=size*100+150, height=size*100,bg='grey70')
    # placing the buttons
    closeButton= Button(master,text ="exit",command=master.destroy)
    closeButton.place(x=size*100+10,y=size*100-40)
    resetButton= Button(master,text ="reset",command=reset)
    resetButton.place(x=size*100+10,y=20)
    BFSButton= Button(master,text="BFS",command=BFS)
    BFSButton.place(x=size*100+10,y=60)
    DFSButton= Button(master,text="DFS",command=DFS)
    DFSButton.place(x=size*100+10,y=100)
    aStarButton= Button(master,text="A*",command=aStar)
    aStarButton.place(x=size*100+10,y=140)
    solveButton= Button(master,text="solve",command=solve)
    solveButton.place(x=size*100+10,y=180)
    solveTermButton= Button(master,text="solve terminal",command=solveTerminalButton)
    solveTermButton.place(x=size*100+10,y=220)
    cnv.pack()
    cnv.bind("<Button-1>",click)
    # drawing the different tiles of the game
    drawgrid()
    # mainloop of the game
    master.mainloop()

# this function displays the help menu that will allow the terminal versions to do the different research algorithm
def help(keyboard):
    if(keyboard): # if the pynput version
        input() # clears the input buffer so that the nex one doesn't cause errors
    choice = int(input('''
which type of search do you want:
1- non informed (DFS)
2- non informed (BFS)
3- informed (A*)
: ''')) # choice of the search algorithm
    if choice == 1:
        DFS()
    elif choice == 2:
        BFS()
    elif choice == 3:
        aStar()

# this function is called after a search in the two terminal version of the game it display all the states of the board during the solution found
def solveTerminal(board):
    global size,solution
    for i in range(len(solution)):
        if(solution[i]=='U'):
            move=moveUp
        elif(solution[i]=='D'):
            move=moveDown
        elif(solution[i]=='L'):
            move=moveLeft
        elif(solution[i]=='R'):
            move=moveRight
        move(board,size)
        print("\n---------- etape ",i,", deplacement: ",solution[i]," ----------")
        printBoardAscii(board,size)
    print("the path to do was: ",solution)

# this function allows for the end of the game for the pynput terminal version
def onRelease(key):
    if key == Key.esc:
        return False

# this functions deal with the user inputs for the pynput terminal version
def onPress(key):
    err=False
    try:
        if key.char=='d':
            moveRight(board,size)
        elif key.char=='q':
            moveLeft(board,size)
        elif key.char=='z':
            moveUp(board,size)
        elif key.char=='s':
            moveDown(board,size)
        elif key.char=='h':
            help(True)
        elif key.char=='q':
            return False
        else:
            err=True
    except AttributeError:
        if key==Key.right:
            moveRight(board,size)
        elif key==Key.left:
            moveLeft(board,size)
        elif key==Key.up:
            moveUp(board,size)
        elif key==Key.down:
            moveDown(board,size)
        else:
            err=True
    os.system(clear)
    printBoardAscii(board,size)
    if len(solution)>0:
        solveTerminal(board)
        return False
    if(err):
        print("incorrect keystroke")
    if(hasWon(board)):
        print("you win!!!!!!")
        return False

# this is the main loop of the pynput terminal version
def advancedTerminal():
    printBoardAscii(board,size)
    with Listener(on_press=onPress, on_release=onRelease) as listener:
        listener.join()

# this is the mainloop of the "classic" terminal version (no external library)
def classicTerminal():
    global board,size,clear
    inputSet=['u','d','l','r','h','q']
    game=True
    while game:
        helped=False
        os.system(clear)
        printBoardAscii(board,size)
        move=input()
        move=move.lower()
        while not move in inputSet:
            print("invalid input allowed inputs  are : u d l r h")
            move= input()
            move=move.lower()
        if(move=='u'):
            moveUp(board,size)
        elif(move=='d'):
            moveDown(board,size)
        elif(move=='l'):
            moveLeft(board,size)
        elif(move=='r'):
            moveRight(board,size)
        elif(move=='h'):
            help(False)
            if len(solution)>0:
                helped=True
                solveTerminal(board)
        elif(move=='q'):
            game=False
        if(hasWon(board)):
            if not helped:
                os.system(clear)
                printBoardAscii(board,size)
            game = int(input("would you like to play again? 0=no 1=yes: "))==1
            if(game):
                shuffle(board,size)
    return None

def benchmark():
    global board
    lTime=[0,0,0]
    lLen=[0,0,0]
    lMemory=[0,0,0]
    board = init(3)
    for i in range(100):
        print("progression: ",i,"%")
        reset(False)
        statastar=aStar(True)
        statDFS=DFS(True)
        statBFS=BFS(True)
        lTime[0]+=statastar[0]
        lLen[0]+=statastar[1]
        lMemory[0]+=statastar[2]
        lTime[1]+=statDFS[0]
        lLen[1]+=statDFS[1]
        lMemory[1]+=statDFS[2]
        lTime[2]+=statBFS[0]
        lLen[2]+=statBFS[1]
        lMemory[2]+=statBFS[2]
    for i in range(3):
        lMemory[i]=lMemory[i]/100
        lLen[i]=lLen[i]/100
        lTime[i]=lTime[i]/100
    print("|data\t\t|A*  \t\t|DFS \t\t|BFS \t\t")
    print("|Temps\t|",lTime[0],"\t\t|",lTime[1]," \t\t|",lTime[2],"\t\t")
    print("|longueur\t|",lLen[0],"\t\t|",lLen[1],"\t\t|",lLen[2],"\t\t")
    print("|memoire\t|",lMemory[0],"\t\t|",lMemory[1],"\t\t|",lMemory[2],"\t\t")
'''
|data           |A*             |DFS            |BFS 
|Temps  | 3.9805738282203675            | 1.0029904375076304            | 3.941730303764343 
|longueur       | 22.34                 | 45.66                 | 22.34
|memoire        | 767324.36             | 6433051.52            | 20558353.12
'''

# pseudo main of the program lets the user choose which version of the game to play (depending on what's available) 
def main():
    global board,size,mode,available,onlyClassicTerm,images
    if available and not onlyClassicTerm:
        while mode <1 or mode >4:
            try:
                print('''enter which version do you want to play (please note that what you control is the position of the empty space):
1 - terminal controled with regular python inputs (u=up,d=down,l=left,r=right) h for search menu q to quit
2 - terminal controlled with keyboard (z,q,s,d and/or arrows)  press h then enter for ai menu
3 - graphical (mouse controlled use the buttons to naviguate)
4 - benchmark''')
                mode = int(input())
            except:
                print("incorrect input")
    elif not available and not onlyClassicTerm:
        while mode <1 or mode >2:
            try:
                print('''enter which version do you want to play (please note that what you control is the position of the empty space):
1 - terminal controled with regular python inputs (u=up,d=down,l=left,r=right) h for search menu q to quit
2 - terminal controlled with keyboard (z,q,s,d and/or arrows)  press h then enter for ai menu''')
                mode = int(input())
            except:
                print("incorrect input")
    elif available and onlyClassicTerm:
        while mode <1 or mode >2:
            try:
                print('''enter which version do you want to play (please note that what you control is the position of the empty space):
1 - terminal controled with regular python inputs (u=up,d=down,l=left,r=right) h for search menu q to quit
2 - graphical (mouse controlled use the buttons to naviguate)''')
                mode = int(input())
            except:
                print("incorrect input")
        if(mode==2):
            mode+=1
    else:
        mode=1
    if mode==4:
        benchmark()
    else:
        board=init()
    shuffle(board, size) 
    if mode==1:
        classicTerminal()
    elif mode ==2:
        advancedTerminal()
    elif mode==3:
        images=images and input("do you want to play with images (y/n): ").lower()=="y"
        graphical()

# we execute the main
main()