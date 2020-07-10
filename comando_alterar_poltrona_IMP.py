import sessao
import usuario
import poltrona

import html_pag_ver_poltrona
import html_pag_mensagem_de_erro

def processa(ses, args):

  # Determina se usuario é administrador
  assert sessao.eh_administrador(ses)

  # Extrair dados de {args}
  try:
    # Obter id da poltrona
    id_poltrona = args['id_poltrona']
    assert id_poltrona is not None, 'id_poltrona obrigatório para atualizar'

    id_trecho = args['id_trecho']
    assert id_trecho is not None, 'id_trecho obrigatório para atualizar'

    id_compra = args['id_compra']
    assert id_compra is not None, 'id_compra obrigatório para atualizar'

    numero = args['numero']
    assert numero is not None, 'numero obrigatório para atualizar'

    oferta = args['oferta']
    assert oferta is not None, 'oferta obrigatório para atualizar'

    preco = args['preco']
    assert preco is not None, 'preco obrigatório para atualizar'


  except KeyError as ex:
    return html_pag_mensagem_de_erro.gera(ses, ("** Erro ao extrair os dados do dicionario de argumentos. Verifique se os campos foram preenchidos**"))

  # Editar poltrona
  try:
    pol = poltrona.busca_por_identificador(id_poltrona)
    mods = { 
      'id_trecho': id_trecho,
      'numero': numero,
      'oferta': oferta == 'on',
      'preco': float(preco)
    }
    poltrona.muda_atributos(pol, mods)
    pag = html_pag_ver_poltrona.gera(ses, pol, None, False, None)

  except:
    pag = html_pag_mensagem_de_erro.gera(ses, ("** Um erro ocorreu ao alterar a poltrona **"))
  
  return pag
