import os
# demondstration of file handaling
def main():
    print("Enter the name of the file that you want to open for reading puspose : ")
    File_name = input()

    if os.path.exists(File_name):
        fobj = open(File_name,"r") # read mode
        if fobj:
            print("File Successfully opened in the read mode")

            Line1 = fobj.readline()
            Line2 = fobj.readline()
            Line3 = fobj.readline()

            print("First line is: ", Line1)
            print("Second line is: ", Line2)
            print("Third line is: ", Line3)

            fobj.close()
        else:
            print("Unable to open file")
    else:
        print("There is no such file")

if __name__ == "__main__":
    main()