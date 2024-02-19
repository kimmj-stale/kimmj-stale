import tkinter as tk

counter = 0
selected_items = []
all_bill = 0
ame_bill = 0
ade_bill = 0
tea_bill = 0
smoo_bill = 0
way = ""
input_money = 0

def money_all():
    global input_money
    input_money = int(entry.get())
    label.config(text = f"{input_money}원 이 충전되었습니다")

def switching_frame01_out():
    global way#----나중에 문제 발생 가능성 있음
    frame0.pack_forget()
    frame1.pack()
    way = "포장"

def switching_frame01_in():
    global way
    frame0.pack_forget()
    frame1.pack()
    way = "매장"

def switching_frame12():
    frame1.pack_forget()
    frame2.pack()

def all_payments():
    global all_bill , ame_bill , ade_bill , smoo_bill , tea_bill
    ame1_bill = selected_items.count('아메리카노(ICE)')*2900
    ame2_bill = selected_items.count('아메리카노(HOT)')*2400
    ame3_bill = selected_items.count('헤이즐넛 아메리카노')*3400
    ame4_bill = selected_items.count('아메리카노 디카페인')*2400
    ame5_bill = selected_items.count('카푸치노')*3400
    ame6_bill = selected_items.count('카페라떼')*4000
    ame7_bill = selected_items.count('초코 라떼')*4900

    ade1_bill = selected_items.count('복숭아 아이스티')*2900
    ade2_bill = selected_items.count('레몬 아이스티')*2900
    ade3_bill = selected_items.count('석류 에이드')*3900
    ade4_bill = selected_items.count('깔라만시 에이드')*3900
    ade5_bill = selected_items.count('자몽 에이드')*3400

    tea1_bill = selected_items.count('콤부차')*2900
    tea2_bill = selected_items.count('율무차')*2900
    tea3_bill = selected_items.count('보이차')*2900
    tea4_bill = selected_items.count('청귤차')*2900
    tea5_bill = selected_items.count('생강차')*3000
    tea6_bill = selected_items.count('페퍼민트 티')*2900

    smoo1_bill = selected_items.count('망고 스무디')*4500
    smoo2_bill = selected_items.count('딸기 스무디')*4500
    smoo3_bill = selected_items.count('블루베리 스무디')*4900
    smoo4_bill = selected_items.count('플레인요거트 스무디')*4300
    smoo5_bill = selected_items.count('말차 스무디')*4500
    smoo6_bill = selected_items.count('모카 스무디')*5400

    ame_bill = ame1_bill + ame2_bill + ame3_bill + ame4_bill + ame5_bill + ame6_bill + ame7_bill + ame8_bill + ame9_bill
    ade_bill = ade1_bill + ade2_bill + ade3_bill + ade4_bill + ade5_bill
    tea_bill = tea1_bill + tea2_bill + tea3_bill + tea4_bill + tea5_bill + tea6_bill
    smoo_bill = smoo1_bill + smoo2_bill + smoo3_bill + smoo4_bill + smoo5_bill + smoo6_bill

    all_bill = ame_bill + ade_bill + tea_bill + smoo_bill
    label_payment.config(text=f"총 금액 {all_bill}원 입니다.")

    if all_bill <= input_money:
        switching_frame12()
    else:
        label.config(text = "금액이 부족합니다. 다른 결제 수단을 이용해 주세요")
#버튼
def button_clicked_cafe():
    frame1.pack_forget()
    frame3.pack()

def button_clicked_ade():
    frame1.pack_forget()
    frame4.pack()

def button_clicked_tea():
    frame1.pack_forget()
    frame6.pack()

def button_clicked_smoo():
    frame1.pack_forget()
    frame7.pack()
#버튼 - 메뉴
def button_clicked(item):
    global counter
    counter = counter + 1
    selected_items.append(item)
    added_label()

def added_label(message = ""):
    label_msg = tk.Label(root , text = "")
    label_msg.config(text = f"{counter} 개 담았습니다. {message}\n  선택된 항목:\n{'\n'.join(selected_items)}")

def denied():
    global counter
    if counter > 0:
        counter =counter - 1
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
    label.config(text = f"주문해 주셔서 감사합니다. \n 총 주문 금액: {all_bill} \n 주문 목록:{selected_items} \n 주문 방식:{way}")

def button_cancel31():
    frame3.pack_forget()
    frame1.pack()

def button_cancel41(): 
    frame4.pack_forget()
    frame1.pack()

def button_cancel61():
    frame6.pack_forget()
    frame1.pack()

def button_cancel71():
    frame7.pack_forget()
    frame1.pack()

root = tk.Tk()
root.title('카페 키오스크')
root.geometry("1000x600")

frame0 = tk.Frame(root)

button_switch1 = tk.Button(frame0 , text = "포장" , command = switching_frame01_out , height = 10 , width = 10)
button_switch2 = tk.Button(frame0 , text = "매장" , command = switching_frame01_in , height = 10 , width = 10)

button_switch1.pack(side = "left" , anchor = "center" , padx = 15, pady = 15)
button_switch2.pack(side = "right" , anchor = "center" , padx = 15, pady = 15)
frame0.pack()

