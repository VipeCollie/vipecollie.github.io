
def arene(largeur,taille):
    interieur=largeur-2
    with open("arène.txt" , "w") as f :
        f.write("1"*largeur)
        f.write("\n")
        f.write("1"*largeur)
        f.write("\n")  
        for loop in range(taille):
            f.write("1")
            for loop in range(interieur):
                f.write(" ")
            f.write("1")
            f.write("\n")
        f.write("1"*largeur)
        f.write("\n")
        f.write("1"*largeur)
        f.write("\n")

arene(int(input("selectionner la largeur de l'arène :")),int(input("selectionner la longueur de l'arène :")))