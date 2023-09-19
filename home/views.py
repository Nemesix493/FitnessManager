from django.shortcuts import render

# Create your views here.


def homepage(request, *args, **kwargs):
    context = {
        'title': 'Home',
        'is_connected': 'You are not connected !',
        'nav_list': [
            {
                'name': 'login',
                'link': '/auth/login/'
            }
        ],
    }
    if request.user.is_authenticated:
        context['is_connected'] = 'You are connected !'
        context['nav_list'] = [
            {
                'name': 'logout',
                'link': '/auth/logout/'
            }
        ]
    return render(request, 'home/homepage.html', context)
