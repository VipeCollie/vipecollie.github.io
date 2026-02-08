---
layout: default
title: "Python : dictionnaires"
date: 2025-11-08
categories: [blog, jekyll]
---

<style>
/*  */
.highlight {
  background: #f4f4f4;
  border-radius: 8px;
  padding: 1rem;
  overflow-x: auto;
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  font-size: 0.95em;
}
</style>

# Codage : xxx

Voici les lignes de code que j'ai réalisées.
Choisissez un article et cela déduira son montant de votre porte-monnaie

<img src="/assets/image/1.jpg" alt="1" width="50" height="50">

{% highlight python %}
menu ={
    "poisson":{"prix":6.50 , "stock":10},
    "pomme":{"prix":0.80, "stock":23},
    "poulet":{"prix":16.80,"stock":7}
}
commande_passé={
    "poisson":0,
    "pomme":0,
    "poulet":0
}
argent={
    "argent":50
}
def commande(menu):
    choix=input("choissisez le produit que vous voulez :")
    if choix not in menu:
        print("ce produit n'est pas dans le menu")
        return
    if menu[choix]["stock"]==0:
        print("ce produit n'a plus de stock")
        return
        
    else:
        print(f"veuillez payer le prix de {menu[choix]['prix']} €")
        if argent["argent"]<menu[choix]["prix"]:
            print("vous n'avez pas assez d'argent pour payer ")
        else:
            menu[choix]["stock"]-=1
            commande_passé[choix]+=1
            print("merci pour votre achat")
            argent["argent"]=argent["argent"]-menu[choix]["prix"]
        if commande_passé[choix]==3:
            print("vous avez achettez trois fois ce produit voici un offert")
            commande_passé[choix]-=3 
    print(f"il vous reste {argent["argent"]} €")





for i in range(3):

    commande(menu)
{% endhighlight %}




