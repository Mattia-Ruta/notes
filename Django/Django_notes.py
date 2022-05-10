"""
Django Notes
"""

#Inside CMD:
django-admin startproject New_Project
#Creates a new Django Projekt in current directory

python manage.py runserver #Will show server information
#run Ctrl-C to exit server

#Inside settings.py, make sure you add your server's domain or IP
#In settings.py:
ALLOWED_HOSTS = ['123.123.123.123', 'domain.com']

"""
New App
"""
python manage.py startapp New_App
#Will create a new app within the Django project called New_App

#Once you create a new app, include it in Projekt folder's settings.py file
INSTALLED_APPS = [
    'New_App',
    'Others',
    '...',
]

#First thing is make a temporary view for new app
#Open New_App's folder and find views.py:
from django.http import HttpResponse #Imports HttpResponse
def index(request):
    response = "This page is working"
    return HttpResponse(response)

"""
URLs.py
"""
#Next create a new urls.py file for the new app
#Inside urls.py:
from django.urls import path #This lets you use the path() function
from . import views #This allows you to use your function views from inside views.py

#Next create a variable for the URL patterns
urlpatterns = [
    path("", views.index, name="index"),
]
#Will call first argument which is request from user, being the URL
#Second argument is which view will be rendered when you visit the path
#Third argument gives a name to the URL path so you can call back on it later

#Before continuing, be sure to go to urls.py file in main project directory
from django.urls import include, path
#Include() will let you add to the list with path
#Under the URLPATTERNS list, add the new path for the new view
urlpatterns = [
    path('hello/', include('hello.urls')),
] #First argument tells you the name the of the URL path that calls next argument
#Second argument goes inside hello module and pull urls.py file from there
#This path will link the two files together

"""
Dynamic URLs, Mapping, and Namespaces
"""
"""
It's important to be able to keep your URLs and mapping as clean as possible. Django has built in functionality for this.
You can keep your URLs separated by app name and avoid confusion and errors by using namespaces
"""
#You can pass in a data type as information to grab for a dynamic URL that changes depending on that information
urlpatterns = [
    path('products/<int:id>/', lookupview, name = 'product'), #Default is using the id of the DB objekt
    path('products/<slug:slug>/', lookupview, name = 'product-slug'), #You can also use other data types like str and slug
    path('products/<int:id>/detail', lookupview, name = 'product-detail'), #Adding more slashes gives you more options for URL mapping
]

#Once you create a field for the URL to populate, you have to include this as an argument in your view!!
#Whatever data type you include in the URl will be passed along
def lookupview(request, id): #Make sure the name of the arg is the same as the <int:id> name in the URL pattern
    obj = Product.objects.get(id = id) #set id to pass the info along of the id you included in the URL

#Inside urls.py, you can set your app_name to create your namespace for organisation
app_name = 'products' #For html links use {% url 'products:index' %} to specify which app you're going to
urlpatterns = [
    path('', product_list_view, name = 'product-list'),
]

#Be sure to import reverse whenever you use it:
from django.urls import reverse

#This is to force a namespace to be used if you reverse to a URL:
def get_absolute_url(self):
    return reverse('products:product-detail', kwargs={'id': self.id}) #products: will open the namespace of products


"""
Starting Main Site
"""
"""
After you finish creating the framework, you can start working on the HTML pages
You need to create folders that will hold the files
Inside the New App's folder, create a folder called templates
  inside templates, create a new folder called the New App's name
    Inside this New_App folder, create the index.html page
  Links that are referenced to this will show as .../New_App/index.html

If you use layout.html as a template, be sure to start the document with
{% extends "New_App/layout.html" %}
"""
#Once you create the index file, you have to render it from views.py
#edit the index function as so:
def index(request):
  return render(request, "New_App/index.html")
#This will tell the programme to call on that index.html file to render as the page
from django.shortcuts import render
#Calling a function from outside the HTML page is done using {{ variable }}

"""
Using CSS Pages
"""
"""
To attach a CSS file to the page, you have to create a new folder
Inside the New_App's directory make a folder called static
Within static create a folder with the name of the New_App
Make a file called styles.css here and make the stylesheet
In the HTML file now, add a line on the top:
{% load static %}
This will tell the file to load the static folder which contains stylesheet
Use django syntax to call upon the sheet.
In the <head></head> container:
<link href="{% static 'New_App/styles.css' %}" rel="Stylesheet">
"""

"""
Views.py
"""
#Make sure to import all the functions you need to use from Django's database
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def brian(request):
    return HttpResponse("hello, Brian!")
    #This gives a new view that will just return the HTTP Response 'hello, brian!'

#To allow new views to be shown on site, you need to update them on URLs list in New_App directory
urlpatterns = [
    path("", views.index, name="index"),
    path("brian", views.brian, name="brian"),
]   #In second argument, it will pull function defined as brian from views.py
#It will have the tag of 'brian' so when /brian URL is visited, it will put that view instead

def index(request):
    var = Table.objects.all()
    return render(request, 'tasks/index.html', {
        "tasks": var
    }) #This will define the index function in views and bring up tasks/index.html file
