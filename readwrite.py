with open('name.txt') as f:
    full_text = f.read()

print(full_text)

# Writing a text file
with open('hello.txt', 'w') as f:
    f.write('Hello, my name is ')
    f.write(full_text)
    f.write('.')
    f.write('\n')
