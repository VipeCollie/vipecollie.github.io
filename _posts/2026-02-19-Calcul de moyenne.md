---
layout: default
title: "Python : Calcul de moyenne"
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

# Codage : Calcul de moyenne

Voici les lignes de code que j'ai réalisées.
Choisisser des notes et cela calculera la moyenne de ces notes.

<img src="/assets/image/1.jpg" alt="1" width="50" height="50">

{% highlight python %}
notes= {}
notes["mathéo"] = [12,15,17,13]
notes["lucas"]  = [8,14,12,10]
notes["alice"]  = [15,16,18,20]








moyennes= {}
moyennes["mathéo"] = (sum(notes["mathéo"]))/len(notes["mathéo"])
moyennes["lucas"]  = (sum(notes["lucas"]))/len(notes["lucas"])
moyennes["alice"]  = (sum(notes["alice"]))/len(notes["alice"])


print(moyennes)

print(max(moyennes))
print(notes)


{% endhighlight %}



<a href="https://vipecollie.github.io" target="_blank" rel="noopener">
Retour
</a>
