import trecho
import poltrona
import html_resumo_de_trecho
import html_table
import html_texto
import html_span


def gera(trcs, alterar):
  linhas = [].copy()

  ht_logo = html_texto.gera("<b> Logo </b>", None, None, None, None, "10px", None, None, "#60a3bc")
  ht_codigo = html_texto.gera("<b> Código </b>", None, None, None, None, "10px", None, None, "#60a3bc")
  ht_origem = html_texto.gera("<b> Origem </b>", None, None, None, None, "10px", None, None, "#60a3bc")
  ht_destino = html_texto.gera("<b> Destino </b>", None, None, None, None, "10px", None, None, "#60a3bc")
  ht_dt_partida = html_texto.gera("<b> Data partida </b>", None, None, None, None, "10px", None, None, "#60a3bc")
  ht_dt_chegada = html_texto.gera("<b> Data chegada </b>", None, None, None, None, "10px", None, None, "#60a3bc")
  ht_num_poltronas = html_texto.gera("<b> Poltronas </b>", None, None, None, None, "10px", None, None, "#60a3bc")

  ht_cabecalho = [ ht_logo, ht_codigo, ht_origem, ht_destino, ht_dt_partida, ht_dt_chegada, ht_num_poltronas ]
  linhas.append(ht_cabecalho)

  for trc in trcs:
    ver = True
    alterar_trc = alterar
    linha = html_resumo_de_trecho.gera(trc, ver, alterar)
    linhas.append(linha)
  ht_itens = html_table.gera(linhas)

  width_pct = ("50%")
  estilo_final = f"width: {width_pct}; padding: 15px; border-radius: 15px 50px 20px; display: flex; align-items: center;"
  bloco_final = html_span.gera(estilo_final, ht_itens)

  return bloco_final
