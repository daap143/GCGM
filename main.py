#imports
from app import git , graph

#banner

banner = '''
     GGGG      CCCC     GGGG    MM       MM
    GG  GG    CC  CC   GG  GG   MMMM   MMMM
   GG        CC    C  GG        MM MM MM MM
   G         C        G         MM  MMM  MM
   GG  GGG   CC       GG  GGG   MM   M   MM
   GG    GG  CC    C  GG    GG  MM       MM
    GG   GG   CC  CC   GG   GG  MM       MM
     GGGGG     CCCC     GGGGG   MM       MM
'''
print(banner,"\nGitHub Contribution Graph Modifyre/Manipulator \n           by @daap143 (MAYANK DEEP) \n \n NOTE: Read the README file here or \n at https://www.github.com/daap143/GCGM/README.md \n or you can simply watch the tutorial on https://www.youtube.com/.... ")


def take_url():
     #input repo_url and usr/token/email
     repo_url = input("\n Paste The Repo URL : ")
     #git.clone function
     repo = git.clone(repo_url)
     if(repo == 0):
          take_url()
     else:
          return repo

take_url()
#progress msg

#input the msg/txt to show in the commit graph and year

#graph function

#git.commit

#git.push

#progress msg
