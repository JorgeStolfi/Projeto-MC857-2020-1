import compra
import html_botao_radio
import html_botao_submit
import html_botao_simples
import html_form
import html_label

def gera(cpr):
  id_compra = compra.obtem_identificador(cpr)
  ht_titulo = html_label.gera("Selecione o método de pagamento", ": ")
  ht_opcoes = \
    html_botao_radio.gera("metodo", "paypau",   "PayPau")      + "<br/>" + \
    html_botao_radio.gera("metodo", "mrcard",   "MonsterCard") + "<br/>" + \
    html_botao_radio.gera("metodo", "boleto",   "Boleto")      + "<br/>" + \
    html_botao_radio.gera("metodo", "deposito", "Depósito")    + "<br/>" + \
    html_botao_radio.gera("metodo", "bois",     "Bois gordos") + "<br/>" + \
    html_botao_radio.gera("metodo", "balas",    "Balinhas")    

  ht_submit = html_botao_submit.gera("Alterar", "alterar_pagamento", {'id_compra': id_compra}, '#55ee55')

  ht_campos = \
    ht_titulo + "<br/>" + \
    "" + "<br/>" + \
    ht_opcoes + "<br/>" + \
    "" + "<br/>" + \
    ht_submit
  return html_form.gera(ht_campos)
