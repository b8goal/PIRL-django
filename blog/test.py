import pandas as pd
import numpy as np
#from import_export import test
from sklearn.tree import DecisionTreeClassifier


## DecisionTree Test ##

def data_city(data):
    # 시도코드 범주형변수 연속형변수로 변경
    data["시도코드"] = data["시도코드"].replace(
        {11: "서울", 26: "부산", 27: "대구", 28: "인천", 29: "광주", 30: "대전", 31: "울산", 36: "세종", 41: "경기도", 42: "강원도", 43: "충북",
         44: "충남", 45: "전북", 46: "전남", 47: "경북", 48: "경남", 49: "제주"})
    data['추천병원'] = data.apply(city, axis=1)
    return data


# 고당지 예방사업 대상자 분류
def abnormal(data):
    cnt=0
    if (((data['성별코드']==1) & (data['HDL콜레스테롤']<40))|((data['성별코드']==2) & (data['HDL콜레스테롤']<50))):
        cnt += 1 
    if (((data['성별코드']==1) & (data['허리둘레']>=90))|((data['성별코드']==2) & (data['허리둘레']>=85))):
        cnt += 1
    if (((data['수축기혈압']>=130)|(data['이완기혈압']>=85))):
        cnt += 1
    if ((data['트리글리세라이드']>=150)):
        cnt += 1
    if (data['식전혈당(공복혈당)']>=100):
        cnt += 1
    if cnt >=3:
        return 1
    elif cnt <3:
        return 0

# 당뇨병 위험도
def diabetes_risk(data_w):
    data_w['dy'] = 51.1116 + (-1.2187 * data_w['성별코드']) + (1.3616 * data_w['연령대코드(5세단위)']) + (
                0.2219 * data_w['허리둘레']) + (0.1178 * data_w['수축기혈압']) + (-0.0173 * data_w['이완기혈압']) + (
                               0.0427 * data_w['트리글리세라이드']) + (-0.0020 * data_w['HDL콜레스테롤']) + (
                               -0.0402 * data_w['LDL콜레스테롤']) + (0.5043 * data_w['흡연상태']) + (
                               -1.5737 * data_w['알콜성간염여부']) + (0.1593 * data_w['BMI'])
    data_w['당뇨위험도'] = ((data_w['dy'] - 100) / (126 - 100) * 100) + 10
    data_w[data_w['dy'] >= 120]
    return data_w

# 고혈압 위험도
def High_blood_pressure(data_w):
    data_w['gy1'] = 75.7549 + (-3.4975 * data_w['성별코드']) + (1.1881 * data_w['연령대코드(5세단위)']) + (
                0.1391 * data_w['허리둘레']) + (0.0393 * data_w['식전혈당(공복혈당)']) + (0.0234 * data_w['트리글리세라이드']) + (
                                0.0746 * data_w['HDL콜레스테롤']) + (0.0022 * data_w['LDL콜레스테롤']) + (
                                -0.3170 * data_w['흡연상태']) + (0.3323 * data_w['알콜성간염여부']) + (0.7180 * data_w['BMI'])
    data_w['gy2'] = 50.6702 + (-2.5805 * data_w['성별코드']) + (0.3346 * data_w['연령대코드(5세단위)']) + (
                0.0679 * data_w['허리둘레']) + (0.0179 * data_w['식전혈당(공복혈당)']) + (0.0200 * data_w['트리글리세라이드']) + (
                                0.0567 * data_w['HDL콜레스테롤']) + (0.0128 * data_w['LDL콜레스테롤']) + (
                                0.0152 * data_w['흡연상태']) + (0.0171 * data_w['알콜성간염여부']) + (0.4667 * data_w['BMI'])
    data_w['고혈압위험도(수축)'] = (data_w['gy1'] - 120) / (140 - 120) * 100
    data_w['고혈압위험도(이완)'] = (data_w['gy2'] - 80) / (90 - 80) * 100
    return data_w

def g_danger(data_w):
    if data_w['고혈압위험도(수축)'] >= data_w['고혈압위험도(이완)']:
        return data_w['고혈압위험도(수축)']
    else :
        return data_w['고혈압위험도(이완)']

