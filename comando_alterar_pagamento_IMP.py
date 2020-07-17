import sessao
import usuario
import compra

import html_pag_ver_compra
import html_pag_mensagem_de_erro


def processa(ses, args):

  
  
  # Extrair dados de {args}
  try:
    # Obter id da compra
    id_cpr = args['id_compra']
    assert id_cpr is not None, 'id_cpr obrigatório para atualizar'
    forma_pag = args['metodo']
    assert id_cpr is not None, 'id_cpr obrigatório para atualizar'
    
    


  except KeyError as ex:
    #sys.stderr.write("args = " + str(args) + "\n")
    return html_pag_mensagem_de_erro.gera(ses, ("** Erro ao extrair os dados do dicionario de argumentos. Verifique se os campos foram preenchidos**\n" + "args = " + str(args) + "\n"))


  # Editar passageiro
  try:
    cpr = compra.busca_por_identificador(id_cpr)
    novos_attr = {'forma_pag': forma_pag}
    compra.muda_atributos(cpr, novos_attr)

    # Atualiza a pagina com os novos valores
    pag = html_pag_ver_compra.gera(ses, cpr, False, False, None)

  except:
    pag = html_pag_mensagem_de_erro.gera(ses, ("** Um erro ocorreu ao alterar o passageiro **"))

  return pag
