import json
import re

from django.http import HttpResponse
from django.shortcuts import render

from App.CFalgorithm import get_similar_movies
from.models import User, data_movies, Movieratings, Movielinks
from django.contrib import messages
import random,  MySQLdb
from imdb import IMDb

ia = IMDb()


# Create your views here.
def IndexPage(request):
    return render(request, 'Index.html')

def WelcomePage(request):
    return render(request, 'Welcome.html')

def testPage(request):
    return render(request, 'test.html')

def Ratepage(request):
    moviedata=data_movies.objects.all()
    # moviedt = {'moviedata':moviedata}
    # return render('Rate.html',locals())
    return render(request, 'Rate.html',{'moviedt':moviedata})

def show_view(request):
    movied = data_movies.objects.all()
    return render(request,'Rate.html',{'movies':movied})

from. import CFalgorithm
def get_rec(request):
    movieratedlist = []
    movieratedlist2 = []
    secondseries = []
    thirdseries = []
    genres_list_a = []
    data = {}
    movie_rec_genres_list = []
    if request.session['Email']:

        print(1)
        print(request.session['Email'])
        # print()
        login_user = User.objects.filter(Email=request.session['Email'])[0]

        movierated=Movieratings.objects.filter(user_id=login_user.id)
        for i in movierated:
            movieratedtuple= (i.moviename,i.userratings)
            movieratedlist.append(movieratedtuple)
    # print(movieratedlist[0])
    # print(type(movieratedlist[0]))
    # action_lover = [("(500) Days of Summer (2009)",5),
    #                 ("10 Cloverfield Lane (2016)",1),
    #                 ("10,000 BC (2008)",1),
    #                 ('American President, The (1995)',1),
    #                 ('Casino (1995)',1),
    #                 ('Waiting to Exhale (1995)', 1)]
    # print(action_lover[0])
    # print(type(action_lover[0]))
            movieratedlist2.append(i.moviename)
        similar_movies = pd.DataFrame()
        # print(similar_movies)
        for movie,rating in movieratedlist:
            similar_movies = similar_movies.append(get_similar_movies(movie,rating),ignore_index=True)
        # similar_movies.head()。
        # print(similar_movies.sum().sort_values(ascending=False))
        # print(type(similar_movies.sum().sort_values(ascending=False)))
        newseries=similar_movies.sum().sort_values(ascending=False)
        print(newseries)
        # print(newseries.index[0])
        # print(type(newseries.index[0]))
        secondseries=list(newseries.index)
        for i in range(len(movieratedlist2)):
            if movieratedlist2[i] in secondseries:
                secondseries.remove(movieratedlist2[i])
        thirdseries=secondseries[0:10]
        print(secondseries[0:10])


        for i in thirdseries:
            print(i)
            movie_rated = data_movies.objects.filter(title=i)[0]
            print(movie_rated)
            m_gerens = movie_rated.genres
            head, symbol, tail = m_gerens.partition('|')
            genres_list_a.append(head)
            #

            movie_rec_genres_list.append(i + m_gerens)
        list_genres = ['Action', 'Adventure', 'Animation',
                       "Children's", 'Comedy', 'Crime', 'Documentary', 'Drama',
                       'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery',
                       'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western', '(no genres listed)']

        list_genres_ratings = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # str1 = ['Action', 'Drama', 'Comedy', 'Action']
        n = 0
        for i in genres_list_a:
            if i == 'Action':
                list_genres_ratings[0] = list_genres_ratings[0] + 1
            elif i == 'Adventure':
                list_genres_ratings[1] = list_genres_ratings[1] + 1
            elif i == 'Animation':
                list_genres_ratings[2] = list_genres_ratings[2] + 1
            elif i == "Children's":
                list_genres_ratings[3] = list_genres_ratings[3] + 1
            elif i == 'Comedy':
                list_genres_ratings[4] = list_genres_ratings[4] + 1
            elif i == 'Crime':
                list_genres_ratings[5] = list_genres_ratings[5] + 1
            elif i == 'Documentary':
                list_genres_ratings[6] = list_genres_ratings[6] + 1
            elif i == 'Drama':
                list_genres_ratings[7] = list_genres_ratings[7] + 1
            elif i == 'Fantasy':
                list_genres_ratings[8] = list_genres_ratings[8] + 1
            elif i == 'Film-Noir':
                list_genres_ratings[9] = list_genres_ratings[9] + 1
            elif i == 'Horror':
                list_genres_ratings[10] = list_genres_ratings[10] + 1
            elif i == 'Musical':
                list_genres_ratings[11] = list_genres_ratings[11] + 1
            elif i == 'Mystery':
                list_genres_ratings[12] = list_genres_ratings[12] + 1
            elif i == 'Romance':
                list_genres_ratings[13] = list_genres_ratings[13] + 1
            elif i == 'Sci-Fi':
                list_genres_ratings[14] = list_genres_ratings[14] + 1
            elif i == 'Thriller':
                list_genres_ratings[15] = list_genres_ratings[15] + 1
            elif i == 'War':
                list_genres_ratings[16] = list_genres_ratings[16] + 1
            elif i == 'Western':
                list_genres_ratings[17] = list_genres_ratings[17] + 1
            else:
                list_genres_ratings[18] = list_genres_ratings[18] + 1
            n = n + 1
        m = 0
        for i in list_genres_ratings:
            if i == 0:
                list_genres_ratings[m] = 'false'
            #     print(1)
            # else:
            #     print(2)
            m = m + 1
            # print(m)
        for k, v in zip(list_genres, list_genres_ratings):
            data.update({k: v, }, )
        print(data)
    # for i in secondseries:
    # if request.session['Email']:
    #         login_user = User.objects.filter(Email=request.session['Email'])[0]
    #         # print(i)
    #         print(Movieratings.objects.filter(user_id=login_user.id,)[0])
            # if i==Movieratings.objects.filter(user_id=login_user.id).moviename:
            #     del secondseries[i]

    # thirdseries=secondseries.head()
    # print(thirdseries),
    #     movie_rec_genres_list = []
    #     for i in secondseries[0:10]:
    #         moviedetail = data_movies.objects.get(title=i)
    #         # a = moviedetail.all()
    #         # movie_list=moviedetail.objects.all()
    #         print(moviedetail.movieId)
    #         print(moviedetail.title)
    #         print(moviedetail.genres)
    #         movie_rec_genres_list.append(moviedetail.genres)
            # print(type(moviedetail.title))
            # return HttpResponse('detail-%s' % (context))
            # movie_Imdb = Movielinks.objects.filter(movieId=moviedetail.movieId)
            # print(movie_Imdb[0].imdbId)
            # movie_imdb = ia.get_movie(movie_Imdb[0].imdbId)
            # # print("Cover url: %s" % movie_imdb['cover url'])
            # str = movie_imdb['cover url']
            # head, symbol, tail = str.partition('@')
            # # print(head)
            # # print(head + '@._V1_SX1010_CR0,0,1010,1500_.jpg')
            # # print(tail)
            # # print(tail[0])
            # if tail[0] != '@':
            #     movie_poster_url = head + '@._V1_SX303_CR0,0,303,450_.jpg'
            # else:
            #     movie_poster_url = head + '@@._V1_SX303_CR0,0,303,450_.jpg'
            #
            # movie_poster_url_list.append(movie_poster_url)
    return render(request,'GetRec.html',{'rec_list': movie_rec_genres_list, 'data': json.dumps(data)})

