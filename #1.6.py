alice_candies=int(input("Nhập vào số kẹo của Alice: "))
bob_candies=int(input("Nhập vào số kẹo của Bob: "))
carol_candies=int(input("Nhập vào số kẹo của Carol: "))
sum=alice_candies + bob_candies + carol_candies
to_smash = sum % 3
print("Số kẹo dư sau khi chia đều là: ",to_smash)