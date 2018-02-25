print("\t\tWelcome to coin flipper program.\n\t\t\tJust FLIP it!")

#The program  takes input as an integer from user
#and flips coin equal to this number of times.
#Then prints total sum of heads and tails separately.
#At the end asks user to restart program or not.

from random import randint as rint

again="yes"
#added 'while' to easily restart the game.
while again=="yes":
    flip=0
    coin=["head","tail"]
    headnum=0
    tailnum=0
    
    #----------------------------------------------------------------------
    #start of 'while' loop that will...   
    while True:
        #...prevent 'errors' caused by 'string input'...
        try:
            times= int(input("\nHow many times U wanna flip the coin?  "))
            #...and PC overload(asiri yukleme) caused by 'long integer(more than 6 characters)'.
            if len(str(times))>6:
                print(
                    """
              Upss, it's too much even for me.
    Can't handle numbers with more than 6(six) characters.
                    """
                    )
            else:
                break
        #in case of error following will be executed.
        except ValueError:
            print("Please, enter only numbers.")
    #----------------------------------------------------------------------

    for flip in range(times):
        flip += 1
        side = rint(0,1)
        if (side==0):
            headnum += 1
        elif (side==1):
            tailnum +=1
        #prints result of every flip.
        print ("Flip",flip,":",coin[side])

    #'for' loop ended, prints final results.
    print ("\n\n Total:\n\tHeads:",headnum,"\n\tTails:",tailnum)

    #Asks to restart program or not.
    #strip() ==> deletes 'spaces' at begin and end.
    #lower() ==> makes characters lowercase.
    again= input("\n\nDo U wanna repeat?  ").strip().lower()
    print ("----------------------------------------------------")
    #Program ends if answer different than 'yes'.
    #If input is 'yes' than 'again = "yes"' and 'while'(at very top) loop restarts.



