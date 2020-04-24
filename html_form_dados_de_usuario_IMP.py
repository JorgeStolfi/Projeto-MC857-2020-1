import html_input
import html_botao_submit
import html_botao_simples

def gera(id_usuario, atrs, admin, texto_bt, cmd):
  if id_usuario != None:
    novo = False
    # Inclui campo 'id_usuario' no formulário:
    if admin != None:
      # Mostra o id do usuario somente se quem está alterando é administrador:
      html_id_usuario = html_input.gera(None, "readonly", "id_usuario", id_usuario, None, None)
    else:
      html_id_usuario = html_input.gera(None, "hidden", "id_usuario", id_usuario, None, None)
  else:
    novo = True
    html_id_usuario = ""

  # For simplicity:
  if atrs == None: atrs = {}.copy()

  # Dados brutos para as linhas. Para cada linha, o rótulo, tipo do "<input>", nome do campo, e dica.
  dados_linhas = (
    ( "Nome",             "text",     "nome",          None,                  False, ),
    ( "E-mail",           "email",    "email",         "xxx@xxx.xxx.xx",      False, ),
    ( "CPF",              "text",     "CPF",           "xxx.xxx.xxx-xx",      False, ),
    ( "Telefone",         "text",     "telefone",      "+xx(xx)x-xxxx-xxxx",  False, ),
    ( "Documento",        "text",     "documento",     "Número, tipo, órgão", False, ),
    ( "Senha",            "password", "senha",         None,                  False, ),
    ( "Confirmar senha",  "password", "conf_senha",    None,                  False, ),
    ( "Administrador",    "checkbox", "administrador", None,                  False, ),
  )

  html_tabela = tabela_de_campos(dados_linhas, atrs, admin)

  html_submit = html_botao_submit.gera(texto_bt, cmd, None, '#55ee55')

  html_cancel = html_botao_simples.gera("Cancelar", 'principal', None, '#ee5555')

  html_campos = \
    ( "    " + html_id_usuario + "\n" if html_id_usuario != "" else "") + \
    ( html_tabela + "\n" ) + \
    ( "    " + html_submit + "\n" ) + \
    ( "    " + html_cancel + "\n" )
  return monta_formulario(html_campos)

# FUNÇÕES INTERNAS:

def tabela_de_campos(dados_linhas, atrs, admin):
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

  sys.stderr.write("TABELA: atrs = %s\n" %str(atrs))

  # Converte os dados brutos das linhas para fragmentos HTML:
  linhas = [].copy()
  for rot, tipo, chave, dica, adm_only in dados_linhas:
    if admin or not adm_only:
      # Valor corrente do atributo:
      val = (atrs[chave] if chave in atrs else None)
      # Converte {rot} para rótulo HTML:
      html_rotulo = html_label.gera(rot, ": ")
      # Cria o elemento "<input .../>":
      html_campo = campo_editavel(tipo, chave, val, dica)
      if html_campo != None:
        linhas.append((html_rotulo, html_campo,))

  # Monta a tabela com os fragmentos HTML:
  html_tabela = html_tabela.gera(linhas)

  return html_tabela

def campo_editavel(tipo, chave, val, dica):
  """Retorna o HTML de um item "input" do formulário
  de dados de usuário. Pode devolver {None} para não mostrar esse item.

  O elemento terá o dado {tipo} ("text", "password", etc.), nome {chave},
  valor inicial {val}, e a {dica} especificada (se {val} for {None}).
  O valor inicial {val} é convertido para string de maneira adequada
  ao seu tipo.

  Se a chave for 'senha', não mostra o {val}"""

  if chave == 'senha': val = None

  # Converte val para HTML:
  if val == None:
    html_valor = None
  elif type(val) is str:
    html_valor = val
  elif type(val) is bool:
    html_valor = ('on' if val else 'off')
  elif type(val) is float:
    html_valor = ("%.2f" % val)
  elif type(val) is int:
    html_valor = ("%d" % val)
  else:
    erro_prog("valor inválido = \"" + str(val) + "\"")

  # Dica e valor inicial são mutuamente exclusivos:
  if html_valor == None:
    html_dica = dica
  else:
    html_dica = None

  html_campo = html_input.gera(None, tipo, chave, html_valor, html_dica, None)
  return html_campo

def monta_formulario(conteudo):
  """Dado um trecho de HTML {conteudo} que define os campos "<input ...>" necessários, envolve o mesmo
  em "<form>...</form>", com rótulos etc num estilo padrão."""
  fam_fonte = "Courier"
  peso_fonte = None
  tam_fonte = "18px"
  estilo = \
    "  display: inline-block;" + \
    "  font-family: " + fam_fonte + ";" + \
    "  font-size: " + tam_fonte + ";" + \
    "  padding: 5px;"
  html_cru = html_form.gera(None, conteudo)
  html = html_span.gera(estilo, html_cru)
  return html
