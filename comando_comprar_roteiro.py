import comando_comprar_roteiro_IMP

def processa(ses, args):
  """Esta função é chamada quando o usuário aperta o botão "Comprar Roteiro" em
  uma página de visualização de roteiro.

  O parâmetro {args} é um objeto {Objeto_roteiro} (vide {roteiro.py}). Ou seja,
  é uma lista de ID de trechos que respeitam a ordem cronológica das viagens. Campos
  de {args} com o valoe {None} devem ser ignorados.

  O parâmetro {args} tem uma chave 'ids_trechos', seu valor deve ser um string
  que consiste de uma lista de identificadores de trechos separados 
  por vírgulas, como "T-00000005,T-00001234,T-00000001".

  O resultado deve ser uma página com a visualização do carrinho com a nova
  compra."""
  return comando_comprar_roteiro_IMP.processa(ses, args)
