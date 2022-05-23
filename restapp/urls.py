from django.urls import path
from .views import AuthUserRegistrationView,ClientListStates,UserById, CameraCreate, CameraById, LogoutView, UserLoginView,ExitingCreate,EnteringCreate, UserList, ClientList, ServerList, CameraList, ClientDetail, ClientCreate, ClientById,EnteringList,ExitingList,ExitingById, EnteringById

urlpatterns = [

    path('register', AuthUserRegistrationView.as_view()),
    path('login', UserLoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('statistics/', ClientListStates.as_view()),

    path('user/list', UserList.as_view()),
    path('user/<int:pk>', UserById.as_view()),
    path('server/list', ServerList.as_view()),

    path('camera/list', CameraList.as_view()),
    path('camera/create', CameraCreate.as_view()),
    path('camera/<int:pk>', CameraById.as_view()),

    path('entering/list', EnteringList.as_view()),
    path('entering/create', EnteringCreate.as_view()),
    path('entering/<int:pk>', EnteringById.as_view()),

    path('exiting/list', ExitingList.as_view()),
    path('exiting/create', ExitingCreate.as_view()),
    path('exiting/<int:pk>', ExitingById.as_view()),


    path('client/list', ClientList.as_view()),
    path('client/create', ClientCreate.as_view()),
    path('client/<int:pk>/', ClientDetail.as_view()),
    path('client/<int:pk>', ClientById.as_view()),

    ]
