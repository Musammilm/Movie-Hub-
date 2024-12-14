import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.db import models
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import redirect, render
from .models import*
from .import views
from django.contrib.auth import authenticate
import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import bs4 as bs
import urllib.request
import numpy as np
from django.template.loader import render_to_string
import random
# Create your views here.
def index(request):
    return render(request,'index.html')

def user_main(request):
    a1=theatre_data.objects.all()
    return render(request,'user_main.html',{"key":a1})

def home(request):
    suggestions = get_suggestions()
    return render(request,'home.html')

def about(request):
    return render(request,'new_about.html')



def userlogin(request):
    if request.method=="POST":
        username = request.POST['username']
        Password = request.POST['password']
        print('hfhfhffhfh')
        user = auth.authenticate(request, username=username, password=Password)
        try:
            usersData = user_data.objects.get(user_name = user )
        except:
            usersData = None
        if usersData is not None:
            auth.login(request, user)
            return redirect(user_main)
        else:
            return render(request,'userlogin.html',{'key':'invalid login'})
    return render(request,'userlogin.html')






def userlogged(request,tk):
    th=theatre_data.objects.get(id=tk)
    movie=add_movies.objects.filter(theatre=th).all()

    m={
        'key':movie
       }
    return render(request,'userlogged.html',m)

def moviedetails(request,tk):
    details=add_movies.objects.get(id=tk)
    k=add_movies.objects.filter(id=tk).values()
    for i in k:
        movi=i["movie_name"]
        l=set.objects.filter(moviename=movi).values()
    a={
        'key1':details,
        'key4':l,
    }
    return render(request,"moviedetails.html",a)


def booking(request,pk):
    details=add_movies.objects.get(id=pk)
    k=add_movies.objects.filter(id=pk).values()
    for i in k:
        movi=i["movie_name"]
        tk = i["no_tickets"]
    l=set.objects.filter(moviename=movi).values()
    if tk==0:
        c="No Tickets Available ..."
    else:
        c="You Can Book Now !!!"
    a={
        'key1':details,
        'key4':l,
        'key5':c     
    }
    username = request.user
    sea=[]
    if request.method=="POST":
        theatre = request.POST['theatre']
        movie_name = request.POST['movie']
        showtime = request.POST['showtime']
        Date = request.POST['date']
        price_1_tk = request.POST['tk_price']
        no_tickets = request.POST['count']
        
        tk_available = request.POST['tk_available']
        
        Status = " Given "

        total = int(price_1_tk) * int(no_tickets)
        tname = theatre_data.objects.get(id=theatre)

        balance_ticket = int(tk_available) - int(no_tickets) 

        for i in range(1,int(no_tickets)+1):
            rand= random.randint(1,50)
            sea.append(rand)

        
        booked_data(theatre= tname,
                book_name=username,
                movie_name=movie_name,
                showtime=showtime,
                Date=Date,
                price_1_tk=price_1_tk,
                no_tickets=no_tickets,
                Total_amount=total,
                seat_no=sea
                
                ).save()
        
        add_movies.objects.filter(movie_name = movie_name).filter(theatre=theatre).update(no_tickets = balance_ticket)
        payments(name=username,amount=total,Status=Status).save()
        ddd={"keyyy":total}
        return render(request,"payment.html",ddd)
    return render(request,'booking.html',a)

def bookedsuccess(request):
    return render(request,'bookedsuccess.html')


def payment(request):

    return render(request,'payment.html')

def theatrelogged(request):
    tname = theatre_data.objects.get(tuser_name=request.user)
    theatre=add_movies.objects.filter(theatre=tname).all()
    t={'key2':theatre}
    return render(request,'theatrelogged.html',t)

def tc_balance(request):
    tname = theatre_data.objects.get(tuser_name=request.user)
    theatre=add_movies.objects.filter(theatre=tname).all()
    t={'key2':theatre}
    return render(request,'tk_available.html',t)

def booking_details(request):
    tname = theatre_data.objects.get(tuser_name=request.user)
    theatre=booked_data.objects.filter(theatre=tname).all()
    t={'key2':theatre}
    return render(request,'booking_details.html',t)
