import requests
from bs4 import BeautifulSoup
import os
file = open("data.txt","w",encoding="utf-8")

url=input("Url adress:   ")
response=requests.get(url)
content=response.content
soup=BeautifulSoup(content,"html.parser")

def oneElemet():
    tag=str(input("Enter tag:  "))
    i=0
    paragraph=soup.find_all(tag)
    number=int(input("""\n\nMore than the number of pieces will not be processed.,\nHow many content?:  """))
    length=int(input("""\n\nlowest character limit for content:  """))
    lst=[]
    for par in paragraph:
        par=par.text
        if(len(par)<length):
            continue
        par=par.strip()
        par=par.replace("\n","")
        lst.append(par)
        print(par)
        i+=1
        if(i==number):
            print("{} data received..\n\n".format(number))
            break
    q1=input("Do you want to save? Y / N:   ")  
    if(q1=="Y" or q1=="y"):
        for line in lst:
            file.write(line+"\n")
        print("Save successful\n File path: {}".format(os.getcwd()))
        file.close()

def twoElement():
    tag=str(input("1st Enter tag:  "))
    tag2=str(input("2nd Enter tag:  "))
    tag3=str(input("3th Enter tag:  "))
    i=0
    paragraph=soup.find_all(tag,{tag2:tag3})
    number=int(input("""\n\nMore than the number of pieces will not be processed.,\nHow many content?:  """))
    length=int(input("""\n\nlowest character limit for content:  """))
    lst=[]
    for par in paragraph:
        par=par.text
        if(len(par)<length):
            continue
        par=par.strip()
        par=par.replace("\n","")
        lst.append(par)
        print(par)
        i+=1
        if(i==number):
            print("{} data received..\n\n".format(number))
            break
    q1=input("Do you want to save? Y / N:   ")  
    if(q1=="Y" or q1=="y"):
        for line in lst:
            file.write(line+"\n")
        print("Save successful\n File path: {}".format(os.getcwd()))
        file.close()

def sourceCode():
    answer=input("Are you sure the site source code will be displayed? Y/N :")
    if(answer=="Y" or answer=="y"):
        print(soup)
        answer=input("Do you want to save? Y / N:   ")
        if(answer=="y" or answer=="Y"):
            ans=input("1-Save site code\n2-Save texts in site\nMake your choice:   ")
            if(answer=="1"):
                file.write(str(soup))
                print("Save successful\n File path: {}".format(os.getcwd()))
            elif(answer=="2"):
                soup=soup.text.replace("\n","")
                file.write(str(soup))
                print("Save successful\n File path: {}".format(os.getcwd()))
    
