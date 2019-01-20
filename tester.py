#01-19-2019
#Program to test string class using user input
# declaring  program function declaration
# program requirements provided by professor on prompt
def sortbyincreasinglength(wordbank):
    print("Option 0")
    temp tempstring = " "
    # len(list)
    # max(list)
    # min(list)
    # cmp(list1, list2)
    # append(obj)
    # remove(obj)
    # count(obj)
    # insert(index, obj)


def sortbydecreasinglength(wordbank):
     print("Option 1")
def sortbythemostvowels(wordbank):
     print("Option 2")
def sortbytheleastvowels(wordbank):
    print("Option 3")
def capitalizeeveryothercharacter(wordbank):
    print("Option 4")
def reversewordordering(wordbank):
    print("Option 5")
def foldwordsonmiddleoflist(wordbank):
    print("Option 6")


def main():
    bankofwords = []
    morewords = "Y"
    print("\t\t*********Text Container Program************ " )
# // Loop: while the user wants to continue processing more lists of words
    while (morewords == "Y"):
            word = input ("Enter a word in the list: ")
            bankofwords.append(word)
            if( input ( "\t\t*********Press N to Stop Entering Words Or Y To Enter Add a word*************") == "N"):
                  morewords = "N"
            # ending if condition statement
    # ending while statement
    i = 0
    print("\t\t************Words In The Set Are The Following**************")
    for i in range( (len(bankofwords)) ):
            print (bankofwords[i])
    # ending for loop statement
#     // Loop: while the user want to enter more words (minimum of 8)
    exit = 0
    while (exit == 0):
        print("\t\t***********Choose An Option************")
        print("0- Sort By In creasing Length ")
        print("1- Sort By Decreasing Length ")
        print("2- Sort By The Most Vowels ")
        print("3- Sort By The Least Vowels ")
        print("4-Capitalize Every Other Character ")
        print("5- Reverse Word Ordering ")
        print("6-Fold Words On Middle Of List ")
        option = int(input())
        print(option)
        if option == 0:
            sortbyincreasinglength(bankofwords)
        elif option ==1:
            sortbydecreasinglength(bankofwords)
        elif option ==2:
            sortbythemostvowels(bankofwords)
        elif option ==3:
            sortbytheleastvowels(bankofwords)
        elif option ==4:
            capitalizeeveryothercharacter(bankofwords)
        elif option ==5:
            reversewordordering(bankofwords)
        elif option ==6:
            foldwordsonmiddleoflist(bankofwords)
        # ending if else condition statement


main()


