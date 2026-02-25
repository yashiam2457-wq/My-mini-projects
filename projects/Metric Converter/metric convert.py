from tkinter import *
from tkinter import ttk
class converter():
    def __init__(self):
        self.angles={"Radian":"Rad","Degree":"\N{DEGREE SIGN}","Gradian":"Grad"}
        self.lengths={"Metre":"m","Kilometre":"km","Centimetre":"cm","Milimetre":"mm","Micrometre":"\u03bcm","Nanometre":"nm","Parsecs":"pc","Light Years":"ly","Astrnomical":"ab","Rack":"U","Nautical Mile":"nmi","Mile":"mi","Cable":"cb","Fathoms":"ftm","Yards":"yd","Inches":"in","Feets":"ft","Points":"pt"}
        self.speeds=["Metre per second","Kilometre per second","Kilometre per hour","Miles per hour","Feets per second","Knots"]
        self.spdu=["m/s","km/s","km/h","mile/h","ft/s","kt"]
        self.areas=["Square metre","Hectares","Acres","Ares","Square Foot","Square inch","Square Kilometre","Square Centimetre","Square Milimetre"]
        self.aru=["m\u00b2","ha","acres","ares","ft\u00b2","in\u00b2","km\u00b2","cm\u00b2","mm\u00b2"]
        self.volumes=["Cubic metre","Liter","Mili Liter","Micro Liter","Gallon","Quarts","Pints","Cups","Cubic feet","Cubic inch"]
        self.volu=["m\u00b3","L","mL","\u03bcL","gal","qt","pt","cup","ft\u00b3","in\u00b3"]
        self.masses=["Grams","Tonn","Pounds","Ounces","Stones","Kilograms","Miligrams"]
        self.massu=["gm","T","lb","oz","st","kg","mg"]
        self.times=["Seconds","Minutes","Hours","Days","Weeks","Months","Years","Decades","Centuries"]
        self.timeu=["s","min","h","d","weeks","months","years","decades","centuries"]
        self.temper=["Kelvin","Celsius","Fahrenheit","Rakine"]
        self.tempu=["K","\N{DEGREE SIGN}C","\N{DEGREE SIGN}F","\N{DEGREE SIGN}R"]
        self.datas=["Nibbles","Bits","Bytes",
                    "Kilobytes","Megabytes","Gigabytes","Terabytes","Petabytes","Exabytes","Zettabytes","Yottabytes"
                    "Kibibytes","Mibibytes","Gibibytes","Tebibytes","Pebibytes","Exbibytes","Zebibytes","Yobibytes"]
        self.datau=["nibble","b","B","kB","MB","GB","TB","PB","EB","ZB","YB""kiB","MiB","GiB","TiB","PiB","EiB","ZiB","YiB"]
    #unit measurements
    #to
    def yocto_to(self,x):#y
        return x*10**(-24)
    def zepto_to(self,x):#z
        return x*10**(-21)
    def atto_to(self,x):#a
        return x*10**(-18)
    def femto_to(self,x):#f
        return x*10**(-15)
    def pico_to(self,x):#p
        return x*10**(-12)
    def nano_to(self,x):#n
        return x*10**(-9)
    def micro_to(self,x):#mu
        return x*10**(-6)
    def mili_to(self,x):#m
        return x/1000
    def centi_to(self,x):#c
        return x/100
    def deci_to(self,x):#d
        return x/10
    def deca_to(self,x):#da
        return x*10
    def hecto_to(self,x):#h
        return x*100
    def kilo_to(self,x):#h
        return x*1000
    def mega_to(self,x):#M-million
        return x*10**6
    def giga_to(self,x):#G-billion
        return x*10**9
    def tera_to(self,x):#T-Trillion
        return x*10**12
    def petta_to(self,x):#P-quadrillion
        return x*10**15
    def exa_to(self,x):#E-quintillion
        return x*10**18
    def zetta_to(self,x):#Z-sextillion
        return x*10**21
    def yotta_to(self,x):#Y-septillion
        return x*10**24
    #from
    def to_yocto(self,x):
        return x*10**24
    def to_zepto(self,x):
        return x*10**21
    def to_atto(self,x):
        return x*10**18
    def to_femto(self,x):
        return x*10**15
    def to_pico(self,x):
        return x*10**12
    def to_nano(self,x):
        return x*10**9
    def to_micro(self,x):
        return x*10**6
    def to_mili(self,x):
        return x*1000
    def to_centi(self,x):
        return x*100
    def to_deci(self,x):
        return x*10
    def to_deca(self,x):
        return x/10
    def to_hecto(self,x):
        return x/100
    def to_kilo(self,x):
        return x/1000
    def to_mega(self,x):
        return x*10**(-6)
    def to_giga(self,x):
        return x*10**(-9)
    def to_tera(self,x):
        return x*10**(-12)
    def to_petta(self,x):
        return x*10**(-15)
    def to_exa(self,x):
        return x*10**(-18)
    def to_zetta(self,x):
        return x*10**(-21)
    def to_yotta(self,x):
        return x*10**(-24)
    #length-                     km,cm,mm,nm,micro m
    #to m
    def parsecs_to(self,x):
        return x*3.0857*10**16
    def light_year_to(self,x):
        return x*9.4607*10**15
    def astronomical_to(self,x):
        return x*1.496*10**11
    def rack_to(self,x):
        return x*0.0445
    def nautical_mile_to(self,x):
        return x*1852
    def mile_to(self,x):
        return x*1609.344
    def cable_to(self,x):
        return x*219.456
    def fathoms_to(self,x):
        return x*1.8288
    def yard_to(self,x):
        return x*0.9144
    def feet_to(self,x):
        return x*0.3048
    def inch_to(self,x):
        return x*0.0254
    def point_to(self,x):#screen pixel
        return x*0.0004#1pt
    #from m
    def to_parsecs(self,x):
        return x/(3.0857*10**16)
    def to_light_year(self,x):
        return x/(9.4607*10**15)
    def to_astronomical(self,x):
        return x/(1.496*10**11)
    def to_rack(self,x):
        return x/0.0445
    def to_nautical_mile(self,x):
        return x/1852
    def to_mile(self,x):
        return x/1609.344
    def to_cable(self,x):
        return x/219.456
    def to_fathoms(self,x):
        return x/1.8288
    def to_yard(self,x):
        return x/0.9144
    def to_feet(self,x):
        return x/0.3048
    def to_inch(self,x):
        return x/0.0254
    def to_point(self,x):#screen pixel
        return x*2834.6#1pt
    #angle
    #to degree
    def radian_to(self,x):
        return x*57.2958
    def gradian_to(self,x):
        return x*0.9
    #from degree
    def to_radian(self,x):
        return x*0.0175
    def to_gradian(self,x):
        return x*1.1111
    #speed
    #to mps or m/s
    def kmph_to(self,x):
        return x*3.6
    def milesph_to(self,x):
        return x*2.2369
    def feetps_to(self,x):
        return x*3.2808
    def knot_to(self,x):
        return x*1.9438
    def kmps_to(self,x):
        return x*10**(-3)
    #from mps or m/s
    def to_kmph(self,x):
        return x/3.6
    def to_milesph(self,x):
        return x/2.2369
    def to_feetps(self,x):
        return x/3.2808
    def to_knot(self,x):
        return x/1.9438
    def to_kmps(self,x):
        return x*1000
    #area-  km^2,cm^2,mm^2
    #to m^2
    def hectares_to(self,x):
        return x*10**(-4)
    def acres_to(self,x):
        return x/4046.8564
    def sqfoot_to(self,x):
        return x*10.7639
    def ares_to(self,x):
        return x*100
    def sqinch_to(self,x):
        return x/1550.0031
    #from m^2
    def to_hectares(self,x):
        return x*10000
    def to_acres(self,x):
        return x*4046.8564
    def to_sqfoot(self,x):
        return x/10.7639
    def to_ares(self,x):
        return x/100
    def to_sqinch(self,x):
        return x*1550.0031
    #volume-           ml,micro L
    #to m^3
    def liter_to(self,x):
        return x*10**(-3)
    def gallon_to(self,x):
        return x/264.172
    def quarts_to(self,x):
        return x/1056.6883
    def pints_to(self,x):
        return x/2113.3763
    def cups_to(self,x):
        return x/4000
    def cbfeet_to(self,x):
        return x/35.314667
    def cbinch_to(self,x):
        return x/61023.7440947
    #from m^3
    def to_liter(self,x):
        return x*1000
    def to_gallon(self,x):
        return x*264.172
    def to_quarts(self,x):
        return x*1056.6883
    def to_pints(self,x):
        return x*2113.3763
    def to_cups(self,x):
        return x*4000
    def to_cbfeet(self,x):
        return x*35.314667
    def to_cbinch(self,x):
        return x*61023.7440947
    #Mass-                kg,mg
    #to g
    def tonn_to(self,x):
        return x*10**6
    def pounds_to(self,x):
        return x*453.5924
    def ounces_to(self,x):
        return x*28.3495
    def stone_to(self,x):
        return x*6350.293
    #from g
    def to_tonn(self,x):
        return x*10**(-6)
    def to_pounds(self,x):
        return x/453.5924
    def to_ounces(self,x):
        return x/28.3495
    def to_stone(self,x):
        return x/6350.293
    #time
    #to seconds
    def minutes_to(self,x):
        return x*60
    def hours_to(self,x):
        return x*3600
    def days_to(self,x):             #1440 min
        return x* 86400    #sec
    def weeks_to(self,x):            # 168 h=10080 min
        return x*604800
    def months_to(self,x):          #4.3482 weeks=30.4375 days=730.5 h=43830 min
        return x*2629800
    def years_to(self,x):           #52.1786 weeks=365.25 days=8766 h=525960 min
        return x*31557600
    def decades_to(self,x):
        return x*315576000
    def centuries_to(self,x):
        return x*3155760000
    #from seconds
    def to_minutes(self,x):
        return x/60
    def to_hours(self,x):
        return x/3600
    def to_days(self,x):            
        return x/86400    
    def to_weeks(self,x):          
        return x/604800
    def to_months(self,x):         
        return x/2629800
    def to_years(self,x):
        return x/31557600
    def to_decades(self,x):
        return x/315576000
    def to_centuries(self,x):
        return x/3155760000
    #temperature
    #to kelvin
    def celsius_to(self,x):
        return x+273.15
    def fahrenheit_to(self,x):
        return ((x-32)*5/9)+273.15
    def rakine_to(self,x):
        return x/1.8
    #from kelvin
    def to_celsius(self,x):
        return x-273.15
    def to_fahrenheit_to(self,x):
        return ((x-273.15)*9/5)+32
    def to_rakine(self,x):
        return x*1.8
    #frequency only have hertz,Khz,Mhz,Ghz,Thz so metric can work
    #Data size
    #to bytes
    def nibble_to(self,x):
        return x/2
    def bits_to(self,x):
        return x/8
    def kibi_to(self,x):
        return x/1024
    def mibi_to(self,x):
        return x*1024**(-2)
    def gibi_to(self,x):
        return x*1024**(-3)
    def tebi_to(self,x):
        return x*1024**(-4)
    def pebi_to(self,x):
        return x*1024**(-5)
    def exbi_to(self,x):
        return x*1024**(-6)
    def zebi_to(self,x):
        return x*1024**(-7)
    def yobi_to(self,x):
        return x*1024**(-8)
    #from bytes
    def to_nibble(self,x):
        return x*2
    def to_bits(self,x):
        return x*8
    def to_kibi(self,x):
        return x*1024
    def to_mibi(self,x):
        return x*1024**2
    def to_gibi(self,x):
        return x*1024**3
    def to_tebi(self,x):
        return x*1024**4
    def to_pebi(self,x):
        return x*1024**5
    def to_exbi(self,x):
        return x*1024**6
    def to_zebi(self,x):
        return x*1024**7
    def to_yobi(self,x):
        return x*1024**8
    #Tip
    def tipcal(self,x,y,z):#x=subtotal y=split z=tip%
        return x*z/100,x+(x*z/100),(x+(x*z/100))/y
             #tip , total , splits
