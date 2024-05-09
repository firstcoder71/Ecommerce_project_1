from django.urls import path
from Shop import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . forms import LoginForm,MyPasswordChangeForm,MyPasswordResetForm,MySetPasswordForm

urlpatterns = [
   path('', views.base,name='base'),
   path('home/', views.ProductView.as_view(), name='home'),
   path('all/', views.AllProductView.as_view(), name='alls'),
   path('drese/', views.DresesProductView.as_view(), name='dreses'),
   path('bag/', views.BagProductView.as_view(), name='bag'),
   path('shoes/', views.ShoesProductView.as_view(), name='shoes'),
   path('accesories/', views.AccesoriesProductView.as_view(), name='accesories'),

   path('all-products/', views.AallProductView.as_view(), name='allpro'),

   path('winter-collect/', views.WinterProduct, name='winter'),
   path('winter-collect/<slug:data>', views.WinterProduct, name='winteritem'),


   #path('accesories/', views.Best_SellingProductView.as_view(), name='bestselling'),
   path('registration/', views.CustormerRegistrationView.as_view(), name='customerregistration'),
   path('accounts/login/', auth_views.LoginView.as_view(template_name='Shop/login.html', authentication_form=LoginForm), name = 'login'),
   path('logout/', auth_views.LogoutView.as_view(next_page='login'),name='logout'),

   path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name = 'Shop/passwordchange.html', form_class=MyPasswordChangeForm, success_url = '/passwordchangedone/'), name='passwordchange'),
   path('passwordchangedone/', auth_views.PasswordChangeView.as_view(template_name='Shop/passwordchangedone.html'), name='passwordchangedone'),


   path('password-reset/', auth_views.PasswordResetView.as_view(template_name='Shop/reset_password.html', form_class = MyPasswordResetForm), name='password_reset'),

   path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='Shop/password_reset_done.html'), name='password_reset_done'),


   path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='Shop/password_reset_confirm.html', form_class = MySetPasswordForm), name='password_reset_confirm'),


   path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='Shop/password_reset_complete.html'), name='password_reset_complete'),



   path('shopcard/', views.shop_card,name='shopcard'),
   path('productpage/<int:pk>', views.product_page.as_view(),name='productpage'),

   path('contact/', views.ContactView.as_view(),name='contact'),
   path('categories/', views.AallCategoryView.as_view(),name='categories'),
   path('profile/', views.ProfileView.as_view(),name='profile'),
   path('checkout/', views.check_out,name='checkout'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)