def check_fname():
    try:
        filename = input('Enter file name : ')
        file = open(filename, "r")
        print('The', filename, 'file is on your computer')
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("Data input is incomplete")
    
def read_fname():
    try:
        filename = input('Enter file name : ')
        file = open(filename, "r")
        print('The contents of the', filename, 'file are:')
        print('\n'+file.read())
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("Data input is incomplete")
        
def main():
    print('\nHola, Wellcome Back!\n\n1. Check Filename\n2. Read Filename\n3. Exit\n')
    choice = input('=> ')
    if choice == '1':
        check_fname()
    elif choice == '2':
        read_fname()
    else:
        print('Thanks/nSee You Next Time :)')
        exit()
    
main()
