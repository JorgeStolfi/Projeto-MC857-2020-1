# Implementação do módulo {comando_encerrar_trecho}.

import html_pag_login
import html_pag_ver_trecho
import usuario
import trecho
import poltrona
import sessao
import utils_testes
from valida_campo import ErroAtrib


def msg_campo_obrigatorio(nome_do_campo):
  return "O campo %s é obrigatório." % nome_do_campo

def processa(ses, args):

  args = args.copy() # Por via das dúvidas.

  # Determina se o usuário corrente {usr_ses} é administrador:
  if ses == None:
    # Não deveria acontecer:
    utils_testes.erro_prog("usuário deveria estar logado")
  else:
    usr_ses = sessao.obtem_usuario(ses)
    assert usr_ses is not None
    admin = usuario.obtem_atributos(usr_ses)['administrador']

  id_trc = args["id_trecho"]
  assert id_trc is not None, "id_trecho obrigatório para atualizar"
  args.pop("id_trecho")

  # Pega objeto do trecho a partir do id
  trc = trecho.busca_por_identificador(id_trc)

  # Tenta encerrar o trecho:
  try:
      # Pega ids das poltronas de um trecho
      pols_ids = poltrona.busca_por_trecho(trc)

      # Para cada id de poltrona
      for pol_id in pols_ids:

          # Pega objeto da poltrona a partir do id
          pol = poltrona.busca_por_identificador(pol_id)

          # muda_atributo oferta da poltrona para false
          poltrona.muda_atributos(pol, {"oferta": False})

      # Repete a página de ver trecho com valores correntes (alterados):
      pag = html_pag_ver_trecho.gera(ses, trc, False, False, None)

  except ErroAtrib as ex:
      erros = ex.args[0]
      # Repete a página de ver trecho com os mesmos argumentos e mens de erro:
      pag = html_pag_ver_trecho.gera(ses, trc, False, False, erros)

  return pag
