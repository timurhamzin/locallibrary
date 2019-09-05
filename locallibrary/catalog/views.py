from django.shortcuts import render

# Create your views here.

from catalog.models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()
    num_authors_j = Author.objects.filter(first_name__contains='J').count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic


class BookListView(generic.ListView):
    model = Book
    paginate_by = 1
    # context_object_name = 'my_book_list'   # your own name for the list as a template variable
    # queryset = Book.objects.all()[:5] # Get 5 books containing the title war
    # template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 1
    # context_object_name = 'my_book_list'   # your own name for the list as a template variable
    # queryset = Book.objects.all()[:5] # Get 5 books containing the title war
    # template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location


class AuthorDetailView(generic.DetailView):
    model = Author

    def get_context_data(self, **kwargs):
        obj = kwargs['object']
        context = super(AuthorDetailView, self).get_context_data(**kwargs)
        context.update({'next': Author.objects.filter(id__gt=obj.id).order_by('id').first()})
        return context