def apptabs(z,tab,y):#x=x.angles
    x=converter()
    def evalen():
        anr={("Radian","Degree"):x.radian_to(float(en1.get())),("Degree","Radian"):x.to_radian(float(en1.get())),("Radian","Gradian"):x.radian_to(x.to_gradian(float(en1.get()))),("Gradian","Radian"):x.gradian_to(x.to_radian(float(en1.get()))),("Degree","Gradian"):x.to_gradian(float(en1.get())),("Gradian","Degree"):x.gradian_to(float(en1.get()))}
        if (an1.get(),an2.get()) not in anr.keys():
            uplab(xe=en1.get())
        else:
            print(an1.get(),an2.get())
            uplab(xe=anr[(an1.get()),(an2.get())])
    def uplab(xe):
        print(x.anu[an1.get()],x.anu[an2.get()])
        enlab1.config(text=f"{en1.get()} {x.anu[an1.get()]} = {xe} {x.anu[an2.get()]}")
    def revc():
        f=an1.get() 
        an1.set(an2.get())
        an2.set(f)
        evalen()
    an1=StringVar(tab)
    an2=StringVar(tab)
    conb=Button(tab,text="TO",command=revc)
    angle1=ttk.OptionMenu(tab,an1,an1,*z,command=evalen)
    angle2=ttk.OptionMenu(tab,an2,an2,*z,command=evalen)
    en1=Entry(tab,validate="key",bg="darkgray")
    en1.grid(row=0,column=1,sticky="ew")
    enlab1=Label(tab,text="0 "+y[0]+" = 0 "+y[1],bg="black",fg="white")
    print(an1.get(),'go')
    enlab1.grid(row=0,column=2,sticky="ew")
    angle1.grid(row=2,column=0,ipadx=5,sticky="ew")
    conb.grid(row=2,column=1)
    angle2.grid(row=2,column=2,ipadx=5,sticky="ew")
    an1.set(z[0])
    an2.set(z[1])
