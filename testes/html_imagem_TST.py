import html_imagem
import utils_testes

frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
utils_testes.testa_gera_html(html_imagem, html_imagem.gera, "1", frag, pretty, "GO.png", "Texto alternativo da imagem", 100)