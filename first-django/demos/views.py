from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.core.handlers.wsgi import WSGIRequest

# Create your views here.
def calculator(request) :
    #return HttpResponse('계산기 기능 구현 시작입니다. ')

    # 관련해서 공식문서에서 보기 
    print(f"reuqest = {request}") # request 출력도 가능하다. 
    print(f"request type = {type(request)}")
    print(f"request.__dict__ = {request.__dict__}") # 사용가능한 속성들을 볼 수 있음   
    # 데이터 확인
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    operator = request.GET.get('operator')

    # 계산 
    if operator == '+' :
        result = int(num1) + int(num2)
    elif operator == '-' :
        result = int(num1) - int(num2)
    elif operator == '*' :
        result = int(num1) * int(num2)  
    elif operator == '/' :
        result = int(num1) / int(num2)
    else :
        result = 0

    # 응답
    return render(request, 'calculator.html', {'result' : result}) # html에 result값을 'result'라는 변수명으로 사용할 수 있도록 넘겨준다. 