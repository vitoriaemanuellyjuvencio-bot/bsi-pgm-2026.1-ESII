from multa import calcular_multa_com_carencia

def test_multa_zero_quando_sem_atraso():
    assert calcular_multa_com_carencia(0, 10, 2) == 0.0
    
def test_cobra_dias_alem_da_carencia():
    assert calcular_multa_com_carencia(5, 10, 2) == 30.0