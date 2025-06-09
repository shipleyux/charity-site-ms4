from django.shortcuts import render, redirect
from .forms import DonationForm
from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'core/post_list.html'
    context_object_name = 'posts'

def donate(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donation_thanks')
    else:
        form = DonationForm()
    return render(request, 'core/donate.html', {'form': form})
