import os

def main():
    print("Enter the name of the file that you want to open for reading puspose : ")
    File_name = input()

    if os.path.exists(File_name):
        fobj = open(File_name,"r") # read mode
        if fobj:
            print("File Successfully opened in the read mode")

            Data = fobj.read(10)
            print("Data from file is : ",Data)

            fobj.close()
        else:
            print("Unable to open file")
    else:
        print("There is no such file")

if __name__ == "__main__":
    main()