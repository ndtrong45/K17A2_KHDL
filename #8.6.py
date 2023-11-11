loai_xe=int(input("Nhập vào loại xe(4 hoặc 7): "))
so_km=float(input("Nhập vào số km: "))
thoi_gian_cho=float(input("Nhập vào thời gian chờ: "))
if loai_xe == 4 :
    if so_km <= 0.8 :
        tien_di_chuyen=11000*so_km
    elif 0.8 < so_km < 21:
        tien_di_chuyen=12100*so_km
    else:
        tien_di_chuyen=10000*so_km 
if loai_xe == 7 :
    if so_km <= 0.8 :
        tien_di_chuyen=13000*so_km
    elif 0.8 < so_km < 21:
        tien_di_chuyen=14100*so_km
else:
    tien_di_chuyen=12000*so_km 
if thoi_gian_cho <= 5:
    tien_cho=0
else:
    tien_cho=800*(thoi_gian_cho - 5)
print("Tiền cước: ",tien_cho+tien_di_chuyen) 