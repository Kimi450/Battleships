import time

import random


#sticky forms for input, print it out, display none, display history of moves option

def war():
    #the game
    grid=int(input("Please enter the square grid's size:",))
    print("-----------------------------------------------------------------------------")
    print("Please enter a number between ",1,"and",grid**2,"for the number of ships!")
    ships=int(input("Please enter the number of ships per player:"))
    if ships>(grid**2):
        print("You dont deserve to play this game! I told you to enter a number between",1,"and",grid**grid,"!")
        return


    aiLstInitial=[0 for gridSlots in range((grid**2)-ships)]
    for shipPlacement in range(ships):
        aiLstInitial.append(1)
    random.shuffle(aiLstInitial)

    myLstInitial=[0 for gridSlots in range((grid**2)-ships)]
    for shipPlacement in range(ships):
        myLstInitial.append(1)
    random.shuffle(myLstInitial)

    counter=0
    myLst=[]
    aiLst=[]
    lst=[]

    print("-----------------------------------------------------------------------------")

    #prints out what your grid looks like-------------------------------------------------------------
    print ("My Grid")
    for pos in myLstInitial:
        counter+=1
        lst.append(pos)
        if counter==grid:
            myLst.append(lst)
            print(" ".join(str(num) for num in lst))
            counter=0
            lst=[]
    
    #print()
    #stuff about ai list with positions
    #print("AI Grid")
    
    #prints out what the ai's grid looks like      
    for pos in aiLstInitial:
        counter+=1
        lst.append(pos)
        if counter==grid:
            aiLst.append(lst)
            #print(" ".join(str(num) for num in lst))
            counter=0
            lst=[]


    #hit lists----------------------------------------------------------------------------------------

    aiLstInitialBlank=["_" for gridSlots in range((grid**2))]
    myLstInitialBlank=["_" for gridSlots in range((grid**2))]
    #print("AI Grid")
    myLstBlank=[]
    aiLstBlank=[]
    for pos in aiLstInitialBlank:
        counter+=1
        lst.append(pos)
        if counter==grid:
            aiLstBlank.append(lst)
            #print(" ".join(str(num) for num in lst))
            counter=0
            lst=[]

    #print ("My Grid")
    for pos in myLstInitialBlank:
        counter+=1
        lst.append(pos)
        if counter==grid:
            myLstBlank.append(lst)
            #print(" ".join(str(num) for num in lst))
            counter=0
            lst=[]
 
    print("-----------------------------------------------------------------------------")

    aiBeingHit=0
    meBeingHit=0
    print("Please enter a value between 1 and ",grid,"for both parameters.")
    print("-----------------------------------------------------------------------------")
    while True:
        shouldRestart=True
        #me-----------------------------------------------------------------------------------------
        while shouldRestart:
            shouldRestart=False
            hitRowMe=int(input("Please enter the row number you wish to attack on:",))-1
            hitColMe=int(input("Please enter the column number you wish to attack on:",))-1
            print()
            if hitRowMe>=grid or hitColMe>=grid:
                print("***Invalid input!***")
                shouldRestart=True
                break
            if aiLst[hitRowMe][hitColMe]==1:
                print("You have hit the AI!")
                aiLst[hitRowMe][hitColMe]="_"
                aiLstBlank[hitRowMe][hitColMe]="H"
                aiBeingHit+=1
            elif aiLst[hitRowMe][hitColMe]=="_":
                print("A hit has already been made here by you!")
            elif aiLst[hitRowMe][hitColMe]==" ":
                print("A miss has already been made here by you!")
            else:
                print("You have missed the AI!")
                aiLst[hitRowMe][hitColMe]=" "
                aiLstBlank[hitRowMe][hitColMe]="M"
            if ships==aiBeingHit:
                print()
                print("-----------------------------------------------------------------------------")
                print("***You win!")
                for pos in aiLstInitial:
                    counter+=1
                    lst.append(pos)
                    if counter==grid:
                        aiLst.append(lst)
                        print(" ".join(str(num) for num in lst))
                        counter=0
                        lst=[]
                print("-----------------------------------------------------------------------------")
                return

            #"ai"-----------------------------------------------------------------------------------
            #may not be working
            hitRowAi=random.randint(1,grid)-1
            hitColAi=random.randint(1,grid)-1
            if myLst[hitRowAi][hitColAi]==1:
                print("The computer has hit you!")
                myLst[hitRowAi][hitColAi]="_"
                myLstBlank[hitRowMe][hitColAi]="H"
                meBeingHit+=1
            elif myLst[hitRowAi][hitColAi]=="_":
                print("The computer has already hit you here!")
            elif myLst[hitRowAi][hitColAi]==" ":
                print("The computer has already missed you here!")
            else:
                print("The computer has missed you!")
                myLst[hitRowAi][hitColAi]=" "
                myLstBlank[hitRowMe][hitColAi]="M"
            if ships==meBeingHit:
                print()
                print("-----------------------------------------------------------------------------")
                print("***The computer wins!")
                for pos in myLstInitial:
                    counter+=1
                    lst.append(pos)
                    if counter==grid:
                        aiLst.append(lst)
                        print(" ".join(str(num) for num in lst))
                        counter=0
                        lst=[]
                print("-----------------------------------------------------------------------------")
                return
            print()
            print("Your shots")
            for row in range(grid):
                for item in aiLstBlank[row]:
                    print(item, end=" ")
                print()
            print()
            print("Computer's shots")
            for row in range(grid):
                for item in myLstBlank[row]:
                    print (item, end=" ")
                print()
            print()
            print("-----------------------------------------------------------------------------")
        print()
            
war()
