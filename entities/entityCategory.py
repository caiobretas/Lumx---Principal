from typing import Any


class Category:
    def __init__(self, id=None, recorrencia=None, projeto=None, produto=None, method_id=None, subcategoria4=None, subcategoria3=None, subcategoria2=None, subcategoria=None, categoria=None, categoriaprojecao=None, categoriacustoreceita=None):
        self.id = id if id != "" else None
        self.recorrencia = recorrencia if recorrencia is not None else 'Pontual'
        self.projeto = projeto if projeto != "" else None
        self.produto = produto if produto != "" else None
        self.method_id = method_id if method_id != "" else None
        self.subcategoria4 = subcategoria4 if subcategoria4 != "" else None
        self.subcategoria3 = subcategoria3 if subcategoria3 != "" else None
        self.subcategoria2 = subcategoria2 if subcategoria2 != "" else None
        self.subcategoria = subcategoria if subcategoria != "" else None
        self.categoria = categoria if categoria != "" else None
        self.categoriaprojecao = categoriaprojecao if categoriaprojecao != "" else None
        self.categoriacustoreceita = categoriacustoreceita if categoriacustoreceita != "" else None
    
    def to_tuple(self):
        return (self.id, self.recorrencia, self.projeto, self.produto, self.method_id, self.subcategoria4, self.subcategoria3, self.subcategoria2, self.subcategoria, self.categoria, self.categoriaprojecao, self.categoriacustoreceita)