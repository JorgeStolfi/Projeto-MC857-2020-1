import compra
import trecho
import poltrona
import html_span
import html_botao_submit
import html_botao_simples
import html_estilo_cabecalho_de_tabela
import sys

def gera(pol, alterar, comprar, excluir, fazer_checkin, embarcar):
  
  assert int(alterar) + int(comprar) + int(excluir) <= 1 # No máximo um deve ser "True"

  campos = [].copy() # Campos a devolver

  estilo = "font-size:20px;font-weight:bold;" 

  # Obtem atributos da poltrona:
  id_pol = poltrona.obtem_identificador(pol)
  atrs_pol = poltrona.obtem_atributos(pol)

  numero = atrs_pol['numero']
  preco = atrs_pol['preco']
  oferta = atrs_pol['oferta'] # Se a poltrona está em oferta.
  id_cpr = atrs_pol['id_compra'] # Pedido de compra que reservou a poltrona, ou {None}
  fez_checkin = atrs_pol['fez_checkin'] # Passageiro já fez checkin?
  embarcou = atrs_pol['embarcou'] # Passageiro já embarcou?
  if id_cpr != None:
    # Poltrona está reservada.  Determina a compra:
    cpr = compra.busca_por_identificador(id_cpr)
    assert cpr != None # Paranóia.
  else:
    # Poltrona está livre:
    cpr = None

  args_cmd = { 'íd_poltrona': id_pol } # Argumentos para os comandos.

  # Número da poltrona sempre aparece:
  ht_numero = html_span.gera(estilo, numero)
  campos.append(ht_numero)

  # Preço da poltrona senmpre aparece:
  ht_preco = html_span.gera(estilo, preco)
  campos.append(ht_preco)

  # Indicação de oferta sempre aparece:
  ht_oferta = html_span.gera(estilo + "color:'#ffbb00';", "&#9733;" if oferta else "")
  campos.append(ht_oferta)

  # Coluna de identificador da compra sempre aparece:
  ht_id_cpr = html_span.gera(estilo, id_cpr if cpr != None else "LIVRE")
  campos.append(ht_id_cpr);

  # Coluna de "fez checkin" sempre aparece:
  ht_fez_checkin = html_span.gera(estilo, "CK" if fez_checkin else "")
  campos.append(ht_fez_checkin);

  # Coluna de "embarcou" sempre aparece:
  ht_embarcou = html_span.gera(estilo, "EM" if embarcou else "")
  campos.append(ht_embarcou);

  # Coluna do botão "Ver" sempre aparece:
  ht_bt_ver = html_botao_simples.gera("Ver", "ver_poltrona", {'id_poltrona': id_pol}, "55ee55")
  campos.append(ht_bt_ver);

  # Coluna do botão de ação:
  if alterar:
    ht_bt_acao = html_botao_simples.gera("Alterar", "solicitar_pag_alterar_poltrona", args_cmd, '#bca360')
  elif comprar:
    ht_bt_acao = html_botao_simples.gera("Comprar", 'comprar_poltrona', args_cmd, '#ff0000')
  elif excluir:
    ht_bt_acao = html_botao_simples.gera("Excluir", 'excluir_poltrona', args_cmd, '#ff0000')
  else:
    ht_bt_acao = ""
  campos.append(ht_bt_acao);

  if fazer_checkin:
    # Campos para checkin:
    if cpr != None:
      # Nome e documento do passageiro, e botão de fazer checkin:
      nome_pass = compra.obtem_atributo(cpr, 'nome_pass')
      doc_pass = compra.obtem_atributo(cpr, 'doc_pass')

      ht_nome_pass = html_span.gera(estilo, nome_pass)
      campos.append(ht_nome_pass);

      ht_doc_pass = html_span.gera(estilo, doc_pass)
      campos.append(ht_doc_pass);

      if fez_checkin:
        ht_bt_checkin = ""
      else:
        # Apresentando o botão fazer checkin somente quando o status é pago
        if compra.obtem_atributo(cpr, 'status') == 'pago':
          ht_bt_checkin = html_botao_simples.gera("Checkin", 'fazer_checkin', args_cmd, '#55ee55')
          campos.append(ht_bt_checkin);
    else:
      # Campos em branco:
      campos.append("");
      campos.append("");
      campos.append("");

  if embarcar:
    ht_bt_embarcar = ""
    if fez_checkin:
      ht_bt_embarcar = html_botao_simples.gera("Embarcar", 'embarcar', args_cmd, '#55ee55')
    campos.append(ht_bt_embarcar);

  return campos

def gera_cabecalho(fazer_checkin):

  campos = [].copy() # Campos a devolver

  # Devolve a linha de cabeçalho:
  estilo = html_estilo_cabecalho_de_tabela.gera()
  campos.append(html_span.gera(estilo, "NP"))      # Número da poltrona.
  campos.append(html_span.gera(estilo, "Preço"))   # Preço.
  campos.append(html_span.gera(estilo, "OF"))      # É oferta?
  campos.append(html_span.gera(estilo, "Compra"))  # Compra que reservou.
  campos.append(html_span.gera(estilo, "CK"))      # Passageiro fez checkin?
  campos.append(html_span.gera(estilo, "EM"))      # Passageiro embarcou?
  campos.append("");                               # Botão "Ver".
  campos.append("");                               # Botão "Alterar"/"Comprar"/"Excluir".

  if fazer_checkin:
    campos.append(html_span.gera(estilo, "Passageiro"))   # Nome do passageiro.
    campos.append(html_span.gera(estilo, "Documento"))    # Docmento do passageiro.
    campos.append("")                                     # Botão "Checkin.
  
  return campos

def gera_legenda(fazer_checkin):

  estilo = "font-size:20px;font-weight:bold;" 
  
  legenda_txt = \
    "<br/>" + \
    "NP = Número da poltrona<br/>" + \
    "OF = Passagem em promoção<br/>" + \
    "CK = Passageiro já fez checkin<br/>" + \
    "EM = Passageiro já embarcou<br/>"
  
  ht_legenda = html_span.gera(estilo, legenda_txt)
  return ht_legenda
