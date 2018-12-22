#Python Scraper using pandas and csv to scrape ghlea.com for jail data
#Written by Jason Canfield, 12/22/18
#You will need to sudo pip3 install pandas
#Okay bob, why not, Python is fun anyway!
#Let's scrape some data.

#import the things we need
#Going to use pandas to do our scraping
import pandas as pd
#Going to use csv to write a csv file
import csv

#Set our csv file name
csvfile = 'test.csv'

#Set the URL variables we want to scrape
bookingsurl = 'http://ghlea.com/JailRosters/GHBookings.html'
releasesurl = 'http://ghlea.com/JailRosters/GHReleases.html'
rosterurl = 'http://ghlea.com/JailRosters/GHRoster.html'

#Do the initial scrape of all tables on the given urls
bookingstables = pd.read_html(bookingsurl)
rostertables = pd.read_html(rosterurl)
releasestables = pd.read_html(releasesurl)

#Define which table is the "index" out of tables on the page (the first)
bookingsindex = bookingstables[0].values.tolist()
releasesindex = releasestables[0].values.tolist()
rosterindex = rostertables[0].values.tolist()

#A function to iterate through the index table and concat the secondary tables
def iterate_tables(input_index, input_table, output_type):
    #set our iterator to 1, because 0 is the index, we already have that
    table_iterator = 1
    #check to see if print was requested
    if output_type == "print":
        #for every instance in the index (each person)
        for i in input_index:
            #Print the iteration we are on
            print(table_iterator)
            #Print the data for the iteration
            print(i)
            #print the table associated with this data iteration
            print(input_table[table_iterator].values.tolist())
            #increment the table_iterator for the next loop
            table_iterator += 1
    #check to see if CSV was requested
    elif output_type == "csv":
            #open a file in append mode and refer to it as "output_file"
            with open(csvfile, mode='a') as output_file:
                #Set our writer
                output_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)\
                #give ourselves a way to see the beginning of a capture
                output_writer.writerow("<---------BEGIN CAPTURE--------->")
                #for every instance in the index (each person)
                for i in input_index:
                    #write the instance (person)
                    output_writer.writerow(i)
                    #write the associated table
                    output_writer.writerow(input_table[table_iterator].values.tolist())
                    table_iterator += 1
                #Give ourselves a way to see the end of a capture
                output_writer.writerow("<---------END CAPTURE--------->")
    #check if we are bad at coding and didnt call print or csv
    else:
        print("Failed to parse a list.")

#Call our function and pass along each of the pages to be scraped
iterate_tables(bookingsindex, bookingstables, "csv")
iterate_tables(releasesindex, releasestables, "csv")
iterate_tables(rosterindex, rostertables, "csv")
