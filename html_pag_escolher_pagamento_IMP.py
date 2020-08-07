import sessao
import usuario
import compra
import usuario

import html_pag_generica
import html_form
import html_botao_submit
import html_botao_simples

import re
import html_form_escolher_pagamento

def gera(ses, cpr, erros):
  id_compra = compra.obtem_identificador(cpr);
  ht_form = html_form_escolher_pagamento.gera(cpr)
  ht_cancelar = html_botao_simples.gera("Cancelar", "principal", None, "#ffff00")
  ht_conteudo = html_form.gera(ht_form + " " + ht_cancelar)
  pag = html_pag_generica.gera(ses, ht_conteudo, erros)
  return pag

