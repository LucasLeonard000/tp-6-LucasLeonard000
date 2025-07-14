# Replace the "ANSWER HERE" with your answer

def remove_elements(list_to_remove_elements):
	lista = list_to_remove_elements[:]
	if len(lista) > 5:
		del lista[5]
	if len(lista) > 4:
		del lista[4]	
	if len(lista) > 0:
		del lista[0]

	return lista


def add_elements(list_to_add_elements):
	lista2 = list_to_add_elements[:]
	lista2.insert(0, "Pink")
	lista2.append("Yellow")
	return lista2


def is_empty(list_to_check):
	if len(list_to_check) == 0:
		return True
	else:
		return False

def check_lists(list_to_compare1, list_to_compare2):
	if len(list_to_compare1) > 2 and len(list_to_compare2) > 2:
		if list_to_compare1[2] == list_to_compare2[2]:
			return True
		else:
			return False
	else:
		return False
	

def list_of_lists(list_of_lists_to_modify):
	lista_larga = list_of_lists_to_modify[:]
	if len(lista_larga) > 0:
		lista_larga[0] = lista_larga[0][:2]
	if len(lista_larga) > 1:
		lista_larga[1] = lista_larga[1][1:4]
	if len(lista_larga) > 2:
		lista_larga[2] = lista_larga[2][-2:]
	return lista_larga
