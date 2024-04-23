from django.shortcuts import render,redirect, reverse 
from library.models import Library 
from library.models import Category
from django.http import HttpResponse
from .decorators import superuser_required
from library.forms import CategoryForm , CategoryModelForm 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.models import CustomUser
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SearchForm
from django.utils import timezone
from .models import BorrowingModel

# Create your views here.



def all_users(request):
    users = CustomUser.objects.all()  # Query your custom user model
    return render(request, 'homecategory.html', {'users': users})



def index(request):
   
    library = Library.get_all_products()
    return render(request, 'home.html', context={"library":library})

def index2(request):
    
    library = Library.get_all_products()
    return render(request, 'home2.html', context={"library":library})


def show(request, library_id):
    library = Library.get_specific_products(library_id)
    return render(request, 'show.html', context={"library":library})


@superuser_required
def delete(request, library_id):
    library = Library.objects.get(id=library_id)

    if request.method == 'POST':
        library.delete()
        bact_to_url = reverse('library.home')
        return redirect(bact_to_url)
    
    return render(request,'delete.html',{'library': library})
    
    



@superuser_required
def create(request):
    print(request)
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        if 'image' in request.FILES:
            image = request.FILES['image']
        else:
            image = None
        
        category= None
        if 'category_id' in request.POST:
            category = Category.get_specific_category(request.POST['category_id'])
        library =Library(name=request.POST['name'], image=image, no_of_item=request.POST['no_of_item'])
        library.save()

      
        bact_to_url = reverse('library.home')
        return redirect(bact_to_url)
    
    category = Category.get_all_category()
    return render(request, 'create.html', context={"category":category})



@superuser_required
def edit(request , library_id):
    library = Library.get_specific_products(library_id)
    
    print(request)
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        if 'image' in request.FILES:
            image = request.FILES['image']
        else:
            image = None
        
       
        library = Library.objects.get(id=library_id)
        library.name = request.POST['name']
        library.price = request.POST['price']
        library.image = image
        library.no_of_item = request.POST['no_of_item']
        library.save()
        
        back_to_url = reverse('library.home')
        return redirect(back_to_url)
    
  
    return render(request, 'edit.html', context={"library": library})



################################################################



    
def indexcategory(request):
    
    category = Category.get_all_category()
    return render(request, 'homecategory.html', context={"category":category})




@superuser_required
def createcategory(request):
    print(request)
    if request.method == 'POST':
        request_data = request.POST
        name = request_data['name']
        description = request_data['description']
        category = Category(name=name, description=description)
        category.save()

       
        bact_to_url = reverse('library.homecategory')
        return redirect(bact_to_url)
    return render(request, 'createcategory.html')


##############################   Students  ######################################


@superuser_required
def createViaForm(request):
    form  = CategoryForm()
    
    if request.method == 'POST':
        print(request.POST)
        form = CategoryForm(request.POST)
        if form.is_valid():
                category =Category(name=request.POST['name'], description=request.POST['description'])

                category.save()
                url = reverse('library.homecategory')
                return redirect(url)

        print(form.errors)
        return render(request, 'createcategory.html', context={"form":form})

    return render(request, 'createcategory.html', context={"form":form})



@superuser_required
def createViaModelForm(request):
    form  = CategoryModelForm()
    if request.method == 'POST':
        form  = CategoryModelForm( request.POST)
        if form.is_valid():
           
            form.save() 
            url = reverse('library.homecategory')
            return redirect(url)

        return render(request, 'createcategory.html', context={"form": form})


    return render(request, 'createcategory.html', context={"form":form})




#####################################  Profile   #####################################


@login_required
def profile_view(request):
    user_borrowings = BorrowingModel.objects.filter(user_name=request.user.username)
    context = {
        'user_borrowings': user_borrowings,
    }
    return render(request, 'profile.html', context)

#####################################  Change Password Profile   #####################################

class MyPasswordChangeView(PasswordChangeView):
    template_name = 'password_change_form.html'
    success_url = reverse_lazy('library.profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
    
    #####################################  Delete Profile    #####################################

@login_required
def delete_account_confirmation(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('library.home')  
    return render(request, 'accounts/delete_account_confirmation.html')


    #####################################  Search Profile    #####################################


def search_results(request):
    if 'id' in request.GET:
        user_id = request.GET['id']
        try:
            user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            user = None

        return render(request, 'search_results.html', {'user': user})

    return render(request, 'search_results.html')


    #####################################  Borrow Books    #####################################

@login_required
def borrow_confirmation(request, library_id):
    library = Library.objects.get(id=library_id)
    
    if request.method == 'POST':
        borrowed_item = BorrowingModel(
            user_name=request.user.username,
            book_name=library.name,
        )
        borrowed_item.save()
        return redirect('library.home2')  
    
    return render(request, 'confirm_borrow.html', {'user': request.user, 'library': library})



def all_borrowings(request):
    borrowings = BorrowingModel.objects.all()
    return render(request, 'all_borrowings.html', {'borrowings': borrowings})