from django.urls import path

from .views import accueil

urlpatterns = [
    path('', accueil, name='accueil'),
    # path('formations/', formations, name='formations'),
    # path('formation/detail/<str:pk>', detail, name='detail'),
    # path('payment/<str:pk>', payment_route, name='payment_route'),
    # path('goto_url/<str:pk>', goto_url, name='goto_url'),
    # path('submit-feedback/', submit_feedback, name='submit_feedback'),
]
# handler404 = 'pages.views.page_not_found'
# handler500 = 'pages.views.server_error'