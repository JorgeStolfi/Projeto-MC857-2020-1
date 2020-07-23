import comando_executa_checkin_IMP

def processa(ses, args):
  """
  Esta função é chamada quando o usuário aperta o botão "Fazer Check-in".

  O propósito da função é alterar o atributo 'fez_checkin' para True.
  A sessão {ses} deve pertencer a um administrador. Além disso, {args} deve ser
  um dicionário contendo 'id_poltrona'.
  """
  return comando_executa_checkin_IMP.processa(ses, args)