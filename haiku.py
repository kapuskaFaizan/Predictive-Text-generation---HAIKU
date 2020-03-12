from datamuse import datamuse
import random
from botocore.vendored import requests
import requests 
import time
from typing import Tuple
import json


loc_first   = "https://api.datamuse.com/words?md=s&rel_trg="
loc_related = "https://api.datamuse.com/words?md=s&lc="
loc_rhyme   = "https://api.datamuse.com/words?md=s&lc="

#api = 'http://www.zillow.com/webservice/ProReviews.htm?zws-id='#&screenname='
#idd = 'X1-ZWz17ksx5apxqj_43hp8'
#email ='tinotendamhlanga@yahoo.com'
#screenname = ''
def request_words(url):
    return requests.get(url).json()

def data():
	ur = 'kaggle competitions download -c zillow-prize-1'
	return request_words(ur)

def related_words(word,url):
    related_words_url = f"{url}{word}"
    return request_words(related_words_url)


def rym_trail(word):
	trail_url= f"{loc_rhyme}&rel_rhy={word}"
	return request_words(trail_url)

data()


def start(input_word):
	first_x = related_words(input_word,loc_first)
	first = [i['word'] for i in first_x if i['word'] not in ['.',',']]
	start_5.append(first[-1])
	
	count = 0 
	while(count<=2):
		
		related_x = related_words(start_5[count],loc_related)
		nex = [i['word'] for i in related_x if i['word'] not in ['.',',']]
		start_5.append(nex[0])
		count+=1
	end_word = rym_trail(start_5[-1])
	end = [i['word'] for i in end_word]
	start_5.append(end[-1])
	
	return start_5

#first_line = start(wor)

def second(first_line):
	second_x = related_words(first_line[0],loc_first)
	sec = [i['word'] for i in second_x if i['word'] not in ['.',',']]
	mid_7.append(sec[0])
	
	c = 0
	while(c<=4):
		
		rel_x = related_words(mid_7[c],loc_related)
		nexx = [i['word'] for i in rel_x if i['word'] not in ['.',',']]
		mid_7.append(nexx[0])
		
		c+=1	
	end_ = rym_trail(start_5[-2])
	end_n = [i['word'] for i in end_]
	
	mid_7.append(end_n[c])	
	
	return mid_7

#second(first_line)

def last_(mid_7):
	last = related_words(mid_7[0],loc_first)
	las = [ i['word'] for i in last if i['word'] not in ['.',',']]
	last_5.append(las[0])
	
	counter = 0
	while(counter<=2):
		
		rel_las = related_words(last_5[counter],loc_related)
		new = [i['word'] for i in rel_las if i['word'] not in ['.',',']]
		last_5.append(new[counter])
		counter +=1

	final = rym_trail(start_5[-2])
	final_n = [i['word'] for i in final if i['word'] not in ['.',',']]
	last_5.append(final_n[counter])
	#print(start_5)
	#print(mid_7)
	#print(last_5)
	z =" ".join(start_5)
	z1=" ".join(mid_7)
	z2=" ".join(last_5)
	print(z)
	print(z1)
	print(z2)

#last_(mid_7)
start_5 = []
mid_7 = []
last_5 = []

def main():
    print('hello, welcom to the predictive text haiku generator!')
    flag = True
    while(flag):
    	wor = str(input('What would you like to see a haiku about?  '))
    	first_line = start(wor)
    	second_line =second(first_line)
    	last_(second_line)
    	var = str(input('would you like to see another haiku (yes/no)? '))
    	if var == 'yes':
    		start_5.clear()
    		mid_7.clear()
    		last_5.clear()


    		flag = True
    	else:
    		flag = False


#main()



