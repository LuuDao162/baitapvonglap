dau_vao = input("Nhập vào 2 số: ")
print(type(dau_vao))

print(type(dau_vao))
print(dau_vao)

dau_vao_splited = dau_vao.split(" ")

start = int(dau_vao_splited[0])
end = int(dau_vao_splited[1])
print(start, end)

if (start > end):
    print("Số thúc cần lớn hơn số bắt đầu!!")
else: 
    #Xử lý việc in kết quả:
    for i in range(start, end+1):
        if (i%3 == 0 and i%5 == 0):
            print("FizzBuzz")
        elif (i%5==0):
            print("Buzz")
        elif (i%3==0):
            print("Fizz")
        else:
            print(i)