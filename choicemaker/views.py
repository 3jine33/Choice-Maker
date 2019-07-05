from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import random
from .models import Photo

def home(request):
    return render(request, 'home.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def movie(request) :
    value = 'movie'
    movieList = {}

    movieList[1] = '토이스토리'
    movieList[2] = '스파이더맨'
    movieList[3] = '코코'
    movieList[4] = '레미제라블'
    movieList[5] = '타이타닉'
    movieList[6] = '알라딘'
    movieList[7] = '겨울왕국'
    movieList[8] = '라푼젤'
    i = random.randint(1,8)

    img_name = movieList[i] + ".jpg"

    return render(request, 'movie.html', {'movieList' : movieList[i], 'img_name' : img_name})


def food(request):
    value = 'food'
    foodList = {}
    foodList[1] = '떡볶이'
    foodList[2] = '우동'
    foodList[3] = '피자'
    foodList[4] = '곱창'
    foodList[5] = '돈가스'
    foodList[6] = '라면'
    foodList[7] = '롤초밥'
    foodList[8] = '부대찌개'
    foodList[9] = '샐러드'
    foodList[10] = '쌀국수'
    foodList[11] = '스테이크'
    foodList[12] = '제육볶음'
    foodList[13] = '짜장면'
    foodList[14] = '초밥'
    foodList[15] = '양념치킨'
    foodList[16] = '순대국'
    foodList[17] = '짬뽕'
    foodList[18] = '초밥'
    foodList[19] = '팟타이'
    foodList[20] = '팬케이크'
    foodList[21] = '해장국'
    foodList[22] = '제육볶음'
    foodList[23] = '라면'
    foodList[24] = '삼겹살'   
    foodList[25] = '햄버거' 
    i = random.randint(1,25)

    img_name = foodList[i] + ".PNG"

    return render(request,'food.html',{'foodList':foodList[i], 'img_name' : img_name})

def new (request):
    if request.method == 'POST' :

        myfile1 = request.FILES.get('image1', '')
        myfile2 = request.FILES.get('image2', '')
        myfile3 = request.FILES.get('image3', '')
        myfile4 = request.FILES.get('image4', '')

        picturelist = {}
        picturelist[1] = myfile1
        picturelist[2] = myfile2
        picturelist[3] = myfile3
        picturelist[4] = myfile4

        i = random.randint(1,4)
        myfile = picturelist[i]

        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'newresult.html', {'uploaded_file_url': uploaded_file_url})
    else :
        return render(request, 'new.html')


def photo(request):
    photo = Photo.objects
    return render(request, 'home.html',{'photo':photo})

