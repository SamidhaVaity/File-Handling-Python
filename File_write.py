import os

def main():
    print("Enter the name of the file that you want to open for writing puspose : ")
    File_name = input()

    if os.path.exists(File_name):
        fobj = open(File_name,"a") # append mode
        if fobj:
            print("File Successfully openedin the append mode")

            print("Enter the data that you want to enter in the file")
            Data = input()

            fobj.write(Data) # write the data into the file

            fobj.close()
        else:
            print("Unable to open file")
    else:
        print("There is no such file")

if __name__ == "__main__":
    main()