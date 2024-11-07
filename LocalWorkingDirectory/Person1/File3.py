# file3.py
#This script will read the content from data.txt, modify the data (e.g., replace a word), and save it back into the file
def process_file():
    try:
        with open('data.txt', 'r') as file:
            content = file.read()
        
        # Modify the content (replace a word)
        modified_content = content.replace("test", "processed")
        
        with open('data.txt', 'w') as file:
            file.write(modified_content)
        
        print("File has been processed and updated.")
    except FileNotFoundError:
        print("The file does not exist.")

if __name__ == "__main__":
    process_file()
