# -*- coding: UTF-8 -*-
from tkinter import *
onaika=Tk()
onaika.title("Sääse Pokker Technologies")
onaika.geometry("860x500")
onaika.configure(bg="black")
sortedby=2
sortedby2=0
sortorder="up"
sortorder2="up"
activeside="pl"
switching=0
tadacmts=1
passguessed=0

def stplayers():
    global activeside,switching
    if not activeside=="pl":
        activeside="pl"
        tog_players.config(relief="sunken")
        tog_games.config(relief="raised")
        pht_sbplgm()
        teeheader_pl()
        switching=1
        sbsoted_pl(sortedby)
        switching=0
def stgames():
    global activeside,switching
    if not activeside=="gm":
        activeside="gm"
        tog_players.config(relief="raised")
        tog_games.config(relief="sunken")
        pht_sbplgm()
        teeheader_gm()
        switching=1
        sbsoted_gm(sortedby2)
        switching=0
def popap():
    global npnaika,np_dnbox,np_rnbox
    npnaika=Tk()
    npnaika.title("New player")
    npnaika.geometry("670x330")
    npnaika.configure(bg="maroon")
    np_dn=Label(npnaika,text="Display Name",bg="maroon",
    font=("fixedsys",18,"bold"),fg="white")
    np_dn.grid(row=0,column=0,padx=35,pady=35,sticky="w")
    np_dnbox=Entry(npnaika,font=("fixedsys",18,"bold"))
    np_dnbox.grid(row=0,column=1)
    np_rn=Label(npnaika,text="Real Name",bg="maroon",
    font=("fixedsys",18,"bold"),fg="white")
    np_rn.grid(row=1,column=0,padx=35,sticky="w")
    np_rnbox=Entry(npnaika,font=("fixedsys",18,"bold"))
    np_rnbox.grid(row=1,column=1)
    np_in=Label(npnaika,text="Index",bg="maroon",
    font=("fixedsys",18,"bold"),fg="white")
    np_in.grid(row=2,column=0,padx=35,sticky="w")
    if tadacmts==1:
        np_x_v=str(len(lutec))
    else:
        np_x_v=str(len(lute))
    np_x=Label(npnaika,text=np_x_v,bg="maroon",
    font=("fixedsys",18,"bold"),fg="white")
    np_x.grid(row=2,column=1,pady=35,sticky="w")
    np_ok=Button(npnaika,text="OK",font=("fixedsys",18,"bold"),bg="white",
    command=np)
    np_ok.grid(row=3,column=0,pady=10,padx=50,ipadx=10,sticky="e")
    np_c=Button(npnaika,text="Cancel",font=("fixedsys",18,"bold"),
    command=lambda:npnaika.destroy(),bg="white")
    np_c.grid(row=3,column=1,pady=10,padx=50,sticky="w")
def np():
    lute.append([len(lute),np_dnbox.get(),np_rnbox.get(),1500,0,0,0,0,0,1])
    if activeside=="pl":
        sbsoted_pl_anp()
    os=open("players.txt","r",encoding="utf-8-sig")
    osdata=os.read()
    os.close()
    newosdata=osdata.replace("@",str(len(lute)-1)+" "+str(np_dnbox.get())+" "+str(np_rnbox.get())+"\n@")
    os=open("players.txt","w",encoding="utf-8-sig")
    os.write(newosdata)
    os.close()
    npnaika.destroy()
def popag():
    pass
def phtalumine():
    for label in asi.grid_slaves():
        if int(label.grid_info()["row"])>1:
            label.destroy()
def pht_sbplgm():
    tabel.destroy()
    asi.destroy()
    hd_tabel.destroy()
    hd_asi.destroy()
    kerija.destroy()
def sbsoted_pl_anp():
    global sortedby,lute,sortorder
    if sortorder=="up":
        lute=lute[::-1]
    lute=sorted(lute,key=lambda x : x[sortedby])
    if sortorder=="up":
        lute=lute[::-1]
    phtalumine()
    teetabel_pl()
def sbsoted_pl(sby):
    global sortedby,lute,sortorder
    if switching==0:
        if sortedby==sby:
            if sortorder=="down":
                sortorder="up"
            else:
                sortorder="down"
    if sortorder=="up":
        lute=lute[::-1]
    lute=sorted(lute,key=lambda x : x[sby])
    if sortorder=="up":
        lute=lute[::-1]
    phtalumine()
    teetabel_pl()
    sortedby=sby
