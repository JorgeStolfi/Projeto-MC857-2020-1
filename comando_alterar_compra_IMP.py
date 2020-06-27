import sessao
import usuario
import compra

import html_pag_ver_compra
import html_pag_mensagem_de_erro


def processa(ses, args):

  # Determina se usuario é administrador
  assert sessao.eh_administrador(ses)

  # Extrair dados de {args}
  try:
    # Obter id da compra
    id_cpr = args['id_cpr']
    assert id_cpr is not None, 'id_cpr obrigatório para atualizar'

    # Obter id do usuario
    id_usr = args['id_usr']
    assert id_usr is not None, 'id_usr obrigatório para atualizar'

    # Novo passageiro
    nome_pass = args['nome_pass']
    assert nome_pass is not None, 'nome_pass obrigatório para atualizar'

    # Status
    status = args['status']
    assert status is not None, 'status obrigatório para atualizar'

  except KeyError as ex:
    return html_pag_mensagem_de_erro.gera(ses, ("** Erro ao extrair os dados do dicionario de argumentos. Verifique se os campos foram preenchidos**"))

  # Editar passageiro
  try:
    usr = usuario.busca_por_identificador(id_usr)
    cpr = compra.busca_por_identificador(id_cpr)
    novos_attr = {'cliente':usr, 'status':status, 'nome_pass':nome_pass}
    compra.muda_atributos(cpr, novos_attr)

    # Atualiza a pagina com os novos valores
    pag = html_pag_ver_compra.gera(ses, cpr, False, False, None)

  except:
    pag = html_pag_mensagem_de_erro.gera(ses, ("** Um erro ocorreu ao alterar o passageiro **"))

  return pag
