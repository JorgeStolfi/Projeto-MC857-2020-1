# Implementação do módulo {comando_comprar poltrona}.

import poltrona
import compra
import sessao
import usuario
import html_pag_compra
import html_pag_principal
from valida_campo import ErroAtrib

def processa(ses, args):
  
  # Obtem usuário e carrinho de compras:
  assert ses != None # Comando não deveria ser acessível a usuário não logado. 
  usr_ses = sessao.obtem_usuario(ses)
  assert usr_ses != None # Paranóia.

  admin = usuario.obtem_atributo(usr_ses, 'administrador')
  assert not admin # Admnistrador não deveria ter acesso a este cmd.
  
  #Obtem a poltrona a comprar:
  id_pol = args['id_poltrona'] if 'id_poltrona' in args else None
  assert id_pol != None #  Paranóia (formulário ou botão deve fornecer)
  pol = poltrona.busca_por_identificador(id_pol)
  assert pol != None # Paranóia.

  # Obtém carrinho do usuário:
  carr = sessao.obtem_carrinho(ses)
  assert carr != None # Todo cliente comum deve ter carrinho.
  id_carr = compra.obtem_identificador(carr)

  try:
    if not poltrona.pode_comprar(usr, pol, carr):
      # Não deveria acontecer, mas em todo caso:
      raise ErroAtrib("Esta poltrona não está disponível") 
    
    # Muda a poltrona para comprada
    poltrona.muda_atributos(pol, { 'id_compra': id_carr })

    # Mostra o carrinho do usuário com a poltrona comprada:
    pag = html_pag_compra.gera(ses, cpr, excluir, None)
  except ErroAtrib as ex:
    erros = ex.args[0]
    # Se o trecho da poltrona estiver disponível, mostra o trecho para outra compra:
    id_trc = poltrona.obtem_atributo(pol, 'id_trecho')
    assert id_trc != None # Paranoia.
    trc = trecho.busca_por_identificador(id_trc)
    assert trc != None # Paranoia.
    if trecho.verificar_disponibilidade(trc) and trecho_eh_compativel(cpr, trc):
      # Usuário pode comprar outra poltrona deste trecho:
      pag = html_pag_trecho.gera(ses, trc, None, erros)
    else:
      # Usuário não pode comprar nenuma poltrona neste trecho.
      # Volte para a página principal.
      # !!! Deveria buscar e mostrar roteiros de mesma origem e destino !!!
      pag = html_pag_principal.gera(ses, erros)
  return pag
