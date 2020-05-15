# html_form_acrescentar_trecho_IMP

# Imports trecho_IMP
import trecho_IMP; from trecho_IMP import Objeto_Trecho_IMP
import objeto
import usuario
import trecho
import assento

import tabela_generica
import tabelas
import conversao_sql
import identificador
import valida_campo; from valida_campo import ErroAtrib
from utils_testes import erro_prog, mostra
import sys

# Imports html_form_dados_de_usuario
import html_input
import html_botao_submit
import html_botao_simples
import html_form_tabela_de_campos
import html_form

def gera(atrs, admin,):
  """Retorna o formulário de nova passagem.

  O formuláro contém campos editáveis para as informações que o usuário
  deve preencher.  Se {atrs} não for {None}.

  O parâmetro {admin} diz que o usuário que pediu a criação do usuário
  (NÃO o usuário que está sendo cadastrado!) é administrador. Se for {True}, o
  formulário vai mostrar um checkbox para definir o novo usuário como
  administrador.

  O formulário conterá um botão 'Cadastrar' (de tipo 'submit').
  Quando o usuário clicar nesse botão, será emitido um comando POST com ação
  {cadastrar_usuario}.  Os argumentos desse POST são todos os atributos da classe {Objeto_Usuario},
  com os valores de {atrs} que o usuário deve ter preenchido.

  O formulário também terá um botão simples 'Cancelar',
  que, quando clicado, emite o comando 'principal'."""

  # For simplicity:
  if atrs == None: atrs = {}.copy()

  # Dados brutos para as linhas. Para cada linha, o rótulo, tipo do "<input>", nome do campo, e dica.

  dados_linhas = (
      ( "Código",             "number",     "codigo",          "xxxxxxx",                  False, ),
      ( "Origem",           "text",    "origem",         "Cidade, estado - Pais",      False, ),
      ( "Destino",              "text",     "destino",           "Cidade, estado - Pais",      False, ),
      ( "Data de partida",         "number",     "dt_partida",      "DDMMAA",  False, ),
      ( "Data de chegada",         "number",     "dt_chegada",      "DDMMAA",  False, ),
  )

  ht_tabela = html_form_tabela_de_campos.gera(dados_linhas, atrs, admin)

  ht_submit = html_botao_submit.gera("Submeter", atrs.URL, None, atrs.cor_fundo)

  ht_cancel = html_botao_simples.gera("Cancelar", 'principal', None, atrs.cor_fundo)

  ht_campos = \
    ( "    " + ht_id_usuario + "\n" if ht_id_usuario != "" else "") + \
    ( ht_tabela + "\n" ) + \
    ( "    " + ht_submit + "\n" ) + \
    ( "    " + ht_cancel + "\n" )

  return html_form.gera(ht_campos)

def cria_testes():
  global cache, nome_tb, letra_tb, colunas, diags
  inicializa(True)
  # Atributos dos trechos:
  lista_trechos = \
    [ {
        'codigo':      "AZ 4024",
        'origem':      "VCP",
        'destino':     "SDU",
        'dt_partida':  "2020-05-08 12:45",
        'dt_chegada':  "2020-05-08 13:40",
      },
      {
        'codigo':      "AZ 4036",
        'origem':      "SDU",
        'destino':     "VCP",
        'dt_partida':  "2020-05-08 19:45",
        'dt_chegada':  "2020-05-08 20:40",
      },
      {
        'codigo':      "GO 2333",
        'origem':      "SDU",
        'destino':     "VCP",
        'dt_partida':  "2020-05-08 19:33",
        'dt_chegada':  "2020-05-08 20:27",
      },
    ]
  for atrs in lista_trechos:
    trc = cria(atrs)
    assert trc != None and type(trc) is trecho.Objeto_Trecho
    id_trc = trecho.obtem_identificador(trc)
    sys.stderr.write("trecho %s criado\n" % id_trc)
    html_form_acrescentar_trecho_IMP.gera(atrs, None)
    sys.stderr.write("form_acrescentar_trecho %s criado\n" % id_trc)
  return

def verifica(trc, id, atrs):
  return objeto.verifica(trc, trecho.Objeto_Trecho, id, atrs, cache, nome_tb, letra_tb, colunas, def_obj_mem)

def diagnosticos(val):
  global cache, nome_tb, letra_tb, colunas, diags
  diags = val
  return