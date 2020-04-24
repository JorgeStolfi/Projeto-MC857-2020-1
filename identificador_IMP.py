# Implementação do módulo {identificador}.

import sys

def de_indice(let, indice):
  assert type(let) is str and len(let) == 1
  assert type(indice) is int and indice >= 0
  return "%s-%08d" % (let,indice)

def para_indice(let, ident):
  assert type(let) is str and len(let) == 1
  assert type(ident) is str and len(ident) == 10 
  assert ident[0:1] == let 
  assert ident[1:2] == "-"
  indice = int(ident[2:])
  return indice

def de_lista_de_indices(let, indices):
  idents = [].copy()
  if indices != None:
    assert type(indices) is tuple or type(indices) is list
    # Resultado deve ser uma lista de tuplas, cada uma contendo apenas um índice:
    for el in indices:
      if type(el) is int:
        idents.append(de_indice(let,el))
      elif type(el) is tuple or type(el) is list:
        assert len(el) == 1
        idents.append(de_indice(let,el[0]))
    return idents
  else:
    erro_prog("tipo de " + str(indices) + " inválido")
  
