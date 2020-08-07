# Implementação do módulo {comando_excluir_poltrona}.

import poltrona
import compra
import sessao
import usuario
import html_pag_compra

def processa(ses, args):

  # Obtem o dono da sessão {ses}:
  usr_ses = None if ses == None else sessao.obtem_usuario(ses)
  assert usr_ses != None # Usuário não logado não deveria ter acesso a este comando.
  admin = False if usr_ses == None else usuario.obtem_atributo(usr_ses, 'administrador')
  carr = None if ses == None else sessao.obtem_carrinho(ses) # Carrinho de compras da sessão.

  # Obtem a poltrona a excluir:
  id_pol = args['id_poltrona']
  pol = None if id_pol == None else poltrona.busca_por_identificador(id_pol)
  assert pol != None # A poltrona deve estar identificada em {args}.
  del args['id_poltrona']
  
  # Obtem a compra de onde excluir:
  id_cpr_pol = poltrona.obtem_atributo(pol, 'id_compra')
  cpr_pol = None if id_cpr_pol == None else compra.busca_por_identificador(id_cpr_pol)
  assert cpr_pol != None # A poltrona não pode estar livre.
  
  # Obtem o dono da compra:
  usr_pol = compra.obtem_cliente(cpr_pol)
  assert usr_pol != None # Paranoia.
  
  # Verifica permissão:
  assert admin or (usr_pol == usr_ses) # Outro usuário não deveria ter acesso a este comando.

  try:
    # Ao definir {id_compra} como {None}, estamos excluindo a poltrona
    poltrona.muda_atributos(pol, {'id_compra': None})

    if (not admin) and (cpr_pol != carr):
      # Mudamos o carrinho:
      sessao.muda_atributos(ses, {'carrinho': cpr_pol})
      aviso = ("Seu carrinho agora é a compra %s" % id_cpr_pol)
    else:
      aviso = None

    # Gera a página de retorno:
    pag = html_pag_compra.gera(ses, cpr_pol, None, aviso)
  except ErroAtrib as ex:
    erros = ex[0]
    # Mostra a página da poltrona com mesmos args e erro:
    pag = html_pag_compra.gera(ses, cpr_pol, args, aviso)
  return pag
