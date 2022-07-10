# importing matplotlib module
from matplotlib import pyplot as plt
import csv
import pyttsx3
import speech_recognition as sr
from pandas import *
x=[]
y=[]
z=[]
v=[]
#copying the contents of each column to retrieve the data from list#   
data = read_csv("sorted dataset.csv")
title = data['book_title'].tolist()
author = data['book_authors'].tolist()
Genre = data['genres'].tolist()
print('------------------Welcome to Lets Read It!-------------------------')
print('Search for the recommendation of the best books of your preferences')
print("There are a total of ",len(Genre)," Number of books available with us")
rating = data['book_rating'].tolist()
print('Do you want to say or type your preference')
print('Press 1.To speak, Press 2.To type')
inpt=int(input())
print('Do you want to search a book by author or by genre?')
print('If author, press 1. If genre, press 2:')
a=int(input())


flag='true'
#while(flag):
if((a==1 or a==2) and inpt==1):
    if(a==1):
        print("Please say the name of the author:")
    else:
        print("Please say the genre of books:")
        
    r=sr.Recognizer()
    with sr.Microphone()as source:
        print('Please talk:')
        audio=r.listen(source)
    try:
        text=r.recognize_google(audio)
        print('Recognizing....')
        print(text)
    except sr.UnknownValueError:
        print('Google could not understand audio')
    except sr.RequestError as e:
        print('Could not request results from Google; {0}'.format(e))
        
elif((a==1 or a==2) and inpt==2):
    print('Now,you can start typing')
    text=input()
    #modifying the input to search in the dataset
l=text.split()
fl=0
for i in range(len(l)):
    if(i==len(l)-2 and len(l[i])==1):
        l[i]+='. '
        fl+=1
    elif(len(l[i])==1):
        l[i]+='.'
        fl+=1
if(fl==0):
    s1=text
else:
    s1=''.join(l)
if(a==2):
    s1=s1.capitalize()
print(s1)
if(a==1):
    for i in range(0,len(author)):
        if(s1.upper() in author[i].upper()):
            x.append(author[i])
            y.append(title[i])
            z.append(Genre[i])
            v.append(rating[i])
                
                
else:
    for i in range(len(author)):
        if(isinstance(Genre[i],str)):
            if(s1.upper() in Genre[i].upper()):
                x.append(author[i])
                y.append(title[i])
                z.append(Genre[i])
                v.append(rating[i])
'''else:
    print("Invalid input. Please try'''
    

x1=x[:15]
y1=y[:15]
z1=z[:15]
v1=v[:15]
# Function to plot the bar
plt.bar(y1,v1)
plt.xlabel("Book titles")
plt.ylabel("Ratings out of 5")
plt.title("A graphical representation indicating ratings")
# function to show the plot

def Text_to_Speech(s):
    converter = pyttsx3.init()
    converter.setProperty('rate', 130)
    converter.setProperty('volume', 1)
    converter.say(s)
    converter.runAndWait()


if(len(y1)):
    best=y1[0]
    bknam=x1[0]
    output1="Based on your preferences, we have sorted and found the best book of our database."+best+"is the best book which we found for you,written by"+bknam
    Text_to_Speech(output1)
    print("Based on your preferences, we have sorted and found the best book of our database.")
    print(y1[0],"is the best book which we found for you,written by",x1[0])
    plt.show()
else:
    output2="We don't have any books in our database meeting your requirements"
    Text_to_Speech(output2)
    print("We don't have any books in our database meeting your requirements")
print('Thank you for using our service. Please visit again.')
    


