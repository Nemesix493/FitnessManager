from django.contrib.auth import views as auth_views

login = auth_views.LoginView.as_view(
    template_name='authentication/login.html',
    extra_context={
        'title': 'Login'
    },
    redirect_authenticated_user=True
)

logout = auth_views.LogoutView.as_view()
