def verificar_e_substituir_atributo_por_none(objeto):
    for atributo, valor in vars(objeto).items():
        if isinstance(valor, str) and valor == '':
            setattr(objeto, atributo, None)