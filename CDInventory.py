#------------------------------------------#
# Title: CDInventory.py
# Desc: Creating a CD Inventory using dictionaries
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# JPadilla, 2022-Nov-13, Replaced inner data structure by dictionaries
# JPadilla, 2022-Nov-13, Reorganizing/ Reformatting the structure of the script allowing it to be easily read
#------------------------------------------#

# Declare variabls

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
# TODO replace list of lists with list of dicts
dicRow = {}  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

# Exit the program if the user chooses so

    if strChoice == 'x':
        break

# Add data to the table (2d-list) each time the user wants to add data

    if strChoice == 'a':
        # Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        print()
        intID = int(strID)
        dicRow = {'ID':intID, 'Title': strTitle, 'Artist': strArtist}
        lstTbl.append(dicRow)
        
# Display the current data to the user each time the user wants to display the data

    elif strChoice == 'i':
        print('ID, Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep = ', ')
        print()
        
# Save the data to a text file CDInventory.txt if the user chooses so

    elif strChoice == 's':
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            objFile.write(str(row['ID']) + ',' + row['Title'] + ',' + row['Artist'] + '\n')
        objFile.close()
        print('Entry saved to file! \n')
        
# Load exisitng data from text file

    elif strChoice == 'l':
        lstTbl.clear()
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            dicRow = {'ID': lstRow[0], 'Title':lstRow[1], 'Artist': lstRow[2]}
            lstTbl.append(dicRow)
        objFile.close()
        print('Items in Table:')
        print('ID, Title, Artist')
        for row in lstTbl:
            print(str(row['ID']) + ',' + row['Title'] + ',' + row['Artist'] + '\n')
        pass

# Give option to user to delete existing entry

    elif strChoice == 'd':
        delID = int(input('Enter ID you would like to delete: '))
        for row in range(len(lstTbl)):
            if lstTbl[row]['ID'] == delID:
                del lstTbl[row]
                break
        print('Entry has been deleted! \n')
        pass
        
    else:
        print('Please choose either l, a, i, d, s or x!')

