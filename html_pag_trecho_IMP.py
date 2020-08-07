import usuario
import poltrona
import sessao
import compra
import trecho

import html_form_dados_de_trecho
import html_pag_generica
import html_paragrafo
import html_table
import html_lista_de_poltronas_de_trecho
import html_botao_simples
import html_botao_submit
import html_form
import html_table
import html_span
import html_label

from utils_testes import erro_prog, aviso_prog
import sys

def gera(ses, trc, atrs, erros):
  # Obtem usuário da sessão, determina privilégios:
  usr_ses = None if ses == None else sessao.obtem_usuario(ses)
  admin = sessao.eh_administrador(ses)

  if atrs == None: atrs = {}.copy() # Por via das dúvidas.

  # Botões de acão:
  ht_submit = ""
  if trc == None:
    # Acrescentando novo trecho:
    id_trc = None
    novo = True
    # O submit é "Acrescentar":
    ht_submit += html_botao_submit.gera("Acrescentar", "acrescentar_trecho", None, "#ff0000")
  else:
    # Visualização/alteração de trecho existente:
    assert type(trc) is trecho.Objeto_Trecho
    novo = False

    id_trc = trecho.obtem_identificador(trc)
    assert id_trc != None # Paranóia.

    # Completa {atrs} com atributos de {trc}:
    atrs_trc = trecho.obtem_atributos(trc)
    assert atrs_trc != None # Paranóia
    for ch, val in atrs_trc.items():
      if not ch in atrs: atrs[ch] = val

    # Botoes de ação:
    if admin:
      # O submit é "Alterar":
      ht_submit += html_botao_submit.gera("Alterar", "alterar_trecho", None, "#ff0000")
      # Tem tamém botão "Clonar":
      ht_submit += html_botao_simples.gera("Clonar", "clonar_trecho", {'id_trecho': id_trc}, "#ff0000")

  # Constrói formulário com dados do trecho:
  ht_dados_trecho = html_form_dados_de_trecho.gera(id_trc, atrs, admin, ht_submit)

  # Constrói a lista de poltronas do trecho:
  if novo:
    ht_dados_poltronas = ""
  else:
    # Formata a lista de poltronas:
    ids_pols_todas = poltrona.busca_por_trecho(trc)
    if admin:
      # Mostra todas as poltronas do trecho:
      ids_pols_ver = ids_pols_todas
    else:
      # Mostra só as poltronas disponíveis ou reservadas para compras do usuário {usr}:
      trc_encerrado = atrs_trc['encerrado']
      ids_pols_ver = [].copy()
      for id_pol in ids_pols_todas:
        assert id_pol != None # Paranóia.
        pol = poltrona.busca_por_identificador(id_pol)
        assert pol != None # Paranóia.
        id_cpr_pol =  poltrona.obtem_atributo(pol, 'id_compra')
        cpr_pol = None if id_cpr_pol == None else compra.busca_por_identificador(id_cpr_pol)
        usr_pol = None if cpr_pol == None else compra.obtem_cliente(cpr_pol)
        # Verifica relevância de {pol} para o usuário:
        livre = (cpr_pol == None)
        if (livre and (not trc_encerrado)) or ((usr_ses != None) and (usr_pol == usr_ses)):
          ids_pols_ver.append(id_pol)

    if len(ids_pols_ver) == 0:
      # Não há poltronas a mostrar.
      estilo_aviso = "color:red;font-size:20;"
      ht_dados_poltronas = "<br/>" + html_span.gera(estilo_aviso, "Não há poltronas disponíveis")
    else:
      # Formata a lista de poltronas:
      fazer_checkin = admin # Deve ter botão de "Checkin" em cada poltrona?
      # sys.stderr.write(" ids_pols = %s\n" % str(ids_pols))
      # sys.stderr.write(" id_trc = %s\n" % str(id_trc))

      carr = None if ses == None else sessao.obtem_carrinho(ses)
      ht_dados_poltronas = html_lista_de_poltronas_de_trecho.gera(ids_pols_ver, usr_ses, carr)

  # Botão "Voltar":
  ht_bt_cancel = html_botao_simples.gera("Voltar", 'principal', None, "#ff2200")
  
  # Monta a página:
  ht_conteudo = \
    ht_dados_trecho + "<br/>" +  \
    ht_dados_poltronas + "<br/>" +  \
    ht_bt_cancel 

  pagina = html_pag_generica.gera(ses, ht_conteudo, erros)
  return pagina

