import tkinter as tk

counter = 0
selected_items = []

all_bill = 0
ame_all_bill = 0
ade_all_bill = 0
tea_all_bill = 0
smoo_all_bill = 0

way = ""
input_money = 0

def money_all():
    global input_money
    input_money = int(entry.get())
    label.config(text = f"{input_money}원 이 충전되었습니다")

def switching_frame01_out():
    global way#----나중에 문제 발생 가능성 있음
    frame0.grid_forget()
    frame1.grid()
    way = "포장"

def switching_frame01_in():
    global way
    frame0.grid_forget()
    frame1.grid()
    way = "매장"

def switching_frame12():
    frame1.pack_forget()
    frame2.grid()

def added_label(message=""):
    label.config(text=f"{counter} 개 담았습니다. {message}\n  선택된 항목:\n{'\n'.join(selected_items)}")

def all_payments():
    global all_bill , ame_all_bill , ade_all_bill , tea_all_bill , smoo_all_bill
    ame1_bill = selected_items.count('아메리카노')*2900
    ame2_bill = selected_items.count('더치 커피')*2400
    ame3_bill = selected_items.count('헤이즐넛 아메리카노')*3400
    ame4_bill = selected_items.count('아메리카노 디카페인')*2400
    ame5_bill = selected_items.count('카푸치노')*3400
    ame6_bill = selected_items.count('카페라떼')*4000
    ame7_bill = selected_items.count('초코 라떼')*4900
    ame8_bill = selected_items.count('고구마 라떼')*5400
    ame9_bill = selected_items.count('말차 라떼')*5400
    ame_all_bill = ame1_bill + ame2_bill + ame3_bill + ame4_bill + ame5_bill + ame6_bill + ame7_bill + ame8_bill + ame9_bill

    ade1_bill = selected_items.count('복숭아 아이스티')*2900
    ade2_bill = selected_items.count('레몬 아이스티')*2900
    ade3_bill = selected_items.count('석류 에이드')*3900
    ade4_bill = selected_items.count('깔라만시 에이드')*3900
    ade5_bill = selected_items.count('자몽 에이드')*3400
    ade_all_bill = ade1_bill + ade2_bill + ade3_bill + ade4_bill + ade5_bill

    tea1_bill = selected_items.count('콤부차')*2900
    tea2_bill = selected_items.count('율무차')*2900
    tea3_bill = selected_items.count('보이차')*2900
    tea4_bill = selected_items.count('청귤차')*2900
    tea5_bill = selected_items.count('생강차')*3000
    tea6_bill = selected_items.count('페퍼민트 티')*2900
    tea_all_bill = tea1_bill + tea2_bill + tea3_bill + tea4_bill + tea5_bill + tea6_bill

    smoo1_bill = selected_items.count('망고 스무디')*4500
    smoo2_bill = selected_items.count('딸기 스무디')*4500
    smoo3_bill = selected_items.count('블루베리 스무디')*4900
    smoo4_bill = selected_items.count('플레인요거트 스무디')*4300
    smoo5_bill = selected_items.count('말차 스무디')*4500
    smoo6_bill = selected_items.count('모카 스무디')*5400
    smoo_all_bill = smoo1_bill + smoo2_bill + smoo3_bill + smoo4_bill + smoo5_bill + smoo6_bill

    all_bill = ame_all_bill + ade_all_bill + tea_all_bill + smoo_all_bill
    label_payment.config(text=f"총 금액 {all_bill}원 입니다.")
    if all_bill <= input_money:
        switching_frame12()
    else:
        label.config(text = "금액이 부족합니다. 다른 결제 수단을 이용해 주세요")

def button_clicked(item):
    global counter
    counter += 1
    selected_items.append(item)
    added_label()

def denied():
    global counter
    if counter > 0:
        counter -= 1
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

root = tk.Tk()
root.title('카페 키오스크')
root.geometry("18000x10000")

frame0 = tk.Frame(root)

button_switch1 = tk.Button(frame0, text="포장", command=switching_frame01_out , height = 10 , width = 10)
button_switch2 = tk.Button(frame0, text="매장", command=switching_frame01_in , height = 10 , width=10)

button_switch1.pack(pady = 30)
button_switch2.pack(pady = 30)
frame0.pack()

frame1 = tk.Frame(root)

button_ame1 = tk.Button(frame1, text="아메리카노\n2,900원", command=lambda: button_clicked("아메리카노"))
button_ame2 = tk.Button(frame1, text="더치 커피\n2,400원", command=lambda: button_clicked("더치 커피"))
button_ame3 = tk.Button(frame1, text="헤이즐넛 아메리카노\n3,400원", command=lambda: button_clicked("헤이즐넛 아메리카노"))
button_ame4 = tk.Button(frame1, text="아메리카노 디카페인\n2,400원", command=lambda: button_clicked("아메리카노 디카페인"))
button_ame5 = tk.Button(frame1, text="카푸치노\n3,400원", command=lambda: button_clicked("카푸치노"))
button_ame6 = tk.Button(frame1, text="카페라떼\n4,000원", command=lambda: button_clicked("카페라떼"))
button_ame7 = tk.Button(frame1, text="초코 라떼\n4,900원", command=lambda: button_clicked("초코 라떼"))
button_ame8 = tk.Button(frame1, text="고구마 라떼\n5,400원", command=lambda: button_clicked("고구마 라떼"))
button_ame9 = tk.Button(frame1, text="말차 라떼\n5,400원", command=lambda: button_clicked("말차 라떼"))

