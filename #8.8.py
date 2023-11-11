loai_phong=input("Nhập vào loại phòng(từ 1-8): ")
so_dem=int(input("Nhập vào số đêm"))
if so_dem == 1:
    so_tien={"1":1260000,"2":1550000,"3":183000,"4":1830000,"5":2120000,"6":2120000,"7":2540000,"8":480000}[loai_phong]*so_dem
    print("Số tiền =",so_tien)
elif so_dem <3:
    so_tien={"1":1260000,"2":1550000,"3":183000,"4":1830000,"5":2120000,"6":2120000,"7":2540000,"8":480000}[loai_phong]*so_dem*75/100
    print("Số tiền =",so_tien)  
else:
    so_tien={"1":1260000,"2":1550000,"3":183000,"4":1830000,"5":2120000,"6":2120000,"7":2540000,"8":480000}[loai_phong]*so_dem*70/100
    print("Số tiền =",so_tien)  