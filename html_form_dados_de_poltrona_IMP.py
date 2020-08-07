import poltrona
import html_botao_submit
import html_form_table
import html_form

def gera(id_pol, atrs, admin, ht_submit):
 
  if atrs == None: atrs = {} # Por via das dúvidas.
  atrs = atrs.copy() # Para que as alterações sejam locais.

  atrs['id_poltrona'] = id_pol

  # Dados para {html_form_table.gera}
  # {(rotulo,tipo,chave,dica,visivel,editavel,obrigatorio)}
  dados_linhas = [].copy()

  # Dados para {html_form_table.gera}
  # {(rotulo,tipo,chave,dica,visivel,editavel,obrigatorio)}
  # Todos os campos são "readonly" para clientes comuns.
  # Campos 'oferta' e 'preco' são editáveis por administrador.
  atrs['id_poltrona'] = id_pol
  # Campos de tipo "checkbox" não podem ser obrigatórios pois isso significa "obrig. True".
  dados_linhas = \
    (
      ( "ID",    "text",     'id_poltrona', None,    admin, False, True,  ),
      ("Trecho", "text",     'id_trecho',   None,     True, False, True,  ),  
      ("Compra", "text",     'id_compra',   None,     True, False, True,  ),  
      ("Número", "text",     'numero',      None,     True, False, True,  ),  
      ("Oferta", "checkbox", 'oferta',      None,     True, admin, False, ),
      ("Preço",  "numeric",  'preco',       "NNN.NN", True, admin, True,  ),  
    )

  ht_campos = html_form_table.gera(dados_linhas, atrs)

  ht_conteudo = \
    ht_campos + "<br/>" + \
    ht_submit
  
  ht_form = html_form.gera(ht_conteudo)

  return ht_form
