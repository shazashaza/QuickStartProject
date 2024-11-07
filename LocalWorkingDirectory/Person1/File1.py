# file1.py
#This script will create a text file (data.txt) and write some simple content into it.
def write_to_file():
    with open('data.txt', 'w') as file:
        file.write("Hello, this is a test file.\n")
        file.write("This file contains some simple data.")

if __name__ == "__main__":
    write_to_file()
    print("Data has been written to the file.")
