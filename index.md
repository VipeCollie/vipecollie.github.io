---
layout: default
title: Accueil
---

# Bienvenue sur ma page

## Articles de Blog

{% for post in site.posts %}
- [{{ post.title }}]({{ post.url }})
{% endfor %}
[Présentation](_posts/2025-05-07-presentation.md)
