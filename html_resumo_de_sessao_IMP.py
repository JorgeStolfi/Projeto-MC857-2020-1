import sessao
import compra
import usuario
import html_span
import html_botao_simples

def gera(ses, bt_ver, bt_fechar):
  sessao_id = sessao.obtem_identificador(ses)

  # Pega/monta atributos a mostrar:
  sessao_usuario = sessao.obtem_atributo(ses, 'usr')
  sessao_aberta = sessao.obtem_atributo(ses, 'abrt')
  sessao_cookie = sessao.obtem_atributo(ses, 'cookie')
  sessao_carrinho = sessao.obtem_atributo(ses, 'carrinho')
  sessao_data = sessao.obtem_atributo(ses, 'criacao')

  # Formata informações em HTML:
  ht_sessao_id = formata_texto(sessao_id)
  ht_codigo_usuario = formata_texto(usuario.obtem_identificador(sessao_usuario))
  ht_estado = formata_texto(sessao_esta_aberta(sessao_aberta))
  ht_cookie = formata_texto(sessao_cookie)
  ht_data = formata_texto(sessao_data)
  if sessao_carrinho == None:
    tx_carrinho = ""
  else:
    tx_carrinho = compra.obtem_identificador(sessao_carrinho)
  ht_carrinho = formata_texto(tx_carrinho)

  ht_campos = [ ht_sessao_id, ht_codigo_usuario, ht_estado, ht_cookie, ht_carrinho, ht_data ]
  
  args_bt = {'id_sessao': sessao_id} # Argumentos para os botões.
  cor_bt_admin = '#FFA700' # Cor para botões de adminstrador.

  # O comando para tratar a url "ver_detalhes_sessao" ainda não existe, e deverá ser implementado
  # no futuro.
  if bt_ver:
    ht_bt_fechar = html_botao_simples.gera("Ver", 'ver_detalhes_sessao', args_bt, cor_bt_admin)
    ht_campos.append(ht_bt_fechar)

  if bt_fechar and sessao_aberta:
    ht_bt_fechar = html_botao_simples.gera("Fechar", 'fechar_sessao', args_bt, cor_bt_admin)
    ht_campos.append(ht_bt_fechar)

  return ht_campos


def sessao_esta_aberta(sessao_aberta):
  if sessao_aberta:
    return "Aberta"
  else:
    return "Fechada"


def formata_texto(txt):
  """Formata o texto {txt} com um estilo apropriado."""
  estilo = "font-weight:bold"
  return html_span.gera(estilo, txt)

