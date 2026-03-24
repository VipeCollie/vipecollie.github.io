---
layout: default
title: "Python : Class perroquet"
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

# Codage : Class perroquet

Voici les lignes de code que j'ai réalisées.
Voici un perroquet qui apprend des mots et les répète.

<img src="/assets/image/1.jpg" alt="1" width="50" height="50">

{% highlight python %}
def init_perroquets(perroquet,nom,age):
    perroquet["nom"]=nom
    perroquet["age"]=age
    perroquet["faim"]=1
    perroquet["soif"]=2
    perroquet["memoire"]=10
    perroquet["vocabulaire"]=[]




def Perroquet(nom,age):
    perroquet=dict()
    init_perroquets(perroquet,nom,age)
    return perroquet

def se_nourrir(perroquet):
    while perroquet["faim"]>0:
        if perroquet["faim"]>0:
            print(f"{perroquet['nom']} a faim")
            perroquet["faim"]-=1
            print(f"{perroquet['nom']} a mangé")
            print(perroquet["faim"])
            print(f"{perroquet['faim']}")
        else:
            print(f"{perroquet['Nom']}n'a pas faim")


def s_abreuver(perroquet):
    while perroquet["soif"]>0:
        if perroquet["soif"]>0:
            print(f"{perroquet['nom']} a soif")
            perroquet["soif"]-=1
            print(f"{perroquet['nom']} a bu")
            print(f"{perroquet['soif']}")
        else:
            print(f"{perroquet['Nom']}n'a pas soif")

def veillir(perroquet):
    perroquet["age"]+=1
    print(f"{perroquet['nom']} a veilli")
    print(f"{perroquet['nom']} a maitenant {perroquet['age']} ans")

    


def apprendre(perroquet,mot):
    if mot not in perroquet["vocabulaire"]:
        if perroquet["age"]>10:
            print(f"{perroquet['nom']} a oublier {perroquet['vocabulaire'][0]})")
            del perroquet["vocabulaire"][0]
            perroquet["memoire"]+=1
            print(f"{perroquet['nom']} a oublier un mot")
        if perroquet["memoire"]>0:
            perroquet["memoire"]-=1
            perroquet["vocabulaire"].append(mot)
            print(f"{perroquet['nom']} a appris ")
            print(f"{perroquet['nom']} peut encore apprendre {perroquet['memoire']} fois")
        else:
            print(f"{perroquet['nom']} ne peut plus apprendre de mot")
    else:
        print(f"{perroquet['nom']} connait deja ce mot") 




def jouer(perroquet):
    try:
        if perroquet["energie"]>0:
            perroquet["energie"]-=20
            perroquet["Soif"]+=1
            perroquet["faim"]+=1
            print(f"{perroquet["Nom"]} a joué")
        else:
            print(f"{perroquet["Nom"]} est trop epuisée pour jouer")   
    except KeyError:
        print("le perroquet n'a pas d'energie")


def se_reposer(perroquet):
    try:
        while perroquet["energie"]<80:
            if perroquet["energie"]<80:
                print(f"{perroquet["Nom"]} est epuisé")
                perroquet["energie"]+=20
                print(f"{perroquet["Nom"]} c'est reposé")
            else:
                print(f"{perroquet["Nom"]} n'est pas epuisé")
    except KeyError:
        print("le perroquet n'a pas d'energie")


jouer(Perroquet("kiwi",3))
{% endhighlight %}



<a href="https://vipecollie.github.io" target="_blank" rel="noopener">
Retour
</a>