def sbsoted_gm(sby):
    global sortedby2,lute2,sortorder2
    if switching==0:
        if sortedby2==sby:
            if sortorder2=="down":
                sortorder2="up"
            else:
                sortorder2="down"
    if sortorder2=="up":
        lute2=lute2[::-1]
    lute2=sorted(lute2,key=lambda x : x[sby])
    if sortorder2=="up":
        lute2=lute2[::-1]
    phtalumine()
    teetabel_gm()
    sortedby2=sby
def teeluted():
    lute=[]
    lute2=[]
    lutec=[]
    banned=[]
    try:
        osalejad=open("players.txt","r",encoding="utf-8-sig")
    except:
        osalejad=open("players.txt","w",encoding="utf-8-sig")
        osalejad.write("@")
        osalejad.close()
        osalejad=open("players.txt","r",encoding="utf-8-sig")
    while True:
        line=osalejad.readline().strip()
        if not line=="@":
            if line[0]=="€":
                line=line[1:]
                com=0
            else:
                com=1
            line=line.split()
            vsne=""
            for i in range(len(line)-2):
                vsne+=line[i+2]
                if not i+3==len(line):
                    vsne+=" "
            lute.append([int(line[0]),line[1],vsne,1500,0,0,0,0,0,com])
        else:
            break
    """lute: jrk nr, dn, rn, rnk, PI, pld, G, S, B, com"""
    try:
        sisend=open("games.txt","r",encoding="utf-8-sig")
    except:
        sisend=open("games.txt","w",encoding="utf-8-sig")
        sisend.write("@")
        sisend.close()
        sisend=open("games.txt","r",encoding="utf-8-sig")
    while True:
        rida=sisend.readline().strip()
        if rida[0]=="$":
            gdate=rida[1:]
        elif rida=="@":
            break
        else:
            gname=rida
            gtype=sisend.readline().strip()
            rida3=sisend.readline().strip().split()
            plrs=[]
            reskd=[]
            if gname.endswith("unc"):
                for g in range(int(len(rida3)/2)):
                    plrs.append(int(rida3[g*2]))
                    reskd.append(float(rida3[g*2+1]))
            else:
                for h in range(len(rida3)):
                    plrs.append(int(rida3[h]))
                    reskd.append((1-h/(len(rida3)-1))*2-1)
            lute2.append([len(lute2)+1,gname,gtype,gdate,len(plrs)])
            if len(plrs)>5:
                lute2[-1]=lute2[-1]+[str(lute[plrs[0]][1]),str(lute[plrs[1]][1]),str(lute[plrs[2]][1])]
            else:
                lute2[-1]=lute2[-1]+["-","-","-"]
            """lute2: game index, game name, game type, game date, NoP, G, S, B"""
            pldkd=[]
            for j in range(len(plrs)):
                pldkd.append(25**(1/(1/14*lute[plrs[j]][4]+2)))
                lute[plrs[j]][5]+=1
                lute[plrs[j]][4]+=len(plrs)
            ptdifkd=[]
            for q in range(len(plrs)):
                summa=0
                for k in range(len(plrs)):
                    if not q==k:
                        summa+=lute[plrs[k]][3]
                ptdif=summa/(len(plrs)-1)-lute[plrs[q]][3]
                if reskd[q]<0:
                    enn=-ptdif/50
                else:
                    enn=ptdif/50
                ptdifkd.append(11**(1+0.07*enn))
            enn2=(len(plrs)-1)**2
            nopk=(enn2/(500+enn2))**0.5*5
            if gname.endswith("unc"):
                nopk=1
                gname=gname[:-3]
            for r in range(len(plrs)):
                lute[plrs[r]][3]+=round(reskd[r]*pldkd[r]*ptdifkd[r]*nopk)
            if len(plrs)>5:
                lute[plrs[0]][6]+=1
                lute[plrs[1]][7]+=1
                lute[plrs[2]][8]+=1
            vahe=sisend.readline()
    for ac in range(len(lute)):
        if lute[ac][5]>4 and lute[ac][9]==1:
            lutec.append(lute[ac])
        else:
            banned.append(lute[ac][1])
    return lute,lute2,lutec,banned
