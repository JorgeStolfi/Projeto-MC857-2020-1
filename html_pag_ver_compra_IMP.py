import compra
import html_botao_simples
import html_lista_de_poltronas_de_compra
import html_pag_generica
import html_resumo_de_compra
import html_form_dados_de_compra
import poltrona
import sessao
import usuario
import sys
import json

def gera(ses, cpr, excluir, trocar, erros):

  # Validação dos parâmetros:
  assert cpr != None

  id_compra = compra.obtem_identificador(cpr)

  # Determina o dono da sessão {ses}, e se é administrador.
  usr_ses = sessao.obtem_usuario(ses)
  assert usr_ses != None # Não deveria ver compra sem estar logado.
  admin = sessao.eh_administrador(ses)

  # Determina o dono da compra. Não pode ser {None} nem administrador:
  usr_cpr = compra.obtem_cliente(cpr)
  assert usr_cpr != None
  assert not usuario.obtem_atributo(usr_cpr, 'administrador')

  # Determina se a compra é o carrinho da sessão {ses}:
  eh_carrinho = sessao.obtem_carrinho(ses) == cpr
  
  ht_conteudo = ""
  args_bt = { 'id_compra': id_compra }
  
  # Cabeçalho da compra:
  ht_cpr_resumo = html_form_dados_de_compra.gera(cpr, admin, "Ver", "ver_compra")
  ht_conteudo += ht_cpr_resumo

  # Lista de itens da compra
  ids_poltronas = compra.obtem_poltronas(cpr)
  excluir_pol = excluir
  trocar_pol = trocar
  ht_poltronas = html_lista_de_poltronas_de_compra.gera(ids_poltronas, id_compra, excluir_pol, trocar_pol)

  if (eh_carrinho):
    ht_conteudo += "<label> Esta compra é o seu carrinho atual. </label><br/>\n"
    ht_bt_definir_carrinho = html_botao_simples.gera("Definir Carrinho", 'definir_carrinho', args_bt, '#ff3300')
    ht_conteudo += "<br/>\n" + ht_bt_definir_carrinho
  
  status = compra.obtem_status(cpr)
  if (status == "aberto"):
    ht_bt_finalizar = html_botao_simples.gera("Finalizar Compra", 'finalizar_compra', args_bt, '#ff3300')
    ht_conteudo += "<br/>\n" + ht_bt_finalizar
    ht_bt_continuar_compra = html_botao_simples.gera("Continuar Comprando", 'principal', None, '#ffdd22')

  pag = html_pag_generica.gera(ses, ht_conteudo, erros)
  return pag
