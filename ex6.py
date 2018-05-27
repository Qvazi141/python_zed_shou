# -*- encoding:utf-8 -*-

x = u"Суествует %d типов людей." % 10
binary = "Python"
do_not = u"нет"
y = u"Те кто понимает %s, и те, кто - %s." % (binary, do_not)

print x
print y
print u"Я сказал: %s." % x
print u"А ещё я сказал ' %s'." % y

hilarious = False
joke = u"Разве это не смешно?! %r"

print joke % hilarious

w = u"Эта часть строки слева..."
e = u"Эта часть строки справа."

print w + e
