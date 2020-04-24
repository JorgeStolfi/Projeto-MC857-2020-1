import html_form_entrar_IMP

def gera():
  """Retorna o HTML do formulário para login do usuário.
  O formulário contém campos editáveis onde o usuário deverá digitar
  o email e a senha, e um botão 'Entrar' (de tipo 'submit').

  Quando o usuário clicar no botão 'Entrar', será emitido um comando POST
  com ação {fazer_login}.  Os argumentos desse
  POST são { 'email': {email}, 'senha': {senha} }."""
  return html_form_entrar_IMP.gera()
