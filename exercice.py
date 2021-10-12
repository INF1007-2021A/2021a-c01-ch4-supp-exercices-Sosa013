#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
# Question 1

def is_even_len(string):
	longueur_chaine = len(string)
	if longueur_chaine % 2 == 0:
		print("pair")
	else:
		print("impair")

	return longueur_chaine

# Question 2

def get_num_char(string, char):
	lettre_debut = 0

	for char in string:
		lettre_debut +=1

	return lettre_debut

# Question 3

def get_first_part_of_name(name):
	nouveau_mot = name[0:4]
	nouveau_mot_majuscule = nouveau_mot.capitalize()
	print("Bonjour" + " " + str(nouveau_mot_majuscule))
	return nouveau_mot_majuscule

# Question 4

def get_random_sentence(animals, adjectives, fruits):

	reponse = print("Bonjour, aujourd'hui j'ai vu un " + str(animals[1]) + " s'emparer d'un panier " + str(adjectives[2]) + " plein de " + str(fruits[1]))

if __name__ == "__main__":
	spam = "Bonjour!"
	parity = "pair" if is_even_len(spam) else "impair"
	print(f"Le nombre de caractère dans la chaine '{spam}' est {parity}.")

	eggs = "Hello, world!"
	print(f"Le nombre d'occurrence de l dans '{eggs}' est : {get_num_char(eggs, 'l')}.")

	parrot = "jean-marc"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "bananes")
	print(get_random_sentence(animals, adjectives, fruits))
