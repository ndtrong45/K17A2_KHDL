nam = int(input('Nhập vào năm: '))
if (nam % 400 == 0) or ((nam % 4 == 0) and (nam % 100 != 0)):
    print('Đây là năm nhuận')
else:
    print('Đây không phải là năm nhuận')