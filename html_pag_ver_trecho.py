import html_pag_ver_trecho_IMP

def gera(ses, trc, comprar_pols, alterar_trc, erros):
  """Retorna uma página HTML que mostra os dados do trecho {trc}
  (que deve ser um objeto de tipo {Objeto_Trecho}).

  A página terá um cabeçalho com resumo das informações do trecho
  (vide {html_resumo_de_trecho.gera}), em seguida uma lista das poltronas
  do trecho.

  O parâmetro {comprar_pols} indica que o dono da sessão {ses} pode
  comprar assentos neste trecho. (Só deveria ser {True} se a sessão
  {ses} estiver aberta e o dono NÃO for administrador.) Se for {True},
  cada poltrona livre terá um botão "Comprar" que, quando clicado,
  emitirá o comando "solicitar_pag_comprar_bilhete" com o identificador
  da potrona como argumento 'id_poltrona' e o identificador do carrinho
  da sessão como argumento 'id_compra'.
  
  Porém, se {comprar_pols} for {True} mas uma das poltronas já estiver
  reservada para essa compra, as poltronas livres ficarão
  sem botão "Comprar", e essa poltrona apenas terá um botão "Trocar"
  que gera o comando "trocar_postrona" com o argumento 'id_poltrona'.

  O parâmetro {alterar_trc} indica que o dono da sessão {ses} pode
  modificar atributos do trecho. (Só deveria ser {True} se a sessão
  {ses} estiver aberta e o dono FOR administrador.) Se for {True}, cada
  poltrona terá um boão "Alterar" que, quando clicado, emitirá o comando
  "solicitar_pag_alterar_potrona" com o identificador da poltrona no
  argumento 'id_poltrona'.
  
  Se {alterar_trc} for {True}, haverá também na página um botão
  "Alterar" na página, que emitirá o comando
  "solicitar_pag_alterar_trecho"; um botão "Clonar" que emite o comando
  "solicitar_pag_clonar_trecho"; e um botão "Encerrar" que emite o
  comando "encerrar_trecho". Estes comandos vão receber no parâmetro
  'id_trecho' o identificador {id_trecho} do trecho {trc}.

  """
  return html_pag_ver_trecho_IMP.gera(ses, trc, comprar_pols, alterar_trc, erros)
