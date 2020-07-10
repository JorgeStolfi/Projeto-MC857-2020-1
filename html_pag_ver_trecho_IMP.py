import html_pag_generica
import html_texto
import html_paragrafo
import html_table
import html_lista_de_poltronas_de_trecho
import html_resumo_de_trecho
import html_botao_simples
import html_botao_submit
import poltrona
import sessao
import compra
import trecho
from utils_testes import erro_prog, aviso_prog

from trecho import obtem_atributos, obtem_poltronas

def gera(ses, trc, comprar, alterar, erros):
  if comprar:
    assert (ses != None) and (not sessao.eh_administrador(ses)): # Paranóia.
    id_cpr = sessao.obtem_carrinho(ses)
  else:
    id_cpr = None

  if alterar:
    assert sessao.eh_administrador(ses) # Paranóia.

  # Idenfiticadores do trecho e do carrinho:
  id_trc = trecho.obtem_identificador(trc)

  # Dados gerais do trecho:
  bt_alterar_trecho = alterar
  bt_clonar_trecho = alterar
  bt_fechar_trecho = alterar
  linha_resumo = html_resumo_de_trecho.gera \
    (trc, False, bt_alterar_trecho, bt_clonar_trecho, bt_fechar_trecho)
  ht_resumo = " ".join(linha_resumo) 

  # Lista de poltronas:
  pols_ids = poltrona.busca_por_trecho(trc)
  bt_compar_poltrona = comprar
  bt_trocar_poltrona = comprar
  ht_pols = html_lista_de_poltronas_de_trecho.gera \
    (pols_ids, id_trc, bt_trocar_poltrona, bt_comprar_poltrona, id_cpr)
  ht_conteudo = ht_resumo + "<br/>" + ht_pols
  return html_pag_generica.gera(ses, ht_conteudo, erros)

