import random
import sys
import tkinter as ttk


class Spelare:
    def __init__(self, name, index):
        self.name = name
        self.index=index
        self.points = []
        self.moments = []
        dice = []
        for n in range(5):
            dice.append(random.randint(1, 6))
        self.dices = dice

        self.antal_kast = 0
    def spel():
        pass

#lista med alla moment

def ettor(dice):
	print(dice, "under ettor")
	points = []
	if 1 not in dice:
		print("Hello")
	else:
		for n in range(5):
			if dice[n] == 1:
				points.append(dice[n])
		return 1 * len(points)

def tvåor(dice):
	points = []
	if 2 not in dice:
		return 0
	else:
		for n in range(5):
			if dice[n] == 2:
				points.append(dice[n])
		return 2 * len(points)
def treor(dice):
	points = []
	if 3 not in dice:
		return 0
	else:
		for n in range(5):
			if dice[n] == 3:
				points.append(dice[n])
		return 3 * len(points)
def fyror(dice):
	points = []
	if 4 not in dice:
		return 0
	else:
		for n in range(5):
			if dice[n] == 4:
				points.append(dice[n])
		return 4 * len(points)
def femmor(dice):
	points = []
	if 5 not in dice:
		return 0
	else:
		for n in range(5):
			if dice[n] == 5:
				points.append(dice[n])
		return 5 * len(points)
def sexor(dice):
	points = []
	if 6 not in dice:
		return 0
	else:
		for n in range(5):
			if dice[n] == 6:
				points.append(dice[n])
		return 6 * len(points)
def three_of_a_kind(dice):
	points = []
	dice.sort()
	for n in range(5):
		if dice[n] == dice[2]:
			points.append(dice[n])
		if len(points) == 3:
			return sum(dice)
		else:
			return 0
def four_of_a_kind(dice):
	points = []
	for n in range(5):
		if dice[n] == dice[2]:
			points.append(dice[n])
		if len(points) == 4:
			return sum(dice)
		else:
				return 0
def full_house(dice):
	list_1 = []
	list_2 = []
	dice.sort()
	for n in range(5):
		if dice[n] == dice[4]:
			list_1.append(dice[n])
		if dice[n] == dice[0]:
			list_2.append(dice[n])
	if (len(list_1) == 3 or len(list_2) == 3) or (len(list_1) == 2 or len(list_2) == 2):
		return sum(dice)
	else:
		return 0
def small_straight(dice):
	sort = []
	[sort.append(number) for number in dice if number not in sort]
	sort.sort()
	range_list = list(range(min(sort), max(sort) + 1))
	if sort == range_list:
		return sum(range_list)
	else:
		return 0
def large_straight(dice):
	sort = []
	[sort.append(number) for number in dice if number not in sort]
	sort.sort()
	range_list = list(range(min(sort), max(sort) + 1))
	if sort == range_list and len(range_list) == 5:
		return sum(range_list)
	else:
		return 0
def yatzy(dice):
	points = []
	for n in range(5):
		if dice[n] == dice[0]:
			points.append(dice[n])
	if len(points) == 5:
		return 50
	else:
		return 0
def chans(dice):
	return sum(dice)

moment_lista = [ chans, ettor, tvåor, treor, fyror, femmor, sexor, three_of_a_kind, four_of_a_kind, full_house, small_straight, large_straight, yatzy ]

class Knappar:
    def __init__(self, window, row, column, text, width, height, sticky, command):
        self.window = window
        self.row = row
        self.column = column
        self.font = ('Ariel', 18)
        self.text = text
        self.command = command
        self.width = width
        self.height = height
        self.sticky = sticky
        self.btn = ttk.Button(window, width=self.width, height=self.width, text = self.text, background='gray', command = self.command)
        self.btn.grid(row = self.row, column = self.column, sticky=self.sticky)
    def destroy():
        print("Hello")
class Textruta:
	def __init__(self, window, row, column, width, sticky):
		self.window = window
		self.row = row
		self.column = column
		self.width = width
		
	
		self.sticky = sticky
		self.text_ruta = ttk.Entry(window, width=self.width)
		self.text_ruta.grid(row=self.row, column=self.column, sticky=self.sticky)

