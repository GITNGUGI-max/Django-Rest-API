from django.shortcuts import render, get_object_or_404
from .models import Book, BookInstance, Author, Genre
from django.views import generic
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from catalog.forms import RenewBookForm
# Create your views here.
from django.contrib.auth.decorators import permission_required


@permission_required('catalog.can_mark_returned')
def renew_book_librarian(request, pk):
    	book_instance = get_object_or_404(BookInstance, pk=pk)

    	if request.method == 'POST':

    		form = RenewBookForm(request.POST)

    		if form.is_invalid():

    			book_instance.due_back = form.cleaned_data['renewal_date']
    			book_instance.save()

    			return HttpResponseRedirect(reverse('/'))

    		else:
    		

    			proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)	
    			form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})

    		context={
	    		'form':form,
	    		'book_instance':book_instance,
    		}	

    		return render(request, 'catalog/book_renew_librarian.html', context)


def index(request):

	num_books=Book.objects.all().count()
	num_instances=BookInstance.objects.all().count()
	num_instances_available=BookInstance.objects.filter(status__exact='a').count()

	num_authors=Author.objects.count()
	num_genre=Genre.objects.all().count()

	num_visits =request.session.get('num_visits', 0)
	request.session['num_visits']=num_visits+1


	context={
	'num_books':num_books,
	'num_instances':num_instances,
	'num_instances_available':num_instances_available,
	'num_authors':num_authors,
	'num_genre':num_genre,
	'num_visits':num_visits
	}
	return render(request, 'index.html', context=context)

from django.contrib.auth.mixins import LoginRequiredMixin

class BookListView(LoginRequiredMixin, generic.ListView):
	
	model=Book	

	context_object_name='book_list'
	queryset=Book.objects.filter(title__icontains="") [:50]
	template_name='books/book_list.html'
	paginate_by =13

class BookDetailView(generic.DetailView):
	
		model=Book	

		def book_detail_view(request, primary_key):
			book=get_object_or_404(Book, pk=primary_key)
			return render(request, 'catalog/book_detail.html', context={'book':book})
class AuthorListView(generic.ListView):
	model=Author	
	paginate_by =2			

class AuthorDetailView(generic.DetailView):
	 model = Author 

	 # def author_detail_view(request, primary_key):
	 # 	author=get_object_or_404(Author, pk=primary_key)
	 # 	return render(request, 'catalog/author_detail.html', context={'author':author})


from django.contrib.auth.mixins import LoginRequiredMixin

class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name ='catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10
    
    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from catalog.models import Author

class AuthorCreate(PermissionRequiredMixin, CreateView):
	model=Author
	fields = '__all__'
	initial ={'date of death': '05/01/2020'}

	permission_required='can_mark_returned'

class AuthorUpdate(PermissionRequiredMixin, UpdateView):
	model=Author
	fields=['first_name', 'last_name', 'date_of_birth', 'date_of_death']
	permission_required='can_mark_returned'

class AuthorDelete(PermissionRequiredMixin, DeleteView):
	model=Author
	success_url=reverse_lazy('authors')		
	permission_required='can_mark_returned'

class BookCreate(PermissionRequiredMixin, CreateView):
	model=Book
	fields = '__all__'
	initial ={'date of death': '05/01/2020'}
	permission_required='can_mark_returned'


class BookUpdate(PermissionRequiredMixin, UpdateView):
	model=Book
	fields='__all__'
	permission_required='can_mark_returned'

class BookDelete(PermissionRequiredMixin, DeleteView):
	model=Book
	success_url=reverse_lazy('books')	

	permission_required='can_mark_returned'
		


