# Implementação do módulo {utils_testes}.

import sys
import re
import inspect
import json
from bs4 import BeautifulSoup as bsoup  # Pretty-print of HTML

def erro_prog(mens):
  fr = inspect.stack()[2]
  sys.stderr.write("  File %s, line %d, in %s: ** erro: %s\n" % (fr[1],fr[2],fr[3],mens))
  assert False

def aviso_prog(mens, grave):
  fr = inspect.stack()[2]
  tipo = ("** erro" if grave else "!! aviso")
  sys.stderr.write("  File %s, line %d, in %s: %s %s\n" % (fr[1],fr[2],fr[3],tipo,mens))
  return

def mostra(ind,mens):
  sys.stderr.write("%*s%s\n" % (ind,'',mens))

def testa_modulo_html(modulo, rotulo, res, frag, pretty):
  prefixo = "testes/saida/"
  nome_mod = modulo.__name__
  nome_arq = nome_mod + "." + rotulo
  f = open(prefixo + nome_arq + '.html', 'w')
  # sys.stderr.buffer.write((str(*args) + "\n").encode('utf-8'))
  cabe = \
    "<!DOCTYPE HTML>\n" + \
    "<html>\n" + \
    "<head>\n" + \
    "<meta charset=\"UTF-8\"/>\n" + \
    "</head>\n" + \
    "<body style=\"background-color:#eeeeee; text-indent: 0px\">\n"
  roda = \
    "</body>\n" + \
    "</html>\n"  
  if frag:
    pag = cabe + res + roda
  else:
    pag = res
  if pretty:
    pag = bsoup(pag + "\n", "html.parser").prettify()
  f.buffer.write(str(pag).encode('utf-8'))
  f.close()

def testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args):
  nome_fn = funcao.__name__
  func_rot = nome_fn + "." + rotulo
  try:
    res = funcao(*args)
    testa_modulo_html(modulo, func_rot, res, frag, pretty)
  except Exception as ex:
    fr = inspect.stack()[2]
    msg = ("File %s, line %d, in %s\n" % (fr[1], fr[2], str(fr[3])))
    msg += ("** erro em testa(%s): %s\n" % (func_rot, str(ex)))
    sys.stderr.write(msg + "\n")
    res = str(msg)
    testa_modulo_html(modulo, func_rot, res, True, pretty)
    raise

def formata_dict(dados):
  """Esta função de depuração recebe um dicionário {dados}
  e devolve um string é um fragmento HTML5 que mostra esses
  dados em formato relativamente legível (JSON com quebras de
  linha e indentação)."""
  dados_lin = json.dumps(dados, indent='&nbsp;&nbsp;', sort_keys=True, separators=(',<br/>', ': '))
  dados_lin = re.sub(r'\[', '[<br/>', dados_lin)
  dados_lin = re.sub(r'\{', '{<br/>', dados_lin)
  dados_lin = re.sub(r'\},', '  \},', dados_lin)
  return dados_lin
