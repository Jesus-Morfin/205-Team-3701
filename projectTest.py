import pywhatkit as pwt

#Source: https://www.youtube.com/watch?v=8IV7PFFBVZU




count = 0
print("Enter how many video you want to search up: ")
videoSearches =int(input())

while (count < videoSearches):   
    count = count + 1
    searchBar = input("Enter a Title: ")
    searchBar.upper()
    pwt.playonyt(searchBar)
    #this is a test run