#The third argument will unlock vars inside the HTML file itself so it can be referenced
#To use them, you have to assign them a value, which is done as a dictionary

HttpResponseRedirect(reverse("function", args=(flight.id)))
#It will redirect user to the next page
#reverse() will retrieve first arg in the path function inside URLPATTERNS list
#If you use the name 'index', it will retrieve the path of ""
#First arg is the name of the function to go back to from views.py file
#Second arg will apply whatever argument that function needs

#To print to console all variables inside request.session
for key, value in request.session.items():
    print('{} => {}'.format(key, value))

"""
Models/Classes
"""
#Within models.py file, create a new class and set what the table's columns will be in database
class Flight(models.Model):
    origin = models.CharField(max_length=64, label='Origin')
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()
#If you're using foreign keys, referrincing other tables,
#You need to use an argument within models.ForeignKey()
models.ForeignKey(Referenced_Class, on_delete=models.CASCADE, related_name="name")
#ForeignKey() calls on a different class you already set, which you put in first argument
#on_delete asks what you do if it's deleted, CASCADE will delete the class as well
#Related_name is a reference you put so you can call on it later, like an origin tag for a flight
#The related name would be 'arrivals' because it can be linked later on

models.ManyToManyField(Referenced_Class)
#This links another Class/model to the field in the table you're editing

"""
Models/Classes Fields
"""
class Table(models.Model):
    field 1 = models.Field(required=00, options) #This is template of how fields are written

#Character Field, max_length is required
models.CharField(max_length=64)

#Bigger text field, useful for comments or longer text
models.TextField()

#Standard Date Field, most sites have built in calendar
models.DateField(auto_now=True)
#auto_now = True will automatically set the date to when the objekt was saved!
#This will make it so you can't set a date yourself
#auto_now_add=True will automaticalls set the date to when objekt was first created
#This will make it so you can't set a date for yourself
#You can only add one of these arguments!

#Same args as DateField but adds time as well
models.DateTimeField()

#Basic field for an integer
from django.core.validators import MaxValueValidator, MinValueValidator
#If you use the validators, be sure to import them from Django
models.IntegerField()
#MinValueValidator(2000) will set the minimum value to 2000
#MaxValueValidator(2020) will set the maximum value to 2020


#Basic field for a float
models.FloatField()

#Basic time field
models.TimeField()

#URL Field. default max_length=200 but you can change as argument
models.URLField()

#Decimal Field, max_digits is max including decimals and decimal_places is the actual decimal places
models.DecimalField(max_digits=5, decimal_places=2)
#This would be for a number with a max of 999.99

#! You can use a function to validate if a field is valid!
from django.core.exceptions import ValidationError
import datetime
now = datetime.datetime.now()
def validate_year(value):
    if value < 2000 or value > now.year + 1:
        raise ValidationError(f'Please enter a year between 2000 and {now.year + 1}!')


"""
New Forms, Not Based From Anything
"""

from django import forms
class NewForm(forms.Form): #Brings new class from forms and adds fields to the form
    field = forms.CharField(label="Field 1", max_value=64) #Standard character field
    field 2 = forms.IntegerField(label="Field 2", min_value=1, max_value=2)
    field 3 = forms.CharField(widget=forms.Textarea) #Will bring bigger box
    field 4 = forms.DateField(widget=forms.SelectDateWidget) #Lets you select a date
    field 5 = forms.EmailField() #brings email field
    field 6 = forms.URLField() #brings URL field

    field 7 = forms.CharField(label='label', widget=forms.TextInput(attrs={ #you can use widgets
        'placeholder': 'Field 7 Here', #this is to adjust the HTML part of the form
        'class': 'New-Class', #You can even change the class
        'id': 'field7', #You can also set custom ID's for each element
        'rows': 20, #Sets how tall the text field is
        'cols': 120, #Sets how wide the text field is
    }))

    field 99 = forms.DateField(widget=forms.SelectDateWidget(years=Year_Choices)) #Can only choose from list
    #You have to make sure you declare a list of the available choices for this!!!
#This has to be before the form you reference it from!!!
Year_Choices = ['1993', '1994', '1995']

#Another example of this:
colour_choices = ['blue', 'Blue', 'red', 'Red']
class Form(forms.Form):
    favourite_colours = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=colour_choices,)
    )
#This will bring list of choices and not make it required
#Checkbox multipe will be pulled from forms and applies
#The choices available will be from the list you provide
#The first in the paid is the name of the info given
#The second is the name that will be published on the site

#min/max value sets the min/max values for ints in the field, mostly optional
#To call a form onto the page, you need to add it to the function in views.py under render/request
"form": NewForm()
#This allows function to be called within page as a variable
#To call the form function in, you need to use {{ form }} to call it using the name you set

"""
Creating Forms based on Models
"""
#Create a forms.py file in the app's directory and import ModelForm from django's forms module
#Since you're basing your form off your own models, be sure to import the models you're referencing!
from django.forms import ModelForm
from transaction.models import Transaction

#For the get_absolute_url() to work, import reverse to go back to a prev page
from django.urls import reverse