def teeheader_pl():
    global hd_tabel,hd_asi,tabel,asi,kerija
    hd_tabel=Canvas(onaika,borderwidth=0,width=557,height=23)
    hd_asi=Frame(hd_tabel)
    hd_tabel.grid(row=2,column=1,columnspan=8)
    hd_tabel.create_window((0,0),window=hd_asi,anchor="nw")
    hd_asi.bind("<Configure>", lambda event,
    hd_tabel=hd_tabel: hd_tabel.configure(scrollregion=tabel.bbox("all")))

    if len(lute)<20:
        gsize=20
    else:
        gsize=len(lute)

    tabel=Canvas(onaika,borderwidth=0,width=557,height=410)
    asi=Frame(tabel)
    kerija=Scrollbar(onaika,command=tabel.yview)
    tabel.configure(yscrollcommand=kerija.set)
    kerija.grid(row=2,column=9,rowspan=60,sticky="ns")
    tabel.grid(row=3,column=1,rowspan=gsize+1,columnspan=8)
    tabel.create_window((0,0),window=asi,anchor="nw")
    asi.bind("<Configure>", lambda event,
    tabel=tabel: tabel.configure(scrollregion=(0,29,1000,20.925*gsize+29)))

    mt_hashtop=Button(asi,text="#",font=("fixedsys",14),width=2)
    mt_hashtop.grid(row=1,column=1)
    mt_dn=Button(asi,text="Display Name",font=("fixedsys",14),width=24)
    mt_dn.grid(row=1,column=2)
    mt_rnk=Button(asi,text="Ranking",font=("fixedsys",14),width=9)
    mt_rnk.grid(row=1,column=3)
    mt_PI=Button(asi,text="PI",font=("fixedsys",14),width=5)
    mt_PI.grid(row=1,column=4)
    mt_pld=Button(asi,text="pld",font=("fixedsys",14),width=5)
    mt_pld.grid(row=1,column=5)
    mt_G=Button(asi,text="G",font=("fixedsys",14),width=5)
    mt_G.grid(row=1,column=6)
    mt_S=Button(asi,text="S",font=("fixedsys",14),width=5)
    mt_S.grid(row=1,column=7)
    mt_B=Button(asi,text="B",font=("fixedsys",14),width=5)
    mt_B.grid(row=1,column=8)

    pl_hashtop=Button(hd_asi,text="#",bg="white",activebackground="#FFB3B3",
    font=("fixedsys",14),width=2)
    pl_hashtop.grid(row=1,column=1)
    pl_dn=Button(hd_asi,text="Display Name",bg="white",activebackground="#FFB3B3",
    command=lambda:sbsoted_pl(1),font=("fixedsys",14),width=24,anchor="w")
    pl_dn.grid(row=1,column=2)
    pl_rnk=Button(hd_asi,text="Ranking",bg="white",activebackground="#FFB3B3",
    command=lambda:sbsoted_pl(3),font=("fixedsys",14),width=9)
    pl_rnk.grid(row=1,column=3)
    pl_PI=Button(hd_asi,text="PI",bg="white",activebackground="#FFB3B3",
    command=lambda:sbsoted_pl(4),font=("fixedsys",14),width=5)
    pl_PI.grid(row=1,column=4)
    pl_pld=Button(hd_asi,text="pld",bg="white",activebackground="#FFB3B3",
    command=lambda:sbsoted_pl(5),font=("fixedsys",14),width=5)
    pl_pld.grid(row=1,column=5)
    pl_G=Button(hd_asi,text="G",bg="white",activebackground="#FFB3B3",
    command=lambda:sbsoted_pl(6),font=("fixedsys",14),width=5)
    pl_G.grid(row=1,column=6)
    pl_S=Button(hd_asi,text="S",bg="white",activebackground="#FFB3B3",
    command=lambda:sbsoted_pl(7),font=("fixedsys",14),width=5)
    pl_S.grid(row=1,column=7)
    pl_B=Button(hd_asi,text="B",bg="white",activebackground="#FFB3B3",
    command=lambda:sbsoted_pl(8),font=("fixedsys",14),width=5)
    pl_B.grid(row=1,column=8)