def main():
    b=["DEL","(",")","/","7","8","9","*","4","5","6","-","1","2","3","+",".","0","%","="]
    root=Tk()
    x=converter()
    root.title("Unit Converter")
    root.geometry("520x280")
    tab=ttk.Notebook(root)
    angle=ttk.Frame(tab)
    length=ttk.Frame(tab)
    speed=ttk.Frame(tab)
    area=ttk.Frame(tab)
    volume=ttk.Frame(tab)
    data=ttk.Frame(tab)
    timec=ttk.Frame(tab)
    mass=ttk.Frame(tab)
    temp=ttk.Frame(tab)
    tip=ttk.Frame(tab)
    tab.add(angle,text="Angle")
    tab.add(length,text="Length")
    tab.add(speed,text="Speed")
    tab.add(area,text="Area")
    tab.add(volume,text="Volume")
    tab.add(data,text="Data")
    tab.add(timec,text="Time")
    tab.add(mass,text="Mass")
    tab.add(temp,text="Temperature")
    tab.add(tip,text="Tip")
    tab.grid(row=0,column=0,columnspan=30,sticky="ew")
    apptabs(x.angles,angle,x.anu)
    apptabs(x.lengths,length,x.lenu)
    apptabs(x.speeds,speed,x.spdu)
    apptabs(x.areas,area,x.aru)
    apptabs(x.volumes,volume,x.volu)
    apptabs(x.datas,data,x.datau)
    apptabs(x.times,timec,x.timeu)
    apptabs(x.masses,mass,x.massu)
    apptabs(x.temper,temp,x.tempu)
    def clr():
        tab.nametowidget(tab.select()).winfo_children()[3].delete(0,END)
        uplab()
    def bk():
        t=tab.nametowidget(tab.select()).winfo_children()[3]
        c=t.get()
        t.delete(0,END)
        t.insert(END,c[:-1])
    def uplab(r="0"):
        t=tab.nametowidget(tab.select()).winfo_children()[4]
        l=tab.nametowidget(tab.select()).winfo_children()[3]
        e=t.cget("text").split(" ")
        print(str(l.get()),e[1],r,e[-1])
        t.config(text=f"{str(l.get())} {e[1]} = {r} {e[-1]}")
    def inen(s):
        t=tab.nametowidget(tab.select()).winfo_children()[3]
        e=t.get()
        t.delete(0,END)
        t.insert(END,e+str(s))
        if t.get().isnumeric():
            evalen()
    def evalen():
        t=tab.nametowidget(tab.select()).winfo_children()[1].cget("text")
        l=tab.nametowidget(tab.select()).winfo_children()[2].cget("text")
        e=tab.nametowidget(tab.select()).winfo_children()[3].get()
        print(t,l,e)
        if e=="":
            return
        elif not e.isnumeric():
            tab.nametowidget(tab.select()).winfo_children()[4].config(text="UNKNOWN VARIABLE")
            return
        anr={("Radian","Degree"):x.radian_to(float(e)),("Degree","Radian"):x.to_radian(float(e)),("Radian","Gradian"):x.radian_to(x.to_gradian(float(e))),("Gradian","Radian"):x.gradian_to(x.to_radian(float(e))),("Degree","Gradian"):x.to_gradian(float(e)),("Gradian","Degree"):x.gradian_to(float(e))}
        #lenr={(x.lengths[0],x.length[1])}
        if "frame" in str(tab.select()):
            
            print(str(tab.nametowidget(tab.select())))
            uplab(anr[(t,l)])
    for i in tab.nametowidget(tab.select()).winfo_children():
        print(i)
    Button(root,text="CLEAR",font=("Arial",16),width=5,command=clr).grid(row=1,column=0,sticky="ew")
    Button(root,text="DEL",font=("Arial",16),width=5,command=bk).grid(row=1,column=1,sticky="nsew")
    Button(root,text="(",font=("Arial",16),width=5,command=lambda g="(":inen(g)).grid(row=1,column=2,sticky="nsew")
    Button(root,text=")",font=("Arial",16),width=5,command=lambda g=")":inen(g)).grid(row=1,column=3,sticky="nsew")
    Button(root,text="/",font=("Arial",16),width=5,command=lambda g="/":inen(g)).grid(row=1,column=4,sticky="nsew")
    Button(root,text="7",font=("Arial",16),width=5,command=lambda g="7":inen(g)).grid(row=2,column=1,sticky="nsew")
    Button(root,text="8",font=("Arial",16),width=5,command=lambda g="8":inen(g)).grid(row=2,column=2,sticky="nsew")
    Button(root,text="9",font=("Arial",16),width=5,command=lambda g="9":inen(g)).grid(row=2,column=3,sticky="nsew")
    Button(root,text="*",font=("Arial",16),width=5,command=lambda g="*":inen(g)).grid(row=2,column=4,sticky="nsew")
    Button(root,text="4",font=("Arial",16),width=5,command=lambda g="4":inen(g)).grid(row=3,column=1,sticky="nsew")
    Button(root,text="5",font=("Arial",16),width=5,command=lambda g="5":inen(g)).grid(row=3,column=2,sticky="nsew")
    Button(root,text="6",font=("Arial",16),width=5,command=lambda g="6":inen(g)).grid(row=3,column=3,sticky="nsew")
    Button(root,text="-",font=("Arial",16),width=5,command=lambda g="-":inen(g)).grid(row=3,column=4,sticky="nsew")
    Button(root,text="1",font=("Arial",16),width=5,command=lambda g="1":inen(g)).grid(row=4,column=1,sticky="nsew")
    Button(root,text="2",font=("Arial",16),width=5,command=lambda g="2":inen(g)).grid(row=4,column=2,sticky="nsew")
    Button(root,text="3",font=("Arial",16),width=5,command=lambda g="3":inen(g)).grid(row=4,column=3,sticky="nsew")
    Button(root,text="+",font=("Arial",16),width=5,command=lambda g="+":inen(g)).grid(row=4,column=4,sticky="nsew")
    Button(root,text=".",font=("Arial",16),width=5,command=lambda g=".":inen(g)).grid(row=5,column=1,sticky="nsew")
    Button(root,text="0",font=("Arial",16),width=5,command=lambda g="0":inen(g)).grid(row=5,column=2,sticky="nsew")
    Button(root,text="%",font=("Arial",16),width=5,command=lambda g="/100":inen(g)).grid(row=5,column=3,sticky="nsew")
    Button(root,text="=",font=("Arial",16),width=5,command=evalen).grid(row=5,column=4,sticky="nsew")
    root.mainloop()
if __name__=="__main__":
    main()
    #x=converter(10)
    #print(x.to_gibi())