from tkinter import *
from tkinter import ttk
from random import *

f=open("kysimused2.txt")
andmed=f.readlines()
f.close()

#KÕIK VAJALIKUD MUUTUJAD TEKITAME VÄLJASPOOL FUNKTSIOONE, ET MITTE SAADA 100 VIGA IGA REA KOHTA
küsimuste_arv=len(andmed)
küsimusi_ala_kohta=küsimuste_arv//5 #kategooriaid on 5, seega küsimusi kategooria kohta n/5
küsitud_küsimused=[] #takistame korduvate küsimuste küsimist
mäng="Y" # vajalik restardi jaoks
elud=3;küsimusi_vastatud=0
ajalugu=0;geograafia=0;sport=0;teadus=0;kultuur=0 #kroonid
vastus="";kasutaja_vastus=""; kasutaja_valik=""; kategooria=""
küsimuse_silt="";ajaloo_silt="";geograafia_silt="";spordi_silt="";teaduse_silt="";kultuuri_silt="" #neile hakkame labeleid omistama
teine_kord=False
kroon=False

def algus():
    global teine_kord; global vastus;global elud; global küsimusi_vastatud; global kroon;global kasutaja_valik #globaalseid muutujaid peab pidevalt muutma
    global küsimuse_silt; global ajaloo_silt;global geograafia_silt;global spordi_silt;global teaduse_silt;global kultuuri_silt; global kategooria
    global ajalugu;global geograafia; global sport; global teadus; global kultuur
    
     #valime arvu, mis saab olema küsimuse listi indeksiks
    
    if teine_kord and küsimusi_vastatud!=3: #esimesel korral see ei lähe meil töölegi
        kasutaja_vastus=kasutaja_sisend.get()
        if kasutaja_vastus==vastus:
            messagebox.showinfo(message="ÕIGE VASTUS")
            küsimusi_vastatud+=1
            if kroon==True:#KAS SAAB KROONI VÕI MITTE
                if kasutaja_valik=="A":
                    ajalugu+=1;kategooria="AJALUGU"
                elif kasutaja_valik=="B":
                    geograafia+=1;kategooria="GEOGRAAFIA"
                elif kasutaja_valik=="C":
                    sport+=1;kategooria="SPORT"
                elif kasutaja_valik=="D":
                    teadus+=1;kategooria="TEADUS"
                elif kasutaja_valik=="E":
                    kultuur+=1;kategooria="KULTUUR"
                messagebox.showinfo(message="Palju õnne, võitsite järgmise krooni: "+kategooria)
                küsimusi_vastatud-=1
                kroon=False
        else:
            messagebox.showinfo(message="VALE VASTUS, ÕIGE VASTUS ON "+vastus)
            elud-=1
    juhuslik_valik=randint(0, küsimuste_arv-1)
    if küsimusi_vastatud!=3:       
        if juhuslik_valik>-1 and juhuslik_valik<küsimusi_ala_kohta:
            kategooria="AJALUGU"
        elif juhuslik_valik>küsimusi_ala_kohta-1 and juhuslik_valik<küsimusi_ala_kohta*2:
            kategooria="GEOGRAAFIA"
        elif juhuslik_valik>küsimusi_ala_kohta*2-1 and juhuslik_valik<küsimusi_ala_kohta*3:
            kategooria="SPORT"
        elif juhuslik_valik>küsimusi_ala_kohta*3-1 and juhuslik_valik<küsimusi_ala_kohta*4:
            kategooria="TEADUS"
        elif juhuslik_valik>küsimusi_ala_kohta*4-1 and juhuslik_valik<küsimusi_ala_kohta*5:
            kategooria="KULTUUR"   
        messagebox.showinfo(message="Valitud kategooria on: "+kategooria)
    elif küsimusi_vastatud==3:
         #KEERULINE OSA , POLE VEEL HEAD SKEEMI VÄLJA MÕELNUD. Peaks kuvama valiku aladest (a,b,c,d,e) ning kui kasutaja sisestab enda valiku ja vajutab nuppu
        #peaks järgmisel korral tekkima just õige kategooria küsimus. Kusjuures enne nuppu vajutust ei tohi tööle minna õige vastuse funktsioon. Arvatavasti kuvamise peaks ikkagi viima õige vastuse funktsiooni...
        if kroon==False:
            
            messagebox.showinfo(message="""PALJU ÕNNE, VASTASITE KOLMELE KÜSIMUSELE ÕIGESTI.
NÜÜD SAATE KROONIKÜSIMUSELE VASTATA""")
            küs.destroy();VarA.destroy();VarB.destroy();VarC.destroy();VarD.destroy()
            
            küsimuse_silt=ttk.Label(raam, text="Vali kategooria"); küsimuse_silt.place(y=100,x=10)
            ajaloo_silt=ttk.Label(raam, text="Ajalugu - A"); ajaloo_silt.place(y=120,x=10)
            geograafia_silt=ttk.Label(raam, text="Geograafia - B"); geograafia_silt.place(y=140,x=10)
            spordi_silt=ttk.Label(raam, text="Sport - C"); spordi_silt.place(y=160,x=10)
            teaduse_silt=ttk.Label(raam, text="Teadus - D"); teaduse_silt.place(y=180,x=10)
            kultuuri_silt=ttk.Label(raam, text="Kultuur - E"); kultuuri_silt.place(y=200,x=10)
            kroon=True
        else:
            küsimuse_silt.destroy(); ajaloo_silt.destroy();geograafia_silt.destroy();spordi_silt.destroy();teaduse_silt.destroy();kultuuri_silt.destroy()
            kasutaja_valik=kasutaja_sisend.get()
            if kasutaja_valik=="A":
                juhuslik_valik=randint(0, küsimusi_ala_kohta-1)
            elif kasutaja_valik=="B":
                juhuslik_valik=randint(küsimusi_ala_kohta, küsimusi_ala_kohta*2-1)
            elif kasutaja_valik=="C":
                juhuslik_valik=randint(küsimusi_ala_kohta*2, küsimusi_ala_kohta*3-1)
            elif kasutaja_valik=="D":
                juhuslik_valik=randint(küsimusi_ala_kohta*3, küsimusi_ala_kohta*4-1)
            elif kasutaja_valik=="E":
                juhuslik_valik=randint(küsimusi_ala_kohta*4, küsimusi_ala_kohta*5-1)
            küsimusi_vastatud=0
            print(juhuslik_valik)
        
            
    info.destroy() #kustutame selle jura pärast esimest vajutust
    elude_inf=ttk.Label(raam, text="Elusid jäänud: "+str(elud));elude_inf.place(x=10,y=20)
    küsimuste_inf=ttk.Label(raam, text="Küsimusi vastatud: "+str(küsimusi_vastatud));küsimuste_inf.place(x=100,y=20)
    kroonid=ttk.Label(raam, text="KROONID: Ajaloo kroon: "+str(ajalugu)+", Geograafia kroon: "+str(geograafia)+", Spordi kroon: "+str(sport));kroonid.place(x=10,y=40)
    kroonid2=ttk.Label(raam, text="Teaduse kroon: "+str(teadus)+", Kultuuri kroon: "+str(kultuur)); kroonid2.place(x=10,y=60)
     #SIIA ALLA TULEVAD LISATINGIMUSED
    def õige_vastus(küsimus): #Funktsioon otsustab ära, milline on õige vastus ja kuvab kogu kasutajale vajaliku info ekraanile
        global küs;global VarA; global VarB; global VarC; global VarD
        if teine_kord:
            küs.destroy();VarA.destroy();VarB.destroy();VarC.destroy();VarD.destroy()
            
               
        küsimus=küsimus.strip().split(";")
        küs=ttk.Label(raam, text=küsimus[0]); küs.place(y=100,x=10) #siin topima väljundi ekraanile
        VarA=ttk.Label(raam, text=küsimus[1].strip("*"));VarA.place(y=120,x=10)
        VarB=ttk.Label(raam, text=küsimus[2].strip("*"));VarB.place(y=140, x=10)
        VarC=ttk.Label(raam, text=küsimus[3].strip("*"));VarC.place(y=160, x=10)
        VarD=ttk.Label(raam, text=küsimus[4].strip("*"));VarD.place(y=180,x=10)
        for element in küsimus:
            if "*" in element:
                vastus=element.strip("*").split(")")[0]
        return vastus
    if küsimusi_vastatud!=3:
        vastus=õige_vastus(andmed[juhuslik_valik])      
    teine_kord=True

raam=Tk()
raam.title("Trivia Crack")
raam.geometry("300x400")
kasutaja_sisend=ttk.Entry(raam);kasutaja_sisend.place(y=320,x=120,width=60) #seda võiks kuidagi peita enne esimest vajutust
info=ttk.Label(raam, text="Siia kirjutada mängu reeglid", font=("Times new roman", 16)); info.place(y=40,x=10)
nupp=ttk.Button(raam, text="Jätkamiseks vajuta siia", command=algus)
nupp.place(y=350, x=80 ,width=140)