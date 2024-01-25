#imports
from os import system

#def clone
def clone(repo_url):
    #extract dir name function
    # i = len(repo_url)
    try:
        repo= extract(repo_url)
        system(f"git clone {repo_url}")
        system(f"cd {repo} && touch temp.txt")
        return repo

    except:
        print(f"ERROR:{repo_url} is  Not a Valid URL , try again")
        return 0



#def commit
def commit(array,repo):
    for i in array:
        system(f"cd {repo} && echo -e '{i}\n' >> temp.txt && git add -A && git commit -m '{i}' --date '{i}'")
        # print(f"cd {repo} && echo -e '{i}\n' >> temp.txt && git commit  -m '{i}' --date '{i}'")
    push(repo)
#def push
def push(repo):
    system(f"cd {repo} && git push -u origin main")

#def extract
def extract(repo_url):
    if "/" in repo_url:
        repo = repo_url.rstrip('/').split('/')[-1].replace('.git', '')
        return repo
    else:
        return 0
