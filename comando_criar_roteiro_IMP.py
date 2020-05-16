# Implementação do comando criar roteiro
import trecho
import html_pag_ver_trecho

def processa(ses, args):

    #recebo args com origem e destino
    origem = args['origem']
    destino = args['destino']

    #Verificar se recebemos origem e destino não vazio
    if origem != " " and destino != " "
        #ALGORITIMO DE BUSCA DE ROTEIROS NO DB - A SER IMPLEMENTADO
        #Assumindo que recebemos um lista de roteiros desta busca
        roteiros = trecho.busca_por_trecho(origem, destino)

        #chamo modulo que chama html com a lista de roteiros
        pag = html_pag_ver_trecho.gera(ses, roteiros)
    else:
        #gerar msg de erro de dados invalidos
