import time
import random

print()
print('welcome')
print()
name=input('Enter your name : ')

starttime=time.time()


G_statements=[['what is 5+5 ?','10']]
G_statements.append(['what is the square root of 9 ?','3'])
G_statements.append(['what is 30 / 3 ?','10'])
G_statements.append(['what is 24 x 2 ?','48'])
G_statements.append(['what is 40 / 10 ?','4'])


g_statements=[['who is the first prime minister of india?','jawaharlal nehru']]
g_statements.append(['who is the first female prime minister of india?','indira ghandi'])
g_statements.append(['which symbol is used to represent equal to ?','='])
g_statements.append(['who is the first female president of india?','prathiba patil'])
g_statements.append(['in which planet we live on','earth'])


def starta():
    global score
    score=0
    for i in G_statements:
        print(''+i[0])
        while True:
            try:
                ans=int(input('Answer:'))
                break
            except ValueError:
                print('characters not accepted , please enter a number')
        if ans==int(i[1]):
            print('correct!')
            score=score+1
          
            print()
        else:
            print('incorrect,correct answer is',i[1])
            print()

     

def startb():
    global score1
    score1=0
    for i in g_statements:
        print(''+i[0])
        while True:
            
                ans=(input('Answer:'))
                break
            
        if ans==(i[1]):
            print('correct!')
            score1=score1+1
            
            print()
        else:
            print('incorrect,correct answer is',i[1])
            print()
    

starta()
startb()
print('Total score = ',score+score1,'out of 10')  
endtime=time.time()
ttime=(endtime-starttime)/60
print(ttime,'min')