def city(row):
    if (row['시도코드'] == "서울") | (row['시도코드'] == "인천"):
        return "서울대병원"
    elif (row['시도코드'] == "대전"):
        return "을지병원"
    else:
        return "포항성모병원"

def Abnormal_lipid(data_w):
    # 총콜레스테롤을 일상데이터로 예측하는 모델
    data_w['zy1'] = 140.9385 + (5.8364 * data_w['성별코드']) + (0.3364 * data_w['연령대코드(5세단위)']) + (
                0.0312 * data_w['허리둘레']) + (-0.0923 * data_w['수축기혈압']) + (0.4293 * data_w['이완기혈압']) + (
                                -0.0475 * data_w['식전혈당(공복혈당)']) + (1.1031 * data_w['흡연상태']) + (
                                -5.1559 * data_w['알콜성간염여부']) + (0.8152 * data_w['BMI'])
    # 트리글리세라이드
    data_w['zy2'] = -98.8747 + (-4.1023 * data_w['성별코드']) + (1.3725 * data_w['연령대코드(5세단위)']) + (
                1.0172 * data_w['허리둘레']) + (0.0545 * data_w['수축기혈압']) + (0.4913 * data_w['이완기혈압']) + (
                                0.2436 * data_w['식전혈당(공복혈당)']) + (9.0455 * data_w['흡연상태']) + (
                                -6.3159 * data_w['알콜성간염여부']) + (1.7515 * data_w['BMI'])
    # HDL콜레스테롤
    data_w['zy3'] = 79.0985 + (5.2658 * data_w['성별코드']) + (-0.5458 * data_w['연령대코드(5세단위)']) + (
                -0.2058 * data_w['허리둘레']) + (0.0263 * data_w['수축기혈압']) + (0.0308 * data_w['이완기혈압']) + (
                                -0.0173 * data_w['식전혈당(공복혈당)']) + (-0.4091 * data_w['흡연상태']) + (
                                0.9784 * data_w['알콜성간염여부']) + (-0.4813 * data_w['BMI'])
    # LDL콜레스테롤
    data_w['zy4'] = 81.4303 + (1.2324 * data_w['성별코드']) + (0.5803 * data_w['연령대코드(5세단위)']) + (
                0.0413 * data_w['허리둘레']) + (-0.1272 * data_w['수축기혈압']) + (0.2978 * data_w['이완기혈압']) + (
                                -0.0784 * data_w['식전혈당(공복혈당)']) + (-0.2834 * data_w['흡연상태']) + (
                                -4.9449 * data_w['알콜성간염여부']) + (0.9410 * data_w['BMI'])
    data_w['이상지질혈증 위험도(총콜)'] = (data_w['zy1'] - 200) / (240 - 200) * 100
    data_w['이상지질혈증 위험도(트리)'] = (data_w['zy2'] - 150) / (200 - 150) * 100
    data_w['이상지질혈증 위험도(HDL)'] = (data_w['zy3'] - 60) / (40 - 60) * 100
    data_w['이상지질혈증 위험도(LDL)'] = (data_w['zy4'] - 100) / (160 - 100) * 100
    return data_w

def max_disease(row):
    return row[['이상지질혈증 위험도(총콜)','이상지질혈증 위험도(트리)',
                '이상지질혈증 위험도(HDL)','이상지질혈증 위험도(LDL)']].max()


def test_model(data):
    data = data_city(data) # 시도코드 정제를 통한 파생변수 추천병원 생성

    data_w = diabetes_risk(data)
    data_w = High_blood_pressure(data_w)
    data_w['고혈압위험도'] = data_w.apply(g_danger, axis=1)
    data_w = Abnormal_lipid(data_w)
    data_w['이상지질혈증 위험도'] = data_w.apply(max_disease, axis=1)
    data_w = data_w.round(3)
    dt = []
    dt.append(data_w['당뇨위험도'][0])
    dt.append(data_w['고혈압위험도'][0])
    dt.append(data_w['이상지질혈증 위험도'][0])
    return dt
