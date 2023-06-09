from pandas import DataFrame

from entities.entityBillings import Billing


from repositories.repositoryBase import RepositoryBase

class RepositoryBillings( RepositoryBase ):

    def __init__(self, connection: str, engine: str, schema: str, tableName: str):
        super().__init__(connection= connection, engine=engine, schema=schema, tableName=tableName)

    def insertBilling(self, lst: list[Billing]):
        super().salvaDatabase(lst)

    def getRoyalties(self) -> list[Billing]:
        lst_aux: list[Billing] = []
        for index, row in self.database.iterrows():
            row = Billing(
            collection_id = row['collection_id'],
            collection_name = row['collection_name'],
            billing_upfront = row['billing_upfront'],
            billing_monthly = row['billing_monthly'],
            billing_currency = row['billing_currency'],
            billing_royaltyPrimary = row['billing_royaltyPrimary'],
            billing_royaltySecundary = row['billing_royaltySecundary'],
            billing_royaltyPIX = row['billing_royaltyPIX'],
            billing_walletAPI_10000 = row['billing_walletAPI_10000'],
            billing_walletAPI_10001_50000 = row['billing_walletAPI_10001_50000'],
            billing_walletAPI_50001_100000 = row['billing_walletAPI_50001_100000'],
            billing_walletAPI_100000_250000 = row['billing_walletAPI_100000_250000'],
            billing_walletAPI_250000 = row['billing_walletAPI_250000'])
            lst_aux.append(row)
        return lst_aux
