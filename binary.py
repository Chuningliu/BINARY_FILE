# Create a binary file with name and roll number. 
# Search for a given roll number and display the name,
# if not found display appropriate message.

import pickle
def write():
    f=open("Studentsdetails.txt","wb")
    while True:
        roll=int(input("Enter the Roll no.:-"))
        name=input("Enter the name of the Students:-")
        a=[roll,name]
        pickle.dump(a,f)
        rec=input("Wanna add more Students?(Y/N)")
        if rec in "Nn":
            break
    f.close()
def Read():
    f=open("Studentsdetails.txt","rb")
    try:
        while True:
            b=pickle.load(f)
            print(b)
    except EOFError:
        f.close()
write()
Read()
def search():
    found=0
    Find=int(input("Enter the Roll no. whose name to be display:-"))
    f=open("Studentsdetails.txt","rb")
    try:
        while True:
            b=pickle.load(f)
            if b[0]==Find:
                print(b[1])
                found=1
                break
    except EOFError:
        f.close()
    if found==0:
        print("Sorry!! No such name exist......")
write()
search()

       

        

