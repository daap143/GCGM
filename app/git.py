#imports
from os import system

#def clone
def clone(repo_url):
    #extract dir name function
    i = len(repo_url)
    extract(i,repo_url)
    #clone cmd
    #system(f"git clone {repo_url}")

#def commit


#def push


#def extract
def extract(i,repo_url):
    temp = []
    while(repo_url[i-1]!="/"):
        temp.append(repo_url[i-1])
        i-=1
    repo = put(temp)
    print(repo)

def put(temp):
    j = len(temp) - 1
    string = ""
    while(j>=0):
        string = string + temp[j]
        j-=1
    return string

