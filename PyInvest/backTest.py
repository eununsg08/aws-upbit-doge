import pyupbit
import numpy as np

#ohlcv = open, hight, low, close, volume 당일 시가, 고가, 저가, 종가, 거래량에 대한 데이터
df = pyupbit.get_ohlcv("KRW-DOGE", count=7)

#변동폭 * k 계산 = (고가 - 저가) * k값
df['range'] = (df['high'] - df['low']) * 0.1
# target(매수가), range 컬럼을 한칸씩 밑으로 내림(.shift(1))
df['target'] = df['open'] + df['range'].shift(1)

# ror(수익율), np.where(조건문, 참일때 값, 거짓일때 값)
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'],
                     1)

#누적 곱 계산(cumprod) => 누적 수익율
df['hpr'] = df['ror'].cumprod()
#Draw Down(하락폭) 계산(누적 최대 값과 현재 hpr 차이 / 누적 최대값 * 100)
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
#MDD(Max Draw Down)하락폭 최대값 계산
print("MDD(%): ", df['dd'].max())
#엑셀 저장
df.to_excel("도지코인 백테스팅 결과.xlsx")