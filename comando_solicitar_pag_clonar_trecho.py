import comando_solicitar_pag_clonar_trecho_IMP

def processa(ses, args):
  """Esta função é chamada quando o administrador aperta o botão "Clonar" 
  em uma linha ou página associada a um trecho existente {trc}.  
  O dicionário {args} deve conter um campo 'id_trecho' com 
  o identificador desse trecho.  
  
  A função retorna uma página para a criação de um novo trecho, com cada
  atributo inicializado com os atributos correntes do trecho {trc}."""
  return comando_solicitar_pag_clonar_trecho_IMP.processa(ses, args)
