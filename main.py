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
          year = int(input("Enter the year: "))
          option = int(input("Choose Graph Options:\n 1)Enter 1 for random commints \n 2)Enter 2 for Text Graph\n \nEneter(1 or 2): "))
          if (option==1):
              array = graph.random_commits(year)
              git.commit(array,repo)
          else:
               txt = input("Enter The text you wanna display in the Graph:")
               array = graph.text(txt,year)
               git.commit(array,repo)

take_url()
