import logging

def verificar_e_transformar_string(string: str) -> list[int] | int:
    if not string: return
    try:
        if "," in string:
            valores = string.split(",")
            lista_inteiros = [int(valor) for valor in valores]
            return lista_inteiros
        else:
            valor = int(string)
            return [valor]
    except Exception as e:
        logging.error(e)
        return string