def teeheader_gm():
    global hd_tabel,hd_asi,tabel,asi,kerija
    hd_tabel=Canvas(onaika,borderwidth=0,width=624,height=24)
    hd_asi=Frame(hd_tabel)
    hd_tabel.grid(row=2,column=1,columnspan=9)
    hd_tabel.create_window((1,1),window=hd_asi,anchor="nw")
    hd_asi.bind("<Configure>", lambda event,
    hd_tabel=hd_tabel: hd_tabel.configure(scrollregion=tabel.bbox("all")))

    if len(lute2)<20:
        gsize=20
    else:
        gsize=len(lute2)

    tabel=Canvas(onaika,borderwidth=0,width=624,height=410)
    asi=Frame(tabel)
    kerija=Scrollbar(onaika,command=tabel.yview)
    tabel.configure(yscrollcommand=kerija.set)
    kerija.grid(row=2,column=10,rowspan=100,sticky="ns")
    tabel.grid(row=3,column=1,rowspan=gsize+1,columnspan=9)
    tabel.create_window((1,0),window=asi,anchor="nw")
    asi.bind("<Configure>", lambda event,
    tabel=tabel: tabel.configure(scrollregion=(0,29,1000,20.925*gsize+29)))

    mt2_hashtop=Button(asi,text="#",font=("fixedsys",14),width=2)
    mt2_hashtop.grid(row=1,column=1)
    mt2_index=Button(asi,text="№",font=("fixedsys",14),width=2)
    mt2_index.grid(row=1,column=2)
    mt2_gn=Button(asi,text="Name",font=("fixedsys",14),width=16)
    mt2_gn.grid(row=1,column=3)
    mt2_type=Button(asi,text="Type",font=("fixedsys",14),width=10)
    mt2_type.grid(row=1,column=4)
    mt2_date=Button(asi,text="Date",font=("fixedsys",14),width=10)
    mt2_date.grid(row=1,column=5)
    mt2_nop=Button(asi,text="NoP",font=("fixedsys",14),width=3)
    mt2_nop.grid(row=1,column=6)
    mt2_G=Button(asi,text="G",font=("fixedsys",14),width=8)
    mt2_G.grid(row=1,column=7)
    mt2_S=Button(asi,text="S",font=("fixedsys",14),width=8)
    mt2_S.grid(row=1,column=8)
    mt2_B=Button(asi,text="B",font=("fixedsys",14),width=8)
    mt2_B.grid(row=1,column=9)

    gm_hashtop=Button(hd_asi,text="#",bg="white",activebackground="#FFB3B3",
    font=("fixedsys",14),width=2)
    gm_hashtop.grid(row=1,column=1)
    gm_index=Button(hd_asi,text="№",bg="white",activebackground="#FFB3B3",
    command=lambda:sbsoted_gm(0),font=("fixedsys",14),width=2)
    gm_index.grid(row=1,column=2)
    gm_gn=Button(hd_asi,text="Name",bg="white",activebackground="#FFB3B3",
    command=lambda:sbsoted_gm(1),font=("fixedsys",14),width=16,anchor="w")
    gm_gn.grid(row=1,column=3)
    gm_type=Button(hd_asi,text="Type",bg="white",activebackground="#FFB3B3",
    command=lambda:sbsoted_gm(2),font=("fixedsys",14),width=10)
    gm_type.grid(row=1,column=4)
    gm_date=Button(hd_asi,text="Date",bg="white",activebackground="#FFB3B3",
    command=lambda:sbsoted_gm(3),font=("fixedsys",14),width=10)
    gm_date.grid(row=1,column=5)
    gm_nop=Button(hd_asi,text="NoP",bg="white",activebackground="#FFB3B3",
    command=lambda:sbsoted_gm(4),font=("fixedsys",14),width=3)
    gm_nop.grid(row=1,column=6)
    gm_G=Button(hd_asi,text="G",bg="white",activebackground="#FFB3B3",
    command=lambda:sbsoted_gm(5),font=("fixedsys",14),width=8)
    gm_G.grid(row=1,column=7)
    gm_S=Button(hd_asi,text="S",bg="white",activebackground="#FFB3B3",
    command=lambda:sbsoted_gm(6),font=("fixedsys",14),width=8)
    gm_S.grid(row=1,column=8)
    gm_B=Button(hd_asi,text="B",bg="white",activebackground="#FFB3B3",
    command=lambda:sbsoted_gm(7),font=("fixedsys",14),width=8)
    gm_B.grid(row=1,column=9)
