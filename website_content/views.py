from django.shortcuts import render, redirect


# Create your views here.
def home_view(request):
    context = {}
    if not request.user.is_authenticated:
        return redirect('user_account:login_first')
    return render(request, 'website_content/home_page.html', context)
