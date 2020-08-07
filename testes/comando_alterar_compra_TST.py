#! /usr/bin/python3

import comando_alterar_compra
import tabelas
import trecho
import usuario
import sessao
import base_sql
import utils_testes
import compra

import sys

# Conecta no banco e carrega alimenta com as informações para o teste

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB", None, None)
assert res is None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes(False)

# Sessao de teste
ses = sessao.busca_por_identificador("S-00000004")

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = comando_alterar_compra
  funcao = modulo.processa
  frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False  # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

def testa_novo_passageiro():
  # Valores originais
  id_cpr = 'C-00000001'
  cpr = compra.busca_por_identificador(id_cpr)
  status = compra.obtem_atributo(cpr, 'status')

  # Novos valores
  nome_pass = 'Novo Passageiro'
  args = {'id_compra': id_cpr, 'status': status, 'nome_pass': nome_pass}
 
  testa("NovoPass", ses, args)

  # Valores atualizados
  cpr_mod = compra.busca_por_identificador('C-00000001')
  nome_pass_mod = compra.obtem_atributo(cpr_mod, 'nome_pass')
  assert nome_pass_mod == nome_pass, "Compra não atualizada"

def testa_nome_passageiro_null():
  # Valores originais
  id_cpr = 'C-00000001'
  cpr = compra.busca_por_identificador(id_cpr)
  usr = compra.obtem_cliente(cpr)
  id_usr = usuario.obtem_identificador(usr)
  status = compra.obtem_atributo(cpr, 'status')
  nome_pass_org = compra.obtem_atributo(cpr, 'nome_pass')

  # Novos valores
  args = {'id_compra': id_cpr, 'id_usr': id_usr, 'status': status}
 
  testa("NoPass", ses, args)

  # Valores atualizados
  cpr_mod = compra.busca_por_identificador('C-00000001')
  nome_pass_mod = compra.obtem_atributo(cpr_mod, 'nome_pass')
  
  assert nome_pass_mod == nome_pass_org, "Compra não atualizada"

# Executa os testes
testa_novo_passageiro()
testa_nome_passageiro_null()
