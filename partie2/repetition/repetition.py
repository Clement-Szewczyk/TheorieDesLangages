import sys
sys.path.append('../../')
from automate import Automate

import os
from IPython.display import display, Image

if os.path.exists('repet1.png'):
    os.remove('repet1.png')
if os.path.exists('repet.png'):
    os.remove('repet.png')


#Automate 1

automate1 = Automate({'a', 'b'})

automate1.ajouter_etat('0', initial=True)
automate1.ajouter_etat('1', initial=True)
automate1.ajouter_etat('2', terminal=True)

automate1.ajouter_transition('0', ['a'], '2')
automate1.ajouter_transition('1', ['b'], '2')

print('Automate à répéter:')
automate1.to_png('repet1')
display(Image('repet1.png'))

print("\n\n")

# Repetition de l'automate 1
print("Repetition de l'automate :\n")
automate = automate1.repetition()
automate.to_png('repet')
display(Image('repet.png'))