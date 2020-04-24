# Imlementação do módulo {valida_campo}

import sys, re
import valida_campo

def nome_de_usuario(rotulo, val, nulo_ok):
  if val == None and not nulo_ok: return [ "campo '%s' não pode ser omitido" % rotulo, ]
  erros = []
  if type(val) is not str:
    erros += [ "campo '%s' deve ser string" % rotulo ]
  else:
    n = len(val)
    if n < 6:
      erros += [ "campo '%s' (%d caracteres) muito curto" % (rotulo,n), ]
    elif n > 60:
      erros += [ "nome de usuário (%d caracteres) muito longo" % (rotulo,n), ]
    # !!! Verificar caracteres permitidos !!!
  return erros

def CPF(rotulo, val, nulo_ok):
  if val == None and not nulo_ok: return [ "campo '%s' não pode ser omitido" % rotulo, ]
  erros = []
  if type(val) is not str:
    erros += [ "campo '%s' deve ser string" % rotulo ]
  elif not re.match(r'^[0-9]{3}[.][0-9]{3}[.][0-9]{3}[-][0-9]{2}$', val):
    erros += [ "campo '%s' tem formato inválido, deveria ser 'xxx.xxx.xxx-xx'" % rotulo ]
  # !!! Verificar dígitos de controle !!!
  return erros
  
# def linha_de_endereco(rotulo, val, nulo_ok):
#   if val == None and not nulo_ok: return [ "campo '%s' não pode ser omitido" % rotulo, ]
#   erros = []
#   if type(val) is not str:
#     erros += [ "campo '%s' deve ser string" % rotulo ]
#   else:
#     n = len(val)
#     if n < 2:
#       erros += [ "campo '%s' (%d caracteres) muito curto" % (rotulo,n), ]
#     elif n > 60:
#       erros += [ "nome de usuário (%d caracteres) muito longo" % (rotulo,n), ]
#     # !!! Verificar caracteres permitidos !!!
#   return erros

def cidade_UF(rotulo, val, nulo_ok):
  # !!! Implementar !!!
  return []
  
def senha(rotulo, val, nulo_ok):
  # !!! Implementar !!!
  return []

def email(rotulo, val, nulo_ok):
  # !!! Implementar !!!
  return []

# def endereco(rotulo, val, nulo_ok):
#   # !!! Implementar !!!
#   return []

def CEP(rotulo, val, nulo_ok):
  # !!! Implementar !!!
  return []

def telefone(rotulo, val, nulo_ok):
  # !!! Implementar !!!
  return []

def documento(rotulo, val, nulo_ok):
  # !!! Implementar !!!
  return []

def administrador(rotulo, val, nulo_ok):
  # !!! Implementar !!!
  return []
