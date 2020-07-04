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
  linha_resumo = html_resumo_de_trecho.gera(trc, False, alterar, alterar)
  ht_resumo = " ".join(linha_resumo) 
  pols_ids = poltrona.busca_por_trecho(trc)
  if ses == None:
    id_carrinho = None
  else:
    carrinho = sessao.obtem_carrinho(ses)
    if carrinho == None:
      id_carrinho = None
    else:
      assert type(carrinho) is compra.Objeto_Compra
      id_carrinho = compra.obtem_identificador(carrinho)
  if id_carrinho == None: assert not comprar
  trc_id = trecho.obtem_identificador(trc)
  ht_pols = html_lista_de_poltronas_de_trecho.gera(pols_ids, trc_id, alterar, comprar, id_carrinho)
  ht_btn = html_botao_simples.gera("Encerrar", "encerrar_trecho", {"id_trecho": trc_id}, "red")
  ht_conteudo = ht_resumo + "<br/>" + ht_pols + "<br/>" + ht_btn
  return html_pag_generica.gera(ses, ht_conteudo, erros)
