#Wyliczanie NWD i NWW

print "Podaj dwie liczby naturalne: "
a = input("Pierwsza: ")
b = input("Druga: ")

if a > b:
	w=a
	m=b
else:
	w = b
	m = a

r = w % m
while r:
	w = m
	m = r
	r = w % m

print "NWD liczb %i i %i wynosi %i, a ich NWW wynosi %i" % (a,b,m,a*b/m)
