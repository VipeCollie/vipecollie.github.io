---
layout: default
title: "OpenClassrooms : Bases de Python"
date: 2025-11-08
categories: [blog, jekyll]
---

# OpenClassrooms : Bases de Python

J’ai suivi la formation **OpenClassrooms : Bases de Python**.

Contrairement à Citizen Code, cette formation propose à la fois des **vidéos** et des **cours écrits**, ce qui m’a permis de mieux comprendre les concepts abordés.  
Elle m’a aidé à apprendre les bases du langage Python, notamment la création de fonctions, les calculs et l’utilisation des entrées utilisateur.

Je recommande cette formation pour bien débuter en programmation Python.

<img src="/assets/image/Openclassroom1.jpg" alt="Formation OpenClassrooms Python" width="700" height="500">

## Exemple de code réalisé

Voici un exemple de programme que j’ai réalisé pendant la formation.  
Il permet de calculer un salaire horaire à partir d’un salaire annuel.

{% highlight python %}



def salaire_mensuel(salaire_annuel):
    return salaire_annuel / 12


def salaire_hebdomadaire(salaire_mensuel):
    return salaire_mensuel / 4


def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    return salaire_hebdomadaire / heures_travaillees


heures = int(input("Entrez le nombre d'heures travaillées par semaine : "))
salaire_annuel = int(input("Entrez le montant de votre salaire annuel (€) : "))

mensuel = salaire_mensuel(salaire_annuel)
hebdo = salaire_hebdomadaire(mensuel)
horaire = salaire_horaire(hebdo, heures)

print(f"Vous gagnez {horaire:.2f} € par heure.")
{% endhighlight %}

  
