#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

import codecs, sys

outf = codecs.getwriter('utf-8')(sys.stdout, errors='replace')
stdout = outf

age = input('Сколько тебе лет? ')
height = input('Каков твой рост? ')
weight = input('Сколько ты весишь? ')

print("Итак, тебе %s лет, в тебе %s роста и %s кг веса." % \
      (age, height, weight))
