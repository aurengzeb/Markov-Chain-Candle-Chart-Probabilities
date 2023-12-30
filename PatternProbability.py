import os
import statistics
from collections import Counter
import logging
import h5py
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
import time
from statistics import mean,stdev
import matplotlib.patches as mpatches
import math
import glob
##import SentimentAnalysis as SA
import pandas as pd
from statistics import mean,stdev
import matplotlib.pyplot as plt

def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier

def main():
    corepath = os.path.dirname(os.path.abspath(__file__))
    timeframe = [168,720]#Week and Month Probable State
    tscorerepo = []
    FirstTimeFrameforAll = []
    HalfofitTimeFrameforAll = []
    FullOfTF = []
    SecondHalfofitTimeFrameforAll = []

    Inferencespath = corepath+"/Dataprocessing/"
    current = glob.glob(Inferencespath+"*.csv")
    Inferences_Timeframe = [1,4]#Using 4 and 1h timeframe

    import random
    randomized = []
##    for i in range(0, 10):
##        a = random.randint(0, 64)
##        randomized.append(bin(a))
##        print(a, bin(a))


##    try:
    nextanalysis = 0
    for t in Inferences_Timeframe:
        for k in current:
            Split1st = k.split(".csv")
            Split2nd = Split1st[0].split("\\")
            if float(Split2nd[-1]) == float(t):
                thefileswillbe = k
                break

        selectfiles = pd.read_csv(thefileswillbe)
        data = pd.read_csv(thefileswillbe)
        data["daily_return"] = data["Close"].pct_change()

        print(thefileswillbe)
        data["state"] = np.where(data["daily_return"] >= 0, "1","0")
##            print(data)
##            up_counts = len(data[data["state"]=="up"])
##            down_count = len(data[data["state"]=="down"])
##            up_to_up = len(data[(data["state"] == "up") & (data["state"].shift(-1)=="up")])/ len(data.query('state=="up"'))
##            down_down = len(data[(data["state"] == "down") & (data["state"].shift(-1)=="down")])/ len(data.query('state=="down"'))
##            down_to_up = len(data[(data["state"] == "up") & (data["state"].shift(-1)=="down")])/ len(data.query('state=="up"'))
##            up_to_down = len(data[(data["state"] == "down") & (data["state"].shift(-1)=="up")])/ len(data.query('state=="down"'))

        patternreduce = [1,-1,-2,2]
        #selectivemethodforbinary = "BRUTE"
        for p in patternreduce:
            print("TRYING WITH %i PATTERN..."%p)
            regression = []
            if p == 1:
                patternrange = 2**6
                bitfill = 6
            elif p == -1:
                patternrange = 2**5
                bitfill = 5
            elif p == -2:
                patternrange = 2**4
                bitfill = 4
            elif p == 2:
                patternrange = 2**7
                bitfill = 7
            for i in range(patternrange):
                if p==2:
