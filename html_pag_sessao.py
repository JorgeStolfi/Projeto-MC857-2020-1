import html_pag_sessao_IMP

def gera(ses, ses_ver, erros):
  """Retorna uma página HTML que mostra os dados da sessão {ses_ver}
  (que deve ser um objeto de tipo {Objeto_Sessao}), para visualização ou
  alteração.
  
  O parâmetro {ses} é a sessão que pediu esta página, e não pode ser
  {None}. O parâmetro {erros} é uma lista de mensagens de erro a mostrar
  no alto da página. Pode ser {None}.
  
  A página terá um <form>...</form> com campos <input> para os atributos
  da compra, Vide detalhes em {html_form_dados_de_compra.gera}.
  
  Entende-se que a sessão {ses_ver} está sendo visualizada e
  possivelmente alterada.  Neste caso, a sessão deve pertencer a um
  administrador ou ao cliente que é dono da sessao {ses_ver}. O
  formulário incluirá um campo visível 'id_sessao' com o ID de
  {ses_ver}, como "readonly". No futuro, pode haver campos editáveis;
  mas por enquanto todos são "readonly". Se a sessão estiver aberta,
  haverá um botão "Fechar" para fechá-la. (Esta é a única
  alteração possível por enquanto.)"""
  return html_pag_sessao_IMP.gera(ses, ses_ver, erros)
