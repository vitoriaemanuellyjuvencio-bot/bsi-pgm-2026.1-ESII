from desconto import calcular_bonus

def test_bonus_zero_quando_nao_adianta():
    assert calcular_bonus(0, 5) == 0.0
def test_bonus_quando_devolve_antes():
    assert calcular_bonus(3, 5) == 15.0
def test_bonus_nunca_negativo():
    assert calcular_bonus(-2, 5) == 0.0