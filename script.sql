-- CREATE TEMPORARY TABLE IF NOT EXISTS prices AS
-- --     SELECT DATE(subqueryB.date), subqueryB.conversionSymbol AS token, POWER(c.close, -1) * subqueryB.close AS close
-- --     FROM finance.prices_crypto AS c
-- --     RIGHT JOIN (
-- --         SELECT time, close, conversionSymbol, date
-- --         FROM finance.prices_crypto
-- --         ) AS subqueryB ON c.time = subqueryB.time
-- --     WHERE c.conversionsymbol = 'BRL';

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