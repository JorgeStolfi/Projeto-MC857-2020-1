import utils_testes

import base_sql
import tabelas
import sessao
import poltrona
import comando_alterar_poltrona

# Conecta no banco e carrega alimenta com as informações para o teste
utils_testes.mostra(0, "Conectando com base de dados...")
res = base_sql.conecta("DB", None, None)
assert res is None

utils_testes.mostra(0, "Conectando com base de dados...")
tabelas.cria_todos_os_testes()

# Sessao de teste (administrador)
ses = sessao.busca_por_identificador("S-00000004")

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = comando_alterar_poltrona
  funcao = modulo.processa
  frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False  # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

# TODO: id_compra não é um valor crítico (Eu acho) mas atualmente ele não é atualizado, mesmo sendo obrigatório. Revisar comando_alterar_poltrona!
def testa_novos_valores():
    id_poltrona = "A-00000001"
    poltrona_antiga = poltrona.busca_por_identificador(id_poltrona)
    assert poltrona_antiga is not None, "Poltrona A-00000001 não encontrada no banco"

    # Valores antigos
    atributos_antigos = poltrona.obtem_atributos(poltrona_antiga)

    # Novos valores
    nova_oferta = "off"
    novo_preco = "88.00"
    args = {'id_poltrona': id_poltrona,
     'id_trecho': atributos_antigos['id_trecho'], 
     'id_compra': atributos_antigos['id_compra'], 
     'numero': atributos_antigos['numero'], 
     'oferta': nova_oferta, 
     'preco': novo_preco}
    
    testa("ValoresAlterados", ses, args)

    # Valores atualizados
    poltrona_atualizada = poltrona.busca_por_identificador(id_poltrona)
    atributos_atualizados = poltrona.obtem_atributos(poltrona_atualizada)
    
    assert atributos_atualizados['oferta'] == False, "Oferta não atualizada"
    assert atributos_atualizados['preco'] == float(novo_preco), "Preco não atualizado"

def testa_id_invalido():
    # Argumentos com id de poltrona inexistente no banco (outros valores nao importam)
    args = {'id_poltrona': 'A-0000000X',
     'id_trecho': 'x', 
     'id_compra': 'x', 
     'numero': 'x', 
     'oferta': 'x', 
     'preco': '0.00'}
    
    testa("IdInvalido", ses, args)

def testa_valores_criticos_invalidos():
    id1 = "A-00000001"
    ptr1 = poltrona.busca_por_identificador(id1)
    assert ptr1 is not None, "Poltrona A-00000001 não encontrada no banco"

    # Valores antigos
    atributos_antigos = poltrona.obtem_atributos(ptr1)

    ptr2 = poltrona.busca_por_identificador("A-00000002")
    assert ptr2 is not None, "Poltrona A-00000002 não encontrada no banco"

    # Argumentos com id de trecho E número sendo usado por outra poltrona (A-00000002)
    args_mesmo_trecho = {'id_poltrona': id1,
     'id_trecho': poltrona.obtem_atributo(ptr2, 'id_trecho'), 
     'id_compra': atributos_antigos['id_compra'], 
     'numero': poltrona.obtem_atributo(ptr2, 'numero'), 
     'oferta': 'on' if atributos_antigos['oferta'] else 'off', 
     'preco': atributos_antigos['preco']}
    
    testa("MesmoTrechoENumero", ses, args_mesmo_trecho)

utils_testes.mostra(0, "Testando alteração bem sucedida...")
testa_novos_valores()

utils_testes.mostra(0, "Testando alteração com id inválido...")
testa_id_invalido()

utils_testes.mostra(0, "Testando alteração com valores críticos inválidos...")
testa_valores_criticos_invalidos()

utils_testes.mostra(0, "Testes realizados com sucesso!")