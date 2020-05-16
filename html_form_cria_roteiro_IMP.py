import html_label
import html_input
import html_tabela
import html_botao_submit
import html_form


def gera():
    linhas = [].copy()

    ht_rotulo = html_label.gera("Origem", ": ")
    ht_campo = html_input.gera(None, "text", "origem", None, True, None, None)
    linhas.append((ht_rotulo, ht_campo,))

    ht_rotulo = html_label.gera("Destino", ": ")
    ht_campo = html_input.gera(None, "text", "destino", None, True, None, None)
    linhas.append((ht_rotulo, ht_campo,))

    # Monta a tabela com os fragmentos HTML:
    ht_tabela = html_tabela.gera(linhas)

    ht_bt_buscar = html_botao_submit.gera("Buscar", 'comando_criar_roteiro', None, '#55ee55')

    ht_campos = \
        ht_tabela + \
        ht_bt_buscar

    ht = html_form.gera(ht_campos)
    return ht
