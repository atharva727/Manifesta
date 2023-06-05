from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

# Views
from django.views import View

# Models
from shop.models import CustomerProfile, Order, VendorProfile, Categories

# Forms
from shop.forms import CustomerSignupForm, VendorSignupForm, CustomerProfileForm, VendorProfileForm, CheckoutForm


# Create your views here.
class IndexView(View):
    def get(self, request):
        context = {'categories': Categories.objects.all()}
        return render(request, "index.html", context)


class VendorPageView(View):

    def get(self, request, id):
        cakeId = [1, 2, 3, 4, 12, 13]
        decoraterId = [5, 6, 7, 14]
        photo = [8, 9]
        if id in cakeId:
            context = {'vendor': VendorProfile.objects.get(id=id),

                       'recommend': [VendorProfile.objects.get(id=5), VendorProfile.objects.get(id=6),
                                     VendorProfile.objects.get(id=7)],
                       'categories': [Categories.objects.get(name='Decorators'), Categories.objects.get(name='Cakes')]
                       }
        elif id in decoraterId:
            context = {'vendor': VendorProfile.objects.get(id=id),

                       'categories': [Categories.objects.get(name='Decorators'), Categories.objects.get(name='Photographers')]
                       }
        else:
            context = {'vendor': VendorProfile.objects.get(id=id),

                       'categories': [Categories.objects.get(name='Photographers')]
                       }

        return render(request, "vendorPage.html", context)


class LoginView(View):

    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)

        # User Logged in
        if user is not None:
            login(request, user)
            path = request.GET.get('next')
            print('path= ', path)
            return HttpResponseRedirect(path)

        context = {'error': "Incorrect Email Address or Password"}
        return render(request, "login.html", context)

    def logout(request):
        if request.user.is_authenticated:
            logout(request)
            path = request.GET.get('next', '/')
            return redirect(path)
        return redirect("/")


class CustomerSignupView(View):

    def get(self, request):
        form = CustomerSignupForm()
        context = {'form': form}
        return render(request, "customerSignup.html", context)

    def post(self, request):
        form = CustomerSignupForm(request.POST)
        print(request.POST)

        if form.is_valid():
            user = form.save()
            CustomerProfile.objects.create(user=user, )
            login(request, user)
            return redirect("customerProfile")

        context = {'form': form}
        return render(request, "customerSignup.html", context)


class CustomerProfileView(View):

    def get(self, request):
        user = request.user.customerprofile
        form = CustomerProfileForm(instance=user)
        context = {'form': form, 'user': user}
        return render(request, "customerProfile.html", context)

    def post(self, request):
        user = request.user.customerprofile
        form = CustomerProfileForm(request.POST, request.FILES, instance=user)
        context = {}
        if form.is_valid():
            form.save()
            context = {'form': form, 'user': user}
        return render(request, "customerProfile.html", context)


class VendorSignupView(View):

    def get(self, request):
        form = VendorSignupForm()
        context = {'form': form}
        return render(request, "vendorSignup.html", context)

    def post(self, request):
        form = VendorSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            VendorProfile.objects.create(user=user, )
            login(request, user)
            return redirect("vendorProfile")

        context = {'form': form}
        return render(request, "vendorSignup.html", context)


class VendorProfileView(View):

    def get(self, request):
        vendor = request.user.vendorprofile
        form = VendorProfileForm(instance=vendor)
        context = {'form': form, 'user': vendor}
        return render(request, "vendorProfile.html", context)

    def post(self, request):
        vendor = request.user.vendorprofile
        form = VendorProfileForm(request.POST, request.FILES, instance=vendor)
        context = {}
        if form.is_valid():
            form.save()
            context = {'form': form, 'user': vendor}
        return render(request, "vendorProfile.html", context)


class AboutUsView(View):
    def get(self, request):
        return render(request, "aboutus.html")


# order
class checkoutView(View):
    def get(self, request, id):
        form = CheckoutForm()
        context = {"form": form, 'vendorid': id}
        return render(request, "checkout.html", context)

    def post(self, request, id):
        orderDeliveryTime = request.POST.get('orderDeliveryTime')
        message = request.POST.get('message')
        address = request.POST.get('address')
        pin_code = request.POST.get('pin_code')
        vendor = request.POST.get('vendor')
        vendor = VendorProfile.objects.get(id=vendor)
        user = request.user.customerprofile
        price = vendor.price
        orderid = Order.objects.create(user=user, vendor=vendor, price=price, orderDeliveryTime=orderDeliveryTime,
                                       message=message, address=address, pin_code=pin_code)
        return redirect("orders")


class ordersPageView(View):
    def get(self, request):
        orders = Order.objects.all()
        context={
            "orders":orders,
        }
        return render(request, "ordersPage.html",context)