#Creating a form based on a model, you need to reference the fields you want to reflect in the form:
class TransactionForm(ModelForm):
    #Only use this definition if you're adjust a field in a form after the model has been made already
    #Returning the clean field in a var called data

    #def clean_<fieldname> to create custom validations for individual fields
    def clean_transaction(self):
        transaction_name = self.cleaned_data.get('name') #You can reference specific fields in the form to check validation
        data = self.cleaned_data
        if len(transaction_name) > 64: #Using python logic, you can check validation of something specific
            raise ValidationError(_('Invalid Name - Longer than 64 characters!')) #You can set a validation error message
        return data #returns the data in the var data if no errors raise

    class Meta: #Including metadata is optional
        ordering = ['name'] #Sorts a list of the form objekts by the param you set
        model = Transaction #Sets the model the form is based on
        fields = ['name', 'amount', 'date', 'notes'] #You have to set which fields to be included in the form
        widgets = { #Widgets are optional, if left out it will return default field types
            'name': Textarea(attrs={'cols': 80, 'rows': 20}), #You can use Django widgets to override default fields
        }
        labels = { #Can override default name for the field names
            'name': _('Name of Transaction'),
        }
        help_texts = { #Shows helpful text
            'name': _('Some useful help text'),
        }
        error_messages = { #Sets error messages for specific errors within fields
            'name': {
                'max_length': _('The name of this transaction is too long!'),
            },
        }
    def get_absolute_url(self): #This is used to retrieve a URL based on the ID of the model from the table
        return reverse('transaction-detail', args=[str(self.id)]) #Brings you to the detail page, with the id as the arg
        #Returns the user to the URL path named 'transaction-detail', but brings the arguments listed with it
        #You can also use a dictionary if you have multiple args or use kwargs instead
        return reverse('transaction-detail', kwargs={'id': self.id}) #f"/transactions/{self.id}/"

    #You can use this other way as well if reverse() doesn't work:
    def get_absolute_url(self):
        return f"/transactions/{self.id}/" #In HTML: href='{{ item.get_absolute_url }}', the item being the obj var in a list of obj

    def __str__(self):#Be sure to set a human-friendly name for an object in this class to be represented as!
        return self.name #Uses the name field as a representation of itself. If it itsn't defined, it shows as an objekt in memory


"""
Validating Forms
"""
#To validate the form itself you need to add an if statement to the function inside views.py:
from django.http import HttpResponseRedirect
from django.urls import reverse

#be sure to import your model to be used in the form
from .models import NewTaskForm

def new_task(request):
    form = NewTaskForm()
    if request.method == "POST":

        #Create a dictionary if you want to use initial data to fill in the fields
        initial_data = {
            'title': 'Initial Title to Use',
        }

        obj = Task.objects.get(id = 1) #This grabs the object with the ID of one

        #You can pass in an object into a field to populate it with that data
        form = NewTaskForm(request.POST or None, initial = initial_data, instance = obj) #Sets form to either the posted data or None/Null
        #Note that initial_data is optional and only if you want initial data to be filled in the form

        if form.is_valid():
            form.save() #saves the form inputted if it's valid
            form = NewTaskForm()

            #All of the form's accessible data is stored inside this:
            print(form.cleaned_data)
            #You can print to see the data in the terminal

            #This creates a new object using the form's cleaned data as an arg
            Task.objects.create(**form.cleaned_data)

            #The following is only used if you hardcode a list called tasks in this page!
            task = form.cleaned_data["new_task"] #Use indexing to call on specific field
            tasks.append(task) #Appends the new info to the list called tasks

            #after new form is reset and saved, it reloades same page with fresh form
            return render(request, 'tasks/add/index.html', {
                'form': form
            })
        else: #This will run if the form is not valid, returning the same page including the info from the form
            print(form.errors) #You can print the form's errors to the terminal for debugging
            return render(request, "tasks/add/index.html", { #Reverts the user back to the url set in tasks:index
                "form": form,
            })
    else: #If there's no POST method, like visiting page for first time, it will create an empty form
        form = NewTaskForm()
    return render(request, 'new_task.html', {
        'form': form, #This will be the context in the HTML page for the form
    })
"""
This will check if the method of request is valid or not
This is by checking if request.method is True or False.
If True, it will run because the form is valid
If False, it will return to the same page again and give the current information they submitted so far
"""
#If request is valid, it creates var called task and puts information inside it from the form
form.cleaned_data dictionary #This is where the info is kept
#To call on a specific field, use indexing to call the field
form.cleaned_data["new_task"]

request.session
#This puts the sessions information from the page
#If there is no new information, you need to create it.
#To check if there is any info you can check a specific tag inside
request.session["name"] #This refers to the specific param inside request.session called 'name'
if "name" not in request.session:
    request.session["name"] = []
#This creates the param called 'name' inside the session and make it an empty list
#You can make this whatever you like
#Be sure to change any global variables to request.session so it stays consistent
request.session["tasks"] += [variable] #Will add variable to list while keeping it intact