frame1 = tk.Frame(root)

button_ame = tk.Button(frame1 , text = "커피" , command = button_clicked_cafe)
button_ade = tk.Button(frame1 , text = "에이드" , command = button_clicked_ade)
button_tea = tk.Button(frame1 , text = "차" , command = button_clicked_tea)
button_smoo = tk.Button(frame1 , text = "스무디" , command = button_clicked_smoo)

button_ame.pack()
button_ade.pack()
button_tea.pack()
button_smoo.pack()

# 가용 금액
entry = tk.Entry(frame1)
entry.pack(side = "bottom" , anchor = "se")

money_enter = tk.Button(frame1 , text = "입금" , command = money_all)
money_enter.pack(side = "right" , anchor = "center")
# 메뉴 버튼
frame1.pack()
frame1.pack_forget()

frame2 = tk.Frame(root)

label_thx = tk.Label(frame2 , text = "구매해 주셔서 감사합니다. 즐거운 시간 보내세요")
label_thx.pack(side = "top", anchor = "center")

button_billprint = tk.Button(frame2 , text = "영수증 출력", command = print_bill)
button_billprint.pack(side="top" , anchor = "center")
#커피 화면
frame2.pack()
frame2.pack_forget()

frame3 = tk.Frame(root)

button_ame1 = tk.Button(frame3 , text = "아메리카노(ICE)" , command = button_clicked("아메리카노(ICE)"))
button_ame2 = tk.Button(frame3 , text = "아메리카노(HOT)" , command = button_clicked("아메리카노(HOT)"))
button_ame3 = tk.Button(frame3 , text = "헤이즐넛 아메리카노" , command = button_clicked("헤이즐넛 아메리카노"))
button_ame4 = tk.Button(frame3 , text = "아메리카노 디카페인" , command = button_clicked("아메리카노 디카페인"))
button_ame5 = tk.Button(frame3 , text = "카푸치노" , command = button_clicked("카푸치노"))
button_ame6 = tk.Button(frame3 , text = "카페라떼" , command = button_clicked("카페라떼"))
button_ame7 = tk.Button(frame3 , text = "초코 라떼" , command = button_clicked("초코 라떼"))

button_ame1.pack(side = "left" , anchor = "nw" , padx = 10, pady = 10)
button_ame2.pack(side = "left" , anchor = "nw" , padx = 10, pady = 10)
button_ame3.pack(side = "left" , anchor = "nw" , padx = 10, pady = 10)
button_ame4.pack(side = "left" , anchor = "nw" , padx = 10, pady = 10)
button_ame5.pack(side = "left" , anchor = "nw" , padx = 10, pady = 10)
button_ame6.pack(side = "left" , anchor = "nw" , padx = 10, pady = 10)
button_ame7.pack(side = "left" , anchor = "nw" , padx = 10, pady = 10)

button_return31 = tk.Button(frame3 , text = "뒤로" , command = button_cancel31)

button_pay = tk.Button(frame3 , text = "결제" , command = all_payments)
button_deny = tk.Button(frame3 , text = "취소" , command = denied)
button_delall = tk.Button(frame3 , text = "전체 취소" , command = button_delall)

button_pay.pack(side = "bottom" , anchor = "ne" , padx = 10, pady = 10)
button_deny.pack(side = "bottom" , anchor = "ne" , padx = 10, pady = 10)
button_delall.pack(side = "bottom" , anchor = "ne" , padx = 10, pady = 10)

button_return31.pack(side = "left" , anchor = "nw")

label = tk.Label(root, text = "")
label.pack(side="bottom", anchor = "sw")

label_count = tk.Label(root, text = "")
label_count.pack(side="bottom", anchor="sw")

label_payment = tk.Label(root, text="")
label_payment.pack(side = "bottom", anchor = "sw")

frame3.pack()
frame3.pack_forget()

frame4 = tk.Frame(root)

button_ade1 = tk.Button(frame4 , text = "복숭아 아이스티" , command = button_clicked("복숭아 아이스티"))
button_ade2 = tk.Button(frame4 , text = "레몬 아이스티" , command = button_clicked("레몬 아이스티"))
button_ade3 = tk.Button(frame4 , text = "석류 에이드" , command = button_clicked("석류 에이드"))
button_ade4 = tk.Button(frame4 , text = "깔라만시 에이드" , command = button_clicked("깔라만시 에이드"))
button_ade5 = tk.Button(frame4 , text = "자몽 에이드" , command = button_clicked("자몽 에이드"))

button_ade1.pack(side = "left" , anchor = "nw" , padx = 10, pady = 10)
button_ade2.pack(side = "left" , anchor = "nw" , padx = 10, pady = 10)
button_ade3.pack(side = "left" , anchor = "nw" , padx = 10, pady = 10)
button_ade4.pack(side = "left" , anchor = "nw" , padx = 10, pady = 10)
button_ade5.pack(side = "left" , anchor = "nw" , padx = 10, pady = 10)

