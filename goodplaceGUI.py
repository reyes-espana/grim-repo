''' 
    initialize a dictionary that holds the Good Place characters' names as a KEY and their favoirite color as the VALUE
    implement functions that allow the user to manipulate the dictionary
    accounts for user input validation and confirmation before implementation
 '''

 
import pyinputplus as pyip
import pandas as pd
import PySimpleGUI as sg

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
    df = pd.DataFrame(list(favoriteColor.items()), columns=['Name', 'Color'])

    sg.theme("DarkGrey11")
    s_title = sg.Text("Search Entry", font=("Verdana", 23), expand_x=True, justification='center')
    s_cancel = sg.Button("Cancel", font=("Verdana", 9), pad=(5,8))
    s_search = sg.Button("Search", font=("Verdana", 9), pad=(5,8))
    s_branchName = sg.Radio("Name", "RADIO", key='name', enable_events=True, default=True, font=("Verdana", 10))
    s_branchColor = sg.Radio("Color", "RADIO", key='color', enable_events=True, font=("Verdana", 9))
    s_branch = [s_branchName, s_branchColor]
    s_branchFrame = sg.Frame("Search by", [s_branch], title_color='white', font=("Verdana", 16), expand_x=True, pad=(5,0), key="radio")
    name_prompt = sg.Text("Enter a Name:", font=("Verdana", 9))
    name_in = sg.Input("", key='NAME')
    name_branch = [name_prompt, name_in]
    name_frame = sg.Frame("Name",[name_branch], title_color='white', font=("Verdana", 14), expand_x=True, pad=(5,6), key="NME")
    color_prompt = sg.Text("Enter a Color:", font=("Verdana", 9))
    color_in = sg.Input("", key='COLOR')
    color_branch = [color_prompt, color_in]
    color_frame = sg.Frame("Color", [color_branch], title_color='white', font=("Verdana", 14), expand_x=True, pad=(5,6), visible=False, key='CLR')

    layout = [[s_title],
              [s_branchFrame],
              [name_frame, color_frame],
              [s_search, s_cancel]
              ]

    window = sg.Window("Search", layout, size=(345, 350), enable_close_attempted_event=True, finalize=True)

    while True:
        event, values = window.read()

        # SEARCH by NAME
        if values['name'] == True:
            name_frame.update(visible=True)
            color_frame.update(visible=False)
            if event == "Search":
                search_name = values ["NAME"].capitalize().strip()

                if search_name not in key_list:
                    if sg.popup_yes_no(search_name + " does not exist. Would you like to create a new entry for "+ search_name + "?", font=('Verdana', 10)) == 'Yes':
                        window.close()
                        add(favoriteColor)
                else:
                    window.close()

                    result_title = sg.Text("Results for '" + search_name + "':")
                    # Display results that match search_name (should only be one)
                    back_button = sg.Button("Cancel")

                    layout = [[result_title],
                        [back_button]
                        ]

                    window = sg.Window("Name", layout, size=(345, 350), enable_close_attempted_event=True)

                    while True:
                        event, values = window.read()
                        if event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT and sg.popup_yes_no("Do you really want to exit?", font=('Verdana', 10)) == 'Yes':
                            break
                        if event == "Cancel":
                            break
                    break

        # SEARCH by COLOR
        if values['color'] == True:
            name_frame.update(visible=False)
            color_frame.update(visible=True)
            if event == "Search":
                search_color = values["COLOR"].capitalize().strip()
                if search_color not in val_list:
                    if sg.popup_yes_no(search_color + " is no one's favorite color. Would you like to add a new entry?", font=('Verdana', 10)) == 'Yes':
                        window.close()
                        add(favoriteColor)
                else:
                    window.close()

                    result_title = sg.Text("Results for '" + search_color + "':")
                    back_button = sg.Button("Cancel")

                    layout = [[result_title],
                        [back_button]
                        ]

                    window = sg.Window("Color", layout, size=(800, 350), enable_close_attempted_event=True)

                    while True:
                        event, values = window.read()
                        
                        if event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT and sg.popup_yes_no("Do you really want to exit?", font=('Verdana', 10)) == 'Yes':
                            break

                        if event == "Cancel":
                            break

                    break
        

        if event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT and sg.popup_yes_no("Do you really want to exit?", font=('Verdana', 10)) == "Yes":
            break

        if event == "Cancel":
            break

    window.close()
    main()
        
'''
        # SEARCH by NAME
        print("Enter a name to find their favorite color: ")
        userName = pyip.inputStr().capitalize().strip()
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

            
    # SEARCH by COLOR
    elif userChoice == 'Color':

        if userColor in val_list:
            name = val_list.index(userColor)
            print(userColor, " is ", key_list[name]+"'s favorite color.")
            print("Would you like to search again?")
            decision = pyip.inputStr().capitalize().strip()
            if decision == 'Yes' or decision == 'Y':
                 search(favoriteColor)
            elif decision == 'No' or decision == 'N':
                 main()
            else:
                 main()
'''

