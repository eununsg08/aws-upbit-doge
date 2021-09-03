import pyupbit

access = "9LmhrSzVNr0ELpsrDoBVCpU2sAcncQcZVHzQuRRW"
secret = "xV0oZoFfPAqrKHyEv28OfyUp9mBTzfu3uisgQqud"
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-DOGE"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회