##                    k = np.random.choice([0, 1], size=(7,), p=[1./3, 2./3])
##                    s = ''.join(str(x) for x in k)
                    s = bin(i)[2:].zfill(bitfill)
                    k = list(s)
                    print("Pattern Regression is %s"%s)
                    dddddu = len(data[(data["state"] == str(k[0])) & (data["state"].shift(-1)==str(k[1])) & (data["state"].shift(-2)==str(k[2])) & (data["state"].shift(-3)==str(k[3])) & (data["state"].shift(-4)==str(k[4])) & (data["state"].shift(-5)==str(k[5])) & (data["state"].shift(-6)==str(k[6]))])
                    ddddd = len(data[(data["state"] == "0") & (data["state"].shift(1)=="0") & (data["state"].shift(2)=="0") & (data["state"].shift(3)=="0") & (data["state"].shift(4)=="0") & (data["state"].shift(5)=="0") & (data["state"].shift(6)=="0")])
                    try:
                        dddddu = dddddu/ddddd
                    except:
                        dddddu = 0

                    ddddu = len(data[(data["state"] == str(k[0])) & (data["state"].shift(-1)==str(k[1])) & (data["state"].shift(-2)==str(k[2])) & (data["state"].shift(-3)==str(k[3])) & (data["state"].shift(-4)==str(k[4])) & (data["state"].shift(-5)==str(k[5]))])
                    dddd = len(data[(data["state"] == "0") & (data["state"].shift(1)=="0") & (data["state"].shift(2)=="0") & (data["state"].shift(3)=="0") & (data["state"].shift(4)=="0") & (data["state"].shift(5)=="0")])
                    try:
                        ddddu = ddddu/dddd
                    except:
                        ddddu = 0


                    uuuuud = len(data[(data["state"] == str(k[0])) & (data["state"].shift(-1)==str(k[1])) & (data["state"].shift(-2)==str(k[2])) & (data["state"].shift(-3)==str(k[3])) & (data["state"].shift(-4)==str(k[4])) & (data["state"].shift(-5)==str(k[5])) & (data["state"].shift(-6)==str(k[6]))])
                    uuuuu = len(data[(data["state"] == "1") & (data["state"].shift(1)=="1") & (data["state"].shift(2)=="1") & (data["state"].shift(3)=="1") & (data["state"].shift(4)=="1") & (data["state"].shift(5)=="1") & (data["state"].shift(6)=="1")])
                    try:
                        uuuuud = uuuuud/uuuuu
                    except:
                        uuuuud = 0


                    uuuud = len(data[(data["state"] == str(k[0])) & (data["state"].shift(-1)==str(k[1])) & (data["state"].shift(-2)==str(k[2])) & (data["state"].shift(-3)==str(k[3]))  & (data["state"].shift(-4)==str(k[4])) & (data["state"].shift(-5)==str(k[5])) ])
                    uuuu = len(data[(data["state"] == "1") & (data["state"].shift(1)=="1") & (data["state"].shift(2)=="1") & (data["state"].shift(3)=="1") & (data["state"].shift(4)=="1") & (data["state"].shift(5)=="1")])
                    try:
                        uuuud = uuuud/uuuu
                    except:
                        uuuud = 0

                    s = ''.join(str(x) for x in k)
                    temp = [thefileswillbe,s,dddddu,ddddu,uuuuud,uuuud]
                    regression.append(temp)
                elif p==1:
##                    k = np.random.choice([0, 1], size=(6,), p=[1./3, 2./3])
##                    s = ''.join(str(x) for x in k)
                    s = bin(i)[2:].zfill(bitfill)
                    k = list(s)
                    print("Pattern Regression is %s"%s)
                    dddddu = len(data[(data["state"] == str(k[0])) & (data["state"].shift(-1)==str(k[1])) & (data["state"].shift(-2)==str(k[2])) & (data["state"].shift(-3)==str(k[3])) & (data["state"].shift(-4)==str(k[4])) & (data["state"].shift(-5)==str(k[5]))])
                    ddddd = len(data[(data["state"] == "0") & (data["state"].shift(1)=="0") & (data["state"].shift(2)=="0") & (data["state"].shift(3)=="0") & (data["state"].shift(4)=="0") & (data["state"].shift(5)=="0")])
                    try:
                        dddddu = dddddu/ddddd
                    except:
                        dddddu = 0

                    ddddu = len(data[(data["state"] == str(k[0])) & (data["state"].shift(-1)==str(k[1])) & (data["state"].shift(-2)==str(k[2])) & (data["state"].shift(-3)==str(k[3])) & (data["state"].shift(-4)==str(k[4]))])
                    dddd = len(data[(data["state"] == "0") & (data["state"].shift(1)=="0") & (data["state"].shift(2)=="0") & (data["state"].shift(3)=="0") & (data["state"].shift(4)=="0")])
                    try:
                        ddddu = ddddu/dddd
                    except:
                        ddddu = 0


                    uuuuud = len(data[(data["state"] == str(k[0])) & (data["state"].shift(-1)==str(k[1])) & (data["state"].shift(-2)==str(k[2])) & (data["state"].shift(-3)==str(k[3])) & (data["state"].shift(-4)==str(k[4])) & (data["state"].shift(-5)==str(k[5]))])
                    uuuuu = len(data[(data["state"] == "1") & (data["state"].shift(1)=="1") & (data["state"].shift(2)=="1") & (data["state"].shift(3)=="1") & (data["state"].shift(4)=="1") & (data["state"].shift(5)=="1")])
                    try:
                        uuuuud = uuuuud/uuuuu
                    except:
                        uuuuud = 0


                    uuuud = len(data[(data["state"] == str(k[0])) & (data["state"].shift(-1)==str(k[1])) & (data["state"].shift(-2)==str(k[2])) & (data["state"].shift(-3)==str(k[3]))  & (data["state"].shift(-4)==str(k[4]))  ])
                    uuuu = len(data[(data["state"] == "1") & (data["state"].shift(1)=="1") & (data["state"].shift(2)=="1") & (data["state"].shift(3)=="1") & (data["state"].shift(4)=="1")])
                    try:
                        uuuud = uuuud/uuuu
                    except:
                        uuuud = 0

                    s = ''.join(str(x) for x in k)
                    temp = [thefileswillbe,s,dddddu,ddddu,uuuuud,uuuud]
                    regression.append(temp)
                elif p==-1:
