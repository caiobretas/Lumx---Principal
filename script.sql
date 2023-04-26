-- CREATE TEMPORARY TABLE IF NOT EXISTS prices AS
--     SELECT DATE(subqueryB.date), subqueryB.conversionSymbol AS token, POWER(c.close, -1) * subqueryB.close AS close
--     FROM finance.prices_crypto AS c
--     RIGHT JOIN (
--         SELECT time, close, conversionSymbol, date
--         FROM finance.prices_crypto
--         ) AS subqueryB ON c.time = subqueryB.time
--     WHERE c.conversionsymbol = 'BRL';

-- SELECT m.*, b.name AS from_, b1.name AS to_, b2.name AS smart_contract, p.close
-- FROM finance.movements_crypto AS m
-- 	LEFT JOIN finance.book_crypto AS b ON b.address = m.from_
-- 	LEFT JOIN finance.book_crypto AS b1 ON b1.address = m.to_
-- 	LEFT JOIN finance.book_crypto AS b2 ON b2.address = m.contractaddress
-- 	LEFT JOIN prices AS p ON DATE(p.date) = DATE(m.datetime) AND p.token = m.tokensymbol
-- ORDER BY DATE(m.datetime) DESC;

-- select distinct fm.*, subcategoria3, subcategoria2, subcategoria, categoria, categoriaprojecao
-- from finance.movements as fm
-- 	left join finance.categories as fc on fc.subcategoria4 = fm.nomeclassificacao;

create table if not exists h_resources.contacts(
id varchar(100) NOT NULL PRIMARY KEY,
idpessoa  varchar(100),
nome varchar(100),
cpfcnpj varchar(100),
nomefantasia varchar(100),
logradouro varchar(100),
nro varchar(100),
complemento varchar(100),
bairro varchar(100),
cep varchar(100),
cidade varchar(100),
uf varchar(100),
nomepais varchar(100),
ativo varchar(100),
email varchar(100),
telefone varchar(100),
cliente varchar(100),
fornecedor varchar(100),
sexo varchar(100),
rg varchar(100),
orgaoemissorrg varchar(100),
ufemissorrg varchar(100),
clientedesde varchar(100),
idclassificacaopreferencial varchar(100),
idcentrocustopreferencial varchar(100),
observacoes varchar(100),
chavepix varchar(100),
tipochavepix varchar(100));