from django.shortcuts import render, redirect, reverse
from django.contrib import messages


# Create your views here.
from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51QMVDMDywWjYZSgWhP1djobcVRd5fzwhj0b3sod3nKW7vISZDKGwKyWgYM63OEuIl8Tw4kd25HKiNrAkdh0Aj8de00RPtXCqRH',
        'client_secret': 'test client secret',
    }
    
    return render(request, template, context)