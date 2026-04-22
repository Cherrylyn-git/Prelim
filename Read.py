file_path = "c:\\Users\\USER\\OneDrive\\Desktop\\Inventory.txt"
with open(file_path, 'r') as file:
    content = file.read()
    
print(content)