"""
Fixed Choices
"""
Choice_1 = 'C1'
Choice_2 = 'C2'
Choices_List = [
Fixed_Choices = models.CharField(
    max_length=2,
    choices=Choices_List,
    default='Choice_1',
)
]
#C1 is the shorter name of the choice which is going in the database as such
#The list will show a list of the choices and name they will have in the page
#The default arg sets what the default choice will be

#Create relationship between different tables
models.ManyToManyField(Flight, blank=True, related_name="passengers")
#First arg shows the Class it can be associated with
#Second arg asks if it's allowed to be blank (like if passenger has no flights)
#Third arg is related name to link them together. This is referenced in views.py when you add var flight.passengers

"""
Database Management
"""
"""
Before you create database, you need to create a model from the models.py file in the app folder
When you migrate into a DB, it will import models
Migration:
    Accessing a DB in general, you need to create one and migrate all the info into it
    In the CMD, begin migrations request in the dir of the main projekt dir:
    python manage.py makemigrations
    This creates the models we defined and readies it for migration. Then migrate them:
    python manage.py migrate

Once you create a DB, you can start adding info to your tables!
Make sure you create the models of the tables for the DB within models.py so they can be accessed by Django
"""
#Create a flight and set the columns to what you set in the declaration
flight = Flight(origin='New York', destination='London', duration=415)
#Built in function for Django that saves changes to the DB:
flight.save()

#Can input function of calling all objects inside of the named Table and save inside a variable
var = Table.objects.all()
#If you print the var, it will give you all the objekts Inside
#This only works with Classes inside of models.py

"""
Migrating an already existing database
"""
#Inside settings.py make sure to use the correct settings for the db
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'budgets', #Name of db
        'HOST': '/var/run/mysqld/mysqld.sock', #Make sure it's correct socket
        'PORT': '3306',
        'USER': 'django',
        'PASSWORD': 'testtest123',
    }
}

#In the terminal, run inspect db to auto-create a models page
#python manage.py inspectdb >> models.py
#>> models.py creates a file for you to edit
#Be sure to manually configure the models still!!!!
#Remove managed=False to let django mange the tables
#Set on_delete for all fields to a standard

#After you adjust the models, be sure to makemigrations and migrate


#Only use fake migrate for specific things that already exist
#python manage.py migrate --fake

#-------------------------------------------------------------------

#Be sure to import all your models! Inside views.py:
from .models import *

#Inside the dictionary of variables inside your function:
return render(request, 'budgets/index.html', {
    'budgets': Table.objects.all(),
})
#The key is the variable you reference on the HTML page
#The value is the info pulled from the table

#Function by itself will give you all objekts inside
Table.objects.all()
#This is called a Queryset and is standard to save in a var called queryset!

#Can filter by a field inside the table
Table.objects.filter(city='New York')
#City is the field inside table and New York is the balue inside that field

#You can infur from fields using two underscores to filter as many times as you like
books = Books.objects.filter(title__contains='wild') #Finds books where title contains the word wild
books = Books.objects.filter(title__icontains='Lennon') #using i in front of a filter makes it not sensitive to case

#Date Functions ----------------------------------------------
#You can use a range, same as BETWEEN in SQL
Table.objects.filter(date__range=["2011-01-01", "2011-01-31"])
Table.objects.filter(date__range=date__year='2011', date__month='01')

import datetime #To use datetime.date() you have to import it
start_date = datetime.date(2005, 1, 1) #datetime way of saving date object
end_date = datetime.date(2005, 3, 31)
Table.objects.filter(custom_date__range=(start_date, end_date)) #__range is the built in function, custom_date is the field name

Table.objects.filter(pub_date__date__gt=datetime.date(2005, 1, 1)) #Checks dates that are greater than the date specified, because of gt (greater than)
Table.objects.filter(pub_date__date__year__gte=2005) #Checks if the year inside pub_date is greater than or equal to 2005. pub_date.date.year
#Dates contain year, month, week, week_day, and day
#For week day, 1 is Sunday and 7 is Saturday, unless USE_TZ is True in settings.py, then it changes depending on db timezone
Table.objects.filter(pub_date__time=datetime.time(14, 30)) #Time is built into datetime as well
Table.objects.filter(pub_date__range=(datetime.time(8), datetime.time(17))) #Checks range between 08.00 and 17.00
Table.objects.filter(timestamp__hour=23) #returns everything from 23.00 - 23.59. Also works with standard time fields. Also has minute and second attributes

#Titles and containing ---------------------------------------
Table.objects.filter(name__in='abc') #checks if name is included in given string, same as SELECT * WHERE name IN ('a', 'b', 'c');
query1 = Table.objects.filter(name__icontains='l') #Results a queryset with all objects with name including the letter l
query2 = Table.objects.filter(book__in=query1) #You can nest a queryset from a previous query in another one
#Returns all objects where book is in the list of query1, which contains the letter l

Table.objects.filter(name__isnull=True) #Refers to IS NULL

#You can retrieve only one entry, knowing there's only one in that table
Table.objects.get(city='Paris')
#You can also get the row which has a specific Primary Key Value
Table.Objects.get(pk=1)

