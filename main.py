# -*- coding: utf-8 -*-

import json
import string
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pylab import *
import numpy as np
from datetime import datetime
import inspect;
import os;
from collections import Counter

punctuation = list(string.punctuation)
stop = punctuation+[ 'a','an','the','rt', 'via','to','of','for','and','or','i','in','at','on','out','with','by',
'de',' ','is','am','are','my','your','our','us','me','you','it','','the','no','have','has','we','her','his','them',
'when','who','where','which','how','that','not','this','&amp;','from','new','la','but']

########################################################################################################################### 
########################################################################################################################### 
###############################################              ############################################################## 
###############################################    PART 1    ##############################################################
###############################################              ############################################################## 
########################################################################################################################### 
########################################################################################################################### 

def find20(fileName):
    
    JSON_file = open(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))+"\\"+ fileName, "r") 
    JSON_file.seek(0)
    term_list  = Counter()
    
    for i in JSON_file:
        tweet = json.loads(i)
        line = [j for j in ((tweet['text']).lower()).split(" ") if j not in stop]
        term_list.update(line)
        
    JSON_file.close()
    return term_list.most_common(20),term_list.most_common(10),term_list.most_common(5)

########################################################################################################################### 
########################################################################################################################### 
def writeTop20(top20, fileName):
    term  = open(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))+"\\"+ fileName, "w")
    
    for i in range(20):
        str_file = unicode(top20[i])
        term.write(str_file)
        if i !=19:
            term.write("\n")
    term.close()

########################################################################################################################### 
###########################################################################################################################            
                                    
def drawTop20(top20, fileName):
    drawList=[[],[]]
    for i in range(20):
        drawList[0].append(top20[i][0])
        drawList[1].append(top20[i][1])
    #---------------------------------------------------------------       
    plt.bar(range(len(drawList[1])), drawList[1])
    x = np.arange(len(drawList[0]))
    plt.xticks(x, drawList[0],rotation='0',horizontalalignment='left', fontsize=8,ha="left")
    plt.title("Tweet Miner" , fontsize= 10)
    plt.ylabel("Tern Frequencies")
    graph1 = plt.get_current_fig_manager()
    graph1.window.showMaximized()
    plt.show()
    plt.savefig(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))+"\\"+ fileName)

########################################################################################################################### 
########################################################################################################################### 
###############################################              ############################################################## 
###############################################    PART 2    ##############################################################
###############################################              ############################################################## 
########################################################################################################################### 
###########################################################################################################################
     
def findDateTop5(fileName,top5):
    JSON_file = open(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))+"\\"+ fileName, "r") 
    JSON_file.seek(0)
    
    timeList = [[]]
    
    for i in range(5):
        timeList[0].append(top5[i][0])
        timeList.append([[],[]])
    
      
    for i in JSON_file:
        tweet = json.loads(i)
        str = [j for j in ((tweet['text']).lower()).split(" ") if j in timeList[0]]
        date = tweet["created_at"]
        created_at_format = '%a %b %d %H:%M:%S +0000 %Y'
        dt=datetime.strptime(date, created_at_format)
        
        if str != []:
            for x in str:
                b=0
                a = timeList[0].index(x)
                #-----------------------------------------------------------
                if timeList[a+1][0] == []:
                    timeList[a+1][0].append(dt)
                    timeList[a+1][1].append(1)
                #-----------------------------------------------------------    
                else:
                    for y in timeList[a+1][0]:
                        b+=1
                        #-----------------------------------------------------------
                        if y.minute == dt.minute and y.hour == dt.hour and y.day == dt.day and y.month == dt.month and y.year == dt.year:
                            timeList[a+1][1][timeList[a+1][0].index(y)] += 1
                            break
                        #-----------------------------------------------------------
                        else:
                            if b == len(timeList[a+1][0]):
                                timeList[a+1][0].append(dt)
                                timeList[a+1][1].append(1)
                                b=0
                                break  
    JSON_file.close()
    return timeList
    
########################################################################################################################### 
########################################################################################################################### 
def writeDateTop5(list, fileName):
    overtime  = open(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))+"\\"+ fileName, "w")
    for i in range(5):
        for j in range(len(list[i+1][0])):
            
            #---------------------------------------------------------
            if list[i+1][0][j].hour < 10:
                str_hour = "0" + unicode(list[i+1][0][j].hour)
            elif len(unicode(list[i+1][0][j].hour)) ==2:
                str_hour = unicode(list[i+1][0][j].hour)
            #-------------
            if list[i+1][0][j].minute < 10:
                str_minute = "0" + unicode(list[i+1][0][j].minute)
            elif len(unicode(list[i+1][0][j].minute)) ==2:
                str_minute = unicode(list[i+1][0][j].minute)  
            #-------------
            if list[i+1][0][j].month < 10:
                str_month = "0" + unicode(list[i+1][0][j].month)
            elif len(unicode(list[i+1][0][j].month)) ==2:
                str_month = unicode(list[i+1][0][j].month)
            #-------------
            if list[i+1][0][j].day < 10:
                str_day = "0" + unicode(list[i+1][0][j].day)
            elif len(unicode(list[i+1][0][j].day)) ==2:
                str_day = unicode(list[i+1][0][j].day)
                
            str = list[0][i] +" "+unicode(list[i+1][0][j].year)+"-"+str_month+"-"+str_day+" "+str_hour+":"+str_minute+":00 "+unicode(list[i+1][1][j])
             #---------------------------------------------------------   
            overtime.write(str)
            if j != len(list[i+1][0])-1:
                overtime.write("\n")
        if i!=4:
            overtime.write("\n")   
    overtime.close()


