from django import forms
from .models import Post
from .models import M1_Train_data
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class M1_dataForm(forms.ModelForm):
    class Meta:
        model = M1_Train_data
        fields =['bmi','location','triglycerides','hdl','ldl','sex','waist',
                 'systolic_pressure','diastolic_pressure','fbs','old','smoke',
                 'alcohol_hepatitis',]
        labels = {'bmi' : 'BMI 지수',
                  'location' : '시도코드',
                  'triglycerides' : '트리글리세라이드',
                  'hdl': 'HDL 지수',
                  'ldl': 'LDL 지수',
                  'sex': '성별',
                  'waist': '허리둘레',
                  'systolic_pressure': '수축기 혈압',
                  'diastolic_pressure': '이완기 혈압',
                  'fbs': '공복혈당 지수',
                  'old': '연령',
                  'smoke': '흡연 상태',
                  'alcohol_hepatitis':'알콜성 감염 여부', }