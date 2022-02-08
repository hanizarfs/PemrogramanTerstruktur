# ============================================   FUNCTION FOR AVERAGE   ===========================================
def average(num):
    sum_num = 0
    for data in num:
        sum_num = sum_num + data          
    average = sum_num / len(num)
    return average

# ===============================================   FUNCTION FOR MAIN  ============================================
def main():
    try:
        print("\n===============================")
        print("   Program Calculate Average   ")
        print("===============================")
        num = int(input('\nEnter integer number : '))
        list_num.append(num)
        again = input("\nEnter numbers again [y/n] ? : ")
        if again == 'y':
            main()
        elif again.lower() == 'n':
            print("\nThe average from", list_num, "is", average(list_num))
            exit()
        else:
            print("\nInput unknown\nPlease enter the correct choice!\n")
            main()
    except ValueError:
        print('\nInput is not an integer')
        main()

# ==============================================   FUNCTION FOR START   ===========================================
def start():
    ask = input('Are you ready to Start this program [y/n] ? ')
    if ask.lower() == 'y':
        main()
    else:
        exit()

# ========================================   LIST TO ACCOMMOD ALL NUMBERS  ========================================
list_num = []

start()
