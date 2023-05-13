from typing import Any


class Category:
    def __init__(self, id, projeto, method_id, subcategoria4, subcategoria3, subcategoria2, subcategoria, categoria, categoriaprojecao, categoriacustoreceita):
        self.id = id
        self.projeto = projeto
        self.method_id = method_id
        self.subcategoria4 = subcategoria4
        self.subcategoria3 = subcategoria3
        self.subcategoria2 = subcategoria2
        self.subcategoria = subcategoria
        self.categoria = categoria
        self.categoriaprojecao = categoriaprojecao
        self.categoriacustoreceita = categoriacustoreceita
    def to_tuple(self):
        return (self.id, self.projeto, self.method_id, self.subcategoria4, self.subcategoria3, self.subcategoria2, self.subcategoria, self.categoria, self.categoriaprojecao, self.categoriacustoreceita)

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