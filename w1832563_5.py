passList=[120,100,100,80,60,40,20,20,20,0]
deferList=[0,20,0,20,40,40,40,20,0,0]
failList=[0,0,20,20,20,40,60,80,100,120]



progressCounter=0
trailerCounter=0
retrieverCounter=0
excludeCounter=0
totalCounter=0

def vertical_histogram():
    
    print("\nVertical Histogram")
    print("Progress   Trailing   Retriever   Excluded")
        
    global progressCounter
    global trailerCounter
    global retrieverCounter
    global excludeCounter
    rangeCounter=max(progressCounter,trailerCounter,retrieverCounter,excludeCounter)
    for i in range(rangeCounter):
        if progressCounter>0:
            print("    *",end="")
            progressCounter-=1
                 
        else:
            print("     ",end="")
        if trailerCounter>0:
            print("         *  ",end="")
            trailerCounter-=1
                 
        else:
            print("            ",end="")
        if retrieverCounter>0:
            print("       *     ",end="")
            retrieverCounter-=1
               
        else:
            print("             ",end="")
        if excludeCounter>0:
            print("      *     ",end="")
            excludeCounter-=1
                
        else:
            print("            ",end="")

        print("")

def histogram():
    print("\nHorizontal Histogram")
    print("Progress ",progressCounter," = "," * "*progressCounter)
    print("Trailer ",trailerCounter," = "," * "*trailerCounter)
    print("Retriever ",retrieverCounter," = "," * "*retrieverCounter)
    print("Exclude ",excludeCounter," = "," * "*excludeCounter)
    print(totalCounter," outcomes in total")
    vertical_histogram()



for i in range(10):
    print("Student",i+1)
    print("Pass mark:",passList[i],"Defer mark:",deferList[i],"Fail mark:",failList[i])
    passMarks=passList[i]
    deferMarks=deferList[i]
    failMarks=failList[i]
    if passMarks==120 and deferMarks+failMarks==0:
        print("Progress")
        progressCounter+=1

    elif passMarks==100 and deferMarks+failMarks==20:
        print("Progress(module trailer)")
        trailerCounter+=1

    elif passMarks==80 and deferMarks+failMarks==40:
        print("Do not progress-module retriver")
        retrieverCounter+=1
 
    elif passMarks==60 and deferMarks+failMarks==60:
        print("Do not progress-module retriver)")
        retrieverCounter+=1

    elif passMarks==40 and deferMarks+failMarks==80:
        print("Do not progress-module retriver)")
        retrieverCounter+=1

    elif passMarks==20 and deferMarks+failMarks==100:

        if deferMarks==20 and failMarks==80 or deferMarks==0 and failMarks==100:
            print("Exclude")
            excludeCounter+=1
        else:    
            print("Do not progress-module retriver)")
            retrieverCounter+=1
        
    else:
        print("Exclude")
        excludeCounter+=1

histogram()
     

           
   
