import sessao
import compra
import usuario
import html_span

def gera(ses):
  sessao_id = sessao.obtem_identificador(ses)

  # Pega/monta atributos a mostrar:
  sessao_usuario = sessao.obtem_atributo(ses, 'usr')
  sessao_estado = sessao.obtem_atributo(ses, 'abrt')
  sessao_cookie = sessao.obtem_atributo(ses, 'cookie')
  sessao_carrinho = sessao.obtem_atributo(ses, 'carrinho')


  # Formata informações em HTML:
  ht_sessao_id = formata_texto(sessao_id)
  ht_codigo_usuario = formata_texto(usuario.obtem_identificador(sessao_usuario))
  ht_estado = formata_texto(sessao_estado)
  ht_cookie = formata_texto(sessao_cookie)
  ht_carrinho = formata_texto(compra.obtem_identificador(sessao_carrinho))

  ht_campos = [ ht_sessao_id, ht_codigo_usuario, ht_estado, ht_cookie, ht_carrinho ]
  
  # args_bt = {'id_trecho': id_trc} # Argumentos para os botões.
  # cor_bt_normal = '#00FF00' # Cor para botões de uso geral.
  # cor_bt_admin = '#FFA700' # Cor para botões de adminstrador.
  
  # if bt_ver:
  #   ht_bt_ver = html_botao_simples.gera("Ver", 'ver_trecho', args_bt, cor_bt_normal)
  #   ht_campos.append(ht_bt_ver)
  #
  # if bt_alterar:
  #   ht_bt_alterar = html_botao_simples.gera("Alterar", 'solicitar_pag_alterar_trecho', args_bt, cor_bt_admin)
  #   ht_campos.append(ht_bt_alterar)
  #
  # if bt_clonar:
  #   ht_bt_clonar = html_botao_simples.gera("Clonar", 'solicitar_pag_clonar_trecho', args_bt, cor_bt_admin)
  #   ht_campos.append(ht_bt_clonar)
  #
  # if bt_fechar:
  #   ht_bt_fechar = html_botao_simples.gera("Encerrar", "encerrar_trecho", args_bt, cor_bt_admin)
  #   ht_campos.append(ht_bt_fechar)

  return ht_campos

def formata_texto(txt):
  """Formata o texto {txt} com um estilo apropriado."""
  estilo = "font-weight:bold"
  return html_span.gera(estilo, txt)

