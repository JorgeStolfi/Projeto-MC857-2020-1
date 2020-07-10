#! /usr/bin/python3

import tabelas
import comando_buscar_usuarios
import sessao
import base_sql
import utils_testes
import usuario

import sys

# Conecta no banco e carrega alimenta com as informações para o teste

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB", None, None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

# Sessão em que o usuário dela é o administrador. Apenas o administrador pode executar este comando de busca.
ses_adm = sessao.busca_por_identificador("S-00000004")

# Usuário válido - temos a garantia que este usuário está na nossa base de dados e que {usr_atrs} possui os atributos
# {'email'} e {'CPF'} definidos. Logo, esperamos que o comando de busca de usuário funcione e retorne uma página com
# as informações do usuário pesquisado.
usr_adm = sessao.obtem_usuario(ses_adm)
usr_adm_atrs = usuario.obtem_atributos(usr_adm)

# Vamos testar agora com uma lista de atributos de usuário que não contém nem o email nem o CPF.
# Neste caso, precisamos voltar à pagina de buscar usuários com uma mensagem de erro.
atrs_incompletos = {'nome': "João sem CPF"}

# Podemos pesquisar um usuário com um CPF inexistente. Neste caso, deveríamos obter uma mensagem de
# erro na página de buscar usuários constatando que não existe um usuário com os dados informados.
atrs_cpf_inexistente = {'CPF': "000.000.000-00"}

# Analogamente, podemos pesquisar um usuário com um email inexistente. Devemos obter uma mensagem de
# erro igual o teste anterior.
atrs_email_inexistente = {'email': "naoexiste@email.com"}

# Por fim, vamos fazer o teste do caso de uma sessão em que o usuário dela NÃO é o administrador. Neste caso,
# uma mensagem de erro deve ser levantada e o comando não deve ser executado.
ses_nao_eh_adm = sessao.busca_por_identificador("S-00000001")

def testa(rotulo, *args):
    """Testa {funcao(*args)}, grava resultado
    em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

    modulo = comando_buscar_usuarios
    funcao = modulo.processa
    frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
    pretty = False  # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
    utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

testa("valido",        ses_adm, usr_adm_atrs)
testa("email-F-CPF-F", ses_adm, atrs_incompletos)
testa("CPF-ruim",      ses_adm, atrs_cpf_inexistente)
testa("email-ruim",    ses_adm, atrs_email_inexistente)
testa("admin-F",       ses_nao_eh_adm, usr_adm_atrs)


