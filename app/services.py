from datetime import datetime

def horarios_se_sobrepoem(inicio1: datetime, fim1: datetime, 
                          inicio2: datetime, fim2: datetime) -> bool:

    """
    Verifica se dois intervalos de tempo se sobrepõem.

    Args:
        inicio1 (datetime): Início do primeiro intervalo.
        fim1 (datetime): Fim do primeiro intervalo.
        inicio2 (datetime): Início do segundo intervalo.
        fim2 (datetime): Fim do segundo intervalo.

    Returns:
        bool: True se os intervalos se sobrepõem, False caso contrário.
    """
    return inicio1 < fim2 and inicio2 < fim1