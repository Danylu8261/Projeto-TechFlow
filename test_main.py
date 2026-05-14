from main import validar_prioridade

def test_prioridade_valida():
    assert validar_prioridade('Alta') == True
    assert validar_prioridade('Média') == True
    assert validar_prioridade('Baixa') == True

def test_prioridade_invalida():
    assert validar_prioridade('Urgente') == False

# Fim dos testes unitáriosgit add .

