sonlar = [1, 2 , 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for son in sonlar :
    print(f"{son} ning kvadrati {son**2} ga teng!") 

sonlar = list(range(111))
sonlar_kvadrati = []
for son in sonlar :
    sonlar_kvadrati.append(son**2)

print(sonlar)
print(sonlar_kvadrati)