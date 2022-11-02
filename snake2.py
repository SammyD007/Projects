from Tkinter import *
import random
import time

class Levely:
  def __init__(self):
    self.urovne=[
    [[0, 0, 0, 0, 0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 1, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]],
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 1, 1, 1, 0, 1, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 1, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 1, 1, 1, 1, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 1, 1, 0, 0, 0, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 1, 0, 0, 1, 0, 0, 1], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1, 1, 0], [0, 0, 1, 1, 1, 0, 0, 0, 0, 0]],  
    ]
    self.data=[[400,13],[400,10],[400,13],[400,13],[400,13],[400,13]]
    print ("Choose from", len(self.urovne), "levels")
    self.vyber=input("Level: ")
    self.vyber-=1
    h=Had(self)

class Had:
  def __init__(self,Levely):
    self.l=Levely
    self.level=self.l.urovne[self.l.vyber]
    self.mrizka=len(self.level[0])
    self.velikost=self.l.data[self.l.vyber][0]
    self.vtelo=100
    self.r=self.l.data[self.l.vyber][1]
    self.x=0
    self.y=0
    self.u=0
    self.k=self.velikost
    self.c=(self.velikost/self.mrizka)
    self.poprve=0
    self.neco=[[0,0],0,0,0]
    self.ukonceni=None
    self.aakce1=None
    self.aakce2=None
    self.aakce3=None
    self.aakce4=None
    self.s=[0,0,0,0]
    self.j=[]
    self.konec=0
    self.score=0
    self.pocet_zelenych=0

    self.okno=Tk() 
    self.platno=Canvas(self.okno,width=self.velikost,height=self.velikost,bg="white")
    self.platno.pack()
    self.tl=Button(self.okno, text="Restart", command=self.start)
    self.tl.pack(fill=BOTH)

    self.start()

    self.okno.bind("<Key-d>", self.akce1)
    self.okno.bind("<Key-w>", self.akce2) 
    self.okno.bind("<Key-s>", self.akce3)
    self.okno.bind("<Key-a>", self.akce4)
    self.okno.bind("<Key-r>", self.start1)



  def akce1(self, klik):
      self.akce11()
  def akce2(self, klik):
      self.akce21()
  def akce3(self, klik):
      self.akce31()
  def akce4(self, klik):
      self.akce41()
  def start1(self, klik):
    self.start()

  def akce11(self):
    if int(self.s[1])%self.c!=0:
        self.aakce1=self.okno.after(9,self.akce11)
    if int(self.s[1])%self.c==0:
        self.x=self.c
        self.y=0
        self.u=0
        if self.poprve==1:
            self.okno.after_cancel(self.aakce1)
        self.stop()
        self.pohyb()
  def akce21(self):
    if int(self.s[0])%self.c!=0:
        self.aakce1=self.okno.after(9,self.akce21)
    if int(self.s[0])%self.c==0:
        self.x=0
        self.y=-self.c
        self.u=0
        if self.poprve==1:
            self.okno.after_cancel(self.aakce2)
        self.stop()
        self.pohyb()
  def akce31(self):
    if int(self.s[0])%self.c!=0:
        self.aakce1=self.okno.after(9,self.akce31)
    if int(self.s[0])%self.c==0:
        self.x=0
        self.y=self.c
        self.u=1
        if self.poprve==1:
            self.okno.after_cancel(self.aakce3)
        self.stop()
        self.pohyb()
  def akce41(self):
    if int(self.s[1])%self.c!=0:
        self.aakce1=self.okno.after(9,self.akce41)
    if int(self.s[1])%self.c==0:
        self.x=-self.c
        self.y=0
        self.u=0
        if self.poprve==1:
            self.okno.after_cancel(self.aakce4)
        self.stop()
        self.pohyb()

  def pohyb(self):
    self.smrt()
    if self.konec==1:
        return None
    self.test()
    s=self.platno.coords(self.hlava)
    self.s=self.platno.coords(self.hlava)
    self.platno.delete(ALL)

    self.hlava=self.platno.create_rectangle(s[0],s[1],s[2],s[3], fill="green4", outline="white")
    self.jablko=self.platno.create_rectangle(self.j[0],self.j[1],self.j[2],self.j[3], fill="red", outline="red")
    for x in range(self.mrizka):
      for y in range(self.mrizka):
        if self.level[x][y]==0:
          continue
        if self.level[x][y]==1:
          #KURVVAAAAA x,y,x,y
          self.block=self.platno.create_rectangle(y*self.c,(x*self.c),(y*self.c)+self.c,(x*self.c)+self.c, fill="black")
    self.test()

    s=self.platno.coords(self.hlava)
    self.poloha.append(s)
    self.delka=len(self.poloha)

    if s[self.u]<=self.k:
        self.dx=self.x
        self.dy=self.y

    self.platno.move(self.hlava,self.dx/10,self.dy/10)
    s=self.platno.coords(self.hlava)
    self.nahrada=self.platno.create_rectangle(s[0],s[1],s[2],s[3], fill="green4", outline="green4")
    if s[self.u]>=self.k:
        self.dx=0
        self.dy=0
        bla="Restart-Score:", int(self.score)
        self.tl.config(text=bla)

    for a in range(self.delka):
      if 1==1:
        self.ocas=self.platno.create_rectangle(self.poloha[a][0],self.poloha[a][1],self.poloha[a][2],self.poloha[a][3], fill="green2", outline="green2")
        self.poloha_zeleny=self.platno.coords(self.ocas)
        self.zeleny.append(self.poloha_zeleny)
        self.pocet_zelenych=len(self.zeleny)
        if self.pocet_zelenych>=self.delka:
            del self.zeleny[0]

    if self.delka>=self.vtelo:
      self.neco=self.poloha[0]
      del self.poloha[0] 
    self.s=self.platno.coords(self.hlava)
    self.nahrada=self.platno.create_rectangle(s[0],s[1],s[2],s[3], fill="green4", outline="green4")
    self.ukonceni=self.okno.after(self.r,self.pohyb)

  def smrt(self):
    s=self.platno.coords(self.hlava)
    bla="Restart-Score:", int(self.score)
    if self.level[int(s[1]/self.c)][int(s[0]/self.c)]==1:
      self.platno.delete(self.hlava)
      self.tl.config(text=bla)
      self.konec=1
      self.smrtak=self.platno.create_rectangle(s[0],s[1],s[2],s[3], fill="brown", outline="brown")
    for b in range(len(self.zeleny)):
      if s==self.zeleny[(b-1)]:
        self.platno.delete(self.hlava)
        self.tl.config(text=bla)
        self.konec=1
        self.smrtak=self.platno.create_rectangle(s[0],s[1],s[2],s[3], fill="brown", outline="brown")

  def stop(self):
      if self.poprve==1:
        self.okno.after_cancel(self.ukonceni)
      self.poprve=1



  def start(self):
    self.vtelo=60
    self.platno.delete("all")
    self.tl.config(text="Restart")
    self.poloha=[]
    self.zeleny=[]
    self.konec=0
    self.pocet_zelenych=0
    self.score=0
    self.poprve=0
    self.dx=0
    self.dy=0
    if self.aakce1!=None:
      self.okno.after_cancel(self.aakce1)
      self.aakce1=None
    if self.aakce2!=None:
      self.okno.after_cancel(self.aakce2)
      self.aakce2=None
    if self.aakce3!=None:
      self.okno.after_cancel(self.aakce3)
      self.aakce3=None
    if self.aakce4!=None:
      self.okno.after_cancel(self.aakce4)
      self.aakce4=None


    for x in range(self.mrizka):
      for y in range(self.mrizka):
        if self.level[x][y]==0:
          continue
        if self.level[x][y]==1:
          #KURVVAAAAA x,y,x,y
          self.block=self.platno.create_rectangle(y*self.c,(x*self.c),(y*self.c)+self.c,(x*self.c)+self.c, fill="black")

    self.hlava=self.platno.create_rectangle(0,0,self.c,self.c, fill="green4", outline="green4")
    self.generace()
    s=self.platno.coords(self.hlava)
    self.dx=self.c
    self.dy=self.c

  def generace(self):
    self.nx=random.randint(0,self.mrizka-1)
    self.ny=random.randint(0,self.mrizka-1)

    for x in self.zeleny:
        if int(x[0]/self.c)==self.nx and int(x[1]/self.c)==self.ny:
            self.generace()
    if self.level[self.ny][self.nx]==1:
      self.generace()

    if self.level[self.ny][self.nx]!=1:
      self.jablko=self.platno.create_rectangle(self.nx*self.c,self.ny*self.c,self.nx*self.c+self.c,self.ny*self.c+self.c, fill="red", outline="red")

  def test(self):
    s=self.platno.coords(self.hlava)
    self.j=self.platno.coords(self.jablko)

    if s==self.j:
      self.vtelo+=5
      self.score+=0.5
      self.generace()

  def mezery(self):
    for x in range(30):
      print ("")

levliky=Levely()    
mainloop()
