from django.shortcuts import render, redirect
from .forms import DonationForm
from django.views.generic import ListView
from .models import Post
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import UpdateView
from .models import ContactMessage
from django import forms
import stripe
from django.conf import settings



class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_thank_you')
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})

def contact_thank_you(request):
    return render(request, 'core/contact_thank_you.html')




def home_view(request):
    latest_posts = Post.objects.order_by('-created_on')[:3]
    return render(request, 'core/home.html', {
        'latest_posts': latest_posts
    })



class PostListView(ListView):
    model = Post
    template_name = 'core/post_list.html'
    context_object_name = 'posts'

def donate(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            amount = int(form.cleaned_data['amount'] * 100)  # convert pounds to pence

            stripe.api_key = settings.STRIPE_SECRET_KEY

            success_url = request.build_absolute_uri('/donation-thank-you')
            cancel_url = request.build_absolute_uri('/donate')

            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'gbp',
                        'product_data': {
                            'name': 'Donation',
                        },
                        'unit_amount': amount,
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url=success_url,
                cancel_url=cancel_url,
            )
            return redirect(session.url, code=303)
    else:
        form = DonationForm()
    
    return render(request, 'core/donate.html', {'form': form})

def donation_thank_you(request):
    return render(request, 'core/donation_thank_you.html')


class PostDetailView(DetailView):
    model = Post
    template_name = 'core/post_detail.html'
    context_object_name = 'post'

@method_decorator(login_required, name='dispatch')
class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['title', 'slug', 'content']
    template_name = 'core/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_staff

@method_decorator(login_required, name='dispatch')
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'slug', 'content']
    template_name = 'core/post_form.html'

    def get_success_url(self):
        return self.object.get_absolute_url()

    def test_func(self):
        return self.request.user == self.get_object().author


@method_decorator(login_required, name='dispatch')
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'core/post_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        return self.request.user == self.get_object().author


def types_of_abuse_view(request):
    return render(request, 'core/types_of_abuse.html')

def about_us(request):
    return render(request, 'core/about_us.html')