########################################################################################################################### 
########################################################################################################################### 
def drawTop5(list, fileName):
    hours =[]
    for i in range(len(list[1][0])):
        #---------------------------------------------------------
        if list[1][0][i].hour < 10:
            str_hour = "0" + unicode(list[1][0][i].hour)
        elif len(unicode(list[1][0][i].hour)) ==2:
            str_hour = unicode(list[1][0][i].hour)
        #-------------
        if list[1][0][i].minute < 10:
            str_minute = "0" + unicode(list[1][0][i].minute)
        elif len(unicode(list[1][0][i].minute)) ==2:
            str_minute = unicode(list[1][0][i].minute)  
        hours.append(str_hour+":"+str_minute) 
        
        
    fig, xy = plt.subplots()
    xy.plot(list[1][0], list[1][1] ,label=list[0][0])
    xy.plot(list[2][0], list[2][1], label=list[0][1])
    xy.plot(list[3][0], list[3][1], label=list[0][2])
    xy.plot(list[4][0], list[4][1], label=list[0][3])
    xy.plot(list[5][0], list[5][1], label=list[0][4])
    
    
    plt.xticks(list[1][0], hours,horizontalalignment='center',fontsize=9)
    
    plt.xlabel("Time")
    plt.ylabel("Frequency of occurrence")
    
    xy.legend()
    
    graph2 = plt.get_current_fig_manager()
    graph2.window.showMaximized()
    
    plt.show()
    plt.savefig(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))+"\\"+ fileName)

########################################################################################################################### 
########################################################################################################################### 
###############################################              ############################################################## 
###############################################    PART 3    ##############################################################
###############################################              ############################################################## 
########################################################################################################################### 
########################################################################################################################### 

def matrixTop10(top10, fileName):
    JSON_file = open(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))+"\\"+ fileName, "r") 
    JSON_file.seek(0)
    
    list = [[]]
    for i in range(10):
        list[0].append(top10[i][0])
        list.append([[],[]])
        
    for i in range(10):
        for j in range(10):
            if list[0][i] != list[0][j]:
                list[i+1][0].append(list[0][j])
                list[i+1][1].append(0)


    #---------------------------------------------------------
    
    for i in JSON_file:
        tweet = json.loads(i)
        x = tweet['text'].lower().split(" ")
        str=[]
        for j in x:
            if j in list[0]:
                if j not in str:
                    str.append(j)
        if str != []:
            for j in str:
                a = list[0].index(j)
                for x in str:
                    if j !=x:
                        b = list[a+1][0].index(x)
                        list[a+1][1][b] += 1
    JSON_file.close()
    return list

########################################################################################################################### 
########################################################################################################################### 
def writeTop10(list, fileName):
    
    occur  = open(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + "\\" + fileName, "w")
    for i in range(10):
        for j in range(9):
            str=unicode(list[0][i])+"-"+unicode(list[i+1][0][j])+" "+unicode(list[i+1][1][j])
            occur.write(str)
            if j != 8 or i != 9:
                occur.write("\n")
    occur.close()
    
########################################################################################################################### 
########################################################################################################################### 
def drawMatrix(matrix, fileName,top10):
    list =[[],[]]
    for i in range(10):
        list[0].append(top10[i][0])
        list[1].append(top10[i][0])
    matris = []
    maxi=[]
    for i in range(10):
        maxi.append(max(matrix[i+1][1]))
    for i in range(10):
        matris.append(matrix[i+1][1])
        matris[i].insert(i,max(maxi)*2)
        
        
    matshow(matris)
    plt.xticks(range(len(list[1])),list[0],horizontalalignment='center',fontsize=9)
    plt.yticks(range(len(list[1])),list[0],horizontalalignment='right',fontsize=9)
    graph3 = plt.get_current_fig_manager()
    graph3.window.showMaximized()
    show()
    
    plt.savefig(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))+"\\"+fileName )

############################################################################################################################
############################################################################################################################
#################################################                             ##############################################
#################################################          MAIN PROGRAM       ##############################################
#################################################                             ##############################################
############################################################################################################################
############################################################################################################################

top20,top10,top5 = find20("tweet_data.json")

writeTop20(top20, "outputs/term_frequencies.txt")
drawTop20(top20, "outputs/term_frequencies.png")
 
dateList = findDateTop5("tweet_data.json", top5)
writeDateTop5(dateList, "outputs/term_frequencies_overtime.txt")
drawTop5(dateList, "outputs/term_frequencies_overtime.png")

matrixList = matrixTop10(top10, "tweet_data.json")
writeTop10(matrixList, "outputs/term_cooccurrences.txt")
drawMatrix(matrixList, "outputs/term_cooccurrences.png",top10)