class GUI:
    def __init__(self):
        self.window = ttk.Tk()
        self.window.geometry("1000x1000")
        self.window.title("yatzy")

        self.entry = ttk.Entry(self.window, width = 12)
        self.entry.grid(row=0, column=3, sticky=ttk.W+ttk.E)
        
        
        klar = Knappar(self.window, 0, 1, "Skapa protokoll", 8, 1, ttk.E+ttk.W ,command = lambda: self.protokoll(self.entry.get()))
        
        start_yatzy = Knappar(self.window, 0, 0, "starta yatzy", 8, 3, ttk.E+ttk.W, command =lambda: yatzy.spel())
        self.window.mainloop()
	
    def protokoll(self, namn):
		
        spelarlista = str(namn)
        if spelarlista !="":
            spelare = spelarlista.split()
            for n in range(len(spelare)):
                player_obj = Spelare(spelare[n], n)
                player_btn = Knappar(self.window, 1, n+2, spelare[n], 3, 2, ttk.W, None)          
            tärningar = Knappar(self.window, 0, 2, "Slå tärning", 8, 1, ttk.W, command=lambda: self.tärningar(player_obj))
            btn_list = []
            namn = Knappar(self.window, 1, 1, "namn", 3, 2, ttk.S, command=lambda: self.poäng)
            
            print(player_obj.dices, "under protokoll")
            
            self.ettor = Knappar(self.window, 2, 1, "ettor", 3, 2,ttk.S,command=lambda: moment_lista[1](player_obj.dices))
            self.tvåor = Knappar(self.window, 3, 1, "tvåor", 3, 2,ttk.S, command=lambda: moment_lista[2](player_obj.dices))
            self.treor = Knappar(self.window, 4, 1, "treor", 3, 2,ttk.S, command=lambda: moment_lista[3](player_obj.dices))
            self.fyror = Knappar(self.window, 5, 1, "fyror", 3, 2,ttk.S, command=lambda: moment_lista[4](player_obj.dices))
            self.femmor = Knappar(self.window, 6, 1, "femmor", 3, 2,ttk.S, command=lambda: moment_lista[5](player_obj.dices))
            self.sexor = Knappar(self.window, 7, 1, "sexor", 3, 2,ttk.S, command=lambda: moment_lista[6](player_obj.dices))
            self.ett_par = Knappar(self.window, 8, 1, "ett par",3, 2, ttk.S, command=lambda: self.poäng(player_obj.dices))
            self.två_par = Knappar(self.window, 9, 1, "två par", 3, 2,ttk.S, command=lambda: self.poäng(player_obj.dices))
            self.triss = Knappar(self.window, 10, 1, "triss", 3, 2,ttk.S, command=lambda: self.poäng(player_obj.dices))
            self.kåk = Knappar(self.window, 11, 1, "kåk", 3, 2,ttk.S, command=lambda: self.poäng(player_obj.dices))
            for n in range(2, 12): #rader
                for i in range(2, len(spelare) + 2): #kolonner
                    btn = Textruta(self.window, n, i, 3, ttk.E+ttk.W+ttk.S)
                    btn_list.append(btn)
        else:
            pass
    def poäng(self):
            print("test")
	
    def get_number(self, d):
        if d == 1:
            return '\u2680'
        elif d == 2:
            return '\u2681'
        elif d == 3:
            return '\u2682'
        elif d == 4:
            return '\u2683'
        elif d == 5:
            return '\u2684'
        elif d == 6:
            return '\u2685'


    def tärningar(self, namn):
        spelarlista = str(namn)
        spelare = spelarlista.split()
        player_list = []
        for n in range(len(spelare)):
            player_obj = Spelare(spelare[n], n)
            player_list.append(player_obj)
		
        print(player_list[0].name, "spelar lista")
        num_d1 = self.get_number(player_list[0].dices[0])
        num_d2 = self.get_number(player_list[0].dices[1])
        num_d3 = self.get_number(player_list[0].dices[2])
        num_d4 = self.get_number(player_list[0].dices[3])
        num_d5 = self.get_number(player_list[0].dices[4])
        print(player_list[0].dices[0], player_list[0].dices[1], player_list[0].dices[2], player_list[0].dices[3], player_list[0].dices[4], "under tärningar")
        player_list[0].dices = [player_list[0].dices[0], player_list[0].dices[1], player_list[0].dices[2], player_list[0].dices[3], player_list[0].dices[4]]
        
        #create dice labels
        dice_label1 = ttk.Label(self.window, text = "", font=('Helvetice', 50))
        dice_label1.grid(row=1, column=0)
        dice_label2 = ttk.Label(self.window, text = "", font=('Helvetice', 50))
        dice_label2.grid(row=2, column=0)
        dice_label3 = ttk.Label(self.window, text = "", font=('Helvetice', 50))
        dice_label3.grid(row=3, column=0)
        dice_label4 = ttk.Label(self.window, text = "", font=('Helvetice', 50))
        dice_label4.grid(row=4, column=0)
        dice_label5 = ttk.Label(self.window, text = "", font=('Helvetice', 50))
        dice_label5.grid(row=5, column=0)
	   
	    #update label
        dice_label1.config(text=num_d1)
        dice_label2.config(text=num_d2)
        dice_label3.config(text=num_d3)
        dice_label4.config(text=num_d4)
        dice_label5.config(text=num_d5)
        
        

class yatzy:
	def spel():
		grafic = GUI()
		n = int(input("Hur många ska spela spelet? "))
		lista = []
		for c in range(n):
			a = input("Vad heter du ")
			b = Spelare(a, c)
			lista.append(b)
		for k in range(n):
			print(lista[k].name)	
			print(lista[k].index)
		poäng_lista = []
		while lista[k].antal_kast <= 1:
		    for k in range(n):
		        grafic.tärningar()
		for k in range(n):
			poäng_lista.append(sum(lista[k].points))
		poäng_lista.sort()
		högst_poäng = poäng_lista[-1]
		for k in range(n):
			if sum(lista[k].points) == högst_poäng:
				print(lista[k].name, "vann spelet och fick", sum(lista[k].points), "poäng")
			svar = input("Vill ni spela om? (ja/nej)")
			if svar == "ja":
				yatzy.spel()
			else:
				print("Tack för att ni spelade")
				sys.exit()		
		
		
        
import random
def main():
	GUI()
	
	
	
if __name__=='__main__':
	main()

		