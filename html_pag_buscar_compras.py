import html_pag_buscar_compras_IMP

def gera(ses, atrs, admin, erros):
  """ Retorna uma página contendo o formulário para buscar pedidos de compra.
  Normalmente é usada por administradores. Os campos do formulário são 
  um subconjuto dos atributos de um objeto da classe {Objeto_Compra}.

  Se {atrs} não for {None}, deve ser um dicionário
  que define os valores iniciais dos campos.
  
  A página terá um botão de tipo 'submit' com texto "Buscar" que,
  quando acionado, emite uma ação POST com comando 'buscar_trechos. 
  Haverá também um botão simples com texto "Cancelar" que emite
  o comando 'principal'."""
  return html_pag_buscar_compras_IMP.gera(ses, atrs, admin, erros)