#Some built in functions ----------------------------------
#Will count the number of items in a table
Table.objects.count()

Table.objects.filter(id__gt=4) #Id > 4, gt for greater than
#gte, greater than or equal to. lt is less than, lte is less than or equal to
Table.objects.filter(title__startswith='Dictionary') #case sensitive. Use istartswith for case insensitive
Table.objects.filter(title__endswith='Lennon') #case sensitive. Use iendswith for case insensitive

#Ordering Results ----------------------------------------
Table.objects.order_by('-pub_date') #minus sign means DESC for results list
Table.objects.order_by('name')[:5] #Returns only first 5 items in results list ('LIMIT 5' in SQL) index 0 to 5, not inclusive
#Join a results list together into a string:
output = ', '.join([question.question_text for question in question_list])
#Lists question_text from each question in question_list and seperates by first join section (question1.text, question2.text, question3.text)

#List Comprehension (python) -------------------------------
fruits = ['apple', 'cherry']
newlist = [x for x in fruits if 'a' in x] #Short hand for adding to new list items from fruits that include 'a'
#Same as this code:
for x in fruits:
    if 'a' in x:
        newlist.append(x)

#In the interactive shell you can run queries and add entries
#python manage.py shell
from app.models import *
#After importing your models you can run the same queries as in views

#timezone is a builtin function, django.utils have some good functions to use
from django.utils import timezone
newobj = ModelName(field1="string", date=timezone.now())
#Once you have the object, you can manipulate it
#Be sure to save the object to write it to the db
newobj.save()
newob.delete() #To delete an object from db by object method

#Once it's saved you can access its attributes as a python object
newobj.id #returns id of object
q.field1 #returns value of field1
q.field2 = "new value" #You can change the value of it
q.save() #Be sure to save it if you change it at all

#You can loop through a queryset list and print values from it
for question in Question.objects.all():
    print(question.question_text)


"""
Checking if an object exists or a 404 Error
"""
#Import the 404 error from django.shortcuts
#In views:
from django.shortcuts import render, get_object_or_404
def detail(request, question_id):
    question = Question.objects.get(Question, question_id=question_id) #You can also pass a queryset instead of Model


#You can also use a different function called Http404
from django.http import Http404

try: #Will try the query, checking if the user has a template object
    #If you use the get_object_or_404 method, it will automatically show a 404 page if it doesn't exist.
    template = get_object_or_404(Template, account=request.user) #Model is first arg and

    #Use standard .get() method if you plan on using the Http404 raised function below instead
    template = Template.objects.get(id = id, account = request.user)

except Template.DoesNotExist: #If this error shows, it will run following code
    template = None #Will set the var to None instead of the DoesNotExist error!
if template is not None:
    ...#run this code if there is a template
else:
    raise Http404 #This will show a 404 page

#Works for db objects
try:
    question = Question.objects.get(pk=question_id)
except Question.DoesNotExist:
    raise Http404('Question does not exist')


"""
Using DB objekts as default views built into Django
"""
#Once you create models and forms and a DB to store things, you can create pages for users to be able to adjust them
#In views.py, import the functions you need to create those pages:
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from .models import Transaction

class TransactionListView(ListView): #Lets you have a list of objects in a class
    queryset = Transaction.objects.all() #Be sure to include a queryset
    model = Transaction
class TransactionDetailView(DetailView): #Gives a detail page of a specific objekt
    model = Transaction
    fields = ['name', 'amount', 'date', 'notes'] #Be sure to tell which fields to show up on the detail page
class Transaction_Create(CreateView):
    model = Transaction
    fields = ['name', 'amount', 'date', 'notes'] #Gives a form to use, be sure to tell which fields to allow
    def form_valid(self, form): #Assigns the user who made the form to the form data usings the field called 'account'
        form.instance.account = self.request.user
        return super().form_valid(form)
class Transaction_Update(UpdateView): #Allows the user to update a specific objekt
    model = Transaction
    fields = ['name', 'amount', 'date', 'notes']
class Transaction_Delete(DeleteView): #Lets user delete a specific objekt
    model = Transaction
    success_url = reverse_lazy('transactions_delete') #You need to give a link for it to go after you delete it

"""
By default, the views will send the user to the individual transaction view after they submit info
If you want to change that, you can put success_url and set it to a lazy reverse to a different page
This is done in the example of deleting the Transaction

When you create the HTML pages, the default will be the transaction_form.html derived from the model name,
but you can change that!
"""
#Putting a new field in the view:
class Transaction_Create(CreateView):
    template_name_suffix = '_create' #Changes transaction_form.html to transaction_create.html
