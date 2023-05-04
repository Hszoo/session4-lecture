"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from demos.views import calculator # demos의 뷰 파일에서 함수 가져왓 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculator/', calculator) # 첫번째 매개변수 url로 들어오면 두번째 함수를 실행시켜라 ** 함수는 import 받아서 사용 
    # url../calculator 요청 받으면, views의 calculator함수로 넘겨줌 , 그게 매개변수 request인 것 , 그러니까  url 처리는 뷰에서
]
