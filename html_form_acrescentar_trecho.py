
import html_form_acrescentar_trecho_IMP

# imports trecho
import trecho_IMP; from trecho_IMP import Objeto_Trecho_IMP

def gera(atrs, admin,):
  """Retorna o formulário de nova passagem.

  O formuláro contém campos editáveis para as informações que o usuário
  deve preencher.  Se {atrs} não for {None}.

  O parâmetro {admin} diz que o usuário que pediu a criação do usuário
  (NÃO o usuário que está sendo cadastrado!) é administrador. Se for {True}, o
  formulário vai mostrar um checkbox para definir o novo usuário como
  administrador.

  O formulário conterá um botão 'Cadastrar' (de tipo 'submit').
  Quando o usuário clicar nesse botão, será emitido um comando POST com ação
  {cadastrar_usuario}.  Os argumentos desse POST são todos os atributos da classe {Objeto_Usuario},
  com os valores de {atrs} que o usuário deve ter preenchido.

  O formulário também terá um botão simples 'Cancelar',
  que, quando clicado, emite o comando 'principal'."""
  return html_form_acrescentar_trecho_IMP.gera(atrs, admin)

  # FUNÇÕES PARA DEPURAÇÃO

def verifica(trc, id, atrs):
  """Faz testes de consistência básicos de um objeto {trc} de classe {Objeto_Trecho}, 
  dados o identificador esperado {id}, e os atributos esperados {atrs}.
  
  Especificamente, verifica as funções {obtem_identificador(trc)},
  {obtem_atributos(trc)} e {busca_por_identificador(id)}.
  
  Devolve {True} se os testes deram certo, {False} caso contrário. Também
  imprme diagnósticos em {sys.stderr}."""
  return trecho_IMP.verifica(trc, id, atrs)

def cria_testes():
  """Limpa a tabela de trechos com {inicializa(True)}, e cria pelo menos três trechos
  para fins de teste, incluindo-os na tabela.  Não devolve nenhum resultado.
  
  Deve ser chamada apenas uma vez no ínicio da execução do programa, 
  depois de chamar {base_sql.conecta}.""" 
  trecho_IMP.cria_testes()

def diagnosticos(val):
  """Habilita (se {val=True}) ou desabilita (se {val=False}) a
  impressão em {sys.stderr} de mensagens de diagnóstico pelas 
  funções deste módulo."""
  trecho_IMP.diagnosticos(val)

