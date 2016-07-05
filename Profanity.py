import random

msg = ["That's not a nice thing to say","Someone once told me if you don't have anything nice to say, don't say anything at all",
       "Try to be nicer","Ooh! That might hurt someone's feelings..","Snap!Looks like you are angry..."]
ch = 'y'
count = 0
badCount = 0;
newBad = []
i = 0

with open('bad.txt','r') as f:
    for word in f:
        newBad.append(word[:len(word)-1])

while (ch=='y'):
    fileName =  input('Enter file name to Upload(if in different directory, entire absolute path)')
    count = 0
    flag = 0
    badCount = 0
    with open(fileName,'r') as f:
        for bad_sent in f:
            for i in bad_sent.split():
                count = count+1
                if i in newBad:
                    badCount = badCount+1
                    flag = 1
                    j = random.randint(0,len(msg)-1)
        if flag==1:
            print('------------------------------------------------------------------------------')
            print('\tBad word(s) detected')
            print('------------------------------------------------------------------------------')
            print (msg[j])
            print('------------------------------------------------------------------------------')
            print ('Number of words ', count)
            print('Number of Bad words ',badCount)
            print('Percentage bad words ',(badCount/count)*100,'%')
            print('------------------------------------------------------------------------------')
            print('------------------------------------------------------------------------------')
        else:
                print ("\nYour file was fine")
        ch = input('Do you wish to continue?')
