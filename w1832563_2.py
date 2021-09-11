total=120
# Prompt 
marksList=[0,20,40,60,80,100,120]
while True:
   
    try: # Prompt user to enter marks
        passMarks=int(input("Enter pass marks : "))
        deferMarks=int(input("Enter defer marks: "))
        failMarks=int(input("Enter fail marks: "))


        if passMarks+deferMarks+failMarks==total:
            if passMarks in marksList and deferMarks in marksList and failMarks in marksList:
                
                if passMarks==120 and deferMarks+failMarks==0:
                    print("Progress\n")
                
                elif passMarks==100 and deferMarks+failMarks==20:
                    print("Progress(Module Trailer)\n") 
                
                elif passMarks==80 and deferMarks+failMarks==40 or passMarks==60 and deferMarks+failMarks==60:
                    print("Do not progress-module retriever\n")
            
                
                elif passMarks==40 and deferMarks+failMarks==80:
                     if deferMarks==0 and failMarks==80:
                        print("Exclude\n")
                     else:
                        print("Do not progress-module retriever\n")

                 
                elif passMarks==20 and deferMarks+failMarks==100:  
                     if deferMarks==20 and failMarks==80 or deferMarks==0 and failMarks==100:
                        print("Exclude\n")
                     else:
                        print("Do not progress-module retriever\n")    

               
                elif passMarks==0 and deferMarks+failMarks==120:  
                     if deferMarks==40 and failMarks==80 or deferMarks==20 and failMarks==100 or deferMarks==0 and failMarks==120:
                        print("Exclude\n")
                     else:
                        print("Do not progress-module retriever\n")      
            else:
                print("Out of range\n")
        else:
            print("Incorrect Total\n")
        
    except:
        print("Integer required\n")
       