"""
Check the forms section of the HTML notes
The "delete" view expects to find a template named with the format model_name_confirm_delete.html
Check the form section in the HTML notes for more structure!
"""
"""
The delete view expects a template named transaction_confirm_delete.html
This can also be changed by putting a template_name_suffix field in the DeleteView class!
Check deleting forms in the HTML notes for how to structure it!
"""
#Now inside urls.py you need to update the URL paths to the transaction views
urlpatterns = [
    path('transactions/', views.TransactionListView.as_view(), name='transactions'),
    path('transaction/create/', views.Transaction_Create.as_view(), name='transaction-create'),
    path('transactions/<int:pk>', views.TransactionDetailView.as_view(), name='transaction-detail'),
    path('transaction/<int:pk>/update/', views.Transaction_Update.as_view(), name='transaction-update'),
    path('transaction/<int:pk>/delete/', views.Transaction_Delete.as_view(), name='transaction-delete'),

    #Create a path to your delete view function if you don't use the as_view() built in function
    path('transaction/<int:pk>/my_delete', views.Trasaction_Delete, name = 'transaction-delete'),
]

#Import redirect to redirect the user after they confirm the deletion
from django.shortcuts import redirect

#Create your own delete view for a delete confirm page if you don't use the built in function
def Transaction_Delete(request, pk):
    obj = get_object_or_404(Transaction, pk)
    #Make sure it's a POST request so the user is sure they want to delete the objekt
    if request.method == 'POST':
        #confirm delete
        obj.delete()
        #After they delete the objekt, you want to redirect them somewhere else so they don't see a 404 error
        return redirect('../../') #This returns the user back 2 URl /'s, so if it was products/2/delete, it returns products/

    #This renders the deletion page, if they first arrive it will ask if they want to delete the objekt
    return render(request, 'transaction/product_delete.html', {
        'object': obj
    })



"""
Users and Logging in/out
"""
#Django comes with default views for logging in and out which you can pull by including it in URLS:
from django.contrib.auth import views as auth_views
URLPATTERNS = [
    path('accounts/', include('django.contrib.auth.urls')),
]#This includes a few views built in

#If you navigate to the site/admin it will show an error but also show all URLs included in the views
"""
accounts/ login/ [name='login']
accounts/ logout/ [name='logout']
accounts/ password_change/ [name='password_change']
accounts/ password_change/done/ [name='password_change_done']
accounts/ password_reset/ [name='password_reset']
accounts/ password_reset/done/ [name='password_reset_done']
accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/ reset/done/ [name='password_reset_complete']
"""
"""
You have to create the templates to be used
!!Be sure to create a templates folder in the PROJEKT's ROOT DIRECTORY!!
Inside this templates folder, created another folder called registration

Now inside the projekt's settings.py file (projectfolder > projectfolder > settings.py)
"""
import os #Be sure to import the os
TEMPLATES = [
    {'DIRS': [os.path.join(BASE_DIR, 'templates')],
    'APP_DIRS': True,}
]
"""
This will link the templates folder in your projekt to the URLs etc
!!Check the Users.html file in django notes for the templates and locations!!
"""

"""
Logging In
"""
"""
Create the login.html page in the registration folder you created
After you create a login page you can already log a user in!
By default it redirects you to the user's profile page but you can change this!
"""
#In the Projekts's dir > projekt's settings.py file:
LOGIN_REDIRECT_URL = '/budgets/' #This will reroute user back to budgets app

"""
Logging Out
"""
#Be sure to create the logged_out.html page in the registration folder!

"""
Password Reset
"""
"""
Create the password_reset_form.html file in the registration folder you created
You have to make a form which will input the user's email to send them a password reset page
Check the users HTML notes to see the templates!

Be sure to also create the password_reset_done.html page to show that the email has been sent!

Once you create that page to show it sent, you need to create the email that will send to the users:
Inside the same folder, create a password_reset_email.html. Check HTML notes for template

Once you make the email template, you need to make the page they will go to in their link!
In the same registration folder make the password_reset_confirm.html file!

Last page to make is the completion page which shows the user after they make a new password:
In registration folder make password_reset_complete.html file!

In the end you need these files in the Projektdir/templates/registration folder:
    -logged_out.html
    -login.html
    -password_reset_complete.html
    -password_reset_confirm.html
    -password_reset_done.html
    -password_reset_email.html
    -password_reset_form.html

Because you need emails to work, you can't test the reset email without the functionality
To temporarily see emails in the console while developing, open your projekt's settings.py file:
"""
#In the settings.py file:
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
"""
Users and Authorisation
"""
"""
You can use a decorator to force users to be logged in to view content!
If not logged in when they look at a page with the decorator,
the site will redirect to the login URL set in settings.LOGIN_URL in projektdir's settings.py file
Using the @login_required decorator ONLY WORKS ON VIEW FUNCTIONS! ex: index()
"""
#Be sure to import the login_required decorator!
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    ...

"""
Class-Based Views
"""
"""
If you want to require a user to be logged in for a class view, you need to use a LoginRequiredMixin instead!
"""
#Be sure to import the mixins
from django.contrib.auth.mixins import LoginRequiredMixin

#Inside your class views, use the mixin as the first argument!
class View(LoginRequiredMixin, View):
    ...

"""
Assigning model objekts to specific users
"""
"""
Once you make it so you have to login to view content on your site, you need to assign
objekts to the users who create them. To do this, you need to assign users to objekts!

First step is to create the field itself in the model!
"""
#In models.py, import the User class to access it
from django.contrib.auth.models import User

