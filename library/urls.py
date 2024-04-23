from django.urls import path
from . import views
from library.views import (show,delete,index,create,edit,createcategory,indexcategory , MyPasswordChangeView , delete_account_confirmation
                         ,createViaForm,createViaModelForm,index2,all_users , profile_view , borrow_confirmation , all_borrowings
                        , search_results)

urlpatterns = [
   
  
    # library _ Products
    path('<int:library_id>', show, name='library.show'),
    path('<int:library_id>/delete', delete, name='library.delete'),
    path('', index, name='library.home'),
     path('home2/', index2, name='library.home2'),
    path('create', create, name='library.create'),
    path('<int:library_id>/edit', edit, name='library.edit'),
    
    # Students
    path('createcategory', createcategory, name='library.createcategory'),
    path('homecategory', all_users, name='library.homecategory'),
   
    # Students Forms
    path('forms/create', createViaForm, name='library.createForm'),
    path('forms/model/create', createViaModelForm, name='library.createForm'),
   
    # Profile Settings
    path('profile/', views.profile_view, name='library.profile'),
    path('change_password/', views.MyPasswordChangeView.as_view(), name='library.password_change_form'),
    path('delete_account_confirmation/', views.delete_account_confirmation, name='library.delete_account_confirmation'),
    path('search_results/', views.search_results, name='library.search_results'),
    
    # Borrow Books 
    path('borrow_confirm/<int:library_id>/', views.borrow_confirmation, name='library.borrow_confirmation'),
    path('all_borrowings/', views.all_borrowings, name='library.all_borrowings'),
   


    
    
    
    

]
