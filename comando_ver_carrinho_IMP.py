import html_pag_ver_carrinho
import html_pag_mensagem_de_erro
import sessao
import usuario


def processa(ses, args):
  try:
    # Validações, por via das dúvidas:
    assert ses != None   # Deveria acontecer.
    assert sessao.aberta(ses)  # Deveria acontecer.
    usr = sessao.obtem_usuario(ses)
    assert usr != None # Deveria acontecer.
    assert not usuario.obtem_atributo(usr, 'administrador')  # Deveria acontecer.
    cpr = sessao.obtem_carrinho(ses)
    assert cpr != None # Deveria acontecer

    # Monta página:
    pag = html_pag_ver_carrinho.gera(ses, cpr, None)
    return pag
  except:
    pag = html_pag_mensagem_de_erro.gera(ses, "Acesso inválido ao carrinho.")
    return pag