#Edit your instance model to include the user!
class Transaction(models.Model):
    name = models.CharField(max_length=64)
#If you want an instance to be able to have a blank user, like books in a library that aren't rented yet
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

#If you want instances to only exist with an account/user attached
    account = models.ForeignKey(User, on_delete=models.CASCADE)

"""
Within the Create class view of the instance, you need to include the field of the user!
In the case of transaction, it'll pull the user who requested the form and put it in the field!
If you don't include that field in the fields var in the class, it won't show the user!
"""
#In views.py:
class Transaction_Create(LoginRequiredMixin, CreateView):#Make sure you use LoginRequiredMixin to avoid users seeing other users!
    model = Transaction
    fields = ['name', 'amount', 'date', 'notes']
    def form_valid(self, form):#Creates instance of a valid form and includes new params
        form.instance.account = self.request.user #Changes the 'account' field in the instance to the user who requested it
        return super().form_valid(form) #Returns the valid form with the new params
"""
Listing Views for Specific Users
"""
#Inside the class-based view for listing instances, create a new function:
class LoanedBookInstanceListView(LoginRequiredMixin, ListView):
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html' #Sets a custom template for the list view
    paginate_by = 10

    #Returns list of books with borrower set as user and filters by 'o' which is borrowed.
    #You can also order the list by an attribute!
    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

"""
Class-Based Views Built-in Functions
"""
#Be sure to import your models into your views so you can reference them
from .models import *
from .forms import * #This will import the default modelform for creating and updating an objekt
from django.urls import reverse #For DeleteView to be able to reverse URL back to a previous page

class ArticleListView(ListView):
    template_name = 'articles/article_list_custom.html' #You can use a custom template for the views
    queryset = Article.objects.all() #returns the queryset of all the objects

class ArticleDetailView(DetailView):
    queryset = Article.objects.all()

    def get_object(self): #Returns the single object by finding the id passed through the URL
        _id = self.kwargs.get('id') #Finds the kwarg called 'id' in the instance
        return get_object_or_404(Article, id = _id)


class ArticleCreateView(CreateView):
    form_class = ArticleModelForm #Sets the form from .forms to create an objekt
    def form_valid(self, form):
        cleaned_data = form.cleaned_data #The data inputted is saved inside cleaned_data
        return super().form_valid(form)

    def get_success_url(self):
        return '#' #this refers to a URL to go to once you successfully create an objekt

#UpdateView is very similar to DetailView
class ArticleUpdateView(UpdateView):
    def get_object(self):
        _id = self.kwargs.get('id')
        return get_object_or_404(Article, id = _id)
    def form_valid(self, form):
        return super().form_valid(form)

class ArticleDeleteView(DeleteView):
    template_name = 'articles/delete_article.html'
    def get_object(self):
        _id = self.kwargs.get('id')
        return get_object_or_404(Article, id = _id)
    def get_success_url(self):
        return reverse('articles:article-list') #Returns the user back to the list page, make sure you use the right name

"""
Custom Class Used as a View using Raw Framework
"""
#You can create a custom class that is used as a view using the base View class
#The built in Django Class-based views are a much cleaner version of this, but this is what it is basically doing
from django.views import View
from django.shortcuts import render, get_object_or_404
from .models import Course #Imports your Course model for it to work
from .forms import CourseForm #Imports your custom Course form for creation form

class CourseView(View):
    template_name = 'about.html' #You can set custom vars to be saved in the instances, this case the template it renders
    #GET method
    context = {} #Good to set before so you can just append to it if needed
    def get(self, request, id=None, *args, **kwargs): #If you set id to None, you make it so it's not required
        if id is not None: #If default, no obj is pulled. Instead default GET returns no id
            obj = get_object_or_404(Course, id=id)#If id is not None, it will set it to what you passed in
            context['object'] = obj
        return render(request, self.template_name, context) #You can reference self.var for anything you set above
        #You can change a var using the URl if you do GET method, so you can change the template it goes to later

    #POST method
    def post(request, *args, **kwargs):
        return render(request, template_name, context)

class CourseListView(View):
    template_name = 'courses/course_list.html' #Set the template to one you made for this view
    queryset = Course.objects.all() #Filter your queryset as needed
    def get(self, request, *args, **kwargs):
        context = {'objects_list': self.queryset}
        return render(request, self.template_name, context)
        #This will render the page using the template name you set and add the queryset to the var called 'objects_list'

class CourseCreateView(View):
    template_name = 'courses/course_create.html'
    def get(self, request, *args, **kwargs):
        form = CourseFor() #Sets the form to the custom one you imported from .forms
        context = {'form': form}
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        form = CourseForm(request.POST) #Pulls the info from the POSTed data
        if form.is_valid():
            form.save()
            form = CourseForm() #resets the form after you saved it to a fresh form
        context = {'form': form}
        return render(request, self.template_name, context)