def addmovie(request):
    theatre = theatre_data.objects.get(tuser_name=request.user)
    if request.method=="POST":
        movie_name=request.POST["movie_name"]
        Director=request.POST["Director"]
        caste=request.POST["caste"]
        Category=request.POST["Category"]
        Language=request.POST["Language"]
        Date=request.POST["Date"]
        Date1=request.POST["Date1"]
        set_show=request.POST["set_show"]
        no_tickets=request.POST["no_tickets"]
        no_screen=request.POST["no_screen"]
        price=request.POST["price"]
        image=request.FILES['image']
        add_movies(theatre = theatre,movie_name=movie_name,Director=Director,caste=caste,Category=Category,
        Language=Language,Date = Date,Date1=Date1,set_show=set_show,no_tickets=no_tickets,no_screen=no_screen,
        price=price,image=image).save()
        return redirect(theatrelogged)
    return render(request,'addmovie.html')

# def setshow(request):
#     tname = theatre_data.objects.get(tuser_name=request.user)
#     sets=addmovies.objects.filter(theatre=tname).all()
    
#     s={'key3':sets}
#     if request.method=="POST":
#         m=request.POST["movienames"]
#         t=request.POST["movieshow"]
#         d=request.POST["date"]
#         d1=request.POST["date1"]
#         p=request.POST["price"]
#         set(moviename=m,time=t,Date=d,Date1=d1,price=p).save()
#         return redirect(theatrelogged)
#     return render(request,'setshow.html',s)

def succes(request):
    return render(request,'theatresucces.html')




def theatrelogin(request):
    if request.method=="POST":
        username = request.POST['username']
        Password = request.POST['password']
        user = auth.authenticate(request, username=username, password=Password)
        try:
            usersData = theatre_data.objects.get(tuser_name = user ,is_active=True)
        except:
            usersData = None
        if usersData is not None:
            auth.login(request, user)
            return redirect(theatrelogged)
        else:
            return render(request,'theatrelogin.html',{'key':'invalid login'})
    
    return render(request,'theatrelogin.html')

