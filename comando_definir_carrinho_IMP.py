# Implementação do módulo {comando_definir_carrinho}.
import comando_ver_carrinho
import compra
import trecho
import sessao
import html_lista_de_trechos
import html_pag_generica
import html_pag_buscar_trechos
import sys

from valida_campo import ErroAtrib

def processa(ses, args):
  # Validações, por via das dúvidas:
  assert ses != None   # Deveria acontecer.
  assert sessao.aberta(ses)  # Deveria acontecer.
  assert 'id_compra' in args # Deveria acontecer

  # obter compra
  id_compra = args['id_compra']
  cpr = compra.busca_por_identificador(id_compra)

  if cpr == None:
    erros = ["compra \"" + id_compra + "\" não existe"]
    return html_pag_mensagem_de_erro(ses, erros)

  # trocar o carrinho pela compra
  attrs = {
    'carrinho': cpr
  }
  sessao.muda_atributos(ses, attrs)

  # mostrar carrinho atualizado
  return comando_ver_carrinho.processa(ses, args)
