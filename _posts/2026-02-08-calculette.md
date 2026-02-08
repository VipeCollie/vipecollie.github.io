---
layout: default
title: "Python : Calculette"
date: 2026-01-02
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

# Codage : Calculette

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



