# Implementação do módulo {comando_fazer_login}.

# Interfaces do projeto usadas por esta implementação:
import usuario
import sessao
import compra
import html_pag_mensagem_de_erro
import html_pag_principal

# Outros módulos usados por esta implementação:
import secrets

def processa(ses, dados):
  if ses != None:
    # Não deveria acontecer, mas por via das dúvidas:
    return html_pag_mensagem_de_erro.gera(ses, "Favor sair da sessão corrente primeiro")
    
  email = dados['email']
  senha = dados['senha'] 
  id_usuario = usuario.busca_por_email(email)
  
  ses_nova = ses # Caso o login falhe.
  if id_usuario != None:
    usr = usuario.busca_por_identificador(id_usuario)
    atrs_usr = usuario.obtem_atributos(usr)
    if atrs_usr["senha"] == senha:
      cookie = secrets.token_urlsafe(32)
      carrinho = define_carrinho(usr, id_usuario)
      # !!! Deveria retornar a lista de compras em aberto, se houver mais de uma. !!!
      ses_nova = sessao.cria(usr, cookie, carrinho)
      pag = html_pag_principal.gera(ses_nova, None)
    else:
      pag = html_pag_mensagem_de_erro.gera(None, "Senha incorreta")
  else:
    pag = html_pag_mensagem_de_erro.gera(None, "Usuário " + email + " não está cadastrado")
  return pag, ses_nova

def define_carrinho(usr, id_usuario):
  """Esta funcao busca por compras em aberto do usuário {usr}. Se houver alguma nessa 
  condicao, entao uma delas sera usada como carrinho, caso contrario, será criado
  um novo carrinho vazio."""
  # !!! Deveria retornar a lista de todas as compras em aberto, não apenas a primeira encontrada. !!!
  lista_id_compras = compra.busca_por_usuario(id_usuario)
  if not lista_id_compras:
    return compra.cria(usr)
  else:
    for id_compra in lista_id_compras:
      obj_compra = compra.busca_por_identificador(id_compra)
      if compra.obtem_status(obj_compra) == 'aberto':
        return obj_compra
  return compra.cria(usr)
