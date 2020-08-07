import html_form_table_IMP

def gera(dados_linhas, atrs):
  """Retorna HTML de um elemento <table>...</table> com duas colunas:
  rótulos (<label>...<label/>) e campos (<input.../> ou
  <textarea>...</textarea>). 
  
  O parâmetro {dados_linhas} deve ser uma lista de tuplas.
  Cada tupla especifica uma linha da tabela (um campo do formulário).
  
  Os valores iniciais dos campos são obtidos do dicionário {atrs}. Eles
  serão convertidos para um formato adequado para inclusão no HTML.  Em 
  particular, valores de tipo {bool} são convertidos para "on" ou "off", e
  valores {float} são formatados com 2 casas decimais.
  
  Cada elemento de {dados_linhas} é uma sextupla
  
    {(rotulo,tipo,chave,dica,visivel,editavel,obrigatorio)}
  
  onde:
  
    {rotulo} é um string que será usado como rótulo visível do campo; por
    exemplo, "Nome do passageiro".  Se for {None}, o rótulo será
    omitido.
    
    {tipo} é o tipo de elemento.  Pode ser um dos valores do atributo "type" do
    <input> ("text", "email", "password", "date", "number", etc.) segundo 
    o padrão HTML.  O tipo também pode ser "textarea", e nesse caso o elemento será um
    <textarea>...</textarea> em vez de <input>.
    
    {chave} é a chave do valor correspondente no dicionário {atrs}, e também
    será o nome do campo quando o mesmo for enviado ao servidor pelo botão
    de submit.  Por exemplo, 'id_compra' ou 'senha'.
    
    {dica} é um texto de exemplo ("placeholder") que será mostrado quando o
    campo não estiver preenchido, para orientar o usuário sobre a natureza 
    e o formato do dado.  Por exemplo, "HH:MM" ou "+XX(XX)XXXX-XXXX".
    
    {visivel} é um booleano que diz se o campo será visível na página
    gerada. Se for {False}, o campo será excluido da <table> mas
    incluido imediatamente após o </table>, como um <input> de tipo
    "hidden". O valor correspondente será enviado ao servidor quando o
    <form> for submetido.
    
    {editavel} é um booleano que diz se o campo é editável pelo usuário.
    Se for false, o campo será "readonly". Este parãmetro é ignorado
    se {visivel} é {False}
    
    {obrigatorio} é um booleano que diz se o campo é obtigatório.  Afeta a 
    apresentação do campo. Este parãmetro é ignorado
    se {visivel} e/ou {editavel} são {False}
    
  Se o {tipo} for "number", e {atrs} tiver uma chave '{chave}_min',
  o <input> terá também o atributo "min='{vmin}'" onde {vmin} é o valor
  associado a essa chave.
  
  NOTE: o resultado devolvido NÃO é um <form>...</form> mas apenas 
  o conteúdo parcial do mesmo.  Pelo menos um botão de tipo <submit>
  deve ser concatenado, antes ou depois desta tabela, e então tudo
  deve ser incluido em um <form>...</form> para
  ter efeito. Veja {html_form.gera}.

  """
  return html_form_table_IMP.gera(dados_linhas, atrs)
