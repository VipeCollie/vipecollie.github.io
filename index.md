---
layout: default
title: Accueil
---

# Bienvenue sur ma page

Voici mes derniers articles :

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a> - {{ post.date | date: "%Y/%m/%d" }}
    </li>
  {% endfor %}
</ul>

Voici mon portfolio :
<ul>
  {% for post in site.portfolio %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a> - {{ post.date | date: "%Y/%m/%d" }}
    </li>
  {% endfor %}
</ul>
