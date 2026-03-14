---
layout: default
title: "Python : mastermind"
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

# Codage : Mastermind

Voici les lignes de code que j'ai réalisées.
Choisissez un article et cela déduira son montant de votre porte-monnaie

<img src="/assets/image/1.jpg" alt="1" width="50" height="50">

{% highlight python %}
import random




def combinaison(couleur):
    combi=random.sample(couleur, 4)
    return combi



def choix():
    choix_couleur=(input("choisisser 4 couleurs différentes entre R , O ,B ,V ,J: "))
    return list(choix_couleur)

def jeu(): 
    
    couleur=["R","O","B","V","J"]
    f=False
    combi=combinaison(couleur)
    
    while f is False:
        a=0
        z=choix()
        for i in range(4):
            if combi[i]==z[i]:
                a+=1
                
            elif z[i]in combi:
                a+=100
            else:
                pass
        if a==4:
            f=True
            print("trouver")
        elif a==1:
            print("1 bien placée")
        elif a==2:
            print("2 bien placées")
        elif a==3:
            print("3 bien placées")
        elif a==100:
            print("1 mal placée")
        elif a==200:
            print("2 mal placées")
        elif a==300:
            print("3 mal placées")
        elif a==101:
            print("1 bien placée et 1 mal placée")
        elif a==102:
            print("2 bien placées et 1 mal placée")
        elif a==201:
            print("1 bien placée et 2 mal placés")
        elif a==202:
            print("2 bien placées et 2 mal placées")
        elif a==301:
            print("1 bien placée et 3 mal placées")
        else:
            print("rien")
            


jeu()
{% endhighlight %}



<a href="https://vipecollie.github.io" target="_blank" rel="noopener">
Retour
</a>

