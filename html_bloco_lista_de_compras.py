
import html_bloco_lista_de_compras_IMP

def gera(ses, args):
  """Retorna um trecho de HTML que descreve as compras do usuario logado na sessao.

  O parametro {args} contem os argumentos da sessao e eh de onde o modulo tira o id do usuario para fazer a busca das compras associadas.

  O modulo devolve uma pagina HTML generica cujo conteudo eh uma tabela em que cada linha corresponde ao bloco HTML retornado pela funcao {html_bloco_resumo_de_compra.gera({cpr})} onde {cpr} eh um objeto que representa uma compra do usuario"""
  return html_bloco_lista_de_compras_IMP.gera(ses, args)
