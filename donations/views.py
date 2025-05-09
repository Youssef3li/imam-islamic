from django.shortcuts import render, redirect
from .forms import DonationForm

def donate_view(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donation_success')
    else:
        form = DonationForm()
    return render(request, 'donations/donate.html', {'form': form})

def success_view(request):
    return render(request, 'donations/success.html')
