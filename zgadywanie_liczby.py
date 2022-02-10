#GRA W ZGADYWANIE LICZBY - użytkownik podaje liczność zbioru losowych liczb a następnie próbuje odgadnąć, która z nich została wytypowana przez komputer
#przy każdej próbie odgadnięcia użytkownik jest informowany czy podana przez niego liczba jest mniejsza lub większa od tej wytypowanej przez komputer
#po prawidłowym odgadnięciu obok gratulacji wyświetlana jest liczba prób 

import random

end_range = input('Podaj ile liczb chcesz wygenerować: ') #odpowiedź użytkownika jest stringiem

if end_range.isdigit(): #sprawdzenie czy podany string jest liczbą
  end_range = int(end_range) #przekonwertowanie stringa do inta 
    if end_range <= 0:
      print('Następnym razem podaj liczbę większą od zera :)')
      quit() 
else:
  print('Następnym razem podaj prawdziwą liczbę!')
  quit()

#przedział otwarty z prawej strony
#jeśli wstawimy tylko jedną liczbę to wygenerowana zostanie liczba z przedziału od 0 do podanej liczby minus 1
#randint ma przedział zamknięty z prawej strony
random_number = random.randint(0, end_range)  
quesses = 0

while True:
  quesses += 1
  user_quess = input('Spróbuj odgadnąć NASZĄ liczbę: ')
  if user_quess.isdigit():
    end_range = int(user_quess) 
  else:
    print('Następnym razem podaj prawdziwą liczbę!')
    continue #powrót do początku pętli

  if user_quess == random_number:
    print('Zgadłeś, BRAWO!')
    break
  elif user_quess > random_number:
    print('Podana liczba jest zbyt DUŻA')
  else
    print('Podana liczba jest za MAŁA')
    
print('Potrzebowałeś JEDYNIE ' + str(quesses) + ' prób :)')
#print("Potrzebowałeś JEDYNIE", quesses + "prób :)")
