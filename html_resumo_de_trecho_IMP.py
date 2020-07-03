import trecho
import html_texto
import html_botao_simples
import html_imagem


def gera(trc, ver, alterar):
  id_trecho = trecho.obtem_identificador(trc)
  atrs_trecho = trecho.obtem_atributos(trc)
  # atributos trecho
  codigo = atrs_trecho['codigo']
  origem = atrs_trecho['origem']
  destino = atrs_trecho['destino']
  dt_partida = atrs_trecho['dia_partida'] + " " + atrs_trecho['hora_partida']
  dt_chegada = atrs_trecho['dia_chegada'] + " " + atrs_trecho['hora_chegada']
  veiculo = atrs_trecho['veiculo']
  num_poltronas_total = str(trecho.numero_de_poltronas(trc))
  num_poltronas_livres = str(trecho.numero_de_poltronas_livres(trc))
  num_poltronas = num_poltronas_livres + " / " + num_poltronas_total


###
###  # estilos
###  estilo_parag = "\n display:block; word-wrap:break-word;  width: 100%;\n  margin-top: 10px;\n  margin-bottom: 2px;\n  text-indent: 0px;\n  line-height: 75%;"
###
###  # gerando tabela
###  titulos = ("Código", "Origem", "Destino", "Data de Partida", "Data de Chegada")
###  atributos = obtem_atributos(trc)
###  linhas = []
###  for titulo, valor in zip(titulos, atributos.values()):
###    ht_titulo = html_paragrafo.gera(estilo_parag, html_texto.gera(titulo, None, "Courier", "20px", "bold", "2px", "left", "#263238", None))
###    ht_valor = html_paragrafo.gera(estilo_parag, html_texto.gera(valor, None, "Courier", "20px", None, "2px", "left", "#263238", None))
###    linhas.append([ht_titulo, ht_valor])
###
###  tabela = html_table.gera(linhas)
###
###  # ids = obtem_poltronas(trc)
###  ids = []
###  poltronas = ""
###  # poltronas = html_lista_de_poltronas.gera(ses, None, trc, ids, False)
###
###  conteudo = tabela + "<br/>" + poltronas

  # blocos de texto para tabela

  # ht_codigo = ('Código', html_texto.gera(codigo, None, None, None, None, None, None, None, None))
  # ht_origem = ('Origem', html_texto.gera(origem, None, None, None, None, None, None, None, None))
  # ht_destino = ('Destino', html_texto.gera(destino, None, None, None, None, None, None, None, None))
  # ht_dt_partida = ('Data de Partida', html_texto.gera(dt_partida, None, None, None, None, None, None, None, None))
  # ht_dt_chegada = ('Data de Chegada', html_texto.gera(dt_chegada, None, None, None, None, None, None, None, None))
  # ht_num_poltronas = ('Número de Poltronas', html_texto.gera(num_poltronas, None, None, None, None, None, None, None, None))
  
  # recupera o nome da empresa
  empresa = codigo.split(" ")[0] 

  # adicionar html com imagem de logo da empresa
  ht_logo = html_imagem.gera("/" + empresa + ".png", "logo", 20)
  
  ht_codigo = html_texto.gera(codigo, None, None, None, None, None, None, None, None)
  ht_origem = html_texto.gera(origem, None, None, None, None, None, None, None, None)
  ht_destino = html_texto.gera(destino, None, None, None, None, None, None, None, None)
  ht_dt_partida = html_texto.gera(dt_partida, None, None, None, None, None, None, None, None)
  ht_dt_chegada = html_texto.gera(dt_chegada, None, None, None, None, None, None, None, None)
  ht_veiculo = html_texto.gera(veiculo, None, None, None, None, None, None, None, None)
  ht_num_poltronas = html_texto.gera(num_poltronas, None, None, None, None, None, None, None, None)

  ## def add_span_tag(str):
  ##   return "<span style=\"color:blue;font-weight:bold\">" + str + "</span>"
  ## 
  ## ht_campos = (add_span_tag("Código do trecho: ") + ht_codigo,
  ##              add_span_tag("Origem: ") + ht_origem,
  ##              add_span_tag("Data de partida: ") + ht_dt_partida,
  ##              add_span_tag("Destino: ") + ht_destino,
  ##              add_span_tag("Data de chegada: ") + ht_dt_chegada,
  ##              add_span_tag("Assentos livres: ") + ht_num_poltronas,
  ##              botao_ver,
  ##              botao_alterar)
  ht_campos = [ ht_logo, ht_codigo, ht_origem, ht_destino, ht_dt_partida, ht_dt_chegada, ht_num_poltronas ]
  
  # Botões de "Ver" e "Alterar"
  if ver:
    botao_ver = html_botao_simples.gera("Ver", 'ver_trecho', {'id_trecho': id_trecho}, '#00FF00')
    ht_campos.append(botao_ver)

  if alterar:
    botao_alterar = html_botao_simples.gera("Alterar", 'solicitar_pag_alterar_trecho', {'id_trecho': id_trecho}, '#FFA700')
    ht_campos.append(botao_alterar)

  return ht_campos
