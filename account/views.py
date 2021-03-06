from .models import AccountModel
from django.contrib.auth.decorators import login_required
from start_site.models import MainUser
from tgbot.models import User
from .forms import AccountForm
from django.shortcuts import render, redirect
from django.db.models import Sum


@login_required(login_url='/accounts/login')
def account_view(request):
    #Update user profile
    template_name = 'account_page.html'
    user = MainUser.objects.get(pk=request.user.pk)

    try:
        user_tg = User.objects.get(user_id=user.user_tg_id)
    except:
        return redirect(to='/account/id-not-found')
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            project_name = form.cleaned_data.get('project_name')
            if project_name: account_query = AccountModel.objects.filter(user=user_tg, project_name=project_name)
            else: account_query = AccountModel.objects.filter(user=user_tg)
    else:
        form = AccountForm()
        account_query = AccountModel.objects.filter(user=user_tg)

    total_value = account_query.aggregate(Sum('sum_value'))
    return render(request, template_name, {'form': form, 'query': account_query, 'total': total_value})

def tlgrm_id_nfound(request):
    picture = AccountModel.objects.latest('created_at')
    print(picture)
    return render(request, 'not_found.html', {'picture': picture})