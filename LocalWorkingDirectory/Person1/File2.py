# file2.py
#This script will read the content from the text file (data.txt) created by file1.py.
def read_from_file():
    try:
        with open('data.txt', 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print("The file does not exist.")

if __name__ == "__main__":
    read_from_file()
