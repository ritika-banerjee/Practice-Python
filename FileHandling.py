# creating and writing to a file
def create():
        
    with open('user_details.txt', 'w') as f: #  a appends to the end, w overwrites the file
        name = str(input("Enter your name: "))
        f.write(name)

# reading the file
def read_lines():
    with open('user_details.txt', 'r') as file:
        lines = file.read()
        print(lines)

        # count number of words
        print(len(lines.split()))

def check_word():

    word = input("Enter the word you want to find: ").lower()

    with open('user_details.txt', 'r') as file:
        words = file.read().lower()
    
    if word in words.split():

        print(f"{word} exists")

    else:
        print(f"{word} does not exist")

def copy_file(file1, file2):

    with open(file1, 'r') as f:
        lines = f.read()

    with open(file2, 'w') as f:
        f.write(lines)

def append_data(file1):

    with open(file1, 'a') as f:
        f.write("\n")
        f.write(input("what do you want to add? "))

def count_frequency(file):

    with open(file, 'r') as f:
        lines = f.read().lower()

    dic = {}

    for word in lines.split():
        dic[word] = dic.get(word, 0) + 1

    word = input("enter the word whose frequency you want to count: ")

    print(dic.get(word, 0))

def merge_files(files):

    for file in files:

        with open(file, 'r') as f:
            lines = f.read()

        with open("merged.text", 'a') as m:
            m.write("\n")
            m.write(lines)
    
    
            

if __name__=="__main__":

    merge_files(['paragraph.txt', 'copied.txt', 'user_details.txt'])

