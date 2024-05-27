while True:
    try:
        #Read binary number from the user
        binary=input("Enter a binary number : ")
        #Convert binary to decimal using int() function
        decimal=int(binary , 2)
        #Display the equivalent decimal number
        print("Decimal equivalent :",decimal)
        break #Exit the loop if inputs is valid
    except ValueError :
        print("Invalid input. \n  "
        "please enter a valid binary number .")