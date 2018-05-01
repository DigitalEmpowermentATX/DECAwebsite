from django.conf.urls import url
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from user_management import views
urlpatterns = [
    url(r'login/$', auth_views.LoginView.as_view(template_name='login.jinja2'), name='login'),
    url(r'logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'forgot_password/$', auth_views.PasswordResetView.as_view(
        template_name="forgot_password.jinja2", email_template_name='password_reset_email.html',
        subject_template_name='password_reset_subject.txt'), name="password_reset"),
    url(r'forgot_password/done/$', auth_views.PasswordResetDoneView.as_view(
        template_name="forgot_password_done.jinja2"), name="password_reset_done"),
    url(r'^forgot_password/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='forgot_password_confirm.jinja2', success_url=reverse_lazy("login")), name='password_reset_confirm'),
    url(r'register/$', views.register, name='register'),
]
