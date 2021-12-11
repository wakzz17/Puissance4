grille = [ 
    [0,0,0,0,0,0,0],    # 
    [0,0,0,0,0,0,0],    # 
    [0,0,0,0,0,0,0],    # 
    [0,0,0,0,0,0,0],    #---Grille puissance 4 
    [0,0,0,0,0,0,0],    # 
    [0,0,0,0,0,0,0],    # 
] 
 
#--------------------Fonction pour vérifier les bornes max et min de l'input-----------------# 
def verifBornes(numCol): 
    if numCol > 7 or numCol < 0: 
        return 0 
    else: 
        return 1 
#--------------------------------------------------------------------------------------------# 
 
#---------------Fonction changeant la valeur du pion en fonction du tour pour les joueurs--------# 
def valeurPion(tour):                                                                           
    if (tour % 2) == 0:                                                                         
        return 2                                                                                
    else:                                                                                       
        return 1                                                                                
#------------------------------------------------------------------------------------------------# 
 
#--------------------Fonction pour ajouter un pion dans la grille-----------------# 
def Placement(numCol): 
    for i in range(len(grille)-1, -1, -1): 
        if grille[i][numCol] == 0: 
            grille[i][numCol] = valeurPion(tour) 
            break 
    return grille 
#---------------------------------------------------------------------------------# 
 
 
tour = 1 
win = 0 
 
while win == 0: 
 
 
    numCol = int(input('Numéro colonne :')) - 1  
 
    if verifBornes(numCol) == 1: 
        print(Placement(numCol)) 
    tour += 1 

#Conditions de victoire

lin = 5
col = 0

#permet de declarer une victoire horizotale
def horizontalWin(grille) :
    for lin in range (6):
        for col in range (7):
            if  grille[lin][col] == grille [lin][col+1] ==grille[lin][col+2] == grille [lin][col+3] :
                return True 
            else :
                return False
                
#permet de declarer une victoire verticale
def verticalWin(grille) :
    for lin in range (6):
        for col in range (7):
            if  grille[lin][col] == grille [lin+1][col] ==grille[lin+2][col] == grille [lin+3][col] :
                return True 
            else :
                return False
                