def recommend(request):
    data = {}
    movieratedlist = []
    userratingslist = []
    genres_list = []
    # print(1)
    if request.session['Email']:
        # print(1)
        # print(request.session['Email'])
        # print()
        login_user = User.objects.filter(Email=request.session['Email'])[0]
        # print(login_user)
        # print(login_user.id)
        # print(type(login_user))
        movierated=Movieratings.objects.filter(user_id=login_user.id)
        for i in movierated:
            genres1 = data_movies.objects.filter(id=i.movieindex)[0]
            # print(genres1)
            movie_genres = genres1.genres
            head, symbol, tail = movie_genres.partition('|')
            # print(head)
            genres_list.append(head)
            # print(genres_list)
            userratingslist.append(i.userratings)
            # print(userratingslist)
            movieratedtuple= (i.moviename,i.userratings)
            movieratedlist.append(movieratedtuple)
            # print(movieratedtuple)
            # print(type(movieratedtuple))
            # del movieratedtuple

        list_genres = ['Action', 'Adventure', 'Animation',
                       "Children's", 'Comedy', 'Crime', 'Documentary', 'Drama',
                       'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery',
                       'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western', '(no genres listed)']

        list_genres_ratings = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # str1 = ['Action', 'Drama', 'Comedy', 'Action']
        n = 0
        for i in genres_list:
            if i == 'Action':
                list_genres_ratings[0] = list_genres_ratings[0] + userratingslist[n]
            elif i == 'Adventure':
                list_genres_ratings[1] = list_genres_ratings[1] + userratingslist[n]
            elif i == 'Animation':
                list_genres_ratings[2] = list_genres_ratings[2] + userratingslist[n]
            elif i == "Children's":
                list_genres_ratings[3] = list_genres_ratings[3] + userratingslist[n]
            elif i == 'Comedy':
                list_genres_ratings[4] = list_genres_ratings[4] + userratingslist[n]
            elif i == 'Crime':
                list_genres_ratings[5] = list_genres_ratings[5] + userratingslist[n]
            elif i == 'Documentary':
                list_genres_ratings[6] = list_genres_ratings[6] + userratingslist[n]
            elif i == 'Drama':
                list_genres_ratings[7] = list_genres_ratings[7] + userratingslist[n]
            elif i == 'Fantasy':
                list_genres_ratings[8] = list_genres_ratings[8] + userratingslist[n]
            elif i == 'Film-Noir':
                list_genres_ratings[9] = list_genres_ratings[9] + userratingslist[n]
            elif i == 'Horror':
                list_genres_ratings[10] = list_genres_ratings[10] + userratingslist[n]
            elif i == 'Musical':
                list_genres_ratings[11] = list_genres_ratings[11] + userratingslist[n]
            elif i == 'Mystery':
                list_genres_ratings[12] = list_genres_ratings[12] + userratingslist[n]
            elif i == 'Romance':
                list_genres_ratings[13] = list_genres_ratings[13] + userratingslist[n]
            elif i == 'Sci-Fi':
                list_genres_ratings[14] = list_genres_ratings[14] + userratingslist[n]
            elif i == 'Thriller':
                list_genres_ratings[15] = list_genres_ratings[15] + userratingslist[n]
            elif i == 'War':
                list_genres_ratings[16] = list_genres_ratings[16] + userratingslist[n]
            elif i == 'Western':
                list_genres_ratings[17] = list_genres_ratings[17] + userratingslist[n]
            else:
                list_genres_ratings[18] = list_genres_ratings[18] + userratingslist[n]
            n = n + 1
        m = 0
        for i in list_genres_ratings:
            if i == 0:
                list_genres_ratings[m] = 'false'
            #     print(1)
            # else:
            #     print(2)
            m = m + 1
            # print(m)
        for k, v in zip(list_genres, list_genres_ratings):
            data.update({k: v, }, )
        # print(data)
    # else:
    #     #     messages.success(request,'You must login first.')
    #     return render(request, 'Recommendation.html')
    # print(movieratedlist)
        # print(type(movieratedlist[0]))
    # movie_rated = Movieratings.objects.filter(user_id=yan)

    return render(request, 'Recommendation.html',{'movierated_list':movieratedlist, 'data': json.dumps(data)})

