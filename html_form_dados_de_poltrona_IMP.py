import poltrona
import html_botao_submit
import html_form_table
import html_form

def gera(id_pol, atrs_pol, alterar, comprar, excluir, id_cpr, ver_poltrona):

  atrs_pol = atrs_pol.copy() # Para que as alterações sejam locais.

  atrs_pol['id_poltrona'] = id_pol

  # Coinsistência dos parâmetros:

  if alterar:
    # Verifica outros parâmetros:
    assert not (comprar or excluir)
    assert id_cpr == None

  if comprar:
    # Preenche o atributo 'id_compra' com a compra especificada
    assert not (alterar or excluir)
    assert id_cpr != None
    assert atrs_pol['id_compra'] == None
    atrs_pol['id_compra'] = id_cpr

  if excluir:
    # Certifica que o atributo 'id_compra' é a compra especificada
    assert not (alterar or comprar)
    assert id_cpr != None
    assert atrs_pol['id_compra'] == id_cpr

  # Campos a apresentar no formulário:

  dados_linhas = \
    (
      ("ID", "readonly", 'id_poltrona', None, False),  # Readonly.
      ("Trecho", "readonly", 'id_trecho', None, False),  # Readonly.
      ("Compra", "readonly", 'id_compra', None, False),  # Readonly.
      ("Número", "readonly", 'numero', None, False),  # Readonly.
      ("Oferta", "checkbox", 'oferta', None, False),  # Readonly exceto para administradores.
      ("Preço", "numeric", 'preco', None, False),  # Readonly exceto para administradores.
    )

  dados_linhas_adm = \
    (
      ( "ID",     "text", 'id_poltrona', None, False ),
      ( "Trecho", "text", 'id_trecho',   None, True ),      # Readonly
      ( "Compra", "text", 'id_compra',   None, True ),      # Readonly
      ( "Número", "text", 'numero',      None, False ),
      ( "Oferta", "checkbox", 'oferta',      None, False ),
      ( "Preço",  "numeric",  'preco',       None, False ),
    )

  # Todos os campos são readonly para não administradores
  dados_linhas_not_adm = \
    (
      ( "ID",     "text", 'id_poltrona', None, True ),
      ( "Trecho", "text", 'id_trecho',   None, True ),
      ( "Compra", "text", 'id_compra',   None, True ),
      ( "Número", "text", 'numero',      None, True ),
      ( "Oferta", "checkbox", 'oferta',      None, True ),
      ( "Preço",  "numeric",  'preco',       None, True ),
    )

  admin = alterar # Supõe que é administrador se for para alterar.

  if ver_poltrona:
    if admin:
      dados_linhas = dados_linhas_adm
    else:
      dados_linhas = dados_linhas_not_adm

  ht_campos = html_form_table.gera(dados_linhas, atrs_pol, admin, ver_poltrona)

  # Botão:
  args_pol_submit = {'id_poltrona': id_pol}
  if excluir:
    ht_botao = html_botao_submit.gera("Excluir", "excluir_poltrona_de_compra", None, '#bca360')
  elif alterar:
    ht_botao = html_botao_submit.gera("Alterar", "alterar_dados_de_poltrona", None, '#bca360')
  elif comprar:
    ht_botao = html_botao_submit.gera("Comprar", "comprar_poltrona", args_pol_submit, '#bca360')
  else:
    ht_botao = None

  ht_form = \
    ht_campos + \
    ( "<br/>" + ht_botao if ht_botao != None else "" )

  return html_form.gera(ht_form)