button_ade1 = tk.Button(frame1, text="복숭아 아이스티\n2900원", command=lambda: button_clicked("복숭아 아이스티"))
button_ade2 = tk.Button(frame1, text="레몬 아이스티\n2900원", command=lambda: button_clicked("레몬 아이스티"))
button_ade3 = tk.Button(frame1, text="석류 에이드\n3900원", command=lambda: button_clicked("석류 에이드"))
button_ade4 = tk.Button(frame1, text="깔라만시 에이드\n3900원", command=lambda: button_clicked("깔라만시 에이드"))
button_ade5 = tk.Button(frame1, text="자몽 에이드\n3400원", command=lambda: button_clicked("자몽 에이드"))

button_tea1 = tk.Button(frame1, text="콤부차\n2900원", command=lambda: button_clicked("콤부차"))
button_tea2 = tk.Button(frame1, text="율무차\n2900원", command=lambda: button_clicked("율무차"))
button_tea3 = tk.Button(frame1, text="보이차\n2900원", command=lambda: button_clicked("보이차"))
button_tea4 = tk.Button(frame1, text="청귤차\n2900원", command=lambda: button_clicked("청귤차"))
button_tea5 = tk.Button(frame1, text="생강차\n3000원", command=lambda: button_clicked("생강차"))
button_tea6 = tk.Button(frame1, text="페퍼민트 티\n3400원", command=lambda: button_clicked("페퍼민트 티"))

button_smoo1 = tk.Button(frame1, text="망고스무디\n4,500원", command=lambda: button_clicked("망고스무디"))
button_smoo2 = tk.Button(frame1, text="딸기 스무디\n4,500원", command=lambda: button_clicked("딸기 스무디"))
button_smoo3 = tk.Button(frame1, text="블루베리 스무디\n4,900원", command=lambda: button_clicked("블루베리 스무디"))
button_smoo4 = tk.Button(frame1, text="플레인요거트 스무디\n4,300원", command=lambda: button_clicked("플레인요거트 스무디"))
button_smoo5 = tk.Button(frame1, text="말차 스무디\n4,500원", command=lambda: button_clicked("말차 스무디"))
button_smoo6 = tk.Button(frame1, text="모카 스무디\n5,400원", command=lambda: button_clicked("모카 스무디"))

# 가용 금액
entry = tk.Entry(frame1)
entry.pack(side = "bottom" , anchor = "e")

money_enter = tk.Button(frame1 , text = "입금" , command = money_all)
money_enter.pack(side = "bottom" , anchor = "e")
# 메뉴 버튼
label_menu1 = tk.Label(frame1 , text = "COFFEE")
label_menu1.pack(side = "top" , anchor = "nw")

button_ame1.pack(side = "top" , anchor = "nw")
button_ame2.pack(side = "top" , anchor = "nw")
button_ame3.pack(side = "top" , anchor = "nw")
button_ame4.pack(side = "top" , anchor = "nw")
button_ame5.pack(side = "top" , anchor = "nw")
button_ame6.pack(side = "top" , anchor = "nw")
button_ame7.pack(side = "top" , anchor = "nw")
button_ame8.pack(side = "top" , anchor = "nw")
button_ame9.pack(side = "top" , anchor = "nw")

label_menu2 = tk.Label(frame1 , text = "에이드")
label_menu1.pack(side = "top")

button_ade1.pack(side = "top" , anchor = "n")
button_ade2.pack(side = "top" , anchor = "n")
button_ade3.pack(side = "top" , anchor = "n")
button_ade4.pack(side = "top" , anchor = "n")
button_ade5.pack(side = "top" , anchor = "n")

label_menu3 = tk.Label(frame1 , text = "차(TEA)")
label_menu1.pack(side = "top")

button_tea1.pack(side = "top" , anchor = "ne")
button_tea2.pack(side = "top" , anchor = "ne")
button_tea3.pack(side = "top" , anchor = "ne")
button_tea4.pack(side = "top" , anchor = "ne")
button_tea5.pack(side = "top" , anchor = "ne")
button_tea6.pack(side = "top" , anchor = "ne")

label_menu1 = tk.Label(frame1 , text = "COFFEE")
label_menu1.pack(padx = 10 , pady = 250)

button_smoo1.pack(side = "top" , anchor = "e")
button_smoo2.pack(side = "top" , anchor = "e")
button_smoo3.pack(side = "top" , anchor = "e")
button_smoo4.pack(side = "top" , anchor = "e")
button_smoo5.pack(side = "top" , anchor = "e")
button_smoo6.pack(side = "top" , anchor = "e")
# 메뉴 추가/취소/결제 버튼
button_pay = tk.Button(frame1, text="결제", command=all_payments)
button_deny = tk.Button(frame1, text="취소", command=denied)
button_delall = tk.Button(frame1, text="전체 취소", command=button_delall)

button_pay.pack(side = "bottom" , anchor = "se")
button_deny.pack(side = "bottom" , anchor = "se")
button_delall.pack(side = "bottom" , anchor = "se")

frame1.pack()
frame1.pack_forget()

frame2 = tk.Frame(root)

label_thx = tk.Label(frame2, text="구매해 주셔서 감사합니다. 즐거운 시간 보내세요")
label_thx.pack(pady = 30)

button_billprint = tk.Button(frame2, text="영수증 출력", command = print_bill)
button_billprint.pack(pady = 30)

frame2.pack()
frame2.pack_forget()

label = tk.Label(root, text="")
label.pack(side = "bottom" , anchor = "sw")

label_count = tk.Label(root, text="")
label_count.pack(side = "bottom" , anchor = "sw")

label_payment = tk.Label(root, text="")
label_payment.pack(side = "bottom" , anchor = "sw")

root.mainloop()