def detail(request,movienum):
    print(movienum)
    ia = IMDb()
    if movienum != None:
        moviedetail=data_movies.objects.get(pk=movienum)
        # a = moviedetail.all()
        # movie_list=moviedetail.objects.all()
        print(moviedetail.movieId)
        print(moviedetail.title)
        # print(type(moviedetail.title))
        # return HttpResponse('detail-%s' % (context))+++++++++
        movie_Imdb = Movielinks.objects.filter(movieId=moviedetail.movieId)
        print(movie_Imdb[0].imdbId)
        movie_imdb = ia.get_movie(movie_Imdb[0].imdbId)
        print("Cover url: %s" % movie_imdb['cover url'])
        str = movie_imdb['cover url']
        head, symbol, tail = str.partition('@')
        print(head)
        print(head + '@._V1_SX1010_CR0,0,1010,1500_.jpg')
        print(tail)
        print(tail[0])
        if tail[0] != '@':
            movie_poster_url = head + '@._V1_SX303_CR0,0,303,450_.jpg'
        else:
            movie_poster_url = head + '@@._V1_SX303_CR0,0,303,450_.jpg'
        # movie_imdb_a = movie_imdb['cover url'].strip("https://m.media-amazon.com/images/")
        # print(movie_imdb_a)
        # list=[]
        # list.append(movie_imdb_a)
        # print(list[0])
        if request.method == "POST":
            user_ratings = request.POST.get('star_ratings')
            print('test=', user_ratings)
            # if not movienum in Movieratings.movieindex:

            # else:
            #     messages.success(request, 'You have rated this movie.')
            if request.session['Email']:
                # print(1)
                # print(request.session['Email'])
                # print()
                login_user = User.objects.filter(Email=request.session['Email'])[0]
                print(login_user)
                print(login_user.id)

                print(type(login_user))
                # print(login_user.values())
                # list = login_user.values()
                # # print(list[0])
                # dict = list[0]
                # user_name=dict["Username"]
                # print(user_name)
                # print(dict["Username"])
                # print(login_user(0))
                #queryset: https://blog.csdn.net/bbwangj/article/details/79935470
                # print(request.User.Username)
            # else:
            #     print(2)

                # user= User.objects.filter(Username=user_name).values()
                #
                # print(user)
                # if exit(select * from Movieratings)
                m_rated=Movieratings.objects.filter(movieindex=movienum,user_id=login_user.id)
                # print(m_rated[0])
                if m_rated.exists():
                    messages.success(request, 'You have rated this movie.')
                else:
                    messages.success(request, 'Rate:' + request.POST['star_ratings'] + "  Rate Successfully..")

                    user = login_user
                    moviename = moviedetail.title
                    movieindex = movienum

                    userratings = user_ratings
                    Movieratings(user=user, moviename=moviename, movieindex=movieindex, userratings=userratings).save()
            else:
                print("You haven't login yet.")
        return render(request,'detail.html',  {'movie_detail': moviedetail, 'movie_poster1': movie_poster_url})


