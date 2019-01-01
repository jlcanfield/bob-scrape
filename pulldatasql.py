#This time let's make it write to an SQL table if we can figure out how.
import pandas as pd
#Commenting this out, I don't think I need CSV functions
#import csv

#Set the URL and scrape the tables in one
bTables = pd.read_html('http://ghlea.com/JailRosters/GHBookings.html')
#reURL =  pd.read_html('http://ghlea.com/JailRosters/GHReleases.html')
#roURL =  pd.read_html('http://ghlea.com/JailRosters/GHRoster.html')

#create a recallable function that we can re-use as needed for creating an index based on name
#and ID/arresting agency
def newIndex(list):
    i = 0
    for x in list:
        print(list[i][0], list[i][1], list[i][2])
        i += 1
indexList = bTables[0].values.tolist()
#newIndex(bList)

#lets check the next table
#How the hell is this bound to that other data??

#print(indexList[0][0])
#print(bTables[1])

def collate(indexList, tablesList)
        #We need to remove 2 lines from bTables because the first line is the index and the last line is a fucking copyright line
        #for error checking (to ensure that we have one information table per indexed person, we will check the two results)
        indexLength = len(indexList)
        tablesCount = len(bTables) -2
        if indexLength == tablesCount:
            #Create a new, empty listWTFSTOP
            collatedData = []
            #If they are equal, we can collate our Data
            for x in indexList:
                collatedData =
        else:
            #error output
