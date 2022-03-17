
print ("Moran Prarie Reading Challenge")
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
weeks= []
###for I in range (1,5): ###this is calling 4 weeks worth of reading, we want to do one week at a time and read from each week. 
minutesread= [] 
days=['Sunday: ','Monday: ','Tuesday: ','Wednesday: ','Thursday: ','Friday: ','Saturday: ']
for day in days:
        n= input("Minutes Read "+ day) ## Loop through the days of the week Sunday- Saturday
        n = int(n)
        minutesread.append (n) #append means take integer (n) and put it into the list
##print ('Week '+ (str(I)), sum (minutesread))
weeks.append(sum(minutesread))
f= open ('Harrison reading log.txt','w')
f.write ('Week 1 Total Minutes: '+ str(sum(weeks))+'\t') #using an add sign brings the each item into the string. 
f.close ()
print ('Total Minutes ', sum(weeks))
f= open('Harrison reading log.txt','r')
    
    ### now we want to run the function, read from the file and add the total minutes to the file calculation each week. 
    ### copy the function then write then close 

