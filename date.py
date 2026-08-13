
def get_date(n):
    if '/' in n :
        dd,mm,yyyy=n.split("/")

    elif '-' in n:
        dd,mm,yyyy=n.split("-")

    dd=int(dd)
    mm=int(mm)
    yyyy=int(yyyy)     

    if 0<dd<32 and 0<mm<13 :
        return print(f"{yyyy}-{mm}-{dd}")
    else:
        return print("DATE CANNOT BE PROCESSED")


date = get_date(input("what date?: "))


