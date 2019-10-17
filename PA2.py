# Programming Assignment #3 
# Intro. to NLP
# Usman Gohar
# Submitted to Ted Pedersen
# Date:06/10/17

# Implement and Design a python program that will learn an N-gram model language model from an arbitrary number of text files
# It generates a given number of sentences based on the model
# This program works for unigrams, bigrams and trigrams


from __future__ import division		#import library to do floating point division
import random 				#import library to generate random numbers
import nltk				#import NLTK
from nltk import word_tokenize		#import tokenize from NLTK
from nltk.util import ngrams 		#import Ngrams from NLTK
from collections import Counter 	#Python class to count number of times an element occurs in a list
import re 
import sys

reload(sys)
sys.setdefaultencoding('utf8')		#change encoding to unicode (Used in the program)

files=[];				#list of files to be read as input
print sys.argv[2]
for  i in range(3,len(sys.argv)):	#generate the list of files that has been entered as input by user
	files.append(sys.argv[i])

for i in range(0,len(files)):		#Open and read each file and append to generate one single list
	file = open(files[i], "r")
	data=file.read()
	data=unicode(data, errors='ignore')
#	data=data1+data
#	print data

#data.extend(data1)

token = nltk.word_tokenize(data)	#Use tokenize from NLTK to break down the text into words,puntuations,periods etc
size=len(token)				#Total number of Tokens

unigrams=ngrams(token,1)		#This generates a list of unigrams from the set of tokens above. NLTK library function
lis=Counter(unigrams)			#Use Counter to generate frequencies of the unigrams in a dictionary

bigrams = ngrams(token,2)		#Use tokenize from NLTK to break down text into bigrams. Includes periods, punctuation etc.
bi=Counter(bigrams)			#Same as above

trigrams=ngrams(token,3)		#Use tokenize from NLTK to break down text into trigrams.
tri=Counter(trigrams)			#Same as above


############3
#UN={}
#t=nltk.word_tokenize(string)
#uni=ngrams(t,1)
#UN=Counter(uni)
######################


#for key,value in UN.items():

#	UN[key]=(value/len(t))

###################### UNIGRAM FUNCTION ##########################################

def unigramss(lis,n):

	lis1={};			#list to store probabilities of unigrams
	final=[];			#final list to store answer
	for key, value in lis.items():	#calculate probabilities of unigrams by searching for each key and dividing the value(frequency) by total size
		lis1[key]=(value/size)	#Formula: P(A)=C(A)/C(Tokens)

	i=0;
	sent=[];
	while  (i<n):			#Generate N number of sentences
		sent=[]
		x = random.random()	#Generate a random number
		temp_back=0;
		for key,value in lis1.items():				#To find in which unigram probability interval the random number fits in keep on adding the max probability
			temp=value+temp_back;				#of previous interval to the next and pick the unigram for the interval that the random number is in
			if (x>temp_back and x<=temp):			#Keep on generating sentences until a puntuation from these 3 are encountered
				sent.append(key[0])
				print sent
				if key[0]=="." or key[0]=="," or key[0]=="?":         #The class example of dog,mouse and cat intervals can $
                                	print "End of Sentence",i
					i=i+1
                                	break
			temp_back=temp
		final.extend(sent)					#There is one problem where I cannot print them in sentences form. So it will print in columns in unigram list form
									#The period is sometimes joined with the next sentence. But the sentence in essence is correct
	#print str(final)


################## BI-GRAM FUNCTION ##############################################

def bigramss(bi):

	bi1={};				#list to store probabilities of bigrams
	temp1=0;			#temp list
	list=[];
	count=0;			#to calculate probability of bigrams by dividing by Count
	final=[];

	for key,value in bi.items():		#Generate probabilities for each bigram
		list=key;			#Formula : P(A|B)=C(A|B)/C(B)
		temp1=list[1];			
		count=lis[temp1,]
		bi1[key]=value/count

	i=0;
	sent1=[];
	while(i<10):			#Generate N number of sentences 
		sent1=[];
		x=random.uniform(0, 16148)	#Generate random number
        	temp_back=0;
       		for key,value in bi1.items():		#Do the same procedure as in unigrams. Find the interval in which the random number lies
                	temp=temp_back+value;		#Then pick that bigram to generate the sentence
			if (x>temp_back and x<=temp):
                        	sent1.append(key)
				if key[0]=="." or key[0]==",":		#Do that until a period is encountered
                                	print "Sentence",i+1
					i=i+1
                                	break

                	temp_back=temp

		final.extend(sent1)
		print sent1				#AGAIN THE FORMAT OF THE SENTENCE IS NOT CORRECT. BUT IF THE NUMBER OF PERIODS ARE COUNTED IN THE RESULT
							#IT CAN BE VERIFIED THAT THE SENTENCES GENERATED ARE CORRECT

############################# TRI-GRAMS ################################

def trigramss(tri):
	tri1={};			#list probabilities of trigrams
	temp2=0;
	list1=[];
	i=0
	for key,value in tri.items():		#Generate Probabilites for each trigram
		i=i+1				#Formula: P(A|B|C)=C(A|B|C)/C(B|C)
		list1=key;			#The count in the denominator is calculated using frequency of the keys in Bigrams
		temp2=list1[1:]
		count=bi[temp2]
		if count==0:			#This is done in cases where the bigram does not exist and returns a zero
			tri1[key]=0
		else:
			tri1[key]=value/count

	i=0;
	sent2=[]
	final=[];
	while(i<10):				#Generate N number of sentences  using Trigrams
		sent2=[];
		x=random.uniform(0, 16148)
        	#i=i+1;
        	temp_back=0;
       		#print x
        	for key,value in tri1.items():	#Same logic as above. Find the interval where the random number lies and pick trigram to generate sentences
                	temp=temp_back+value;

                	if (x>temp_back and x<=temp):
                        	sent2.append(key)
				if key[0]=="." or key[0]==",":			#Terminate when period encountered
                                	i=i+1
					print "End of Sentence ",i,"\n"
                                	break

                	temp_back=temp
		final.extend(sent2)
		print sent2
#	print final

if (sys.argv[1]=='1'):			#If the second argument of input is one, run unigram function
	unigramss(lis,10)
if (sys.argv[1]=='2'):			#If the second argument of input is two, run bigram function
	bigramss(bi)
if (sys.argv[1]=='3'):			#If the second argument of input is three, run trigram function
	trigramss(tri)





#	print count
#	bi[key]=value/(
#for key,value in bi.items():
#	check=UN[key]
#	bi[key]=(value/UN[key[0])
#print bi['be','fine']
