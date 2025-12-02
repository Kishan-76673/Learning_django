from django.shortcuts import render
from django.http import HttpResponse
import logging
# Create your views here.

def index(request):
    return render(request, 'static/index.html')


# in the views.py, writte the logical part of the application
def home(request):
    return render(request, 'static/index.html',context={'title':'Home - My Website'})
# we can see that all website returns HTML pages
# but here we are returning simple text in the form of HTTP response

logger = logging.getLogger(__name__)
def success_page(request):
    logger.error("This is an error message")
    return HttpResponse("<h1>This is success page</h1>")

# instead of written the html in return statement should return the web page directly... like this

########################################

# Tempplate engine: Django uses a template engine to render HTML pages dynamically.
# It allows you to create HTML files with placeholders for dynamic content.
# When a view function is called, it can pass data to the template, which then generates the final HTML page sent to the user's browser.


def contact(request):   
    # if I want to render the custom title in contact page then I have to pass the context dictionary
    context = {'title': 'Contact Us - My Website'} 
    return render(request, 'static/contact.html', context)

def about(request): 
    people = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 18},
        {'name': 'Charlie', 'age': 35},
        {'name': 'Kishan', 'age': 14},
        {'name': 'Namdev', 'age': 25},
    ]

    for i in people:
        if i['age'] >= 18:
            print(f"{i['name']} is an adult.")

    text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

    vegetables = ['Tomato', 'Potato', 'Cabbage', 'Carrot', 'spinach']

    var1 = ""
    var2 = None
    var3 = "This is var3 — the first non-empty variable"
    # here if the var1 is empty and var2 is None then it will take var3 value
 
    context = {'people': people, 'text': text, 'vegetables': vegetables, 'var1': var1, 'var2': var2, 'var3': var3, 'title': 'about - My Website'}
    return render(request, 'static/about.html', context)


# render() accepts only three arguments: render(request, template_name, context)
    
# context is a dictionary that holds the data you want to pass to the template.
# Why does Django use context?                              
# Because Django follows the MVC pattern (Model–View–Controller), but calls it MVT (Model–Template–View):
# View (Python code) → logic
# Template (HTML) → display
# Context (dictionary) → carries data from View to Template

# Basically: View → (context) → Template