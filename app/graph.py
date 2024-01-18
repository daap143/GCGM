#imports
import random

months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
#creat graph display of 7x48

#define pixel data for each capital/small alphabet

#translate the linear graph to the year graph

#short dates according to the graph

#random
def random_commits(year):
    array= []
    for i in range(0,300):
        array.append(f"{random.choice(months)} {random.randrange(1,29)} {random.randrange(0,23)}:{random.randrange(0,59)}:{random.randrange(0,59)} {year}")
    return(array)
