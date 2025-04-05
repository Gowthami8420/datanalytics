
file=open('test.txt','r')
content=file.read()
print(content)

content1=file.readline()
print(content1)
content2=file.readlines()
print(content2)

#Write on file
file=open('test.txt','a')
writing=file.write(f"new content")
print(writing)
file.close()

import os
if os.path.exists("test.txt"):
    with open('test.txt','r') as file:
        content=file.read()
        print(content)
else:
    print("File does not exit")
    
import os 
try:
    with open ('test.txt','r') as file:
        data=file.read()
    with open('test1.txt','w') as file:
        file.write(data)
    print("file copied successfully")
except FileNotFoundError:
    print("input or output ")
except IOError as e:
    print(f"i/o exception:{e}")
except Exception as e:
    print("An unexcepted error")
    
with open('exp.txt', 'w') as f:
    f.write("Some content")

print("File copied successfully")

import os
os.remove('exp.txt')

    
f=open('exp.txt','w')
import os
os.remove('exp.txt')


# os.rmdir("myfolder")