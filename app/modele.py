import math


class Baza:
    def __init__(self,viata_maxima):
        self.viata=viata_maxima

    def incaseaza_daune(self,daune):
        self.viata-=daune
        if self.viata<0:
            self.viata=0


class Inamic:
    def __init__(self,id_inamic,nume,viata_max,viteza_baza,recompensa):
        self.id=id_inamic
        self.nume=nume
        self.viata=viata_max
        self.viteza_baza=viteza_baza
        self.viteza_curenta=viteza_baza
        self.recompensa=recompensa


        self.x=0.0
        self.y=0.0
        self.index_punct_tinta=1  # Către al câtelea punct de pe traseu se îndreaptă

        self.timp_incetinire_ramas=0.0

    def aplica_incetinire(self, factor, durata):
        self.viteza_curenta=self.viteza_baza*(1.0-factor)
        self.timp_incetinire_ramas=durata

    def actualizeaza_efecte(self,delta_timp):
        if self.timp_incetinire_ramas>0:
            self.timp_incetinire_ramas-=delta_timp
            if self.timp_incetinire_ramas<=0:
                self.timp_incetinire_ramas=0
                self.viteza_curenta=self.viteza_baza


class Turn:
    def __init__(self,x,y,tip_id,tip_comportament,raza,cooldown,daune,factor_incetinire=0.0,
                 durata_incetinire=0.0):
        self.x=x
        self.y=y
        self.tip_id=tip_id
        self.tip_comportament=tip_comportament
        self.raza=raza
        self.cooldown=cooldown
        self.timp_ramas_cooldown=0.0
        self.daune=daune


        self.factor_incetinire=factor_incetinire
        self.durata_incetinire=durata_incetinire

    def poate_trage(self):
        return self.timp_ramas_cooldown<=0

    def in_raza(self,inamic):

        distanta=math.sqrt((self.x-inamic.x)**2+(self.y-inamic.y)**2)
        #Prin teorema lui Pitagora aflam distanta de la turn la inamic
        return distanta<=self.raza