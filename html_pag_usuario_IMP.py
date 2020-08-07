import compra
import usuario
import poltrona
import trecho
import sessao

import html_form_dados_de_usuario
import html_pag_generica
import html_botao_simples
import html_botao_submit
import html_table
import html_span
import html_label
import sys

def gera(ses, usr, atrs, erros):

  # Obtem usuário da sessão, determina privilégios:
  usr_ses = None if ses == None else sessao.obtem_usuario(ses)
  if usr_ses == None:
    # Usuário que pediu não está logado:
    admin = False
    mesmo = False
  else:
    assert type(usr_ses) is usuario.Objeto_Usuario
    admin = usuario.obtem_atributo(usr_ses, "administrador")
    mesmo = (usr_ses == usr)

  if atrs == None: atrs = {}.copy() # Por via das dúvidas.
  
  ht_submit = ""
  ht_bt_cancel = ""
  if usr == None:
    # Cadastramento de novo usuário:
    id_usr = None
    ht_submit += html_botao_submit.gera("Cadastrar", "cadastrar_usuario", None, "#ff0000")
    titulo = "Novo usuário"
  else:
    # Visualização/alteração de usuário existente:
    assert usr_ses != None, "operação não autorizada sem login"
    assert admin or mesmo, "usuário não está autorizado a efetuar esta operação"
    assert type(usr) is usuario.Objeto_Usuario
    id_usr = usuario.obtem_identificador(usr)
    assert id_usr != None # Paranóia.
    
    if mesmo:
      titulo = f"Sua conta"
    else:
      titulo = f"Usuário {id_usr}"
    
    # Completa {atrs} com atributos de {usr}:
    atrs_usr = usuario.obtem_atributos(usr)
    assert atrs_usr != None # Paranóia
    for ch, val in atrs_usr.items():
      if not ch in atrs: atrs[ch] = val

    # Botoes de ação:
    ht_submit += html_botao_submit.gera("Alterar", "alterar_usuario", None, "#ff0000")

  ht_bt_cancel = html_botao_simples.gera("Voltar", 'principal', None, "#ff2200")
  
  ht_titulo = "<h2>" + titulo + "</h2>"
    
  # Cria formulário:
  ht_form = html_form_dados_de_usuario.gera(id_usr, atrs, admin, ht_submit)

  # Botoes adicionais:
  ht_bt_linhas = [].copy()
  if usr != None and not mesmo:
    # Botões para administrador ver objetos associados a usuário:
    args_bt = {'id': id_usr}
    estilo_n = "font-family:\"Courier\";font-size:20;"
    
    n_compras = len(usuario.compras_abertas(usr))
    ht_n_compras = html_span.gera(estilo_n, str(n_compras))
    ht_bt_compras = html_botao_simples.gera("Ver compras", "ver_compras_de_usuario", args_bt, '#eeee55')
    ht_bt_linhas.append((html_label.gera("Compras abertas", ":"), ht_n_compras, ht_bt_compras,))
    
    n_sessoes = len(usuario.sessoes_abertas(usr))
    ht_n_sessoes = html_span.gera(estilo_n, str(n_sessoes))
    ht_bt_sessoes = html_botao_simples.gera("Ver sessões", "ver_sessoes_de_usuario", args_bt, '#eeee55')
    ht_bt_linhas.append((html_label.gera("Sessoes abertas", ":"), ht_n_sessoes, ht_bt_sessoes,))
    
    n_poltronas = len(usuario.poltronas_abertas(usr))
    ht_n_poltronas = html_span.gera(estilo_n, str(n_poltronas))
    ht_bt_poltronas = html_botao_simples.gera("Ver poltronas", "ver_poltronas_de_usuario", args_bt, '#eeee55')
    ht_bt_linhas.append((html_label.gera("Poltronas abertas", ":"), ht_n_poltronas, ht_bt_poltronas,))
    
  ht_bts_ver_coisas = html_table.gera(ht_bt_linhas, ("", "",))
  
  ht_conteudo = \
    ht_titulo + \
    ht_form + "<br/>\n" + \
    ht_bts_ver_coisas + "<br/>" + \
    ht_bt_cancel

  pag = html_pag_generica.gera(ses, ht_conteudo, erros)
  return pag
