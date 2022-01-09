from django.urls import path
from .views import CompanyViewSet, RoomViewSet, TimeViewSet, ReservationViewSet


urlpatterns = [
    path('room/company', CompanyViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('room/room', RoomViewSet.as_view({
        'get': 'list',
    })),
    path('room/roomName/<str:pkname>', RoomViewSet.as_view({
        'get': 'listroomId',
    })),
    path('room/roomId/<str:pk>', RoomViewSet.as_view({
        'get': 'listroomName',
    })),
    path('room/time', TimeViewSet.as_view({
        'get': 'list',
    })),
    path('room/inquire', ReservationViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('room/inquire/<str:pk>', ReservationViewSet.as_view({
        'get': 'listR',
        'put': 'update',
        'delete': 'destroy'
    })),
]