# ========================================   FUNCTION FOR INPUT FILENAME   ========================================
def file():
    global filename
    filename = input('Enter file name : ')

# ===========================================   FUNCTION FOR VIEW DATA   ===========================================
def view_data():
    try:
        view_file = open(filename, "r")
        print('\n'+view_file.read())
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("Data input is incomplete")

# =============================================   FUNCTION FOR ADD DATA   =========================================  
def add_data():
    try:
        view_file = open(filename, "r")
        add_file = open(filename, "a")
        print("\nEnter the data to be added")
        add_data = input("Nama  : ")
        add_file.write("\n\nNama    : "+add_data)
        add_data = input("NPM   : ")
        add_file.write("\nNPM     : "+add_data)
        add_data = input("Prodi : ")
        add_file.write("\nPordi   : "+add_data)
        tanya = input('Enter data again [y/n] ? : ')
        add_file.close
        if tanya.lower() == 'y':
            add_data()
        elif tanya.lower() =='n':
            exit()
        else:
            print('Input unknown')
            return add_data()
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("Data input is incomplete")

# ==============================================   FUNCTION FOR EXIT   ============================================
def ex():
    print('\nSee You Next Time')
    exit()
    
# ==========================================   FUNCTION FOR BACK TO MENU   ========================================
def btm():
    tanya = input('Back to menu [y/n] ? ')
    if tanya.lower() == 'y':
        return main()
    else:
        ex()
    
# =======================================   FUNCTION BECAUSE WRONG INPUT   ========================================
def wrong_input():
    print("Input unknown\nPlease enter the correct choice!")
    main()
    
# =========================================   FUNCTION FOR MAIN PROGRAM   ==========================================
def main():
    print('Hoola, Welcome Back\n\n1. View Data\n2. Add Data\n3. Exit')
    pilih = input('=> ')
    if pilih == '1':
        file()
        view_data()
        btm()
    elif pilih == '2':
        file()
        add_data()
        btm()
    elif pilih == '3':
        ex()
    else:
        wrong_input()
        
main()
