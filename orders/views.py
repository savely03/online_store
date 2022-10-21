from django.shortcuts import render
from .forms import OrderForm
from cart.cart import Cart
from .models import OrderItem


# Create your views here.


def order_create(request):
    form = OrderForm()
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity'],
                )
            cart.clear()
            return render(request, 'orders/created.html', context={'order': order})
    return render(request, 'orders/create.html', context={'form': form, 'cart': cart})
