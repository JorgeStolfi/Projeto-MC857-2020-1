import html_pag_compra
import html_pag_mensagem_de_erro
import sessao
import usuario

def processa(ses, args):
  
  # Validações, por via das dúvidas:
  # Falhas são erros de programação e não do usuário.
  assert ses != None   # Deveria acontecer.
  assert sessao.aberta(ses)  # Deveria acontecer.
  
  usr = sessao.obtem_usuario(ses)
  assert usr != None # Deveria acontecer.
  assert not usuario.obtem_atributo(usr, 'administrador')  # Deveria acontecer.
  
  cpr = sessao.obtem_carrinho(ses)
  assert cpr != None # Deveria acontecer

  # Monta página:
  pag = html_pag_compra.gera(ses, cpr, None, None)
  return pag
