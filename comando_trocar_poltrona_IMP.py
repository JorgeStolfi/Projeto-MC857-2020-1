import html_pag_generica
import html_pag_mensagem_de_erro
import html_lista_de_poltronas_de_trecho
import sessao
import compra
import poltrona
import trecho
import sys

def processa(ses, id_poltrona, id_trecho, id_compra):
  
  # Desassocia poltrona a compra
  pol = poltrona.busca_por_identificador(id_poltrona)
  poltrona.muda_atributos(pol, { 'id_compra': None })

  # Monta página:
  trc = trecho.busca_por_identificador(id_trecho)
  livres = poltrona.lista_livres(trc)  

  if ses == None:
      erros = ["sessao inválida"]
      pag = html_pag_mensagem_de_erro.gera(ses, erros)
  elif trc == None:
    erros = ["trecho não existe"]
    pag = html_pag_mensagem_de_erro.gera(ses, erros)
  else:
    ht_conteudo = html_lista_de_poltronas_de_trecho.gera(livres, id_trecho, None, True, id_compra)
    pag = html_pag_generica.gera(ses, ht_conteudo, None)
  return pag