def userregister(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        Password = request.POST['Password']
        Confirm_Password = request.POST['Confirm_Password']
        email = request.POST['email']
        area_code = request.POST['area_code']
        phone = request.POST['phone']
        location = request.POST['location']
        gender = request.POST['gender']

        if Password==Confirm_Password:
            if User.objects.filter(username=username).exists():
                return render(request,'userregister.html',{'key1':'Your Username Already exist'})
            elif User.objects.filter(email=email).exists():
                return render(request,'userregister.html',{'key1':'Your Email Already exist'})
            else:
                user = User.objects.create_user(username = username, password = Password, email = email )
                user.save()

                tsave = user_data(user_name = user,name=username,email=email, area_code=area_code, phone = phone, location=location ,gender=gender)
                tsave.save()
                return redirect(userlogin)
        else:
            return render(request,'userregister.html',{'key1':'Your password dosent match'})
    
    return render(request,'userregister.html')



def theatreregister(request):
    if request.method=="POST":
        username = request.POST['user_name']
        Password = request.POST['Password']
        Password1 = request.POST['Password1']
        gstno = request.POST['gstno']
        email = request.POST['email']
        License_No = request.POST['License_No']
        phone = request.POST['phone']
        Facilities = request.POST.getlist('Facilities')
        location = request.POST['location']
        specification = request.POST.getlist('specification')

        if Password==Password1:
            if User.objects.filter(username=username).exists():
                return render(request,'theatreregister.html',{'key2':'Your Username Already exist'})
            elif User.objects.filter(email=email).exists():
                return render(request,'theatreregister.html',{'key2':'Your Email Already exist'})
            else:
                user = User.objects.create_user(username = username, password = Password, email = email )
                user.save()

                tsave=theatre_data(tuser_name=user,name=username,gstno=gstno,email=email,License_No=License_No,phone=phone,Facilities=Facilities,location=location,specification=specification)
                tsave.save()
                return redirect(theatrelogin)
        else:
            return render(request,'theatreregister.html',{'key2':'Your password dosent match'})
    
    return render(request,'theatreregister.html')

def adminlogin(request):
     if request.method=="POST":
        username=request.POST['n1']
        password=request.POST['n2']
       
        user = auth.authenticate( username=username, password=password)
        try:
            usersData = User.objects.get(username = username , is_superuser = True)
        except:
            usersData = None
        if usersData is not None:
            auth.login(request, user)
            return redirect(adminlogged)
    
        else:
            return render(request,'adminlogin.html',{'key':'invalid login'})
     return render(request,'adminlogin.html')

def adminlogged(request):
     return render(request,'adminlogged.html')

def admin_theatre(request):
    t2=theatre_data.objects.all()
    d2={'at':t2}
    return render(request,'admin_theatres.html',d2)


def admin_1theatre(request,cck):
    storevalues=theatre_data.objects.get(id=cck)
    return render(request,"admin_1theatre.html",{'att':storevalues})

def delete_theatre(request,cck):
    bstorevalues=theatre_data.objects.get(id=cck)
    bstorevalues.delete()
    return redirect(admin_theatre)

def user_activate(request,ttk):
    my_user = theatre_data.objects.get(id=ttk)
    if my_user.is_active == True:
        user_instance2 = theatre_data.objects.filter(id = ttk).update(is_active = False)
        return redirect (admin_theatre)
    else:
        user_instance1 = theatre_data.objects.filter(id = ttk).update(is_active = True)
        my_user.is_active = True
        return redirect (admin_theatre)
    

def tfeedback(request):
     if request.method=="POST":
        x2=request.POST['a1']
        y2=request.POST['a2']
        z2=request.POST['a3']
        feedback(name=x2,email=y2,description=z2).save()
        return redirect(user_main)
     return render(request,'feedback.html')

def ufeedback(request):
     if request.method=="POST":
        x2=request.POST['a1']
        y2=request.POST['a2']
        z2=request.POST['a3']
        feedbacku(name=x2,email=y2,description=z2).save()
        return redirect(ufeedback)
     return render(request,'ttfeedback.html')

def admin_feedback(request):
    s2=feedback.objects.all()
    s=feedbacku.objects.all()
    
    d2={'fkey':s2,
        'f1key':s,
        
        }
    return render(request,'admin_feedback.html',d2)

def tickets(request):
    username=request.user
    t2=booked_data.objects.filter(book_name=username).all()
    d2={'at':t2}
    return render(request,'ticket.html',d2)


def delticket(request,bk):
    tstorevalues=booked_data.objects.get(id=bk)

    k=booked_data.objects.filter(id=bk).values()
    for i in k:
        theatre=i["theatre_id"]
        name=i["book_name"]
        movie_name = i["movie_name"]
        no_t = i["no_tickets"]
        Total_amount = i["Total_amount"]

    b=add_movies.objects.filter(movie_name=movie_name).filter(theatre_id=theatre).values()
    for j in b:
        global ttk
        ttk=j["no_tickets"]

        

    balance_ticket = int(no_t) + int(ttk)
    add_movies.objects.filter(movie_name = movie_name).filter(theatre_id=theatre).update(no_tickets = balance_ticket)

    Status=" Recived"
    
    payments(name=name,amount=Total_amount,Status=Status).save()
    tstorevalues.delete()
    return redirect(tickets)


def paymentSS(request):
    username=request.user
    t2=payments.objects.filter(name=username).all()
    d2={'aat':t2}
    return render(request,'payments.html',d2)
#movie recomendstionds#
filename = 'nlp_model.pkl'
clf = pickle.load(open(filename, 'rb'))
vectorizer = pickle.load(open('tranform.pkl','rb'))

def get_suggestions():
    data = pd.read_csv('main_data.csv')
    return list(data['movie_title'].str.capitalize())


    
def create_similarity():
    data = pd.read_csv('main_data.csv')
    # creating a count matrix
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(data['comb'])
    # creating a similarity score matrix
    similarity = cosine_similarity(count_matrix)
    return data,similarity

def rcmd(m):
    m = m.lower()
    try:
        data.head()
        similarity.shape
    except:
        data, similarity = create_similarity()
    if m not in data['movie_title'].unique():
        return('Sorry! The movie you requested is not in our database. Please check the spelling or try with some other movies')
    else:
        i = data.loc[data['movie_title']==m].index[0]
        lst = list(enumerate(similarity[i]))
        lst = sorted(lst, key = lambda x:x[1] ,reverse=True)
        lst = lst[1:11] # excluding first item since it is the requested movie itself
        l = []
        for i in range(len(lst)):
            a = lst[i][0]
            l.append(data['movie_title'][a])
        return l
    
# converting list of string to list (eg. "["abc","def"]" to ["abc","def"])
def convert_to_list(my_list):
    my_list = my_list.split('","')
    my_list[0] = my_list[0].replace('["','')
    my_list[-1] = my_list[-1].replace('"]','')
    return my_list

def similarity(request):
    movie = request.GET['name']
    rc = rcmd(movie)
    if type(rc)==type('string'):
         return JsonResponse({'data_string': rc}, status=200, content_type="application/json")
    else:
        m_str="---".join(rc)
        return JsonResponse({'data_string': m_str}, status=200, content_type="application/json")
    
def recommend(request):
    # getting data from AJAX request
    title = request.GET['title']
    cast_ids = request.GET['cast_ids']
    cast_names = request.GET['cast_names']
    cast_chars = request.GET['cast_chars']
    cast_bdays = request.GET['cast_bdays']
    cast_bios = request.GET['cast_bios']
    cast_places = request.GET['cast_places']
    cast_profiles = request.GET['cast_profiles']
    imdb_id = request.GET['imdb_id']
    poster = request.GET['poster']
    genres = request.GET['genres']
    overview = request.GET['overview']
    vote_average = request.GET['rating']
    vote_count = request.GET['vote_count']
    release_date = request.GET['release_date']
    runtime = request.GET['runtime']
    status = request.GET['status']
    rec_movies = request.GET['rec_movies']
    rec_posters = request.GET['rec_posters']

    # get movie suggestions for auto complete
    suggestions = get_suggestions()

    # call the convert_to_list function for every string that needs to be converted to list
    rec_movies = convert_to_list(rec_movies)
    rec_posters = convert_to_list(rec_posters)
    cast_names = convert_to_list(cast_names)
    cast_chars = convert_to_list(cast_chars)
    cast_profiles = convert_to_list(cast_profiles)
    cast_bdays = convert_to_list(cast_bdays)
    cast_bios = convert_to_list(cast_bios)
    cast_places = convert_to_list(cast_places)
    
    # convert string to list (eg. "[1,2,3]" to [1,2,3])
    cast_ids = cast_ids.split(',')
    cast_ids[0] = cast_ids[0].replace("[","")
    cast_ids[-1] = cast_ids[-1].replace("]","")
    
    # rendering the string to python string
    for i in range(len(cast_bios)):
        cast_bios[i] = cast_bios[i].replace(r'\n', '\n').replace(r'\"','\"')
    
    # combining multiple lists as a dictionary which can be passed to the html file so that it can be processed easily and the order of information will be preserved
    movie_cards = {rec_posters[i]: rec_movies[i] for i in range(len(rec_posters))}
    
    casts = {cast_names[i]:[cast_ids[i], cast_chars[i], cast_profiles[i]] for i in range(len(cast_profiles))}

    cast_details = {cast_names[i]:[cast_ids[i], cast_profiles[i], cast_bdays[i], cast_places[i], cast_bios[i]] for i in range(len(cast_places))}

    # web scraping to get user reviews from IMDB site
    sauce = urllib.request.urlopen('https://www.imdb.com/title/{}/reviews?ref_=tt_ov_rt'.format(imdb_id)).read()
    soup = bs.BeautifulSoup(sauce,'lxml')
    soup_result = soup.find_all("div",{"class":"text show-more__control"})

    reviews_list = [] # list of reviews
    reviews_status = [] # list of comments (good or bad)
    for reviews in soup_result:
        if reviews.string:
            reviews_list.append(reviews.string)
            # passing the review to our model
            movie_review_list = np.array([reviews.string])
            movie_vector = vectorizer.transform(movie_review_list)
            pred = clf.predict(movie_vector)
            reviews_status.append('Good' if pred else 'Bad')

    # combining reviews and comments into a dictionary
    movie_reviews = {reviews_list[i]: reviews_status[i] for i in range(len(reviews_list))}     

    # passing all the data to the html file
    # return render_template('recommend.html',title=title,poster=poster,overview=overview,vote_average=vote_average,
    #     vote_count=vote_count,release_date=release_date,runtime=runtime,status=status,genres=genres,
    #     movie_cards=movie_cards,reviews=movie_reviews,casts=casts,cast_details=cast_details)
    
    context = {
            "title":title,
            "poster":poster,
            "overview":overview,
            "vote_average":vote_average,
            "vote_count":vote_count,
            "release_date":release_date,
            "runtime":runtime,
            "status":status,
            "genres":genres,
            "movie_cards":movie_cards,
            "reviews":movie_reviews,
            "casts":casts,
            "cast_details":cast_details
    }
    html_content = render_to_string("recommend.html",context)

    response_data = {
        "template":html_content
    }
    return HttpResponse(json.dumps(response_data), content_type='application/javascript')