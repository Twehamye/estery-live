from django.urls import path
from .import views
from django.contrib.auth import views as auth_view

urlpatterns = [

   path("home/", views.home, name='home'),
   path("", views.index, name='index'),
   path("index_admin/", views.index_admin, name='index_admin'),

   path('about/', views.about, name='about'),
   path('product/', views.product, name='product'),
   path('contact/', views.contact, name='contact'),

   path('login/', views.loginPage, name="login"),
   path('logout/', views.logoutUser, name="logout"),
    
   path('create_employee/', views.createEmployee, name="create_employee"),
   path('update_employee/<str:emp_id>/', views.updateEmployee, name='update_employee'),
   path('delete_employee/<str:emp_id>/', views.deleteEmployee, name='delete_employee'),

   path('create_sale/', views.create_sale, name='create_sale'),
   path('update_sale/<int:id>/', views.updateSale, name='update_sale'),
   path('delete_sale/<int:id>/', views.deleteSale, name='delete_sale'),

   path('create_expense/', views.createExpense, name='create_expense'),
   path('update_expense/<int:id>/', views.updateExpense, name='update_expense'),
   path('delete_expense/<int:id>/', views.deleteExpense, name='delete_expense'),

   path('create_purchase/', views.createPurchase, name='create_purchase'),
   path('update_purchase/<int:id>/', views.updatePurchase, name='update_purchase'),
   path('delete_purchase/<int:id>/', views.deletePurchase, name='delete_purchase'),

        
   path('employee/<str:emp_id>/', views.employee, name='employee'),

   path('all_sale/', views.allSale, name='all_sale'),
   path('all_expense/', views.allExpense, name='all_expense'),
   path('all_purchase/', views.allPurchase, name='all_purchase'),
   path('all_employee/', views.allEmployee, name='all_employee'),

   path('add_product/', views.add_product, name='add_product'),
   path('daily_report/', views.daily_report, name='daily_report'),

   #    path('deposit_csv/', views.deposit_csv, name='deposit_csv'),
   #    path('relative_csv/', views.relative_csv, name='relative_csv'),
   #    path('member_txt/', views.member_txt, name='member_txt'),   

   path('sales/', views.sales_view, name='sales'),
   path('all_sales/', views.SalesListView.as_view(), name='all_sales'),
   path('total_sales/', views.total_sales, name='total_sales'),

   path('image_upload/', views.image_upload_view, name='image_upload'),
   path('stock_upload/', views.stock_upload, name='stock_upload'),
   path('images/', views.ImageListView.as_view(), name='image_list'),
   path('stock/', views.StockListView.as_view(), name='stock_list'),   
   path('edit_image/<pk>/', views.edit_image, name='edit_image'),
   path('delete_image/<pk>/', views.delete_image, name='delete_image'),


]