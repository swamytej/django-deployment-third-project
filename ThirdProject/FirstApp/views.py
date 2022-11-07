from django.shortcuts import render

# Create your views here.
def employees1(request):
    return render(request,'FirstApp/employees1.html');


def employees2(request):
    return render(request,'FirstApp/employees2.html');



import datetime
def wishes3(request):
    date1=datetime.datetime.now()
    msg1='Hello priya/Client...GOOD';
    hr=int(date1.strftime('%H'));
    imgs='image1.jpg';
    if hr<12:
        msg1+=' Morning!!'
        imgs = 'image1.jpg';
    elif hr<16:
        msg1+=' Afternoon!!'
        imgs = 'image2.jpg';
    elif hr<20:
        msg1+=' Evening!!'
        imgs = 'image3.jpg';
    else:
        msg1='Hello priya/Client...Very Good Night!!'
        imgs = 'image4.jpg';
    dict1={'date1':date1,'msg1':msg1,'imgs':imgs}
    return render(request,'FirstApp/wishes3.html',context=dict1);



def imagegallery(request):
    date1 = datetime.datetime.now()
    msg1 = '***DJango-Image-Gallery***';
    dict1 = {'date1': date1, 'msg1': msg1}
    return render(request, 'FirstApp/imgsgallery.html', context=dict1);


def imagegallery2(request):
    date1 = datetime.datetime.now()
    msg1 = '***DJango-Image-Gallery(Product)***';
    dict1 = {'date1': date1, 'msg1': msg1}
    return render(request, 'FirstApp/imagegallery2.html', context=dict1);

def wishes4(request):
    date1 = datetime.datetime.now()
    msg1 = 'hello teja/client....good mrng';
    dict1 = {'date1': date1, 'msg1': msg1}
    return render(request, 'FirstApp/wishes4.html', context=dict1);



def hyperlinks(request):
    date1 = datetime.datetime.now()
    msg1 = '***DJango-Hyperlinks***';
    dict1 = {'date1': date1, 'msg1': msg1}
    return render(request, 'FirstApp/hyperlinks.html', context=dict1);


