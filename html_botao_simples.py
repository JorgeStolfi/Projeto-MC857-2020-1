import html_botao_simples_IMP

def gera(texto, URL, args, cor_fundo):
  """Devolve um fragmento HTML5 que implementa um botão genérico de 
  tipo "<button>", com o {texto} e {cor_fundo} especificados. 
  
  Quando clicado, esse botão emite um comando HTTP 'GET' para o {URL} dado.
  
  Se {args} não for {None}, deve ser um dicionário cujas chaves e
  valores são acrescentadas ao {URL} no formato
  "?{chave1}={valor1}&{chave2}={valor2}...". Por enquanto, as chaves e
  valores devem ser cadeias só com letras ASCII, dígitos, pontos,
  hífens e underscores. Os valores aceitam, além desses caracteres, vírgula."""
  return html_botao_simples_IMP.gera(texto, URL, args, cor_fundo)