def teetabel_pl():
    for d in range(len(lute)*8):
        if d%8==0:
            exec("tb%d = %s" % (d+1, repr(Label(asi,text=str(d//8+1),bg="#FFE5E5",relief="raised",
            font=("fixedsys",14),width=2).grid(sticky="w"+"e",row=d//8+3,column=d%8+1))))
        elif d%8==1:
            exec("tb%d = %s" % (d+1, repr(Label(asi,text=str(lute[d//8][d%8]),bg="#FFE5E5",relief="raised",
            font=("fixedsys",14,"bold"),width=21,anchor="w").grid(sticky="w"+"e",row=d//8+3,column=d%8+1))))
        elif d%8==2:
            exec("tb%d = %s" % (d+1, repr(Label(asi,text=str(lute[d//8][d%8+1]),bg="#FFE5E5",relief="raised",
            font=("fixedsys",14),width=9).grid(sticky="w"+"e",row=d//8+3,column=d%8+1))))
        else:
            exec("tb%d = %s" % (d+1, repr(Label(asi,text=str(lute[d//8][d%8+1]),bg="#FFE5E5",relief="raised",
            font=("fixedsys",14),width=5).grid(sticky="w"+"e",row=d//8+3,column=d%8+1))))
    if len(lute)<20:
        for m in range(20-len(lute)):
            tyhi=Label(asi,text=" ",width=2).grid(sticky="w"+"e",row=len(lute)+m+3,column=1)
def teetabel_gm():
    for d in range(len(lute2)*9):
        if d%9==0:
            exec("tb%d = %s" % (d+1, repr(Label(asi,text=str(d//9+1),bg="#FFE5E5",relief="raised",
            font=("fixedsys",14),width=2).grid(sticky="w"+"e",row=d//9+3,column=d%9+1))))
        elif d%9==1:
            exec("tb%d = %s" % (d+1, repr(Label(asi,text=str(lute2[d//9][d%9-1]),bg="#FFE5E5",relief="raised",
            font=("fixedsys",14),width=2).grid(sticky="w"+"e",row=d//9+3,column=d%9+1))))
        elif d%9==2:
            exec("tb%d = %s" % (d+1, repr(Label(asi,text=str(lute2[d//9][d%9-1]),bg="#FFE5E5",relief="raised",
            font=("fixedsys",14,"bold"),width=13,anchor="w").grid(sticky="w"+"e",row=d//9+3,column=d%9+1))))
        elif d%9==3:
            exec("tb%d = %s" % (d+1, repr(Label(asi,text=str(lute2[d//9][d%9-1]),bg="#FFE5E5",relief="raised",
            font=("fixedsys",14),width=10).grid(sticky="w"+"e",row=d//9+3,column=d%9+1))))
        elif d%9==4:
            exec("tb%d = %s" % (d+1, repr(Label(asi,text=str(lute2[d//9][d%9-1]),bg="#FFE5E5",relief="raised",
            font=("fixedsys",14),width=10).grid(sticky="w"+"e",row=d//9+3,column=d%9+1))))
        elif d%9==5:
            exec("tb%d = %s" % (d+1, repr(Label(asi,text=str(lute2[d//9][d%9-1]),bg="#FFE5E5",relief="raised",
            font=("fixedsys",14),width=3).grid(sticky="w"+"e",row=d//9+3,column=d%9+1))))
        else:
            if tadacmts==0 or not lute2[d//9][d%9-1] in banned:
                exec("tb%d = %s" % (d+1, repr(Label(asi,text=str(lute2[d//9][d%9-1]),bg="#FFE5E5",relief="raised",
                font=("fixedsys",14),width=8).grid(sticky="w"+"e",row=d//9+3,column=d%9+1))))
            else:
                exec("tb%d = %s" % (d+1, repr(Label(asi,text="???",bg="#FFE5E5",relief="raised",
                font=("fixedsys",14),width=8).grid(sticky="w"+"e",row=d//9+3,column=d%9+1))))
    if len(lute2)<20:
        for m in range(20-len(lute2)):
            tyhi=Label(asi,text=" ",width=2).grid(sticky="w"+"e",row=len(lute2)+m+3,column=1)
def togcmts():
    global lute,lutec,tadacmts,activeside,switching,pwentry,pwwin,pwwrong
    if tadacmts==1:
        if passguessed==0:
            pwwin=Tk()
            pwwin.title("Hold on a second!")
            pwwin.geometry("700x400")
            pwwin.configure(bg="maroon")
            pwlabel=Label(pwwin,text="Enter Password",
            bg="maroon",font=("fixedsys",50,"bold"),fg="white")
            pwlabel.grid(row=0,column=0,pady=20,padx=60,columnspan=2)
            pwentry=Entry(pwwin,show="*",width=14,font=("fixedsys",50,"bold"))
            pwentry.grid(row=1,column=0,columnspan=2)
            pwok=Button(pwwin,text="OK",font=("fixedsys",25,"bold"),
            bg="white",command=submitpass)
            pwok.grid(row=2,column=0,pady=30,ipadx=10,padx=60,sticky="e")
            pwcancel=Button(pwwin,text="Cancel",font=("fixedsys",25,"bold"),
            bg="white",command=pwwin.destroy)
            pwcancel.grid(row=2,column=1,sticky="w",padx=60)
            pwwrong=Label(pwwin,text="That's not it...",
            bg="maroon",font=("fixedsys",18,"bold"),fg="maroon")
            pwwrong.grid(row=3,column=0,columnspan=2)
            return
        else:
            cmts.config(text="Comitees only")
            tadacmts=0
    else:
        cmts.config(text="All players")
        tadacmts=1
    lute,lutec=lutec,lute
    if activeside=="pl":
        pht_sbplgm()
        teeheader_pl()
        switching=1
        sbsoted_pl(sortedby)
        switching=0
    else:
        phtalumine()
        teetabel_gm()
def submitpass():
    global tadacmts,passguessed
    if pwentry.get()=="password":
        pwwin.destroy()
        passguessed=1
        togcmts()
    else:
        pwwrong.config(fg="white")
def crds():
    crdwin=Tk()
    crdwin.title("Credits")
    crdwin.geometry("680x370")
    crdwin.config(bg="maroon")
    crdl1=Label(crdwin,text="Programming",
    bg="maroon",font=("fixedsys",18),fg="white")
    crdl1.grid(row=0,column=0,pady=50,padx=60)
    crdl2=Label(crdwin,text="Mihkel Roomet",
    bg="maroon",font=("fixedsys",18,"bold"),fg="white")
    crdl2.grid(row=0,column=1,pady=20,padx=60)
    crdl3=Label(crdwin,text="Moral Support & Inspiration",
    bg="maroon",font=("fixedsys",18),fg="white",wraplength=250)
    crdl3.grid(row=1,column=0,padx=60)
    crdl4=Label(crdwin,text="Norman Kukk",
    bg="maroon",font=("fixedsys",18,"bold"),fg="white")
    crdl4.grid(row=1,column=1,padx=60)
    crdok=Button(crdwin,text="OK",font=("fixedsys",18,"bold"),
    bg="white",command=lambda:crdwin.destroy())
    crdok.grid(row=2,column=0,pady=45,ipadx=10,columnspan=2)
    crdl5=Label(crdwin,text="Copyright © 2015 Sääse Pokker",
    bg="maroon",font=("fixedsys",14,"bold"),fg="white")
    crdl5.grid(row=3,column=0,columnspan=2)

lutec,lute2,lute,banned=teeluted()

empty1=Label(text="",bg="black",height=3)
empty1.grid(row=0,column=0)
empty2=Label(text="oi",bg="black",height=3)
empty2.grid(row=0,column=1)

tog_players=Button(text="Players",width=15,activebackground="#FFB3B3",
command=stplayers,bg="white",relief="sunken",font=("fixedsys",14,"bold"))
tog_players.place(x=10,y=10)
tog_games=Button(text="Games",width=15,activebackground="#FFB3B3",
command=stgames,bg="white",relief="raised",font=("fixedsys",14,"bold"))
tog_games.place(x=160,y=10)

resni=Frame(width=200,height=500,bg="maroon")
resni.place(x=660,y=0)

btn_ap=Button(text="Add Player", width=15,activebackground="#FFB3B3",
command=popap,bg="white",relief="raised",font=("fixedsys",14,"bold"))
btn_ap.place(x=690,y=20)
btn_ag=Button(text="Add Game", width=15,activebackground="#FFB3B3",
command=popag,bg="white",relief="raised",font=("fixedsys",14,"bold"))
btn_ag.place(x=690,y=60)

teeheader_pl()

sbsoted_pl(3)

clbtn=Button(onaika,text="Clear",bg="white",
command=lambda:pht_sbplgm(),font=("fixedsys",14,"bold"),width=15)
clbtn.place(x=690,y=230)

cmts=Button(onaika,text="All players",bg="white",
command=lambda:togcmts(),font=("fixedsys",14,"bold"),width=15)
cmts.place(x=690,y=270)

crdbtn=Button(onaika,text="Credits",bg="white",
command=lambda:crds(),font=("fixedsys",14,"bold"),width=15)
crdbtn.place(x=690,y=310)
#crdbtn.config(state="disabled")

qbtn=Button(onaika,text="Quit",bg="white",
command=lambda:onaika.destroy(),font=("fixedsys",14,"bold"),width=15)
qbtn.place(x=690,y=350)

logo=Label(onaika,text="Sääse Pokker",wraplength=160,
bg="maroon",font=("fixedsys",20,"bold"),fg="white")
logo.place(x=705,y=400)

onaika.mainloop()
