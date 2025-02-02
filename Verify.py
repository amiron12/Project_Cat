
def options(numOfOptions:int, choice):
    if choice>numOfOptions or choice<=0:
        return False
    else:
        return True

def errorPrint():
    print()
    print("--Not a valid option--\n"
          "Try again")
    print()

def nameVer():
    print("Enter your name:")
    try:
        name = str(input())
    except:
        errorPrint()
        return nameVer()
    else:
        if name == "":
            errorPrint()
            return nameVer()
        else:
            return name

def choiceVer(num)->int:
    try:
        choice = int(input())
    except:
        errorPrint()
        return choiceVer(num)

    finally:
        if options(num, choice):
            return choice
        else:
            errorPrint()
            return choiceVer(num)

