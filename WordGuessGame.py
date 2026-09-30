from english_words import get_english_words_set
import random
from colorama import Fore,Style,Back
EnglishWords=get_english_words_set(['web2'],lower=True)


selected=None
print(
    "--------------------------------------WELCOME TO THE WORD GAME---------------------------------------------------------------")
print(
    "-------------------------------THE RULES ARE SIMPLE,YOU HAVE TO GUESS A RANDOM WORD------------------------------------------")
print(
    "-----------GREEN COLORED LETTER MEANS RIGHT LETTER IN RIGHT POSITION,YELLOW MEANS RIGHT LETTER IN WRONG POSITION-------------")
print(
    "-----------------------RED COLORED LETTER MEANS THE LETTER DOESN'T EXIST IN THE WORD-----------------------------------------")
categories = {

    "SCIENCE": ["ATOMIC", "CHEMISTRY", "THERMODYNAMICS", "GLUCOSE", "CELLULAR", "ENERGY", "GRAVITY", "PHYSICS",
                "CHEMICAL", "MOLECULE", "NEURON", "PLANET", "VIRUS","SOLARSYSTEM","ELECTRICITY","THERMODYNAMICS"],
    "MOVIES": ["TITANIC", "GLADIATOR", "GRAVITY", "DIRECTOR", "MOONLIGHT", "SPIDERMAN", "INCEPTION", "INTERSTELLAR",
               "GODFATHER", "WALLE", "LIMELIGHT", "MERMAIDS", "GOODFELLAS", "MALEFICENT","PRESTIGE","AVENGERS","ANTMAN"],
    "GAMES": ["ASSASSINS", "MINECRAFT", "PLAYER", "CONSOLE", "PUZZLE", "WORDLE", "ROBLOX", "RUNNER", "TEKKEN", "TETRIS",
              "VALORANT", "SOLITAIRE", "POKEMON", "PALWORLD","DINOGAME","HORIZON","DOODLE" ],
    "COMPUTER": ["MOUSE", "CURSOR", "PROCESSOR", "SERVER", "KERNEL", "CODING", "SCREEN", "MEMORY", "BINARY", "INTERNET","PACKETS","BOOTING","PROGRAMMING","ETHERNET","TASKBAR","WALLPAPER"],
    "ENVIRONMENT": ["FOREST", "CLIMATE", "OCEAN", "RECYCLE", "HABITAT", "DROUGHT", "GLACIER", "COMPOST", "WETLAND",
                    "CARBON","BIODIVERSITY","REUSE","POLLUTION","GLOBALWARMING"],
    "ANIMALS": ["TIGER", "RABBIT", "EAGLE", "DOLPHIN", "PANDA", "SPIDER", "TURTLE", "MONKEY", "FALCON", "OTTER","SUGARGLIDER","ELEPHANT","GIRAFFE","ZEBRA","CHIMPANZEE","HIPPOPOTAMUS"],
    "FOOD/DRINK": ["PIZZA", "BURGER", "COFFEE", "NOODLE","MOMOS", "CANDY", "BACON", "SALAD", "MANGO", "COOKIE", "MOJITO","SAUCE"],
    "COLORS": ["GREEN", "PURPLE", "ORANGE", "YELLOW", "SILVER", "CRIMSON", "TEAL", "MAROON", "IVORY", "AMBER"],
    "COUNTRIES": ["AUSTRALIA","INDIA","CHINA","SWITZERLAND","FRANCE","ZAMBIA","BRAZIL","ARGENTINA","COLOMBIA","ANGOLA","GERMANY","GHANA","ESTONIA","IRELAND","THAILAND"],
    "SPORTS": ["CRICKET","SWIMMING","TENNIS","BASEBALL","FENCING","LONGJUMP","BASKETBALL","BADMINTON","RUNNING","HIGHJUMP","CYCLING","FOOTBALL","GYMNASTICS","HANDBALL","HOCKEY"]
}

def complete():#difficulty
    print("--------------CHOOSE DIFFICULTY--------------")
    print("1--------EASY------(word length; 4-5 letters)")
    print("2--------MEDIUM----(word length; 6-7 letters)")
    print("3--------HARD------(word length; 8-10 letters)")
    d = int(input("Enter the Number of your choice: "))
    if d == 1:
        min, max = 4, 5#for lengths
    elif d == 2:
        min, max = 6, 7
    elif d == 3:
        min, max = 8, 10
    else:
        print("Enter a valid choice ")
        return complete()

    w11 = random.choice([w for w in EnglishWords if w.isalpha() and min <= len(w) <= max])
    return w11.upper()
