
#~.,;:!.,;:!.,;:!.,;:!.,;:!.,;:!.,;:!##_________________ ##!:;,.!:;,.!:;,.!:;,.!:;,.!:;,.!:;,.~#
############################ - Gestion Contact - #############################
#~.,;:!.,;:!.,;:!.,;:!.,;:!.,;:!.,;:!## ~~~~~~~~~~~~~~~  ##!:;,.!:;,.!:;,.!:;,.!:;,.!:;,.!:;,.~#

__author__ = "Hicham S'hih"


from tkinter import *
import glob as gl

#========================================================================
class Myapp :
    #---------------------------------------------------------------------------------------
    def __init__ (self, master):
        self.master = master
        self.frmbas = Frame (self.master)
        self.frmbas.pack(side =BOTTOM)
        self.frm1 = Frame (self.master)
        self.frm1.pack(side = LEFT)
        self.frm2 = Frame (self.master)
        self.frm2.pack(side = LEFT)
        self.frm3 = Frame (self.master)
        self.frm3.pack(side = LEFT)
        self.clk = -1
        self.com = 0
        self.cntctnom = ""
        self.CreatMenu()
        self.CreatWid()
        #---------------------------------------------------------------------------------------
    def readfichier(self):
        self.fichier = open ("D:\\python\\exposé_phtyon\\git\\Projet-Python\\exposeContact\\mesprofiles.txt", "r")
        self.mscntct = self.fichier.readlines()
        self.contacts = []
        for line in self.mscntct :
            contact = line.strip().split (',')
            self.contacts.append(contact)
        self.fichier.close()
        #---------------------------------------------------------------------------------------
    def appendfichier(self):
        self.fichier = open ("D:\\python\\exposé_phtyon\\git\\Projet-Python\\exposeContact\\mesprofiles.txt", "a")
        #---------------------------------------------------------------------------------------
    def writefichier(self):
        self.fichier = open("D:\\python\\exposé_phtyon\\git\\Projet-Python\\exposeContact\\mesprofiles.txt", "w")
        #---------------------------------------------------------------------------------------
    def CreatMenu(self):
        self.menubar = Menu(self.master)
        self.master.config(menu=self.menubar)
        self.menu = Menu(self.menubar, tearoff=False)
        self.help = Menu(self.menubar, tearoff=False)
        self.menuxrx = Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="File", menu=self.menu)
        self.menubar.add_cascade(label="?", menu=self.help)
        self.help.add_command(label="Aide", command=self.Aide)
        self.menu.add_command(label="Nouveau Contact", command=self.clear)
        self.menu.add_command(label="Contact Recent", command=self.recent_cntct)
        self.menu.add_separator()
        self.menu.add_command(label="Ajouter Contact", command=self.charger)
        self.menu.add_command(label="Modifier Contact", command=self.modifier)
        self.menu.add_separator()
        self.menu.add_cascade(label="Chercher", menu = self.menuxrx)
        self.menuxrx.add_command(label="par téléphone", command=self.cherchertele)
        self.menuxrx.add_command(label="par nom", command=self.cherchernom)
        self.menu.add_separator()
        self.menu.add_command(label="Quiter", command=self.Exit)
        #---------------------------------------------------------------------------------------
    def Exit (self):
        self.master.destroy()
        #---------------------------------------------------------------------------------------
    def recent_cntct (self):
        if self.cntctnom == "" :
            self.lblerror["text"] = "Il y a pas de contact recent pour l'instant"
        else : self.charger_sur()
        #---------------------------------------------------------------------------------------
    def Aide(self):
        Help = Tk()
        Help.title("Aide")
        Help.resizable(width =False, height =False)
        img = "1 >>Ouviriez le dossier où il y a le Programme\n>>Mettez votre photo dans le dossier\n>>nommez votre photo comme exemple : shih_hicham.png\nPS<>il faut que votre Photo doit être en format (*.png)\n"
        hlpimg = Label (Help, text = img) ; hlpimg.pack()
        chmp = "2 >>Pour la Modification ou La création d'un contact il faut\nque tous les champs soit remplis\nPS<>prend soin de saisir les informations correctement\n"
        hlpmod = Label (Help, text = chmp) ; hlpmod.pack()
        cherch = "3 >>Entrer le Nom ou Le telephone comme il est enregistrée \n>>le Contact n'affiche pas s'il n'existe pas avec les contacts\n>>créer un nouveau !!\n"
        cherch = Label (Help, text = cherch) ; cherch.pack()
        btnquit = Button (Help, text = "Quiter", command = lambda x=Help : x.destroy()); btnquit.pack()
        #---------------------------------------------------------------------------------------
    def enregistrer(self):
        self.appendfichier()
        self.fichier.write (self.txtfichier)
        self.fichier.close()
        #---------------------------------------------------------------------------------------
    def clear (self):
        self.nome.delete(0, 'end')
        self.pre.delete(0, 'end')
        self.telee.delete(0, 'end')
        self.emle.delete(0, 'end')
        self.lblerror["text"] = "< || Créer vos contacts || >"
        #---------------------------------------------------------------------------------------
    def dejaexiste (self):
        self.readfichier()
        contact = []
        for contact in self.contacts :
            if self.nomf == contact[0] and self.prf == contact [1] :
                if self.com == 1 :
                    return True
                else :
                    if messagebox.askokcancel("Oops", "{} {} Ce contact est déjà existe !!".format(self.nomf, self.prf)):
                        pass
                    if messagebox.askokcancel ("Okey", "Voulez-vous vider les champes et répeter !?"):
                        self.clear()
                    return True
        return False
    #---------------------------------------------------------------------------------------
    def charger_sur (self):
        self.clear()
        self.imgprf()
        self.nome.insert(0, self.cntctnom)
        self.pre.insert(0, self.cntctpr)
        self.telee.insert(0, self.cntcttele)
        self.emle.insert(0, self.cntcteml)
        #---------------------------------------------------------------------------------------
    def modifier (self) :
        self.com = 1
        self.nomf = self.nome.get()
        self.prf = self.pre.get()
        self.telef = self.telee.get()
        self.emlf = self.emle.get()
        if self.nomf == "" or self.prf == "" or self.telef == "" or self.emlf == "" :
            self.lblerror["text"] = "Appuyer | ? | >> |Aide| >> jeter un coup d'oeil sur 2"
            return
        if not self.dejaexiste() : self.lblerror["text"] = "Vous pouvez pas modifier contact n'existe pas !"
        elif self.dejaexiste() :
            self.com = 0
            if messagebox.askokcancel("Confirmer", "Voulez-vous Continuer la modification") :
                self.readfichier()
                for contact in self.contacts:
                    if self.nomf == contact[0] and self.prf == contact [1] :
                        contact[2], contact[3] = self.telef, self.emlf
                        self.writefichier()
                        for contact in self.contacts :
                            for elm in range (len(contact)):
                                if elm != len (contact)-1:
                                    self.fichier.write(contact[elm]+",")
                                else : self.fichier.write(contact[elm])
                        self.fichier.close()
                        self.lblerror["text"] = "Votre contact est Bien Modifier"
        #---------------------------------------------------------------------------------------
    def chercher (self):
        self.readfichier()
        cher = self.entrer.get()
        self.achercher.append(cher)
        self.a.destroy()
        for contact in self.contacts:
            if self.achercher[0] == "telephone" :
                if contact[2] == self.achercher[1]:
                    self.cntctnom = contact[0]
                    self.cntctpr = contact[1]
                    self.cntcttele = contact[2]
                    self.cntcteml = contact[3]
                    self.charger_sur(); return
            elif self.achercher[0] == "nom":
                if contact[0] == self.achercher[1].lower() :
                    self.cntctnom = contact[0]
                    self.cntctpr = contact[1]
                    self.cntcttele = contact[2]
                    self.cntcteml = contact[3]
                    self.charger_sur(); return
        self.lblerror["text"] = "Appuyer | ? | >> |Aide| >> jeter un coup d'oeil sur 3"
        #---------------------------------------------------------------------------------------
    def cherchertele (self):
        self.readfichier()
        self.a = Tk()
        self.entelep = StringVar()
        tele = Label(self.a, text = "Entrer le telephone de contact"); tele.pack()
        self.entrer = Entry(self.a,textvariable = self.entelep)
        self.entrer.pack()
        btn = Button (self.a, text = 'Chercher', command = self.chercher); btn.pack()
        self.achercher = ["telephone"]
        #---------------------------------------------------------------------------------------
    def cherchernom (self):
        self.readfichier()
        self.a = Tk()
        self.enname = StringVar()
        name = Label(self.a, text = "Entrer le nom de contact"); name.pack()
        self.entrer = Entry(self.a,textvariable = self.enname)
        self.entrer.pack()
        btn = Button (self.a, text = 'Chercher', command = self.chercher); btn.pack()
        self.achercher = ["nom"]
        #---------------------------------------------------------------------------------------
    def contact_suivant(self):
        self.clk += 1
        self.readfichier()
        self.cntctnom = self.contacts[self.clk][0]
        self.cntctpr = self.contacts[self.clk][1]
        self.cntcttele = self.contacts[self.clk][2]
        self.cntcteml = self.contacts[self.clk][3]
        if self.clk >= 1 :
            self.btng.config(state = NORMAL)
            self.btng2.config(state = NORMAL)
        if len (self.contacts)-1 == self.clk :
            self.btnd.config(state = DISABLED)
            self.btnd2.config(state = DISABLED)
        self.charger_sur()
        #---------------------------------------------------------------------------------------
    def contact_precedent (self):
        self.clk -= 1
        self.readfichier()
        self.cntctnom = self.contacts[self.clk][0]
        self.cntctpr = self.contacts[self.clk][1]
        self.cntcttele = self.contacts[self.clk][2]
        self.cntcteml = self.contacts[self.clk][3]
        self.btnd.config(state = NORMAL)
        self.btnd2.config(state = NORMAL)
        if self.clk == 0:
            self.btng.config(state = DISABLED)
            self.btng2.config(state = DISABLED)
        self.charger_sur()
        #---------------------------------------------------------------------------------------
    def dernier_contact (self):
        self.readfichier()
        self.cntctnom = self.contacts[len(self.contacts)-1][0]
        self.cntctpr = self.contacts[len(self.contacts)-1][1]
        self.cntcttele = self.contacts[len(self.contacts)-1][2]
        self.cntcteml = self.contacts[len(self.contacts)-1][3]
        self.charger_sur()
        self.btnd.config(state = DISABLED)
        self.btnd2.config(state = DISABLED)
        self.btng.config(state = NORMAL)
        self.btng2.config(state = NORMAL)
        self.clk = len(self.contacts)-1
        #---------------------------------------------------------------------------------------
    def premier_contact (self):
        self.readfichier()
        self.cntctnom = self.contacts[0][0]
        self.cntctpr = self.contacts[0][1]
        self.cntcttele = self.contacts[0][2]
        self.cntcteml = self.contacts[0][3]
        self.charger_sur()
        self.btnd.config(state = NORMAL)
        self.btnd2.config(state = NORMAL)
        self.btng.config(state = DISABLED)
        self.btng2.config(state = DISABLED)
        self.clk = 0
        #---------------------------------------------------------------------------------------
    def charger(self):
        self.nomf = self.nome.get()
        self.prf = self.pre.get()
        self.telef = self.telee.get()
        self.emlf = self.emle.get()
        if self.nomf == "" or self.prf == "" or self.telef == "" or self.emlf == "" :
            self.lblerror["text"] = "Appuyer | ? | >> |Aide| >> jeter un coup d'oeil sur 2"
            return
        elif self.dejaexiste() : return
        else :
            self.txtfichier = ("{},{},{},{}\n").format(self.nomf, self.prf, self.telef, self.emlf)
            self.enregistrer()
            self.lblerror["text"] = "Votre contact est Bien Enregistrer"
        #---------------------------------------------------------------------------------------
    def imgprf (self):
        self.listimage = gl.glob ("*.png")
        self.nomimg = "{}_{}".format(self.cntctnom, self.cntctpr)
        for imagprf in self.listimage:
            if imagprf[:-4] == self.nomimg :
                self.img = PhotoImage(file = imagprf)
                self.image["image"] =  self.img
                return
        self.lblerror["text"] = "Appuyer | ? | >> |Aide| >> jeter un coup d'oeil sur 1"
        self.img = PhotoImage(file = "default.png")
        self.image["image"] =  self.img
        #---------------------------------------------------------------------------------------
    def openfile (self):
        from tkinter.filedialog import askopenfilename; import os
        self.Photoimg = askopenfilename()
        if self.Photoimg[-4:] in ".png" or ".gif":
            self.Photoimg = os.path.split(self.Photoimg)
            self.Photoimg = PhotoImage(file = self.Photoimg[1])
            self.image["image"] = self.Photoimg
        else :
            self.lblerror["text"] = ["Votre Photo doit être en fotmat .png"]
        #---------------------------------------------------------------------------------------
    def CreatWid(self):
        self.lblerror = StringVar(); self.nom = StringVar();self.pr = StringVar();self.tele = StringVar();self.eml = StringVar()
        self.nom = Label (self.frm1, text = 'Nom') ; self.nom.grid(row = 0, sticky = E)
        self.pr = Label (self.frm1, text = 'Prenom') ; self.pr.grid (row = 1, sticky = E)
        self.tele = Label (self.frm1, text = 'Telephone') ; self.tele.grid (row = 2, sticky = E)
        self.eml = Label (self.frm1, text = 'Email') ; self.eml.grid (row = 3, sticky = E)
        self.nome = Entry (self.frm2, textvariable = self.nom) ; self.nome.grid (row = 0)
        self.pre = Entry (self.frm2, textvariable = self.pr) ; self.pre.grid (row = 1)
        self.telee = Entry (self.frm2, textvariable = self.tele) ; self.telee.grid (row = 2)
        self.emle = Entry (self.frm2, textvariable = self.eml) ; self.emle.grid (row = 3)
        self.img = PhotoImage(file = "default.png")
        self.image = Label (self.frm3, image = self.img)
        self.image.grid (rowspan = 2 , columnspan = 2)
        self.brows = Button(self.frm3, text = "Charger Photo", command = self.openfile); self.brows.grid(row = 2, columnspan = 2)
        self.btng2 = Button(self.frmbas, text = "<<", width = 3, command = self.premier_contact) ; self.btng2.grid(row = 0, column = 0, sticky=EW); self.btng2.config(state = DISABLED)
        self.btng = Button(self.frmbas, text = "<", width = 3, command = self.contact_precedent); self.btng.grid(row = 0,column = 1, sticky=EW); self.btng.config(state = DISABLED)
        self.btnd = Button(self.frmbas, text = ">", width = 3, command = self.contact_suivant) ; self.btnd.grid(row = 0,column = 2, sticky=EW)
        self.btnd2 = Button(self.frmbas, text = ">>", width = 3, command = self.dernier_contact) ; self.btnd2.grid(row = 0,column = 3, sticky=EW)
        self.lblerror = Label(self.frmbas, relief = SUNKEN,text = "Enter toutes les informations s'il vous plait", width = 38, height = 2) ; self.lblerror.grid(row = 1, columnspan = 4)
#=======================================================================
if __name__ == "__main__":
    root = Tk()
    root.title("Gestion Contacts")
    root.resizable(width = False, height = False )
    app = Myapp (root)
    root.mainloop()
    print('nous avons utiliser git pour travailler en équipe')
#############################-FIN DU PROGRAMME-#############################
