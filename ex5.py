# -*- encoding:utf-8 -*-

# About me
name = u"Евгений"
age = 23
weight = 72 # кг
height = 182 # см
eyes = u"Голубые"
teeth = u"Белые"
hair = u"Рыжие"

print u"Давайте поговорим о человеке по имени %s." % name
print u"Его рост состовляет %d см." % height
print u"Он весит %d кг." % weight
print u"На самом деле это не так и много."
print u"Его глаза %s и волосы %s." % (eyes, hair)
print u"Его зубы обычно %s, хотя он любит пить кофе." % teeth
print u"Если я сложу %d, %d и %d, то получу %d." % (
    age, weight, height, weight + age + height)

