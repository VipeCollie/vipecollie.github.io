---
layout: default
title: Accueil
---

# Bienvenue sur ma page

## Articles de Blog

{% for post in site.posts %}
- [{{ post.title }}]({{ post.url }})
{% endfor %}

## Portfolio

{% for page in site.pages %}
  {% if page.path contains '_portfolio' %}
  - [{{ page.title }}]({{ page.url }})
  {% endif %}
{% endfor %}
