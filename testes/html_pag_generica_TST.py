#! /usr/bin/python3

# Este programa pode ser usado para testar funções que
# retornam cadeias de caracteres que são 
# páginas completas em HTML5

# !!! Fazer este programa de teste funcionar !!!
# !!! Ele ptecisa chamar cada função da interface pelo menos uma vez, gravando arquivos ".html" separados. !!!

#Interfaces utilizados por este teste

import tabelas
import usuario
import compra
import sessao
import base_sql
import utils_testes

import sys

# Cria alguns produtos:

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

#usuario teste
usr1_id = usuario.busca_por_CPF("123.456.789-00")
#usr1 = usuario.busca_por_identificador(usr1_id)
#usr1_atrs = usuario.obtem_atributos(usr1)

#sessao de teste
ses = sessao.busca_por_identificador("S-00000001")

#carrinho de teste
#carr = sessao.obtem_carrinho(ses)
cpr_ident = "C-00000003"
cpr = compra.busca_por_identificador(cpr_ident)

#qtd teste
qtd = 2.3











