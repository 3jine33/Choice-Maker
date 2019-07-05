from django.shortcuts import render
import random
def home(request):
    return render(request, 'home.html')

def aboutus(request):
    return render(request, 'aboutus.html')

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
    foodList[15] = '토마토 파스타'
    foodList[16] = '양념치킨'
    foodList[17] = '순대국'
    foodList[18] = '짬뽕'
    foodList[19] = '초밥'
    foodList[20] = '팟타이'
    foodList[21] = '팬케이크'
    foodList[22] = '해장국'
    foodList[23] = '제육볶음'
    foodList[24] = '라면'
    foodList[25] = '삼겹살'   
    foodList[26] = '햄버거' 
    i = random.randint(1,4)

    img_name = foodList[i] + ".PNG"

    return render(request,'food.html',{ 'img_name' : img_name})
#랜덤 

def new (request):
    if request.method == 'POST' and request.FILES['image']:
        myfile = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'new.html', {'uploaded_file_url': uploaded_file_url})
    return render(request, 'new.html')

