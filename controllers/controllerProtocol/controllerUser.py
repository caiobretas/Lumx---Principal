from pandas import DataFrame

from .controllerProtocol import ControllerProtocol

from entities.entityUser import User

class ControllerUsers( ControllerProtocol ):
    def __init__(self, connection):
        super().__init__(connection)

    def get_User(self):
        query = 'select * from blkx.users'
        df: DataFrame = self.run_query(query=query)

        list_aux: list[User] = []
        for index, row in df.iterrows():
            row = User(
            id =  row['id'],
            client_id =  row['client_id'],
            username =  row['username'],
            created_at =  row['created_at'],
            avatar_url =  row['avatar_url'],
            email =  row['email'],
            cpf =  row['cpf'],
            phone =  row['phone'],
            mynt_address =  row['mynt_address'],
            )
            list_aux.append(row)
        
        return list_aux