# ADD
def add(favoriteColor):
    key_list = list(favoriteColor.keys())

    sg.theme("DarkGrey11")
    add_title = sg.Text("New Entry", font=("Verdana", 22), expand_x=True, justification='center')
    add_nprompt = sg.Text("Enter a Name: ", font=("Verdana", 9))
    add_name = sg.Input(key="name")
    add_cprompt = sg.Text("Enter a Color: ", font=("Verdana", 9))
    add_color = sg.Input(key="color")
    back_button = sg.Button("Cancel", font=("Verdana", 9), pad=(5,8))
    submit_button = sg.Button("Submit", font=("Verdana", 9), pad=(5,8))

    layout = [
        [add_title],
        [add_nprompt],
        [add_name],
        [add_cprompt],
        [add_color],
        [submit_button, back_button]
    ]

    window = sg.Window("Add", layout, size=(325, 310), enable_close_attempted_event=True)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT and sg.popup_yes_no("Do you really want to exit?", font=('Verdana', 10)) == "Yes":
            break

        if event == "Cancel":
            break

        if event == "Submit":
            nameAdd = values["name"].capitalize().strip()
            colorAdd = values["color"].capitalize().strip()
            if nameAdd not in key_list:
                if sg.popup_yes_no("Is "+ nameAdd+ "'s favorite color "+ colorAdd+"?", font=('Verdana', 10)) == "Yes":
                    favoriteColor[nameAdd] = colorAdd
                    if sg.popup_yes_no(nameAdd+ " has been added.","Would you like to add another entry?", font=('Verdana', 10)) == "Yes":
                        window.close()
                        add(favoriteColor)
                    else:
                        break
            else: 
                if sg.popup_yes_no(nameAdd+" is already registered.", "Would you like to update an existing entry?", font=('Verdana', 10)) == "Yes":
                    window.close()
                    update(favoriteColor)
                else:
                    window.close()
                    add(favoriteColor)

    window.close()
    main()


# UPDATE
def update(favoriteColor):
    key_list = list(favoriteColor.keys())
    
    sg.theme("DarkGrey11")
    up_title = sg.Text("Update Entry", font=("Verdana", 22), expand_x=True, justification='center', pad=(0,6))
    up_prompt = sg.Text("Enter a name to update their information: ", font=("Verdana", 9), )
    up_name = sg.Input(key="UPname")
    back_button = sg.Button("Cancel", pad=(5,8))
    up_button = sg.Button("Update", pad=(5,8))

    layout = [
        [up_title],
        [up_prompt], 
        [up_name],
        [up_button, back_button]
    ]

    window = sg.Window("Update", layout, size=(325, 310), enable_close_attempted_event=True)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT and sg.popup_yes_no('Do you really want to exit?', font=('Verdana', 10)) == 'Yes':
            break
 
        if event == "Cancel":
            break

        if event == "Update":
            nameUP = values["UPname"].capitalize().strip()

            if nameUP in key_list and sg.popup_yes_no(nameUP+"'s favorite color is "+ favoriteColor[nameUP]+", would you like to update it?", font=('Verdana', 10)) == "Yes":
                window.close()

                layout = [
                    [sg.Text("What is "+ nameUP+"'s new favorite color? ", font=("Verdana", 10))],
                    [sg.Input(key="color", pad=(5,6))],
                    [sg.Button("Submit", pad=(4,8)), sg.Button("Cancel", pad=(4,8))]
                ]

                window = sg.Window("Color", layout, size=(325, 150), enable_close_attempted_event=True)

                while True:
                    event, values = window.read()
                    if event == "Cancel":
                        window.close()
                        update(favoriteColor)
                        break 

                    if event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT and sg.popup_yes_no('Do you really want to exit?', font=('Verdana', 10)) == 'Yes':
                        window.close()
                        update(favoriteColor)
                        break

                    if event == "Submit":
                        colorUP = values["color"].capitalize().strip()
                        if sg.popup_yes_no("Is "+colorUP+" correct?", font=('Verdana', 10)) == "Yes":
                            favoriteColor[nameUP] = colorUP
                            if sg.popup_yes_no(nameUP+"'s favorite color has been updated to "+colorUP+".", "Would you like to update another entry?", font=('Verdana', 10)) == "Yes":
                                window.close()
                                update(favoriteColor)
                            else:
                                window.close()
                                main()
        else:
            break

    window.close()
    main()


