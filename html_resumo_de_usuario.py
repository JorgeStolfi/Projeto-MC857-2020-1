import html_resumo_de_usuario_IMP

def gera(usr):
  """Devolve um fragmento HTML que decreve o usuãrio {usr}, 
  um objeto da classe {Objeto_Usuario}.
  
  O fragmento mostra apenas nome, CPF, e email, e um botão "Ver" que
  dispara um comando HTTP "solicitar_pag_alterar_usuario"
  para mostrar os dados correntes do usuário."""
  return html_resumo_de_usuario_IMP.gera(usr)
