import objeto
import trecho
import poltrona

import html_label
import html_table
import html_botao_submit
import html_botao_simples
import html_form_table
import html_form
import html_imagem
from utils_testes import erro_prog, mostra
import sys
import re

def gera(id_trecho, atrs, admin, ht_submit):

  if atrs == None: atrs = {} # Por via das dúvidas.
  atrs = atrs.copy() # Para que as alterações sejam locais.
  
  # Mostra logotipo da empresa:
  if 'codigo' in atrs and atrs['codigo'] != None:
    cod_empresa = atrs['codigo'].split()[0]
    assert re.fullmatch(r'[A-Za-z]+', cod_empresa)
    ht_logotipo = html_imagem.gera(cod_empresa + '.png', 'Logotipo empresa ' + cod_empresa, 200)
  else:
    ht_logotipo = ""

  # Dados para {html_form_table.gera}
  # {(rotulo,tipo,chave,dica,visivel,editavel,obrigatorio)}
  dados_linhas = [].copy()

  if id_trecho != None:
    # Mostrando trecho existente; inclui campo 'id_trecho' no formulário.
    # O campo é visível para administrador, mas readonly.
    atrs['id_trecho'] = id_trecho
    dados_linhas.append(
      ( "ID",              "text",       "id_trecho",      None,         admin, False, True )
    )
    novo = False
  else:
    # Criando um novo trecho. Não há campo 'id_trecho' no formulário.
    novo = True

  # Todos os campos a seguir são readonly para clientes normais.
  # Todos os campos são obrigatórios se criando trecho.
  # Campos de tipo "checkbox" não podem ser obrigatórios pois isso significa "obrig. True".
  dados_linhas += [
    ( "Código",           "text",       "codigo",         "XX NNNN",        True, novo,  novo,  ),
    ( "Origem",           "text",       "origem",         "XXX",            True, novo,  novo,  ),
    ( "Dia de partida",   "text",       "dia_partida",    "YYYY-MM-DD",     True, admin, novo,  ),
    ( "Hora de partida",  "text",       "hora_partida",   "HH:MM",          True, admin, novo,  ),
    ( "Destino",          "text",       "destino",        "XXX",            True, novo,  novo,  ),
    ( "Dia de chegada",   "text",       "dia_chegada",    "YYYY-MM-DD",     True, admin, novo,  ),
    ( "Hora de chegada",  "text",       "hora_chegada",   "HH:MM",          True, admin, novo,  ),
    ( "Veículo",          "text",       "veiculo",        "XXX-NNNN",       True, admin, novo,  ),
    ( "Encerrado",        "checkbox",   "encerrado",      None,             True, admin, False, ),
  ]
  if novo:
    # Acrescenta um campo para especificar a lista compacta de poltronas:
    dados_linhas.append(
      ( "Poltronas",        "text",       "poltronas",      "1A-20D,33: 90.00; ...",  True, True, True, ),
    )
    

  # Monta a tabela com os fragmentos HTML:
  ht_campos = html_form_table.gera(dados_linhas, atrs)

  ht_conteudo = \
    ht_logotipo + '<br clear="all" />' + \
    ht_campos + "<br/>" + \
    ht_submit

  ht_form = html_form.gera(ht_conteudo)

  return ht_form
