
# 2006~2025 20년간 총 인구 수(단위: 천 명)
# https://www.index.go.kr/unify/idx-info.do?pop=1&idxCd=5060

populations = [48438, 48684, 49055, 49308, 49554
               , 49937, 50200, 50429, 50747, 51015
               , 51218, 51362, 51585, 51765, 51836
               , 51770, 51673, 51713, 51751, 51685]

# 2006~2025 20년간 총 인구 수 데이터만 가지고 2026~2035 인구 수를 예측하라.

# pip install wheel, scikit-learn, matplotlib

import matplotlib.pyplot as plt
import numpy as np

def calcRMSE(src, tar): # calculate RMSE(Root Mean Square Error)
    RMSE = None   # initial value. Not known yet.
    accSquareError = 0.0   # accumulated square error with initial value 0

    if len(src) != len(tar):
        pass
    else:
        if len(src) == 0 or len(tar) == 0:
            pass
        else:
            for idx in range(len(src)):
                error = src[idx] - tar[idx]
                squareError = error*error
                accSquareError = accSquareError + squareError

            avgSquareError = accSquareError/len(src)
            RMSE = np.sqrt(avgSquareError)

    return RMSE


# 분석 대상 데이터
populations = [48438, 48684, 49055, 49308, 49554
               , 49937, 50200, 50429, 50747, 51015
               , 51218, 51362, 51585, 51765, 51836
               , 51770, 51673, 51713, 51751, 51685]

# 데이터 전처리 없음.

# 1. Train test split(Test eval split)
popTest = populations[0:15] # test set
popEval = populations[15:]  # evaluation set

print('popTest:', popTest)
print('popEval:', popEval)


############################################
# 평균: 평균 변화량(AGA)
############################################



############################################
# 평균: 연평균 성장률(CAGR)
############################################

import math

# CAGR = (an/a1)^(1/(n-1)) - 1

############################################
# 이동평균: 단순(Moving Average)
############################################



############################################
# 이동평균: 가중(Weighted MA)
############################################



############################################
# 회귀분석: 단순 회귀(Linear Regression)
############################################

from sklearn.linear_model import LinearRegression

