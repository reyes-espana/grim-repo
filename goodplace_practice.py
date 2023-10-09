
''' 
    initialize a dictionary that holds the Good Place characters' names as a KEY and their favoirite color as the VALUE
    implement functions that allow the user to manipulate the dictionary
    accounts for user input validation and confirmation before implementation
 '''

 
import pyinputplus as pyip
import pandas as pd

# table to hold names and favorite colors of characters in the good place
favoriteColor = {
    "Eleanor": "Blue",
    "Chidi": "Green",
    "Tahani": "Yellow",
    "Jason": "Red",
    "Janet": "Purple"
}

# The following # NOTES are functions implemented in the main() method:
# SEARCH
def search(favoriteColor):
    key_list = list(favoriteColor.keys())
    val_list = list(favoriteColor.values())

    # Ask user if they want to enter a name or a color
    print("Would you like to search with a name or a color? ")
    userChoice = pyip.inputStr().capitalize().strip()
    if userChoice == 'Name':
        # input name to find color
        print("Enter a name to find their favorite color: ")
        userName = pyip.inputStr().strip()
        if userName in key_list:
            color = key_list.index(userName)
            print(userName+"'s favorite color is", val_list[color])
            print("Would you like to seach again?")
            decision = pyip.inputStr().capitalize().strip()
            if decision == 'Yes' or decision == 'Y':
                 search(favoriteColor)
            elif decision == 'No' or decision == 'N':
                 main()
            else:
                 main()
        else:
            print(userName, "is not in the list. Would you like to add it? ")
            decision = pyip.inputStr().capitalize().strip()
            yesorno(decision, favoriteColor)
           
    elif userChoice == 'Color':
        # input color to find name
        print("Enter a color to find who's favorite it is: ")
        userColor = pyip.inputStr().capitalize().strip()
        if userColor in val_list:
        # List all Keys with indicated search Value
            print("\nResults for: '"+ userColor +"'")
            search_results = list(filter(lambda k: favoriteColor[k] == userColor, favoriteColor))
            for key in search_results:
                print(key)
            print("\nWould you like to search again?")
            decision = pyip.inputStr().capitalize().strip()
            if decision == 'Yes' or decision == 'Y':
                search(favoriteColor)
            elif decision == 'No' or decision == 'N':
                main()
            else:
                main()
        else:
            print(userColor, "is no one's favorite color. Would you like to add someone to the list?")
            decision = pyip.inputStr().capitalize().strip()
            yesorno(decision, favoriteColor)

    else:
        print("Please enter 'Name' or 'Color'")
        search(favoriteColor)


# ADD
def add(favoriteColor):
    key_list = list(favoriteColor.keys())
    print("Enter the name of the person you'd like to add: ")
    addName = pyip.inputStr().strip()
    if addName == 'No' or addName == 'N':
        main()
    else:
        print("Is", addName, "the correct name?")
        decision = pyip.inputStr().capitalize().strip()
        if addName in key_list:
            print(addName, "is already registered. If you'd like to add someone by the same name, you must select a nickname and/or include an additinal identifier like a symbol or number.")
            add(favoriteColor)
        else:
            if decision == 'Yes' or decision == 'Y':
                print("What is", addName+"'s favorite color?")
                addColor = pyip.inputStr().capitalize().strip()
                favoriteColor[addName] = addColor
                print("Is", addColor, addName+"'s favorite color?")
                decision = pyip.inputStr().capitalize().strip()
                if decision == 'Yes' or decision == 'Y':
                    print(addName+"'s favorite color,", addColor+", has been added to the list. Would you like to add another name?")
                    decision = pyip.inputStr().capitalize().strip()
                    yesorno(decision, favoriteColor)
                elif decision == 'No' or decision == 'N':
                    del favoriteColor[addName]
                    add(favoriteColor)
                else:
                    add(favoriteColor)
            elif decision == 'No' or decision == 'N':
                add(favoriteColor) 
            else:
                main()


# UPDATE
def update(favoriteColor):
    key_list = list(favoriteColor.keys())

    print("Enter the name of the person whose information you would like to update: ")
    upName = pyip.inputStr().strip()
    if upName in key_list:
        print("What is ", upName+"'s favorite color?")
        upColor = pyip.inputStr().capitalize().strip()
        print("Is", upColor, upName+"'s favorite color?")
        decision = pyip.inputStr().capitalize().strip()
        if decision == 'Yes' or decision == 'Y':
            favoriteColor[upName] = upColor
            print(upName+"'s favorite color has been updated to ", upColor)
            main()
        elif decision == 'No' or decision == 'N':
                update(favoriteColor)
        else:
            update(favoriteColor)
    else:
        print(upName, " is not in the list. Would you like to add it?")
        decision = pyip.inputStr().capitalize().strip()
        yesorno(decision, favoriteColor)


# DELETE
def delete(favoriteColor):
    key_list = list(favoriteColor.keys())
    print("Enter the Name of the person's info you'd like to delete: ")
    itemDelete = pyip.inputStr().capitalize().strip()
    if itemDelete == 'No' or itemDelete == 'N':
         main()
    else:
        if itemDelete in key_list:
            print("Are you sure you want to delete", itemDelete+"'s info?")
            decision = pyip.inputStr().strip()
            # Make sure they want to delete the item
            if decision == 'Yes' or decision == 'Y':
                del favoriteColor[itemDelete]
            print(itemDelete+"'s information has been deleted. Would you like to delete another name?")
            decision = pyip.inputStr().capitalize().strip()
            if decision == 'Yes' or decision == 'Y':
                delete(favoriteColor)
            elif decision == 'No' or 'N':
                main()
            elif decision == 'No' or decision == 'N':
                delete(favoriteColor)
            else:
                delete(favoriteColor)
        else:
            print(itemDelete, "is not in the list, would you like to add them?")
            decision = pyip.inputStr().capitalize().strip()
            yesorno(decision)


# VIEW
def view(favoriteColor):   
    print("\n")    
    df = pd.DataFrame(list(favoriteColor.items()), columns=['Name', 'Color'])
    print(df)
     

# YES/NO
def yesorno(decision, favoriteColor):
    if decision == 'Yes' or decision == 'Y':
        add(favoriteColor)
    elif decision == 'No' or decision == 'N':
        main()
    else:
        print("Please enter 'Yes' or 'No'")
        add(favoriteColor)


# Main method:
# Ask user if they would like to SEARCH, ADD, UPDATE, or DELETE
def main():

# Function Control
        print("\nWould you like to View, Search, Add, Update, or Delete an item?")
        branchChoice = pyip.inputStr().capitalize().strip()
        if branchChoice == 'Search' or branchChoice == 'S':
            search(favoriteColor)
        elif branchChoice == 'Add' or branchChoice == 'A':
            add(favoriteColor)
        elif branchChoice == 'Update' or branchChoice == 'U':
            update(favoriteColor)
        elif branchChoice == 'Delete' or branchChoice == 'D':
            delete(favoriteColor)
        elif branchChoice == 'View' or branchChoice == 'V':
             view(favoriteColor)
             main()
        elif branchChoice == 'Exit' or branchChoice == 'X' or branchChoice == 'Q' or branchChoice == 'No' or branchChoice == 'N':
             exit()
        else:
            print("\nPlease enter 'View', 'Search', 'Add', 'Update', or 'Delete' to interact with the dictionary. \nEnter 'Exit' to quit.")
            main()

if __name__ == "__main__":
    main()