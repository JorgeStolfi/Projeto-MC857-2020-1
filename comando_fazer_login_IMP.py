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
  ses_nova = ses # Caso o login falhe.

  if ses != None:
    # Não deveria acontecer, mas por via das dúvidas:
    pag = html_pag_mensagem_de_erro.gera(ses, "Favor sair da sessão corrente primeiro")
  else:
    erro_email = None # Email não especificado ou não cadastrado.
    erro_senha = None # Senha não especificada ou inválida.

    if 'senha' not in dados:
      erro_senha = "campo 'senha' é obrigatório"
      senha = None
    else:
      senha = dados['senha'] 

    if 'email' not in dados:
      erro_email = "campo 'email' é obrigatório"
      email = None
    else:
      email = dados['email']

    usr = None
    if email != None and senha != None:
      # Obtem o usuário pelo email:
      id_usuario = usuario.busca_por_email(email)
      if id_usuario == None:
        erro_email = "Usuário " + email + " não está cadastrado"
      else:
        usr = usuario.busca_por_identificador(id_usuario)
        assert usr != None
        atrs_usr = usuario.obtem_atributos(usr)
        if atrs_usr["senha"] != senha:
          erro_senha = "Senha incorreta"
          usr = None

    if usr != None:
      cookie = secrets.token_urlsafe(32)
      carrinho = define_carrinho(usr, id_usuario)
      # !!! Deveria retornar a lista de compras em aberto, se houver mais de uma. !!!
      ses_nova = sessao.cria(usr, cookie, carrinho)
      pag = html_pag_principal.gera(ses_nova, None)
    else:
      erros = [ erro_email, erro_senha ]
      pag = html_pag_mensagem_de_erro.gera(None, erros)

  return pag, ses_nova

def define_carrinho(usr, id_usuario):
  """Esta função busca por compras em aberto do usuário {usr}. Se houver alguma nessa 
  condição, então uma delas sera usada como carrinho, caso contrário será criado
  um novo carrinho vazio."""
  lista_ids_compras = compra.busca_por_cliente(id_usuario)
  if not lista_ids_compras:
    return compra.cria(usr)
  else:
    for id_compra in lista_ids_compras:
      obj_compra = compra.busca_por_identificador(id_compra)
      if compra.obtem_status(obj_compra) == 'aberto':
        return obj_compra
  return compra.cria(usr)
