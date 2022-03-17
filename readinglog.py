
print ("Moran Prarie Reading Challenge")
print ('Februrary 14 - March 27, 2022 ')
print ('To be eleigible for a free ticket to Silverwood, Students must: ')
print ('\t' '1. Read 5 out of 7 days for 6 weeks'  )
print ('\t' '2. K-2nd = 20 min/day 5 days/ week')
print ('\t' '3. Record number of mninutes read and weekly totals on the calendar.')
print ('\t' '4. Parent Signature at the bottom and signed form returned by Monday, March 28, 2022')

print ('Week 1')
print ("Monday, Februrary 14") 


def sum (n):
    S=0
    ##for X in range (0,8,n+S):
    S= S+n
    return S    

n= input("Minutes Read ") 
n = int (n)
S = sum (n)
print ('Weekly Minute Totals', n)

print ("Tuesday, February 16")
input ("Minutes Read ")
sum (n+S)
print ("Weekly Minute Totals", n)

