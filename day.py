import os

print ("Read Across America Reading Challenge")
print ('Februrary 14 - March 27, 2022 ')
print ('To be eleigible for a free ticket to Silverwood, Students must: \n ')
print ('\t' '1. Read 5 out of 7 days for 6 weeks'  )
print ('\t' '2. K-2nd = 20 min/day 5 days/ week')
print ('\t' '3. Record number of mninutes read and weekly totals on the calendar.')
print ('\t' '4. Parent Signature at the bottom and signed form returned by Monday, March 28, 2022 \n')


print ("Read Across America Reading Challenge")
print ('Februrary 14 - March 27, 2022 ')
print ('To be eleigible for a free ticket to Silverwood, Students must: \n ')
print ('\t' '1. Read 5 out of 7 days for 6 weeks'  )
print ('\t' '2. K-2nd = 20 min/day 5 days/ week')
print ('\t' '3. Record number of mninutes read and weekly totals on the calendar.')
print ('\t' '4. Parent Signature at the bottom and signed form returned by Monday, March 28, 2022 \n')

# print ('Week 1')
# print ("Monday, Februrary 14") 


def sum (minutes):
    S=0
    for X in minutes:
        S= S+X
    return S   
minutesread= [] 
if os.path.isfile('Daily reading file'):
     f=open('Daily reading file','r')
     for line in f:
         minutesread.append (int (line))
weeks= []
                                   
booksread=[]
days=['Sunday: ','Monday: ','Tuesday: ','Wednesday: ','Thursday: ','Friday: ','Saturday: ']
for day in days [len (minutesread): ]:
        n= input('When done type done '+'\n' "Minutes Read "+ day) ## Loop through the days of the week Sunday- Saturday
        if n =="done":
            break   ##? How do you open up on each day? ex. already put in Monday, how do you open up for Tuesday? 
        n = int(n)
        books = input('What did you read?')
        minutesread.append (n) #append means take integer (n) and put it into the list
                                            ##print ('Week '+ (str(I)), sum (minutesread))
        booksread.append (books)                                    


if len(minutesread) ==7:

    weeks.append(sum(minutesread))
    print (str(books))

    f= open('Daily reading file','w')
    for day in weeks:
        f.write (str(day) + '\n')
    f.close

    f=open('Daily reading file', 'r')
    for line in f:
        days.append (int(line))
    f.close


    f= open ('Books Read','w')
    for books in booksread:
        f.write (books + '\n')
    f.close ()

    f= open ('Books Read', 'r')
    for book in f:
        booksread.append (book)
    f.close ()

    f= open('Harrison reading log.txt','r')
    for line in f:
        weeks.append (int(line))
    f.close ()

    f= open ('Harrison reading log.txt','w')
    for week in weeks:
        f.write (str(week) +"\n")
    f.close ()
    print ('Total Minutes Read this week: ', sum(minutesread))
    print ('Total Minutes Read: ', sum(weeks))
else: 
    f=open ('Daily reading file', 'w')
    for minute in minutesread:
        f.write (str (minute) + '\n')
    f.close ()




