from django.conf.urls import url,include
from v1.views import QuizesView,create_user,user_specificData
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here


urlpatterns = [
    url('quizes/', QuizesView.as_view()),
    url('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # <-- And here
    url('Register/', create_user),
        url('userSpecific/', user_specificData),



    

]