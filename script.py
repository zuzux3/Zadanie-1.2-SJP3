import re

kamiliTomek = 'Kamil ka.mil@google.com, Tomek T_o-me09k@o2.pl'

kamil = re.search("ka.*com", kamiliTomek)
tomek = re.search("T_.*pl", kamiliTomek)

str1 = 'Mail Kamila: {}\nMail Tomka: {}\n'

print(str1.format(kamil.group(), tomek.group()))