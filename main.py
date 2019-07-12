import sys
import validation


if __name__ == "__main__":
    if validation.main(sys.argv[1]) == True:
        print("Given board is Valid!!!")
    else:
        print("Board is invalid!!!")