def Userreg(request):
    if request.method=='POST':
        Username=request.POST['Username']
        Email=request.POST['Email']
        Pwd=request.POST['Pwd']
        User(Username=Username,Email=Email,Pwd=Pwd).save()
        messages.success(request, 'The New User   '+request.POST['Username']+ "   Is Saved Successfully..")
    #     return render(request,'Register.html')
    # else:
    return render(request,'Register.html')

def loginpage(request):
    if request.method=="POST":
        try:
            Userdetails=User.objects.get(Email=request.POST['Email'],Pwd=request.POST['Pwd'])
            print('Username=',Userdetails)
            request.session['Email']=Userdetails.Email
            return render(request,'Index.html')
        except User.DoesNotExist as e:
            messages.success(request,'Username / Password Invalid..')
    return render(request,'Login.html')

def logout(request):
    try:
        del request.session['Email']
    except:
        return render(request,'Index.html')
    return render(request, 'Index.html')


import pandas as pd
def review(request):
    # def getrate_random():
    list1 = []
    list2 = []
    list3 = []

    movie_list = []
    x = pd.tseries
    for i in range(5):
        yan = random.randint(0, 9999)
        movies = data_movies.objects.filter(id=yan)

        for movie in movies:
            print(movie.title)
            list2.append(movie.title)
        list1.append(yan)
    print(list1)
    print(list2)
    if request.method == "POST":
         test=request.POST.get('starratings')
         print('test=',test)
         messages.success(request, 'Rate:' + request.POST['starratings']+"  Rate Successfully..")

    # answer = request.POST['starratings',False]
    # print(answer)
    return render(request,'Review.html',{"list_1":list2})