# DELETE
def delete(favoriteColor):
    key_list = list(favoriteColor.keys())
    
    sg.theme("DarkGrey11")
    del_title = sg.Text("Delete Entry", font=('Verdana', 22), expand_x=True, justification='center', pad=(10,5))
    delete_prompt = sg.Text("Enter a Name to delete the entry:", font=("Verdana",9))
    itemDelete = sg.Input(key="-DELETE_NAME-", pad=(7,4), expand_x=True, justification='left')
    cancel_button = sg.Button("Cancel", pad=(7,10))
    delete_button = sg.Button("Delete", pad=(7,10))

    layout = [
        [del_title],
        [delete_prompt],
        [itemDelete],
        [delete_button, cancel_button]
    ]

    window = sg.Window("Delete", layout, size=(325, 310), enable_close_attempted_event=True, auto_size_text=True,
                       auto_size_buttons=True)

    while True:
        event, values = window.read()

        if event == "Cancel":
            break
        
        if event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT and sg.popup_yes_no('Do you really want to exit?') == 'Yes':
            break
        
        if event == "Delete":
            itemDelete = values["-DELETE_NAME-"].capitalize().strip()
            
            if itemDelete in key_list and sg.popup_yes_no("Are you sure you want to delete", itemDelete+"'s info?", font=('Verdana', 10)) == 'Yes':
                del favoriteColor[itemDelete]
                if sg.popup_yes_no(itemDelete+" has been deleted.", "Would you like to delete another entry?") == "No":
                    window.close()
                    main()
                else:
                    window.close()
                    delete(favoriteColor)
            elif itemDelete not in key_list and sg.popup_yes_no(itemDelete, "is not listed, would you like to add a new entry?", font=('Verdana', 10)) == "Yes":
                window.close()
                add(favoriteColor)
            else: 
                break
    
    window.close()
    main()

            
# VIEW
def view(favoriteColor): 
    key_list = list(favoriteColor.keys())
    val_list = list(favoriteColor.values())  
    entries = [[key, value] for key, value in zip(key_list, val_list)]

    sg.theme("DarkGrey11")
    title = sg.Text("All Entries", font=("Verdana", 22), expand_x=True, justification='center', pad=(0,10))
    back_button = sg.Button("Back", pad=(50, 15))
    preview = sg.Table(values=entries, headings=["Name", "Color"], auto_size_columns=True, alternating_row_color="grey", 
                       display_row_numbers=False, justification='center', key='-TABLE-', expand_x=True, expand_y=True,
                       pad=(50,5))

    layout = [
        [title],
        [preview],
        [back_button]
    ]

    window = sg.Window("View", layout, size=(828, 380), enable_close_attempted_event=True)

    while True:
        event, value = window.read()
        if event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT and sg.popup_yes_no('Do you really want to exit?', font=('Verdana', 10)) == 'Yes':
            break

        if event == "Back":
            break

    window.close()
    main()


# Main method:
# Ask user if they would like to SEARCH, ADD, UPDATE, or DELETE
def main():
        
# Window elements
        sg.theme('DarkGrey11')
        title = sg.Text('Favorite Color', font=('Verdana', 22), expand_x=True, justification='center', pad=(0,12))
        preview = sg.Multiline((pd.DataFrame(list(favoriteColor.items()), columns=['Name', 'Color'])), size=(20,10), font=('Verdana', 11), expand_y=True, expand_x=True, justification='center')
        main_handler = sg.Text('Would you like to View, Search, Add, Update, or Delete an item?', font=('Verdana', 11), expand_x=True, expand_y=True)
        v = sg.Button("View", font=('Verdana', 9))
        s = sg.Button("Search", font=('Verdana', 9))
        a = sg.Button("Add", font=('Verdana', 9))
        u = sg.Button("Update", font=('Verdana', 9))
        d = sg.Button("Delete", font=('Verdana', 9))
        x = sg.Button("Exit", font=('Verdana', 9))

    # Organize Window Elements
        preview = [[preview]]
        control = [[main_handler],
                [v, sg.Text("'View' all current entries.", font=('Verdana', 10))],
                [s, sg.Text("'Search' for a specific entry.", font=('Verdana', 10))],
                [a, sg.Text("'Add' a new entry.", font=('Verdana', 10))],
                [u, sg.Text("'Update' an existing entry.", font=('Verdana', 10))],
                [d, sg.Text("'Delete' an entry.", font=('Verdana', 10))],
                [x]]

        layout = [
            [title],
            [sg.Column(preview, vertical_scroll_only=True, pad=(28,5)), sg.Column(control, pad=(0,0))]
        ]

        window = sg.Window('Favorite Color Dictionary', layout, size=(828, 350), enable_close_attempted_event=True)

# Event Loop: processes "events" and get the "values" of the inputs
        while True:
            event, values = window.read()         
            if event == 'Search':
                window.close()
                search(favoriteColor)
            if event == 'Add':
                window.close()
                add(favoriteColor)
            if event == 'Update':
                window.close()
                update(favoriteColor)
            if event == 'Delete':
                window.close()
                delete(favoriteColor)
            if event == 'View':
                window.close()
                view(favoriteColor)
            if event == sg.WINDOW_CLOSED or event == 'Exit':
                break
            if event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT and sg.popup_yes_no('Do you really want to exit?', font=('Verdana', 10)) == 'Yes':
                break
        exit()
         

if __name__ == "__main__":
    main()