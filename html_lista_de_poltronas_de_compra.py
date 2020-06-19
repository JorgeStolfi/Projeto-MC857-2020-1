
import html_lista_de_poltronas_de_compra_IMP

def gera(ids_poltronas, id_compra, excluir, trocar):
  """Retorna um trecho de HTML que descreve as poltronas cujos identificadores
  estão na lista {ids_poltronas}. Todas elas devem ser parte de um pedido de 
  compra com indetificador {id_compra}, que supostamente foi identificado
  em separado.
  
  O resultado é um elemento "<table>...</table>". Cada linha é 
  gerada por {html_resumo_de_poltrona_de_compra.gera}
  com argumentos {(pol, id_compra, excluir, trocar)}, e 
  tem os dados essenciais do trecho ao qual a poltrona pertence,
  o número da poltrona, e o preço, além dos botões solicitados
  por {exclur} e {trocar}."""
  return html_lista_de_poltronas_de_compra_IMP.gera(ids_poltronas, id_compra, excluir, trocar)
