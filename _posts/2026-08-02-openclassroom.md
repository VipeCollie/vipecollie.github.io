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

Voici les lignes de code que j'ai réalisées.
{%highlight python%}
def salaire_mensuel(salaire_annuel):
  return salaire annuel / 12
{% endhighlight %}

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

  