def choices():#ask which mode
    print("___________________________*CHOOSE YOUR GAME MODE*_____________________________________")
    print("1-COMPLETELY RANDOM")
    print("2-WORD FROM A PARTICULAR FIELD")

    N = (input("Enter the Number of your choice: "))
    print("----------*LET THE FUN BEGIN*------------")
    w=""
    if not N.isdigit():
        print("Enter a valid choice ")
        return choices()
    else:
        N=int(N)
        if N == 1:
           w=complete()
           return w
        elif N == 2:
            w=ChooseACategory()
            return w
        else:
            print("CHOOSE BETWEEN 1 OR 2 ONLY")
            return choices()
def ChooseACategory():#to get from dictionary
    global selected
    print("__________________*CHOOSE A CATEGORY*_____________________")
    atr= list(categories.keys())
    for i in range(len(atr)):
        print(i + 1, "-", atr[i])
    choice = (input("Enter the number of the category:"))
    if not choice.isdigit():
        print("Enter a valid number")
        return ChooseACategory()
    elif int(choice)>len(atr) or int(choice)<0:
        print("Enter a valid number ")
        return ChooseACategory()
    selected=""
    selected = atr[int(choice) - 1]
    wrd=random.choice(categories[selected])
    return wrd
def isValid(word,guess):#guess be in either dictionary or words written by me
    isInLibrary = guess.lower() in EnglishWords
    MyWords = selected is not None and guess in categories[selected]
    return MyWords or isInLibrary


def check(word, guess):
    if len(word) != len(guess):
        print("GUESSED WORD SHOULD BE OF THE SAME SIZE AS THE NUMBER OF BLANKS MENTIONED")
        return 1
    if not isValid(word,guess):
        print("GUESSED WORD SHOULD BE VALID")
        return 1
    return 0

def FindLetter(guess, word):#find the feedback
    green, yellow, red = 0, 0, 0
    l=len(word)
    review = ["_"] * l
    left = list(word)
    for i in range(0, len(word)):
        letter = guess[i]
        if letter == word[i]:
            review[i] = Back.GREEN + Fore.BLACK + letter + Style.RESET_ALL
            left.remove(letter)
            green += 1
    for i in range(len(word)):
        if review[i] == '_':
            if guess[i] in left:
                review[i] = Back.YELLOW + Fore.BLACK + guess[i] + Style.RESET_ALL
                yellow += 1
                left.remove(guess[i])
            else:
                review[i] = Back.RED + Fore.BLACK + guess[i] + Style.RESET_ALL
                red += 1
    if green==l:
        print("YOU GOT IT")
    elif green>l//2:
        print("KEEP GOING. VICTORY IS CLOSE ")
    elif green+yellow>l//2:
        print("GOOD TRY")
    else:
        print("NOT QUITE RIGHT")
    l="".join(review)
    return l
def giveHint(word,guesses):#hinting
    notguessed = []
    for i in range(len(word)):
        a = False
        for g in guesses:
            if g[i] == word[i]:
                a = True
                break
        if not a:
            notguessed.append(i)

    if not notguessed:
        return "You guessed all the letters"

    i = random.choice(notguessed)
    liv = ["_"] * len(word)
    liv[i] = word[i]
    return liv
def Backed(g):
    print("-----------PREVIOUS--GUESSES-----------")
    for x in g:
       print(x)

def main():
    word17=""
    word17=choices()
    aster=len(word17)
    hintsed=False
    win = "---------------YOU WIN---------------"
    loss = "--------------YOU LOSE--------------"
    chances = aster+1
    blank = ["_"] * aster
    print(" ".join(blank))
    print("word length=",aster)
    print("You have ",aster+1," chances to guess the word")
    allguesses = []
    ColorGuesses = []
    while chances > 0:
        guess = (input("Enter your guess: ")).upper()
        chances -= 1


        if check(word17,guess) == 1:
            chances += 1
            continue

        pal=" "
        pal=FindLetter(guess, word17)#get the colored guesses
        print(pal)
        ColorGuesses.append(pal)
        Backed(ColorGuesses)
        allguesses.append(guess)
        if word17 == guess:
            return win
        if chances ==0:
            break
        print("Lives Left: ",chances)
        if chances<3 and hintsed==False:
            ans = input("Do you want a hint?  (y/n): ")
            if ans == "y":
                hintsed = True
                hint = giveHint(word17, allguesses)
                print(" ".join(hint))
            else:
                hintsed = False

    print("The word was ",word17)
    return loss
def Againorno():
    N=input("Do you want to play again? (y/n): ").lower()
    if N=="y":
        return True
    elif N=="n":
        return False
    else:
        print("Please enter y or n ")
        return Againorno()
while True:
   print(main())
   if not Againorno():
       print("Thanks for playing!")
       break


