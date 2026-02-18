---
layout: default
title: "Openclassroom : Bases Python"
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

# Openclassroom : Base Python

J'ai fait la formation Openclassroom : bases Python

A la différence de Citizencode il y a des vidéos et des cours écrits. 
Ca m'a permis d'apprendre les bases de Python.
Essayez!

<img src="/assets/image/Openclassroom1.jpg" alt="1" width="700" height="500">


# Openclassroom Base Python : Fonctions



Voici les lignes de code que j'ai réalisées.Ca sert à déterminer le salaire herbdomaidaire et mensuel en fonction du nombres d'heures par semaine et du salaire annuel.


{% highlight python %}
def salaire_mensuel(salaire_annuel):
    salaire_mensuel=salaire_annuel/12
    return salaire_mensuel

def salaire_hebdomadaire(salaire_mensuel):
    salaire_hebdomadaire=salaire_mensuel/4
    return salaire_hebdomadaire
def salaire_horaire(salaire_hebdomadaire,heures_travailler):
    salaire_horaire=salaire_hebdomadaire/heures_travailler
    return salaire_horaire
H=int(input("ecrivez le nombre d'heures que vous travailler par semaine : "))
sal_ann=int(input("ecrivez le  montant de votre salaire annuel : "))
sal_mens=salaire_mensuel(sal_ann)
sal_hebdo=salaire_hebdomadaire(sal_mens)
sal_hor=salaire_horaire(sal_hebdo,H)
print("vous gagner")
print(sal_hor)
print("€ par heure")
{% endhighlight %}

# Openclassroom Base Python: Calculette

Voici les lignes de code que j'ai réalisées.
Choisissez un article et cela déduira son montant de votre porte-monnaie

<img src="/assets/image/1.jpg" alt="1" width="50" height="50">


{% highlight python %}
nombre1=int(input("choissisez un nombre : "))
nombre2=int(input("choissisez un nombre : "))
operateur=input("choissisez un operateur : ")

if operateur== "+" :
    resultat=nombre1+nombre2
if operateur== "-" :
    resultat=nombre1-nombre2
if operateur == "/":
    resultat=nombre1/nombre2
if operateur == "*":
    resultat=nombre1*nombre2




if nombre2==0 and operateur=="/":
    print("resultat impossible")

else:
    round(resultat)
    print(resultat)
{% endhighlight %}



<a href="https://vipecollie.github.io" target="_blank" rel="noopener">
Retour
</a>
