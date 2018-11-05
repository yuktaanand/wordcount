from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,'home.html')
    
def count(request):
    text=request.GET['text'] 

    cout=text.split()

    worddict={}

    for word in cout:
        if word in worddict:
            worddict[word]+=1
        else:
            worddict[word]=1
   

    return render(request,'count.html',{'text': text,'cout':len(cout),'worddict':worddict.items()})    
    
