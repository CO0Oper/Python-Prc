def findPalindrome():
    loop = True
    while loop == True:
        userIn = input("Enter your phrase: ")
        array = []
        define = 0
        for letter in userIn:
            array += letter
        index = int(array.__len__())
        a = 0
        while index > a:
            if array[a].lower() != array[index - a - 1].lower():
                print("Is not a palindrome")
                a = index
                define = 1
            a += 1

        if define != 1:
            print("Is a palindrome")


        if input("Another one? 1/2") == "y":
            loop = True
        else:
            loop = False



findPalindrome()
