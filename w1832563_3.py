total=120

marksList=[0,20,40,60,80,100,120]


progressCounter=0
trailerCounter=0
retrieverCounter=0
excludeCounter=0
totalCounter=0



def histogram():
    print("\nHorizontal Histogram")
    print("Progress ",progressCounter," = "," * "*progressCounter)
    print("Trailer ",trailerCounter," = "," * "*trailerCounter)
    print("Retriever ",retrieverCounter," = "," * "*retrieverCounter)
    print("Exclude ",excludeCounter," = "," * "*excludeCounter)
    print(totalCounter," outcomes in total")

stop= input("Enter y to continue or q to quit : ")

if stop=="y":
    while True:
        try:
            passMarks=int(input("Enter pass marks : "))
            deferMarks=int(input("Enter defer marks: "))
            failMarks=int(input("Enter fail marks: "))


            if passMarks+deferMarks+failMarks==total:
                if passMarks in marksList and deferMarks in marksList and failMarks in marksList:
                    
                    if passMarks==120 and deferMarks+failMarks==0:
                        print("Progress\n")
                        progressCounter+=1
                        totalCounter+=1
                    
                    elif passMarks==100 and deferMarks+failMarks==20:
                        print("Progress(Module Trailer)\n")
                        trailerCounter+=1
                        totalCounter+=1
                    
                    elif passMarks==80 and deferMarks+failMarks==40 or passMarks==60 and deferMarks+failMarks==60:
                        print("Do not progress-module retriever\n")
                        retrieverCounter+=1
                        totalCounter+=1
                
                    
                    elif passMarks==40 and deferMarks+failMarks==80:
                         if deferMarks==0 and failMarks==80:
                            print("Exclude\n")
                            excludeCounter+=1
                            totalCounter+=1
                         else:
                            print("Do not progress-module retriever\n")
                            retrieverCounter+=1
                            totalCounter+=1

                     
                    elif passMarks==20 and deferMarks+failMarks==100:  
                         if deferMarks==20 and failMarks==80 or deferMarks==0 and failMarks==100:
                            print("Exclude\n")
                            excludeCounter+=1
                            totalCounter+=1
                         else:
                            print("Do not progress-module retriever\n")
                            retrieverCounter+=1
                            totalCounter+=1

                   
                    elif passMarks==0 and deferMarks+failMarks==120:  
                         if deferMarks==40 and failMarks==80 or deferMarks==20 and failMarks==100 or deferMarks==0 and failMarks==120:
                            print("Exclude\n")
                            excludeCounter+=1
                            totalCounter+=1
                         else:
                            print("Do not progress-module retriever\n")
                            retrieverCounter+=1
                            totalCounter+=1

                    stop=input("Enter y to continue or q to quit : ")
                    if stop=="q":
                        histogram()
                        break
                    elif stop=="y":
                        continue
                    else:
                        print("Wrong letter entered")
                        break

                            
                else:
                    print("Out of range\n")
            else:
                print("Incorrect Total\n")
            
        except:
            print("Integer required\n")

elif stop=="q":
    histogram()

else:
    print("Wrong letter entered")


           

