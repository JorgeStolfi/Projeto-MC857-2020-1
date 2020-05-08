import sys
import html_label
import html_input

def gera(dados_linhas, atrs, admin):
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