##                    k = np.random.choice([0, 1], size=(5,), p=[1./3, 2./3])
##                    s = ''.join(str(x) for x in k)
                    s = bin(i)[2:].zfill(bitfill)
                    k = list(s)
                    print("Pattern Regression is %s"%s)
                    dddddu = len(data[(data["state"] == str(k[0])) & (data["state"].shift(-1)==str(k[1])) & (data["state"].shift(-2)==str(k[2])) & (data["state"].shift(-3)==str(k[3])) & (data["state"].shift(-4)==str(k[4]))])
                    ddddd = len(data[(data["state"] == "0") & (data["state"].shift(1)=="0") & (data["state"].shift(2)=="0") & (data["state"].shift(3)=="0") & (data["state"].shift(4)=="0")])
                    try:
                        dddddu = dddddu/ddddd
                    except:
                        dddddu = 0


                    ddddu = len(data[(data["state"] == str(k[0])) & (data["state"].shift(-1)==str(k[1])) & (data["state"].shift(-2)==str(k[2])) & (data["state"].shift(-3)==str(k[3]))])
                    dddd = len(data[(data["state"] == "0") & (data["state"].shift(1)=="0") & (data["state"].shift(2)=="0") & (data["state"].shift(3)=="0")])
                    try:
                        ddddu = ddddu/dddd
                    except:
                        ddddu = 0


                    uuuuud = len(data[(data["state"] == str(k[0])) & (data["state"].shift(-1)==str(k[1])) & (data["state"].shift(-2)==str(k[2])) & (data["state"].shift(-3)==str(k[3]))  & (data["state"].shift(-4)==str(k[4]))  ])
                    uuuuu = len(data[(data["state"] == "1") & (data["state"].shift(1)=="1") & (data["state"].shift(2)=="1") & (data["state"].shift(3)=="1") & (data["state"].shift(4)=="1")])
                    try:
                        uuuuud = uuuuud/uuuuu
                    except:
                        uuuuud = 0


                    uuuud = len(data[(data["state"] == str(k[0])) & (data["state"].shift(-1)==str(k[1])) & (data["state"].shift(-2)==str(k[2])) & (data["state"].shift(-3)==str(k[3]))])
                    uuuu = len(data[(data["state"] == "1") & (data["state"].shift(1)=="1") & (data["state"].shift(2)=="1") & (data["state"].shift(3)=="1")])
                    try:
                        uuuud = uuuud/uuuu
                    except:
                        uuuud = 0

                    s = ''.join(str(x) for x in k)
                    temp = [thefileswillbe,s,dddddu,ddddu,uuuuud,uuuud]
                    regression.append(temp)
                elif p==-2:
##                    k = np.random.choice([0, 1], size=(4,), p=[1./3, 2./3])
##                    s = ''.join(str(x) for x in k)
                    s = bin(i)[2:].zfill(bitfill)
                    k = list(s)
                    print("Pattern Regression is %s"%s)
                    dddddu = len(data[(data["state"] == str(k[0])) & (data["state"].shift(-1)==str(k[1])) & (data["state"].shift(-2)==str(k[2])) & (data["state"].shift(-3)==str(k[3]))])
                    ddddd = len(data[(data["state"] == "0") & (data["state"].shift(1)=="0") & (data["state"].shift(2)=="0") & (data["state"].shift(3)=="0")])
                    try:
                        dddddu = dddddu/ddddd
                    except:
                        dddddu = 0


                    ddddu = len(data[(data["state"] == str(k[0])) & (data["state"].shift(-1)==str(k[1])) & (data["state"].shift(-2)==str(k[2]))])
                    dddd = len(data[(data["state"] == "0") & (data["state"].shift(1)=="0") & (data["state"].shift(2)=="0")])
                    try:
                        ddddu = ddddu/dddd
                    except:
                        ddddu = 0


                    uuuuud = len(data[(data["state"] == str(k[0])) & (data["state"].shift(-1)==str(k[1])) & (data["state"].shift(-2)==str(k[2])) & (data["state"].shift(-3)==str(k[3]))])
                    uuuuu = len(data[(data["state"] == "1") & (data["state"].shift(1)=="1") & (data["state"].shift(2)=="1") & (data["state"].shift(3)=="1")])
                    try:
                        uuuuud = uuuuud/uuuuu
                    except:
                        uuuuud = 0


                    uuuud = len(data[(data["state"] == str(k[0])) & (data["state"].shift(-1)==str(k[1])) & (data["state"].shift(-2)==str(k[2]))])
                    uuuu = len(data[(data["state"] == "1") & (data["state"].shift(1)=="1") & (data["state"].shift(2)=="1") ])
                    try:
                        uuuud = uuuud/uuuu
                    except:
                        uuuud = 0


                    temp = [thefileswillbe,s,dddddu,ddddu,uuuuud,uuuud]
                    regression.append(temp)
            #print(regression)
            whichone = {0:"dddddu",1:"ddddu",2:"uuuuud",3:"uuuud"}

            regrreseditfurther = []
            for j in range(len(regression)):
                combinethepattern = []
                timeframe = regression[j][0]
                pattern = regression[j][1]
                patternprobability  = regression[j][2:len(regression[j])]
                whatthemax = np.max(patternprobability)
                np_array = np.array(patternprobability)
                itemindex = np.where(np_array==whatthemax)
                combinethepattern.append(timeframe)
                combinethepattern.append(pattern)
                combinethepattern.append(whatthemax)
                for i in range(len(itemindex[0])):
                    combinethepattern.append(whichone[itemindex[0][i]])
                regrreseditfurther.append(combinethepattern)
            #print(regrreseditfurther)