class CourseUpdateView(View):
    template_name = 'courses/course_update.html'
    def get_object(self):
        id = self.kwargs.get('id') #Will grab the id from the URL
        obj = None # If no id is passed through the URL, obj will default to None
        if id is not None:
            obj = get_object_or_404(Course, id = id)
        return obj #Returns None if no id is passed through the URL
    def get(self, request, id = None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseForm(instance = obj)
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        context = {}
        obj = self.get_object
        if obj is not None:
            form = CourseForm(request.POST, instance = obj)
            if form.is_valid():
                form.save()
                form = CourseForm()

class CourseDeleteView(View):
    template_name = 'courses/course_delete.html'
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Course, id = id)
        return obj
    def get(self, request, id = None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)
    def post(self, request, id = None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect('/courses/') #Redirect the user back to the main courses list page
        return render(reauest, self.template_name, context)
"""
Admin App
"""
"""
Within Django, the admin app lets you update and change models from the website itself
"""
#To start, you have to create a superuser
#Using the CMD in the projekt dir do:
#python manage.py createsuperuser

#Inside the admin.py app, you'll have to import the models you made so far
from .models import Model_1, Model_2

admin.site.register(Model_1)
admin.site.register(Model_2)
#!!!You have to register every single model you create!!!
#To access the admin app, runserver and access the /admin URL in the browser

class FlightAdmin(admin.ModelAdmin):
    list_display = ('id', 'origin', 'destination', 'duration')
    filter_horizontal = ('flight',)
"""
Creating a class within the admin app lets you customise exactly what info you'll see when you bring up the model
list_display will let you show exactly what parts of the table you want to see in the admin app
filter_horizontal creates a horizontal table to add and remove an attribue within a class
Be sure to update the class it's associated with!
    In the admin.site.register() function, the second arg is the class it will show inside the admin.py page
"""
#This is useful to be able to show the id as well:
admin.site.register(Flight, FlightAdmin)

"""
Testing
"""
"""
DJANGO TEMPLATE FOR LOGGING IN AND OUT!
"""
"""
Users and Logging in/out
"""
"""
Creating a new app called users, we can maintain a list of users and keep track of their logins
Be sure to follow guide for new apps and add it to the INSTALLED_APPS list in settings.py

This is done through Django's DB. It has a lot of functionality built in for authenticating
Apply migrations to the server to save the changes!

With the admin app you can create a superuser to adjust users
Create a templates folder in users dir and start making HTML pages for the dashboard!
layout.html and dashboard.html which extends the layout
Inside the dashboard, you can make a temp greeting for now {{ user.username|default:'Guest' }}
If the user is logged in, it will say the username, if not it will say guest

Create a urls.py file inside the users dir!
Inside urls.py file, be sure to add 3 major fields in terms of users:
    indexing, logging in, and logging out.
"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("accounts/", include('django.contrib.auth.urls')), #This is the default accounts URL's
]

#Inside views.py file, you need to define the functions of thest views and see if the user is logged in
#In login function, it checks if info was POSTed to the server
#If it is, it will put that info in var fields for Django
#If not, it will redirects back to the login page

#These will give you the functions needed to authenticate etc.
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return render(request, 'users/user.html')
"""
Inside of Django's request function, a user is set as an objekt and has attributes which can be called on
is_authenticated can be asked to check if they have logged in.
If not, it will redirect them back to the login page to login
If yes, they will be sent to the user.html page
"""

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'users/login.html', { #Brings to login page
                'message': 'Invalid Credentials!'
            })
"""
These will check if something was posted, and collect info from the form
They will set the username to a var called username and same with password
Since they were saved as vars, you can use them as arguments from Django's built in function!
This will use it to authenticate and check if they logged in
authenticate() takes 3 arguments: request, username, and password
"""
"""
The if statement asks if there is a user or not.
If yes, it will use login() to try logging them in with the user var then redirect to the url 'index'
If no, user var is None and will render page again with extra var for the page called 'message'.
    You can use any message to tell the user their credentials are invalid
    Once you create this message, it will let you access it on the HTML page!
    Make sure you include it in the HTML file itself, check if there is a message using Django logic
"""
"""
Once you make the views, be sure to actually create the login page in templates!
If you create a form to login, you can pass the inputted info into the login function in views
    Check the HTML notes under the Login Forms section to see the HTML code for it!
"""
#Inside of the request var/arg, there are attributes that can be called upon in an HTML page!
#This includes if a user has been logged in!

request.user.username #Can call the logged in user's username!
request.user.email
request.user.first_name
request.user.last_name

#Logging out View
def logout_view(request):
    logout(request)
    return render(request, 'users/login.html', {
        'message': 'Logged Out!'
    }) #This makes sure a user is logged out and outputs a message that they logged out

#You can also override the defaul paths and views by including them:
URLPATTERNS = [
    path('change-password/', auth_views.PasswordChangeView.as_view()),
]
#You can also refer it to a different template than the default:
URLPATTERNS = [
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='change-password.html')),
]#These views are all Class based!
#You must go into views.py and create the classes the views will be based on:
#class LoginView



"""
Restoring Permissions for broken project
"""
#sudo chmod 755 $(find /var/www/html/applications.local -type d)
#sudo chmod 644 $(find /var/www/html/applications.local -type f)
