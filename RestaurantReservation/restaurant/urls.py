from django.urls import path
from .views import RestaurantViewSet, ChainViewSet, TimeViewSet, ReservationViewSet


urlpatterns = [
    path('restaurant/restaurant', RestaurantViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('restaurant/chain', ChainViewSet.as_view({
        'get': 'list',
    })),
    path('restaurant/chainName/<str:pkname>', ChainViewSet.as_view({
        'get': 'listchainId',
    })),
    path('restaurant/chainId/<str:pk>', ChainViewSet.as_view({
        'get': 'listchainName',
    })),
    path('restaurant/time', TimeViewSet.as_view({
        'get': 'list',
    })),
    path('restaurant/inquire', ReservationViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('restaurant/inquire/<str:pk>', ReservationViewSet.as_view({
        'get': 'listR',
        'put': 'update',
        'delete': 'destroy'
    })),
]