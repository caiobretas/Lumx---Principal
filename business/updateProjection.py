from time import time
from viewers.viewerPrices import ViewerPrices
from business.writePrices import WritePrices
from business.writeProjection import WriteProjection

class UpdateProjection(object):
    def __init__(self, pathProjection, connProtocol, connFinance, engineAdmin, schema) -> None:
        timer = time()
        
        WritePrices(path=pathProjection, sheetName = 'Tabela Cotações', connection=connFinance, engine=engineAdmin, schema=schema, tableName='prices_crypto').writePrices()
        WriteProjection(path=pathProjection, connection=connFinance, engine=engineAdmin, schema=schema).insert_projectionTable(sheetName='Tabela Projeção')
        
        print('Projection updated in {:.2f} seconds\n'.format(time() - timer))