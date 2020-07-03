# Implementação do módulo {comando_ver_poltrona}
import poltrona
import html_pag_ver_poltrona
import html_pag_mensagem_de_erro

from valida_campo import ErroAtrib

def processa(ses, args):
    try:
        if ses is None:
          raise ErroAtrib("É necessário uma sessão para ver esta pagina. Autentique-se novamente")

        id_poltrona = args['id_poltrona']
        pol = poltrona.busca_por_identificador(id_poltrona)

        if pol is None:
          raise ErroAtrib("Não foi encontrada uma poltrona com esse identificador")

        pag = html_pag_ver_poltrona.gera(ses, pol, None, False, None)

        return pag

    except ErroAtrib as ex:
      erros = ex.args[0]
      # Repete a página com mensagem de erro:
      pag = html_pag_mensagem_de_erro.gera(ses, erros)
      return pag




