import html_form_tabela_de_campos_IMP

def gera(dados_linhas, atrs, admin):
  """Retorna HTML de uma tabela com duas colunas: rótulos "<label>...<label/> e campos
  editáveis <input.../>".  Os valores iniciais dos campos são obtidos do
  dicionário {atrs}.  O parâmetro booleano {admin} diz se o usuário
  que pediu o formulário é administrador ({True}) ou cliente ({False}).

  O parâmetro {dados_linhas} é uma seqüência de quíntuplas
  {(rot,tipo,chave,dica,adm_only)}, uma para cada linha da tabela.

  O elemento {rot} é o texto a mostrar no rótulo, ou {None} para omitir o rótulo.
  O elemento {adm_only} é um booleano que diz se o campo só deve ser editável
  para administradores. Se for {True}, o campo será "readonly" para usuários normais.

  O campo editável será
  "<input type='{tipo}' name='{chave}' id='{chave}' value='{val}' placeholder='{dica}'/>"
  onde {val} é o valor {args[chave]} apropriadamente convertido para HTML.
  Se o {tipo} for "numeric" também tem "min='1'."""
  return html_form_tabela_de_campos_IMP.gera(dados_linhas, atrs, admin)
