from entities.entityBillings import Billing
from entities.entityVolume import VolumePrimario, VolumeSecundario, VolumeWallets

from repositories.repositoryBillings import RepositoryBillings

class CalculaRoyalties:
    def __init__(self, repository_billings: RepositoryBillings) -> None:
        self.repository_billings: RepositoryBillings = repository_billings

    def calculaRoyalties(self, lstBillings: list[Billing], lstVol: list[VolumePrimario | VolumeSecundario]):
        for vol in lstVol:
            for bill in lstBillings:
                royalties = self.repository_billings.getRoyaltiesbyID(collection_id=vol.collection_id, lst=lstBillings)
                if vol.collection_id == bill.collection_id:
                    vol.billing_royaltyPrimary = royalties[1]