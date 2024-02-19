import tkinter as tk

counter = 0
selected_items = []
all_bill = 0
input_money = 0
#def 파트 - 따로 만들어서 붙이기
def money_all():
    global input_money
    input_money = int(entry.get())
    label.config(text = f"{input_money}")

def switching_frame01_in():
    global way#----나중에 문제 발생 가능성 있음
    frame0.pack_forget()
    frame1.pack()
    way = "포장"

def switching_frame01_out():
    global way
    frame0.pack_forget()
    frame1.pack()
    way = "매장"

def switching_frame12():
    frame1.pack_forget()
    frame2.pack()

def added_label(message=""):
    label.config(text=f"{counter} 개 담았습니다. {message}\n  선택된 항목:\n{'\n'.join(selected_items)}")

def all_payments():
    global all_bill
    ame_bill = selected_items.count('아메리카노') * 2900
    ade_bill = selected_items.count('에이드') * 2900
    kafu_bill = selected_items.count('카푸치노') * 3900
    ble_bill = selected_items.count('블렌디드') * 4000
    smoo_bill = selected_items.count('스무디') * 4500
    all_bill = ame_bill + ade_bill + kafu_bill + ble_bill + smoo_bill
    label_payment.config(text=f"총 금액 {all_bill}원 입니다.")
    if all_bill <= input_money:
        switching_frame12()

def button_clicked(item):
    global counter
    counter = counter + 1
    selected_items.append(item)
    added_label()

def denied():
    global counter
    if counter > 0:
        counter = counter - 1
        removed_item = selected_items.pop()
        added_label(f"{removed_item} 이/가 취소되었습니다.")
    else:
        added_label("취소할 항목이 없습니다.")

def button_delall():
    global counter
    global selected_items
    counter = 0
    selected_items = []
    added_label("주문이 취소되었습니다.")

def print_bill():
    print("주문해 주셔서 감사합니다." , "총 주문 금액: " , all_bill , "주문 목록: " , selected_items , "주문 방식: " , way)


root = tk.Tk()
root.title('카페 키오스크')
root.geometry("1000x600")
#첫 번째 화면
frame0 = tk.Frame(root)

button_switch1 = tk.Button(frame0, text="포장", command=switching_frame01_in)
button_switch2 = tk.Button(frame0, text="매장", command=switching_frame01_out)

button_switch1.pack(side = "left" , anchor = "center" , padx = 50 , pady = 50)
button_switch2.pack(side = "right" , anchor = "center" , padx = 50 , pady = 50)
frame0.pack()
#두 번째 화면
frame1 = tk.Frame(root)

button_1 = tk.Button(frame1, text="아메리카노\n2900원", command=lambda: button_clicked("아메리카노"))
button_2 = tk.Button(frame1, text="에이드\n2900원", command=lambda: button_clicked("에이드"))
button_3 = tk.Button(frame1, text="카푸치노\n3900원", command=lambda: button_clicked("카푸치노"))
button_4 = tk.Button(frame1, text="블렌디드\n4000원", command=lambda: button_clicked("블렌디드"))
button_5 = tk.Button(frame1, text="스무디\n4500원", command=lambda: button_clicked("스무디"))

button_pay = tk.Button(frame1, text="결제", command=all_payments)
button_deny = tk.Button(frame1, text="취소", command=denied)
button_delall = tk.Button(frame1, text="전체 취소", command=button_delall)
#가용 금액
entry = tk.Entry(frame1)
entry.pack(side = "bottom" , anchor = "se")

# 메뉴 버튼
button_1.pack(side = "left", anchor = "nw" , padx = 10, pady = 10)
button_2.pack(side = "left", anchor = "nw" , padx = 10, pady = 10)
button_3.pack(side = "left", anchor = "nw" , padx = 10, pady = 10)
button_4.pack(side = "left", anchor = "nw" , padx = 10, pady = 10)
button_5.pack(side = "left", anchor = "nw" , padx = 10, pady = 10)
# 메뉴 추가/취소/결제 버튼
button_pay.pack(side="bottom", anchor="ne", padx=10, pady=10)
button_deny.pack(side="bottom", anchor="ne", padx=10, pady=10)
button_delall.pack(side="bottom", anchor="ne", padx=10, pady=10)

frame1.pack()
frame1.pack_forget()

frame2 = tk.Frame(root)

button_billprint = tk.Button(frame2 , text = "영수증 출력" , command = print_bill)
button_billprint.pack(side = "left" , anchor = "center")

label_tx = tk.Label(frame2 , text = "구매해 주셔서 감사합니다. 즐거운 시간 보내세요")
label_tx.pack(side = "top", anchor = "center")

frame2.pack()
frame2.pack_forget()

label = tk.Label(root, text="")
label.pack(side = "bottom" , anchor = "sw")

label_count = tk.Label(root, text="")
label_count.pack(side = "bottom" , anchor = "sw")

label_payment = tk.Label(root, text="")
label_payment.pack(side = "bottom" , anchor = "sw")

root.mainloop()