#!/usr/bin/env python3

# importing the necessary files
import requests
from bs4 import BeautifulSoup

# create a dictionary that links the genre to the specific webpage, this is needed for later naming and correlating the sections
website_names = {
    'Jazz':'https://www.songkick.com/metro-areas/24571-uk-cambridge/genre/jazz',
    'Soul':'https://www.songkick.com/metro-areas/24571-uk-cambridge/genre/funk-soul',
    'Indie':'https://www.songkick.com/metro-areas/24571-uk-cambridge/genre/indie-alternative',
    'Rock':'https://www.songkick.com/metro-areas/24571-uk-cambridge/genre/rock',
}
#This will relate our input to the dictionary that is descibed above
key_code = {
    1:'Jazz',
    2:'Soul',
    3:'Indie',
    4:'Rock',
    5: ('Jazz Soul Indie Rock')
}
print('*'*90)
print('*'*90)
underline = ("_"*35)
asterisk = ('*'*90)
# Standard interger input format
key_to_print = int(input(f"""\t\t\tWhat music do you want a report on?
\t\t\t{underline}\n
{asterisk}\n{asterisk}\n\n
1: Jazz\n
2: Soul\n
3: Indie\n
4: Rock\n
5: All\n
\n\n{asterisk}\n{asterisk}\n 
>>> """)) 

print("_"*90)
key_to_printing = key_code[key_to_print]
# a simple for loop which takes into account the different sites and their relative genre names
for name, website in website_names.items():
    if name in key_to_printing:
# this starts the loop with the genre name, important to remember to set up one loop only for correlated data as it will go through that one at a time
        print(f'{name:_^90}')    
    # now it retrives the html files from the website and parsers the file 
    if name in key_to_printing:
        response = requests.get(website)
        soup = BeautifulSoup(response.text, 'html.parser')
   # this cuts down the whole html file into the section that is needed for the information on the page
   # this also is needed to specify the title section of the 
        elements = soup.find_all('li', title=True)
    # then we set up a sub loop to refine down the text file into just the two strings we want
        for element in elements:
            date_time = element['title']
            artist = element.find('strong').text  
            # this just specifies if the date is on a friday, could potentially make a dictionary for this
            if 'Friday' in date_time:
                print(f"{artist} are playing on {date_time}")
    
            if 'Saturday' in date_time:
                print(f"{artist} are playing on {date_time}")
print("_"*90)
print("_"*90)