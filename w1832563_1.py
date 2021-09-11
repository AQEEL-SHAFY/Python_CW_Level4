
# Prompt user to enter marks
passMarks=int(input("Enter pass marks : "))
deferMarks=int(input("Enter defer marks: "))
failMarks=int(input("Enter fail marks: "))


# Conditions for different marks
if passMarks==120 and deferMarks+failMarks==0:
    print("Progress")

elif passMarks==100 and deferMarks+failMarks==20:
    print("Progress(Module Trailer)")
        
elif passMarks==80 and deferMarks+failMarks==40 or passMarks==60 and deferMarks+failMarks==60:
    print("Do not progress-module retriever")
    
        
elif passMarks==40 and deferMarks+failMarks==80:
    if deferMarks==0 and failMarks==80:
        print("Exclude")
    else:
        print("Do not progress-module retriever")

         
elif passMarks==20 and deferMarks+failMarks==100:  
    if deferMarks==20 and failMarks==80 or deferMarks==0 and failMarks==100:
        print("Exclude")
    else:
        print("Do not progress-module retriever")    

       
elif passMarks==0 and deferMarks+failMarks==120:  
   if deferMarks==40 and failMarks==80 or deferMarks==20 and failMarks==100 or deferMarks==0 and failMarks==120:
        print("Exclude")
   else:
        print("Do not progress-module retriever")      
   
    


  
