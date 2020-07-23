import html_pag_generica
import html_form_dados_de_poltrona
import html_botao_simples
import sessao

import poltrona

def gera(ses, pol, id_compra, excluir, erros):
  alterar_pol = sessao.eh_administrador(ses)
  comprar_pol = False
  excluir_pol = excluir
  trocar_pol  = True
  id_pol = poltrona.obtem_identificador(pol)
  atrs_pol = poltrona.obtem_atributos(pol)
  id_trecho = atrs_pol['id_trecho']

  ht_pol = html_form_dados_de_poltrona.gera(poltrona.obtem_identificador(pol), poltrona.obtem_atributos(pol), alterar_pol, comprar_pol, excluir_pol, id_compra, True)
  ht_conteudo = ht_pol

  
  if excluir_pol:
    args_excluir = { 'id_poltrona': id_pol, 'id_compra': id_compra }
    ht_excluir = html_botao_simples.gera("Excluir", 'excluir_poltrona', args_excluir, '#ff4422')
    ht_conteudo += "<br/>\n" + ht_excluir

  if trocar_pol:
    args_trocar = { 'id_poltrona': id_pol, 'id_compra': id_compra, 'id_trecho':id_trecho }
    ht_trocar = html_botao_simples.gera("Trocar", 'trocar_poltrona', args_trocar, '#ff8800')
    ht_conteudo += "<br/>\n" + ht_trocar
  pag = html_pag_generica.gera(ses, ht_conteudo, erros)
  return pag
