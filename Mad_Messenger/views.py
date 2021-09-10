from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def personal_account_details(request, username):
    if request.user.username == username:
        return render(request, 'chat/user_profile_edit.html')
    return render(request, 'chat/user_profile.html')