##            print(corepath+"\PatternRegression.csv")
##            np.savetxt(corepath+"\PatternRegression.csv",
##                regrreseditfurther,
##                delimiter =", ",
##                fmt ='% s')

            selectivepattern = []
            whichtimeframe = []
            uptrenddetection = []
            for i in range(len(regrreseditfurther)):
                if regrreseditfurther[i][2] >=0.6:
                    if regrreseditfurther[i][3] == "uuuuud" or regrreseditfurther[i][3] == "uuuud":
                        print("We detect stored it somewhere...")
                        selectivepattern.append(regrreseditfurther[i][1])
                        uptrenddetection.append(regrreseditfurther[i][3])
                        gettimeframe = regrreseditfurther[i][0]
                        gettimeframe = gettimeframe.split("\\")
                        gettimeframe = gettimeframe[-1].split(".")
                        whichtimeframe.append(gettimeframe[0])

        #Checked Cond is here
            print(selectivepattern,whichtimeframe)
            if len(selectivepattern) > 0:
                print("We managed to find a pattern..Break Loop and perform any pattern detected...")
                nextanalysis = 1
                break
            else:
                print("No pattern detected...")
        if nextanalysis == 1:
            break
    print("LAST P is %i" %p)

    Inferences_Timeframe = list(set(whichtimeframe))
    Inferencespath = corepath+"/Inferences/"
    current = glob.glob(Inferencespath+"*.csv")
    timeframe = 8
    timeframeend = 24
    detectionflag = 0
    thesummary = [[-1,-1,-1,-1]]
    if nextanalysis == 1:
        for t in Inferences_Timeframe:
            thefileswillbe = Inferencespath + t +".csv"
            selectfiles = pd.read_csv(thefileswillbe)
            print("Checking for %ih pattern"%timeframeend)
            print(thefileswillbe)
            datao = pd.read_csv(thefileswillbe)
            datao["daily_return"] = datao["Close"].pct_change()
            datao["state"] = np.where(datao["daily_return"] >= 0, "1","0")
            for h in range(timeframe,timeframeend+1):
                print("Checking the pattern within %ih..." %h)
                data = datao.iloc[0:h]
    ##            print(data)
                isanypatterndetect = []
                for j in range(len(selectivepattern)):
                    k = list(selectivepattern[j])
                    if uptrenddetection[j] == "uuuuud":
                        if p ==2:
                            uuuuud = len(data[(data["state"] == str(k[0])) & (data["state"].shift(-1)==str(k[1])) & (data["state"].shift(-2)==str(k[2])) & (data["state"].shift(-3)==str(k[3])) & (data["state"].shift(-4)==str(k[4])) & (data["state"].shift(-5)==str(k[5])) & (data["state"].shift(-6)==str(k[6]))])
                            isanypatterndetect.append(uuuuud)
                        elif p ==1:
                            uuuuud = len(data[(data["state"] == str(k[0])) & (data["state"].shift(-1)==str(k[1])) & (data["state"].shift(-2)==str(k[2])) & (data["state"].shift(-3)==str(k[3])) & (data["state"].shift(-4)==str(k[4])) & (data["state"].shift(-5)==str(k[5]))])
                            isanypatterndetect.append(uuuuud)
                        elif p ==-1:
                            uuuuud = len(data[(data["state"] == str(k[0])) & (data["state"].shift(-1)==str(k[1])) & (data["state"].shift(-2)==str(k[2])) & (data["state"].shift(-3)==str(k[3]))  & (data["state"].shift(-4)==str(k[4]))  ])
                            isanypatterndetect.append(uuuuud)
                        elif p ==-2:
                            uuuuud = len(data[(data["state"] == str(k[0])) & (data["state"].shift(-1)==str(k[1])) & (data["state"].shift(-2)==str(k[2])) & (data["state"].shift(-3)==str(k[3]))])
                            isanypatterndetect.append(uuuuud)
                    elif uptrenddetection[j] == "uuuud":
                        if p ==2:
                            uuuud = len(data[(data["state"] == str(k[0])) & (data["state"].shift(-1)==str(k[1])) & (data["state"].shift(-2)==str(k[2])) & (data["state"].shift(-3)==str(k[3]))  & (data["state"].shift(-4)==str(k[4])) & (data["state"].shift(-5)==str(k[5])) ])
                            isanypatterndetect.append(uuuud)
                        elif p ==1:
                            uuuud = len(data[(data["state"] == str(k[0])) & (data["state"].shift(-1)==str(k[1])) & (data["state"].shift(-2)==str(k[2])) & (data["state"].shift(-3)==str(k[3]))  & (data["state"].shift(-4)==str(k[4]))  ])
                            isanypatterndetect.append(uuuud)
                        elif p ==-1:
                            uuuud = len(data[(data["state"] == str(k[0])) & (data["state"].shift(-1)==str(k[1])) & (data["state"].shift(-2)==str(k[2])) & (data["state"].shift(-3)==str(k[3]))])
                            isanypatterndetect.append(uuuud)
                        elif p ==-2:
                            uuuud = len(data[(data["state"] == str(k[0])) & (data["state"].shift(-1)==str(k[1])) & (data["state"].shift(-2)==str(k[2]))])
                            isanypatterndetect.append(uuuud)
                print(isanypatterndetect)
                if 1 in isanypatterndetect:
                    print("We detect uptrend pattern within %ih..." %h)
                    detectionflag = 1
                    break
                else:
                    print("No uptrend pattern detected...")
                    detectionflag = 0
        thesummary = [[detectionflag,p,selectivepattern[j],h]]
        print(thesummary)
    print(corepath+"\PatternRegression.csv")
    np.savetxt(corepath+"\PatternRegression.csv",
        thesummary,
        delimiter =", ",
        fmt ='% s')


main()





