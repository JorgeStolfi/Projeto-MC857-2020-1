
import html_lista_de_poltronas_de_usuario_IMP

def gera(ids_poltronas):
  """Retorna um trecho de HTML que descreve as poltronas cujos identificadores
  estão na lista {ids_poltronas}. Todas elas estão associadas à um usuário.
  
  O resultado é um elemento "<table>...</table>". Cada linha é 
  gerada por {html_resumo_de_poltrona_de_usuario.gera}
  com argumentos {(pol)}, e 
  tem os dados essenciais do trecho ao qual a poltrona pertence,
  o número da poltrona, e o preço"""
  return html_lista_de_poltronas_de_usuario_IMP.gera(ids_poltronas)