button_pay = tk.Button(frame4 , text = "결제" , command = all_payments)
button_deny = tk.Button(frame4 , text = "취소" , command = denied)
button_delall = tk.Button(frame4 , text = "전체 취소" , command = button_delall)

button_pay.pack(side = "bottom" , anchor = "ne" , padx = 10, pady = 10)
button_deny.pack(side = "bottom" , anchor = "ne" , padx = 10, pady = 10)
button_delall.pack(side = "bottom" , anchor = "ne" , padx = 10, pady = 10)

label = tk.Label(root, text = "")
label.pack(side="bottom", anchor = "sw")

label_count = tk.Label(root, text = "")
label_count.pack(side="bottom", anchor="sw")

label_payment = tk.Label(root, text="")
label_payment.pack(side = "bottom", anchor = "sw")

frame4.pack()
frame4.pack_forget()

frame6 = tk.Frame(root)

button_tea1 = tk.Button(frame6 , text = "콤부차" , command = button_clicked("콤부차"))
button_tea2 = tk.Button(frame6 , text = "율무차" , command = button_clicked("율무차"))
button_tea3 = tk.Button(frame6 , text = "보이차" , command = button_clicked("보이차"))
button_tea4 = tk.Button(frame6 , text = "청귤차" , command = button_clicked("청귤차"))
button_tea5 = tk.Button(frame6 , text = "생강차" , command = button_clicked("생강차"))
button_tea6 = tk.Button(frame6 , text = "페퍼민트 티" , command = button_clicked("페퍼민트 티"))

button_tea1.pack(side = "left" , anchor = "nw" , padx = 10, pady = 10)
button_tea2.pack(side = "left" , anchor = "nw" , padx = 10, pady = 10)
button_tea3.pack(side = "left" , anchor = "nw" , padx = 10, pady = 10)
button_tea4.pack(side = "left" , anchor = "nw" , padx = 10, pady = 10)
button_tea5.pack(side = "left" , anchor = "nw" , padx = 10, pady = 10)
button_tea6.pack(side = "left" , anchor = "nw" , padx = 10, pady = 10)

button_pay = tk.Button(frame6 , text = "결제" , command = all_payments)
button_deny = tk.Button(frame6 , text = "취소" , command = denied)
button_delall = tk.Button(frame6 , text = "전체 취소" , command = button_delall)

button_pay.pack(side = "bottom" , anchor = "ne" , padx = 10, pady = 10)
button_deny.pack(side = "bottom" , anchor = "ne" , padx = 10, pady = 10)
button_delall.pack(side = "bottom" , anchor = "ne" , padx = 10, pady = 10)

label = tk.Label(root, text = "")
label.pack(side="bottom", anchor = "sw")

label_count = tk.Label(root, text = "")
label_count.pack(side="bottom", anchor="sw")

label_payment = tk.Label(root, text="")
label_payment.pack(side = "bottom", anchor = "sw")

frame6.pack()
frame6.pack_forget()

frame7 = tk.Frame(root)

button_smoo1 = tk.Button(frame7 , text = "망고 스무디" , command = button_clicked("망고 스무디"))
button_smoo2 = tk.Button(frame7 , text = "딸기 스무디" , command = button_clicked("딸기 스무디"))
button_smoo3 = tk.Button(frame7 , text = "블루베리 스무디" , command = button_clicked("블루베리 스무디"))
button_smoo4 = tk.Button(frame7 , text = "플레인요거트 스무디" , command = button_clicked("플레인요거트 스무디"))
button_smoo5 = tk.Button(frame7 , text = "말차 스무디" , command = button_clicked("말차 스무디"))
button_smoo6 = tk.Button(frame7 , text = "모카 스무디" , command = button_clicked("모카 스무디"))

button_smoo1.pack(side = "left" , anchor = "nw" , padx = 10, pady = 10)
button_smoo2.pack(side = "left" , anchor = "nw" , padx = 10, pady = 10)
button_smoo3.pack(side = "left" , anchor = "nw" , padx = 10, pady = 10)
button_smoo4.pack(side = "left" , anchor = "nw" , padx = 10, pady = 10)
button_smoo5.pack(side = "left" , anchor = "nw" , padx = 10, pady = 10)
button_smoo6.pack(side = "left" , anchor = "nw" , padx = 10, pady = 10)

button_pay = tk.Button(frame7 , text = "결제" , command = all_payments)
button_deny = tk.Button(frame7 , text = "취소" , command = denied)
button_delall = tk.Button(frame7 , text = "전체 취소" , command = button_delall)

button_pay.pack(side = "bottom" , anchor = "ne" , padx = 10, pady = 10)
button_deny.pack(side = "bottom" , anchor = "ne" , padx = 10, pady = 10)
button_delall.pack(side = "bottom" , anchor = "ne" , padx = 10, pady = 10)

label = tk.Label(root, text = "")
label.pack(side="bottom", anchor = "sw")

label_count = tk.Label(root, text = "")
label_count.pack(side="bottom", anchor="sw")

label_payment = tk.Label(root, text="")
label_payment.pack(side = "bottom", anchor = "sw")

frame7.pack()
frame7.pack_forget()


root.mainloop()
