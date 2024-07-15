
def select_level(level):
    list_9x9 = "yeki az jadvalaye amade"
    unchangable_list = "تو لیست میگرده اونایی که عددن رو مختصاتشو تو یه لیست ثبت میکنه  [[x1,y1],[x2,y2],[...]....]"
    return list_9x9 ,unchangable_list


def check_raw(list_9x9):
    return True or False

def check_column(list_9x9):
    return True or False

def check_box(list_9x9):
    return True or False


def reset(list_9x9 , unchangable_list):
    "به جز اون مقدارای ثایت بقیه رو پاک می کنه"

    return "list_9x9_new"

def show(list_9x9):
    "اینو خودم نوشتم  لیستو چاپ می کنه"
    pass




def delete(list_9x9 , unchangable_list, X , Y):
    "list_9x9[x][y] = # اگه مختصات قابل تغییر نبود ارور بده اگه نبود به جای عددش # بزاره" 

    return "list_9x9_new"
    


def add(number ,list_9x9 , X , Y):
    "اگه خونه  ای که گفت خالی بود یعنی برابر # بود عدد داده شده رو ثبت کنه اگر نه خظا بده"
    if list_9x9[X][Y] == "#":
        list_temp = list_9x9.copy()
        list_temp[X][Y] = number

        "اگه هر سه نای این چک ها درست بودن اد کنه اگر نه ارور بده"
        if check_box(list_temp) and check_column(list_temp) and check_raw(list_temp):
            list_9x9[X][Y] = number
        else:
            "eror bede"
    else:
        "eror bede"



def start_game(list_9x9 , unchangable_list):
    while True:
        show(list_9x9)
        inp = input()
        if "delete":
            list_9x9 = delete(list_9x9 , unchangable_list , X , Y)
        if "add":
            list_9x9 = add(number ,list_9x9 , X , Y)
        if "reset":
            list_9x9 = reset(list_9x9 , unchangable_list)
        if "اگه همه خونه ها پر شد و تناقض نداشت میگیم بردی":
            "winner"

#=========================================================== menu asli ===========================================================

while True:# از کاربر میپرسه میخوای بازی کنی یا خارج بشی یا قوانین رو ببینی
    if "start" :
        start_game(select_level())
    else:
        exit()