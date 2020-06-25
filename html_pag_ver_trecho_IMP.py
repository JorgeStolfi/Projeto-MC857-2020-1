import html_pag_generica
import html_texto
import html_paragrafo
import html_table 
import html_lista_de_poltronas_de_trecho
import html_resumo_de_trecho
import poltrona
import sessao
import compra
import trecho

from trecho import obtem_atributos, obtem_poltronas

def gera(ses, trc, comprar, alterar, erros):
  linha_resumo = html_resumo_de_trecho.gera(trc, False, False)
  ht_resumo = " ".join(linha_resumo) 
  pols_ids = poltrona.busca_por_trecho(trc)
  if ses == None:
    # Usuário não está logado:
    if alterar:
      aviso_prog("!! usuário não está logado; {alterar} ignorado")
      alterar = False
    if comprar:
      aviso_prog("!! usuário não está logado; {comprar} ignorado")
      comprar = False
    id_carrinho = None
  else:
    carrinho = sessao.obtem_carrinho(ses)
    if carrinho == None:
      # Usuário deve ser administrador; não pode comprar:
      if comprar:
        aviso_prog("!! sessão não tem carrinho; {comprar} ignorado")
        comprar = False
      id_carrinho = None
    else:
      assert type(carrinho) is compra.Objeto_Compra
      id_carrinho = compra.obtem_identificador(carrinho)
  trc_id = trecho.obtem_identificador(trc)
  ht_pols = html_lista_de_poltronas_de_trecho.gera(pols_ids, trc_id, alterar, comprar, id_carrinho)
  ht_conteudo = ht_resumo + "<br/>" + ht_pols
  return html_pag_generica.gera(ses, ht_conteudo, erros)
