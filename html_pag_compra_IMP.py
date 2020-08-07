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

def gera(ses, cpr, atrs, erros):

  # Validação dos parâmetros:
  assert ses != None # Paranóia (cliente deslogado não deve poder ver compra nenhuma).
  assert sessao.aberta(ses) # Paranóia.
  usr_ses = sessao.obtem_usuario(ses)
  assert usr_ses != None # Paranóia.
  admin = usuario.obtem_atributo(usr_ses, 'administrador')
  carr = None if admin or ses == None else sessao.obtem_carrinho(ses)
  
  if atrs == None: atrs = {}.copy() # Por via das dúvidas.

  # Botões de acão:
  ht_submit = ""
  ht_bt_def_carr = ""
  ht_bt_cancel = ""
  args_bt = { 'id_compra': id_cpr }

  if cpr == None:
    # Nova compra:
    assert not admin # Paranóia (administrador não deve poder criar novas compras).
    id_cpr = None
    novo = True
    titulo = "Nova compra"
  else:
    assert type(cpr) is compra.Objeto_Compra
    usr_cpr = compra.obtem_cliente(cpr)
    assert usr_cpr != None # Paranóia.
    assert admin or (usr_ses == usr_cpr) # Paranóia (cliente comum só pode ver compras suas).

    id_cpr = compra.obtem_identificador(cpr)
    assert id_cpr != None # Paranóia.

    # Título da página:
    if admin:
      titulo = f"Compra {id_compra}"
    elif cpr == carr:
      titulo = "Seu carrinho de compras"
    else:
      titulo = f"Sua compra {id_compra}"
      ht_bt_def_carr = html_botao_simples.gera("Definir como carrinho", "definir_carrinho", args_bt, "#44ff00")

    # Completa {atrs} com atributos de {cpr}:
    atrs_cpr = compra.obtem_atributos(cpr)
    assert atrs_cpr != None # Paranóia
    for ch, val in atrs_cpr.items():
      if not ch in atrs: atrs[ch] = val
    
    # Botoes de ação:
    # O submit é "Alterar":
    ht_submit += html_botao_submit.gera("Alterar", "alterar_compra", None, "#ff0000")
    if not admin and (compra.obtem_status(cpr) == 'comprando'):
      # Tem botão submit de "Finalizar compra" que aplica alterações:
      ht_submit += html_botao_submit.gera("Finalizar", "finalizar_compra", None, "#55ff00")
      ht_bt_cancel = html_botao_simples.gera("Continuar comprando", 'principal', None, "#ff2200")
    else:
      ht_bt_cancel = html_botao_simples.gera("Voltar", 'principal', None, "#ff2200")

  ht_titulo = "<h2>" + titulo + "</h2>"

  # Constrói formulário com dados da compra:
  ht_dados_da_compra = html_form_dados_de_compra.gera(id_cpr, atrs, admin, ht_submit)

  # Constrói a lista de poltronas da compra:
  if novo:
    ht_dados_das_poltronas = ""
  else:
    ids_pols = poltrona.busca_por_compra(cpr)

    if len(ids_pols) == 0:
      # Não há poltronas a mostrar.
      estilo_aviso = "color:red;font-size:20;"
      ht_dados_das_poltronas = "<br/>" + html_span.gera(estilo_aviso, "Não há poltronas disponíveis")
    else:
      ht_dados_das_poltronas = html_lista_de_poltronas_de_compra.gera(ids_pols, usr_ses, carr)

    # Verifica tempos de baldeação:
    poltronas_invalidas = compra.verificar_baldeacao(cpr)
    if erros is None: erros = [].copy()
    for id_poltrona in poltronas_invalidas:
      erros.append(f'Poltrona sem tempo para baldeação: {id_poltrona}')

  ht_conteudo = \
    ht_titulo + "\n" + \
    ht_dados_da_compra + "<br/>\n" + \
    ht_bt_def_carr + "\n" + \
    ht_bt_cancel + "<br/>\n" + \
    ht_dados_das_poltronas

  pag = html_pag_generica.gera(ses, ht_conteudo, erros)
  return pag
