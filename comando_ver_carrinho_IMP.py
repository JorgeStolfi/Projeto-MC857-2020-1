import html_pag_ver_compra
import html_pag_generica
import html_resumo_de_compra
import html_pag_mensagem_de_erro
import sessao
import usuario
import compra
import poltrona

def processa(ses, args):

  # Validações, por via das dúvidas:
  assert ses != None   # Deveria acontecer.
  assert sessao.aberta(ses)  # Deveria acontecer.
  usr = sessao.obtem_usuario(ses)
  assert usr != None # Deveria acontecer.
  assert not usuario.obtem_atributo(usr, 'administrador')  # Deveria acontecer.
  cpr = sessao.obtem_carrinho(ses)
  assert cpr != None # Deveria acontecer
  
  # Monta página:
  excluir_pol = True # Mostrar botão "Excluir"
  trocar_pol = True # Mostrar botão "Trocar"
  pag = html_pag_ver_compra.gera(ses, cpr, excluir_pol, trocar_pol, None)
  return pag
