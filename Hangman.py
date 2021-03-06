import random

#region properties
Movies = []
NumberOfTriesLeft = 10
MovieToGuess = ""
MovieToGuessHiddenLetters = []
LettersCorrectlyGuessed = []
MovieToGuessArray = []
MovieCorrectlyGuessed = False
NextAction = ""
userGuessed = ""
#end region

#Handle selecting random from list
def SelectRandomFromList(listToSelectFrom):
    selectedItem = random.choice(listToSelectFrom)
    return selectedItem

#Handles randomly selecting movie to guess and displaying blank to guess  
def CreateAndDisplayMovieToGuess():
    #Convert select movie to array.
    MovieToGuessArray = list(MovieToGuess)

    #Convert movie to guess in blank and show to user
    MovieToGuessHiddenLetters = MovieToGuessArray
    for n, i in enumerate(MovieToGuessHiddenLetters):
        if i != " ":
            MovieToGuessHiddenLetters[n] = '_'
        else:
            MovieToGuessHiddenLetters[n] = ' '
    print(*MovieToGuessHiddenLetters, sep=None)  

def PrintMovieToGuessHiddenLetters():
     for n, i in enumerate(MovieToGuessHiddenLetters):
        if i != " ":
            MovieToGuessHiddenLetters[n] = '_'
     print(*MovieToGuessHiddenLetters, sep=None)

#Handles if char typed exist in the movie title to guess
#also displays the correct letter guessed
def CheckIfLetterIsInMovieTitle(charInput):
    MovieToGuessArray = list(MovieToGuess)
    TempMovieToGuessHiddenLetters = []
    inputExist = False
    letterExist = "no"
    
    #Check if letter entered exist in the title of movie to guess 
    for n, i in enumerate(MovieToGuessArray):
        if i != " ":
            if i == charInput:
                #letter entered exist
                inputExist = True
    #Add entered letter to an array of correctly guessed letters            
    if inputExist == True:
        LettersCorrectlyGuessed.append(charInput)
    
    for x in MovieToGuessArray:
        for y in LettersCorrectlyGuessed:
            if y == x:
                letterExist = "yes"
            elif x == ' ':
                letterExist = "space"
        if letterExist == "yes":
            TempMovieToGuessHiddenLetters.append(x)
        elif letterExist == "no":
            TempMovieToGuessHiddenLetters.append('_')
        elif letterExist == "space":
            TempMovieToGuessHiddenLetters.append(' ')
        letterExist = "no"
    if inputExist == False:
        print ("INCORRECT!!! The letter you guessed does not exist in the title...")                     
    print("\n")
    print(*TempMovieToGuessHiddenLetters, sep=None)
    TempMovieToGuessHiddenLetters.clear()

    #Increment the global number of tries variable
    global NumberOfTriesLeft
    NumberOfTriesLeft -= 1 

#Handles checking if string typed is equal the movie title to guess
def CheckIfStringIsEqualToMovieTitle(stringInput):
    global NumberOfTriesLeft
    global MovieCorrectlyGuessed
    if stringInput.lower() == MovieToGuess.lower():
        MovieCorrectlyGuessed = True
        print("CORRECT!!!! The title is \"" + MovieToGuess + "\".\n")
    else:
        print("Wrong guess...")  
    NumberOfTriesLeft -= 5 

def ResetVariables():
    global MovieToGuess 
    global NumberOfTriesLeft
    global MovieCorrectlyGuessed
    global userGuessed
    global LettersCorrectlyGuessed
    LettersCorrectlyGuessed = []
    MovieToGuess = ""
    NumberOfTriesLeft = 10
    MovieCorrectlyGuessed = False
    userGuessed = ""

#Handles playing the game
def PlayGame():
    ResetVariables()
    global MovieToGuess 
    global NumberOfTriesLeft
    global MovieCorrectlyGuessed
    global userGuessed
    MovieToGuess = SelectRandomFromList(Movies)
    CreateAndDisplayMovieToGuess()  
    while NumberOfTriesLeft > 0 and MovieCorrectlyGuessed == False :
        print("Type a letter or the title to guess the movie: ")
        print("Number of guesses left (-5 for guessing the title & -1 for guessing a letter): " + str(NumberOfTriesLeft))
        userGuessed = input().lower()
        if userGuessed.isalpha() and len(userGuessed) == 1:
            CheckIfLetterIsInMovieTitle(userGuessed)
        elif len(userGuessed) > 1:
            CheckIfStringIsEqualToMovieTitle(userGuessed)
        else:
            print("\nInvalid input...\n")
            CreateAndDisplayMovieToGuess()

#Main Program
#Initialize movies to guess from
Movies.append("clash of the titans")
Movies.append("hot tub time machine")
Movies.append("back to the future")
Movies.append("how to train your dragon")
Movies.append("nightmare on elm street")
Movies.append("the king of staten island")
Movies.append("the assasination of jessie james")
Movies.append("starwars empire strikes back")
Movies.append("terminator judgement day")
Movies.append("the dark knight ")
Movies.append("saving private ryan")
Movies.append("the good the bad and the ugly")

PlayGame()
print("\nPress\np - play again\nx - enter\n")     
NextAction = input().lower()
while NextAction != "x":   
    PlayGame()
    print("\nPress\np - play again\nx - enter\n")     
    NextAction = input().lower()




