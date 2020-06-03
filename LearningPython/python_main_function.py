from Greetings import Greetings
from InsertionSort import InsertionSort
from BinaryTree import BinaryTree

def main():
    again = "y";

    while (again == "y" or again =="Y"):        
        print(
            "####################################################################################################################\n"+
            "####################################################################################################################\n"+
            "###                                                                                                              ###\n"+
            "###  This Is My Python Journey. All classes I created so far are listed below. Choose a number to run the class. ###\n"+
            "###                                                                                                              ###\n"+
            "####################################################################################################################\n"+
            "####################################################################################################################\n")
        print("\t1 - Greetings Class\n")
        print("\t2 - Insertion Sort Using Array")
        print("\t3 - Binary Tree ")
        print("\n\n")
        classNum = input("Enter the class number: ")
        try:
            classNum = int(classNum)
            if (classNum == 1):
                a = Greetings()
                a.showGreetings()
            elif (classNum == 2):
                print ("Not done with the solution. I will commit it soon.")
            else: 
                raise Exception ("Invalid Input. ")
        except Exception: 
            print("Invalid Input. ")
        again = input("Would you like to try again? Type y or Y for yes and anything else for no: ")
        print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            

if __name__== "__main__":
    main()



