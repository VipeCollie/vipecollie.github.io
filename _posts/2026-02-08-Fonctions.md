---
layout: default
title: "Openclassroom : Fonctions"
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

# Openclassroom : Fonctions

J'ai fait la formation Openclassroom : bases Python

A la différence de Citizencode il y a des vidéos et des cours écrits. 
Ca m'a permis d'apprendre les bases de Python.
Essayez!

<img src="/assets/image/Openclassroom1.jpg" alt="1" width="700" height="500">

Voici les lignes de code que j'ai réalisées.


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

