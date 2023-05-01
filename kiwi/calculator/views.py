from django.shortcuts import render

# Create your views here.

def index(request):
    answer=''
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr=request.POST.get('opr')
            if opr=='+':
                answer=n1+n2;
            elif opr=='-':
                answer=n1-n2;
            elif opr=='*':
                answer=n1*n2;
            elif opr=='/':
                answer=n1/n2;
    except:
        answer='Error'
    print(answer)

    return render(request, 'calculator/index.html', {'answer':answer})
