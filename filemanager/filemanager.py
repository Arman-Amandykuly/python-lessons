import os
import os.path
import time
os.system("color 17")
initial_path = "C:"
os.chdir(initial_path)
isclosed = False
welcome = '''WELCOME
'''
instruction = '''
Welcome to Arman\'s file manager 0.0.1!
The functionality of this program is simple, so don\'t worry about commands. They are pretty easy to remember.
cd - the same command as in cmd. It\'s for changing current directory to another
del - delete some stuff
rename - rename directories or files
edit - modify files
rewrite - totally rewrite a file
return - go to parent directory
files - show number of files
dirs - show number of directories
list - show list of stuff which are included in the current directory
help - show instructions again(this text)
color - change color(such as in cmd)

Good luck! :3
'''
def color(c):
    try:
        os.system("color ")
    except:
        pass
def cd(c):
    try:
        os.chdir(c[1])
    except:
        print(c[1])
        print("The directory doesn\'t exist")
def delete(c):
    try:
        if(os.path.isfile(c[1])):
            os.remove(c[1])
        else:
            os.rmdir(c[1])
    except:
        print("No such file or directory")
def rename(c):
    if(len(c)==1):
        print("This command is for renaming files or directories")
    else:
        try:
            if(os.access(c[1],os.F_OK)):
                os.rename(c[1],c[2])
            else:
                print("No such file or directory")
        except:
            print("The file or directory cannot be renamed")
def edit(c):
    try:
        if(os.access(c[1],os.F_OK)):
            k = input()
            m = ""
            while(k!=""):
                m+=k
                k = input()
            with open(c[1],"a") as f:
                f.write(m)
        else:
            print("No such file or directory")
    except:
        print("The file or directory cannot be modified")
def rewrite(c):
    try:
        if(os.access(c[1],os.F_OK)):
            k = input()
            c = "\n"
            while(k!=""):
                c+=k+"\n"
                k = input()
            with open(c[1],"w") as f:
                f.write(c)
        else:
            print("No such file or directory")
    except:
        print("The file or directory cannot be modified")
def rtrn(c):
    try:
        os.chdir("..")
    except:
        print("Impossible to go to parent directory")
def files(c):
    if(os.path.isdir(os.getcwd())):
        stuff = os.listdir()
        n = sum(map(lambda x: os.path.isdir(x),stuff))
        print(len(stuff)-n)
    else:
        print(os.path.split(os.getcwd())[2])
        print("It\'s not a directory")
def dirs(c):
    if(os.path.isdir(os.getcwd())):
        stuff = os.listdir()
        n = sum(map(lambda x: os.path.split(x)=="",stuff))
        print(n)
    else:
        print("It\'s not a directory")
def lst(c):
    if(os.path.isdir(os.getcwd())):
        for i in os.listdir():
            print(i)
    else:
        print("It\'s not a directory")
def hlp(c):
    if(len(c)>1):
        print(instruction)
    else:
        os.system("cls")
        for i in instruction:
            print(i,end = "")
            if(i=="\n"): time.sleep(0.3)
def qt(c):
    global isclosed
    print("Goodbay!!!")
    time.sleep(2)
    isclosed = True
def create(c):
    try:
        if(not os.access(c[1],os.F_OK)):
            k = input()
            m = "\n"
            while(k!=""):
                m+=k+"\n"
                k = input()
            with open(c[1],"x") as f:
                f.write(m)
        else:
            print("The file already exists")
    except:
        print("The file or directory cannot be created")
def color(c):
    try:
        os.system(" ".join(c))
    except:
        pass
content = bytes()
name = ""
def copy(c):
    try:
        if(os.access(c[1],os.F_OK)):
            with open(c[1],"r") as f:
                global content,name
                content,name = f.read(),c[1]
        else:
            print("The file doesn\'t exist")
    except:
        print("The file cannot be copied")
def put(c):
    try:
        with open(c[1],"x") as f:
            f.write(content)
    except:
        print("The file cannot be pasted")
def mkdir(c):
    try:
        os.mkdir(c[1])
    except:
        print("The directory cannot be created")
functions = {"mkdir":mkdir,"put":put,
             "copy":copy,"create":create,
             "cd":cd,"del":delete,
             "list":lst,"dirs":dirs,
             "files":files,"return":rtrn,
             "rename":rename,"edit":edit,
             "rewrite":rewrite,"exit":qt,
             "help":hlp,
             "color":color}
def main():
    while(not isclosed):
        c = input(os.getcwd()+" ").split()
        try:
            if(c[0] in functions.keys()):
                functions[c[0]](c)
            else:
                print("Invalid command")
        except:
            pass
    exit()
hlp(["hello"])
main()