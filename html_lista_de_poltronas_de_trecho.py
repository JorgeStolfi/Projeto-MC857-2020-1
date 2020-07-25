
import html_lista_de_poltronas_de_trecho_IMP

def gera(ids_poltronas, id_trc, alterar_pols, comprar_pols, ver_oferta_pols,
         ver_fez_checkin, checkin_pols, id_cpr):
  """Retorna um trecho de HTML que descreve as poltronas cujos identificadores
  estão na lista {ids_poltronas}.  Todas as poltronas devem pertencer ao 
  trecho cujo identficador é {id_trc}, que supõe-se ter sido
  identificado separadamente.
  
  O resultado é um elemento "<table>...</table>". Cada
  linha é gerada por {html_resumo_de_poltrona_de_trecho.gera}
  com argumentos {(pol, id_trc, alterar_pols, comprar_pol, trocar_pol, id_cpr)}, e 
  tem os número da poltrona, o preço, o pedido de compra
  que atualmente inclui a poltrona, indicação de oferta, 
  além dos botões solicitados por {alterar_pols} e {comprar_pols}.
  
  Especificamente, se {comprar_pols} for {True} e uma das poltronas já estiver
  reservada para essa compra, essa poltrona apenas terá um botão "Trocar"
  que gera o comando "trocar_postrona" com o argumento 'id_poltrona'.
  Se {comprar_pols} for {True} mas nenhuma das poltronas estiver reservada
  para essa compra, todas as poltronas livres terão um botão "Comprar"."""
  return html_lista_de_poltronas_de_trecho_IMP.gera \
    (ids_poltronas, id_trc, alterar_pols, comprar_pols, ver_oferta_pols,
      ver_fez_checkin, checkin_pols, id_cpr)
