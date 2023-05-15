from typing import Any


class Category:
    def __init__(self, id, projeto, produto, method_id, subcategoria4, subcategoria3, subcategoria2, subcategoria, categoria, categoriaprojecao, categoriacustoreceita):
        self.id = id if id != "" else None
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
        return (self.id, self.projeto, self.produto, self.method_id, self.subcategoria4, self.subcategoria3, self.subcategoria2, self.subcategoria, self.categoria, self.categoriaprojecao, self.categoriacustoreceita)

# # class Category1:
#     def __init__(self,
#         id=None,
#         idplanoconta=None,
#         idpai=None,
#         nome=None,
#         ativo=None,
#         controlasaldo=None,
#         tipo=None,
#         descricaotipo=None,
#         cartaocredito=None,
#         tipocontagerencial=None,
#         idtipoimposto=None,
#         nivel=None,
#         grupocontacorrente=None,
#         valoratual=None,
#         saldobloqueado=None,
#         idcontabanco=None,
#         usarextratobanco=None,
#         kamino=None,
#         excluifluxocaixa=None,
#         codigoexterno=None,
#         dataultimoextratoconciliado=None,
#         dataultimoextratopendente=None):

#         self.id = id
#         self.idplanoconta = idplanoconta
#         self.idpai = idpai
#         self.nome = nome
#         self.ativo = ativo
#         self.controlasaldo = controlasaldo
#         self.tipo = tipo
#         self.descricaotipo = descricaotipo
#         self.cartaocredito = cartaocredito
#         self.tipocontagerencial = tipocontagerencial
#         self.idtipoimposto = idtipoimposto
#         self.nivel = nivel
#         self.grupocontacorrente = grupocontacorrente
#         self.valoratual = valoratual
#         self.saldobloqueado = saldobloqueado
#         self.idcontabanco = idcontabanco
#         self.usarextratobanco = usarextratobanco
#         self.kamino = kamino
#         self.excluifluxocaixa = excluifluxocaixa
#         self.codigoexterno = codigoexterno
#         self.dataultimoextratoconciliado = dataultimoextratoconciliado
#         self.dataultimoextratopendente = dataultimoextratopendente