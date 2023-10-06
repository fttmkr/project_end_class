from datetime import date

from django.db.models import Avg, Max, Min
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from blog.models import karbaran, Product

# Create your views here.

all_posts = [
    {
        'slug': 'Python-Programming',
        'title': 'Python.py',
        'author': 'karimi',
        'image': 'img.png',
        'date': date(2019, 3, 3),
        'short_description': 'Python is a Programming Language',
        'content': """What is Python?
            Python is a computer programming language often used to build websites and software, automate tasks, and conduct data analysis. Python is a general-purpose language, meaning it can be used to create a variety of different programs and isn’t specialized for any specific problems. This versatility, along with its beginner-friendliness, has made it one of the most-used programming languages today.

            Stack Overflow's 2022 Developer Survey revealed that Python is the fourth most popular programming language, with respondents saying that they use Python almost 50 percent of the time in their development work. Survey results also showed that Python is tied with Rust as the most-wanted technology, with 18% percent of developers who aren't using it already saying that they are interested in learning Python 

        """
    },


    {
        'slug': 'CSharp',
        'title': 'C#',
        'author': 'karimi',
        'image': 'download.jpg',
        'date': date.today(),
        'short_description': 'CSharp is a Programming Language',
        'content': """What is C# and what is it used for?
         C# (pronounced "See Sharp") is a modern, object-oriented, and type-safe programming language. C# enables developers to build many types of secure and robust applications that run in .NET. C# has its roots in the C family of languages and will be immediately familiar to C, C++, Java, and JavaScript programmers.
     """
    },


    {
        'slug': 'django',
        'title': 'Django',
        'author': 'karimi',
        'image': 'photo6584545652.jpg',
        'date': date.today(),
        'short_description': 'Django is Web Design',
        'content': """What is Django?
        The Django web framework is a free, open source framework that can speed up development of a web application being built in the Python programming language. 
        Django—pronounced “Jango,” named after the famous jazz guitarist Django Reinhardt—is a free, open source framework that was first publicly released in 2005. Django facilitates “rapid development and clean, pragmatic design.” The Django web framework, deployed on a web server, can help developers quickly produce a web frontend that’s feature-rich, secure and scalable.
        Starting with the Django web framework is more efficient way to build a web app than starting from scratch, which requires building the backend, APIs, javascript and sitemaps. With the Django web framework, web developers can focus on creating a unique application and benefit from greater flexibility than using a web development tool.
        """
    },





]


def get_date(post):
    return post['date']

def index(request):

    # d=list(all_posts)
    # context={
    #     'a':d
    # }
    # return render(request, 'blogs/index.html',context)

    sorted_post=sorted(all_posts,key=get_date)
    leatests=sorted_post[-2:]
    return render(request,'blogs/index.html',{'leatest_post':leatests})



def posts(request):
    return render(request,'blogs/post.html',{'post':all_posts})

def single_post(request,slug):
    post=next(post for post in all_posts if post['slug']==slug)
    return render(request,'blogs/post_detalis.html',{'post':post})

def karbaran_list(request):


    all_karbaran = karbaran.objects.all()
    return render(request,'karbaran_list.html', {'all_karbaran': all_karbaran})

def product_list(request):
    all_product = Product.objects.all().order_by('price')
    number_of_product=all_product.count()

    info=all_product.aggregate(Avg('price'),Max('price'),Min('price'),Max('rating'))


    return render(request, 'blogs/Product_list.html', {'all_product': all_product,
                                                       'number_of_product':number_of_product,
                                                       'info':info})

def product_details(request,slug):
    # try:
    #   products=Product.objects.get(id=product_id)
    # except:
    #     raise Http404()
    products = get_object_or_404(Product,slug=slug)
    return render(request,'blogs/product_details.html',{'Product':products})
