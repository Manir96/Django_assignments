#upper case

a = 'Welcome to Django for web and Ai'
print(a.upper())
#lower case
l = 'Welcome to Django for web and Ai'
print(l.lower())

b = '       Python is my favarite language'
print(b.strip())

c = 60
d = 22

f = float(c)
k = float(d)
print('int to float convert',f)
print('int to float convert',k)


dict={
    'name':'Maniruzzaman',
    'vill':'Ghatesshwori',
    'post':'Baheratoil',
    'thana':'Sakhipur',
    'Dist':'Tangail',
    'div':'Dhaka, Bangladesh',
}
for a in dict:
    print(a,'#',dict[a])