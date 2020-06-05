from utils_testes import erro_prog, aviso_prog
import comando_solicitar_pag_acrescentar_trecho

# !!! CONSERTAR !!!

usr_tst = {
            'nome': "Jorge Primus",
            'senha': "123456789",
            'email': "primus@gmail.com",
            'CPF': "111.222.333-44",
            'telefone': "+55(19)9 9289-3344",
            'documento': "11.222.333-5",
            'administrador': True,
            }

ses_tst = { "U-00000001", "ABCDEFGHIJK", "C-00000002"}

comando_solicitar_pag_acrescentar_trecho.processa(ses_tst, "")
