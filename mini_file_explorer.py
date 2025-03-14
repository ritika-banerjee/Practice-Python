import os

files = [f for f in os.listdir() if f.endswith((".txt", ".py"))]
print("Available files: ",files)

filename = input("Enter the file name you want to open: ")

if filename not in files:
    print("File not found")

option = input("Choose an option - (R)ead / (E)dit / (D)elete: ").lower()

if option == "r":
    with open(filename, 'r') as f:
        print(f.read())

elif option == "e":
    new_content = input("Enter new content: ")
    with open(filename, 'w') as f:
        f.write(new_content)
    print("File updated.")

elif option == "d":
    os.remove(filename)
    print("File deleted.")