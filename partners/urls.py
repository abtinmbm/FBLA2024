from django.urls import path
from .views import partner_list, partner_proposal, partner_list_json, partner_terms

urlpatterns = [
    # URL pattern for rendering partner list page
    path('', partner_list, name='partner_list'),
    # URL pattern for retrieving partner list data in JSON format
    path('json/partner_list', partner_list_json, name='partner_list_json'),
    # URL pattern for handling partner proposal form submission
    path('partner', partner_proposal, name='partner_proposal'),
    # URL pattern for terms and conditions page
    path('terms', partner_terms, name='terms'),
]
