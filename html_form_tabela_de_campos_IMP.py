import html_label
import html_input
import html_tabela
from utils_testes import erro_prog
import sys

def gera(dados_linhas, atrs, admin):
  sys.stderr.write("TABELA: atrs = %s\n" %str(atrs))

  # Converte os dados brutos das linhas para fragmentos HTML:
  linhas = [].copy()
  for rot, tipo, chave, dica, adm_only in dados_linhas:
    sys.stderr.write("admin: "+str(admin)+"\n")
    sys.stderr.write("Adm_only: "+str(adm_only)+"\n")
    if admin or not adm_only:
      # Valor corrente do atributo:
      val = (atrs[chave] if chave in atrs else None)
      # Converte {rot} para rótulo HTML:
      ht_rotulo = html_label.gera(rot, ": ")
      # Cria o elemento "<input .../>":
      ht_campo = campo_editavel(tipo, chave, val, dica)
      if ht_campo != None:
        linhas.append((ht_rotulo, ht_campo,))

  # Monta a tabela com os fragmentos HTML:
  ht_tabela = html_tabela.gera(linhas)

  return ht_tabela

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
    ht_valor = None
  elif type(val) is str:
    ht_valor = val
  elif type(val) is bool:
    ht_valor = ('on' if val else 'off')
  elif type(val) is float:
    ht_valor = ("%.2f" % val)
  elif type(val) is int:
    ht_valor = ("%d" % val)
  else:
    erro_prog("valor inválido = \"" + str(val) + "\"")

  # Dica e valor inicial são mutuamente exclusivos:
  if ht_valor == None:
    ht_dica = dica
  else:
    ht_dica = None

  ht_campo = html_input.gera(None, tipo, chave, ht_valor, True, ht_dica, None)
  return ht_campo
