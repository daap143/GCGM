#imports
from os import system

#def clone
def clone(repo_url):
    #extract dir name function
    i = len(repo_url)
    try:
        repo= extract(i,repo_url)
        system(f"git clone {repo_url}")
        return repo

    except:
        print(f"ERROR:{repo_url} is  Not a Valid URL , try again")
        return 0

#def commit


#def push


#def extract
def extract(i,repo_url):
    temp = []
    while(repo_url[i-1]!="/"):
        temp.append(repo_url[i-1])
        i-=1
    while(temp[0] != "."):
        temp.remove(temp[0])
    temp.remove(temp[0])
    j = len(temp) - 1
    repo = put(temp,j)
    return repo

def put(temp,j):
    string = ""
    while(j>=0):
        string = string + temp[j]
        j-=1
    return string
