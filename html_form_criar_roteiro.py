import html_form_criar_roteiro_IMP

def gera():
  """Retorna o HTML do formulário para busca de roteiro.
  O formulário contém campos editáveis onde o usuário deverá digitar
  a origem e o destino da viagem, e um botão 'Buscar' (de tipo 'submit').

  Quando o usuário clicar no botão 'Buscar', será emitido um comando POST
  com ação {comando_criar_roteiro}.  Os argumentos desse
  POST são { 'origem': {origem}, 'destino': {destino} }."""
  return html_form_criar_roteiro_IMP.gera()
