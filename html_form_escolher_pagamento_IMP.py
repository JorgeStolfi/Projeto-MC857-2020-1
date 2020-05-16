import html_botao_radio
import html_botao_submit
import html_botao_simples
import html_form
import html_label
def gera(titulo, post_url):
  # "Visa"/"Boleto"/"Depósito"/"Bois"
  paragrafo = html_label.gera("Selecione o método de pagamento", ": ")
  visa = html_botao_radio.gera("visa", "metodo_pagamento", "Visa")
  boleto = html_botao_radio.gera("boleto", "metodo_pagamento", "Boleto")
  deposito = html_botao_radio.gera("deposito", "metodo_pagamento", "Deposito")
  bois = html_botao_radio.gera("bois", "metodo_pagamento", "Bois")
  ht_submit = html_botao_submit.gera(titulo, post_url, None, '#55ee55')
  ht_cancel = html_botao_simples.gera("Cancelar", 'principal', None, '#ee5555')

  ht_campos = \
    ( "    " + paragrafo + "\n" ) + \
      ( " <br>   "  +  "\n" ) + \
    ( "    " + visa + "\n" ) + \
    ( "    " + boleto + "\n" ) + \
    ( "    " + deposito + "\n" ) + \
    ( "    " + bois + "\n" ) + \
    ( "    " + ht_submit + "\n" ) + \
    ( "    " + ht_cancel + "\n" )
  return html_form.gera(ht_campos)
