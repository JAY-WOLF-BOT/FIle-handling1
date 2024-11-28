
file = open('sample3.txt', 'r')
content = file.read()
print("Using read():")
print(content)
file.close()

print("\nUsing readline():")
file = open('sample3.txt', 'r')
line = file.readline()
while line:
    print(line)
    line = file.readline()
file.close()

# Using open() with readlines()
print("\nUsing readlines():")
file = open('sample3.txt', 'r')
lines = file.readlines()
for line in lines:
    print(line)
file.close()
