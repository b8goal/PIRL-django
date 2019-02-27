from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from .forms import M1_dataForm
from django.shortcuts import redirect
from .disease_risk import init_risk
from .resources import TrainResource
from .test import test_model
from django.shortcuts import render
from tablib import Dataset
import pandas as pd

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post, 'train_datas':train_datas})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    risk_data = init_risk()
    a,b,c,d,e = risk_data['이상지질혈증 위험도(총콜)'][0], risk_data['이상지질혈증 위험도(트리)'][0], risk_data['이상지질혈증 위험도(HDL)'][0],risk_data['이상지질혈증 위험도(LDL)'][0], risk_data['이상지질혈증 위험도'][0]
    f,g,h,i,j = risk_data['이상지질혈증 위험도(총콜)'][1], risk_data['이상지질혈증 위험도(트리)'][1], risk_data['이상지질혈증 위험도(HDL)'][1], risk_data['이상지질혈증 위험도(LDL)'][1], risk_data['이상지질혈증 위험도'][1]
    k,l,m,n,o = risk_data['이상지질혈증 위험도(총콜)'][2], risk_data['이상지질혈증 위험도(트리)'][2], risk_data['이상지질혈증 위험도(HDL)'][2], risk_data['이상지질혈증 위험도(LDL)'][2], risk_data['이상지질혈증 위험도'][2]

    return render(request, 'blog/post_list.html', {'posts': posts ,'a':a,'b':b,'c':c,'d':d,'e':e,'f':f,'g':g,'h':h,'i':i,'j':j,'k':k,'l':l,'m':m,'n':n,'o':o,'risk_data':risk_data})

    #의사결정트리 예제
    #train_Accuracy_Data,test_Accuracy_Data = init_data()
    #return render(request, 'blog/post_list.html', {'posts': posts,'train_Accuracy_Data':train_Accuracy_Data,'test_Accuracy_Data':test_Accuracy_Data})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def M1_simple_upload2(request):
    if request.method == 'POST':
        train_resource = TrainResource()
        dataset = Dataset()
        new_train = request.FILES['myfile2']

        imported_data = dataset.load(new_train.read())
        result = train_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            train_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'core/simple_upload2.html')

def post_data_input(request):
    if request.method == "POST":
        form = M1_dataForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            raw_data = {'BMI' : [post.bmi],
                        '시도코드' : [post.location],
                        '트리글리세라이드' : [post.triglycerides],
                        'HDL콜레스테롤' : [post.hdl],
                        'LDL콜레스테롤' : [post.ldl],
                        '식전혈당(공복혈당)' : [post.fbs],
                        '성별코드' : [post.sex],
                        '허리둘레' : [post.waist],
                        '수축기혈압': [post.systolic_pressure],
                        '이완기혈압': [post.diastolic_pressure],
                        '연령대코드(5세단위)': [post.old // 5],
                        '흡연상태': [post.smoke],
                        '알콜성간염여부' :[post.alcohol_hepatitis],
                        }
            data = pd.DataFrame(raw_data)
            a,b,c= test_model(data)
            mx = int(max(a,b,c))
            mx=50
            return render(request, 'blog/post_result1.html', {'a':a,'b':b,'c':c,'mx':mx})
    else:
        form = M1_dataForm()
    return render(request, 'blog/post_data_input.html',{'form':form})
