
import logging
from ..repositoryBase import RepositoryBase
from entities.comercial.entityPipedriveDeal import PipedriveDeal
class RepositoryPipedriveDeals(RepositoryBase):
    def __init__(self,connection, engine):
        self.schema = 'comercial'
        self.tableName = 'pipe_deals'
        super().__init__(connection, engine, self.schema, self.tableName)
    
    def insert(self, list_deals: list[PipedriveDeal]) -> None:
        if not list_deals:
            return None
        values = [t.to_tuple() for t in list_deals]
        with self.connection.cursor() as cur:
            try:
                placeholders = ','.join(['%s'] * len(values[0]))
                query = f"""
                    INSERT INTO {self.schema}.{self.tableName}
                    (id,title,value,currency,add_time,update_time,stage_change_time,active,deleted,status,probability,next_activity_date,next_activity_time,next_activity_id,last_activity_id,last_activity_date,lost_reason,visible_to,close_time,pipeline_id,won_time,first_won_time,lost_time,products_count,files_count,notes_count,followers_count,email_messages_count,activities_count,done_activities_count,undone_activities_count,participants_count,expected_close_date,last_incoming_mail_time,last_outgoing_mail_time,label,stage_order_nr,person_name,org_name,next_activity_subject,next_activity_type,next_activity_duration,next_activity_note,formatted_value,weighted_value,formatted_weighted_value,weighted_value_currency,rotten_time,owner_name,cc_email,origem,porte,setor,cargo,area,casodeuso,produtos,explicacaonegocio,org_hidden,person_hidden)
                    VALUES ({placeholders})
                    ON CONFLICT (id) DO
                    UPDATE SET
                    id = EXCLUDED.id,
                    title = EXCLUDED.title,
                    value = EXCLUDED.value,
                    currency = EXCLUDED.currency,
                    add_time = EXCLUDED.add_time,
                    update_time = EXCLUDED.update_time,
                    stage_change_time = EXCLUDED.stage_change_time,
                    active = EXCLUDED.active,
                    deleted = EXCLUDED.deleted,
                    status = EXCLUDED.status,
                    probability = EXCLUDED.probability,
                    next_activity_date = EXCLUDED.next_activity_date,
                    next_activity_time = EXCLUDED.next_activity_time,
                    next_activity_id = EXCLUDED.next_activity_id,
                    last_activity_id = EXCLUDED.last_activity_id,
                    last_activity_date = EXCLUDED.last_activity_date,
                    lost_reason = EXCLUDED.lost_reason,
                    visible_to = EXCLUDED.visible_to,
                    close_time = EXCLUDED.close_time,
                    pipeline_id = EXCLUDED.pipeline_id,
                    won_time = EXCLUDED.won_time,
                    first_won_time = EXCLUDED.first_won_time,
                    lost_time = EXCLUDED.lost_time,
                    products_count = EXCLUDED.products_count,
                    files_count = EXCLUDED.files_count,
                    notes_count = EXCLUDED.notes_count,
                    followers_count = EXCLUDED.followers_count,
                    email_messages_count = EXCLUDED.email_messages_count,
                    activities_count = EXCLUDED.activities_count,
                    done_activities_count = EXCLUDED.done_activities_count,
                    undone_activities_count = EXCLUDED.undone_activities_count,
                    participants_count = EXCLUDED.participants_count,
                    expected_close_date = EXCLUDED.expected_close_date,
                    last_incoming_mail_time = EXCLUDED.last_incoming_mail_time,
                    last_outgoing_mail_time = EXCLUDED.last_outgoing_mail_time,
                    label = EXCLUDED.label,
                    stage_order_nr = EXCLUDED.stage_order_nr,
                    person_name = EXCLUDED.person_name,
                    org_name = EXCLUDED.org_name,
                    next_activity_subject = EXCLUDED.next_activity_subject,
                    next_activity_type = EXCLUDED.next_activity_type,
                    next_activity_duration = EXCLUDED.next_activity_duration,
                    next_activity_note = EXCLUDED.next_activity_note,
                    formatted_value = EXCLUDED.formatted_value,
                    weighted_value = EXCLUDED.weighted_value,
                    formatted_weighted_value = EXCLUDED.formatted_weighted_value,
                    weighted_value_currency = EXCLUDED.weighted_value_currency,
                    rotten_time = EXCLUDED.rotten_time,
                    owner_name = EXCLUDED.owner_name,
                    cc_email = EXCLUDED.cc_email,
                    origem = EXCLUDED.origem,
                    porte = EXCLUDED.porte,
                    setor = EXCLUDED.setor,
                    cargo = EXCLUDED.cargo,
                    area = EXCLUDED.area,
                    casodeuso = EXCLUDED.casodeuso,
                    produtos = EXCLUDED.produtos,
                    explicacaonegocio = EXCLUDED.explicacaonegocio,
                    org_hidden = EXCLUDED.org_hidden,
                    person_hidden = EXCLUDED.person_hidden
                    """
                cur.executemany(query, values)
                self.connection.commit()

            except Exception as e:
                logging.error(e)
                
    def getDeals(self) -> list[PipedriveDeal]:
        with self.connection.cursor() as cur:
            query = f"select * from {self.schema}.{self.tableName}"
            try:
                cur.execute(query)
                deals: list[PipedriveDeal] = []
                for row in cur.fetchall():
                    deal = PipedriveDeal(
                        id = row[0],
                        title = row[1],
                        value = row[2],
                        currency = row[3],
                        add_time = row[4],
                        update_time = row[5],
                        stage_change_time = row[6],
                        active = row[7],
                        deleted = row[8],
                        status = row[9],
                        probability = row[10],
                        next_activity_date = row[11],
                        next_activity_time = row[12],
                        next_activity_id = row[13],
                        last_activity_id = row[14],
                        last_activity_date = row[15],
                        lost_reason = row[16],
                        visible_to = row[17],
                        close_time = row[18],
                        pipeline_id = row[19],
                        won_time = row[20],
                        first_won_time = row[21],
                        lost_time = row[22],
                        products_count = row[23],
                        files_count = row[24],
                        notes_count = row[25],
                        followers_count = row[26],
                        email_messages_count = row[27],
                        activities_count = row[28],
                        done_activities_count = row[29],
                        undone_activities_count = row[30],
                        participants_count = row[31],
                        expected_close_date = row[32],
                        last_incoming_mail_time = row[33],
                        last_outgoing_mail_time = row[34],
                        label = row[35],
                        stage_order_nr = row[36],
                        person_name = row[37],
                        org_name = row[38],
                        next_activity_subject = row[39],
                        next_activity_type = row[40],
                        next_activity_duration = row[41],
                        next_activity_note = row[42],
                        formatted_value = row[43],
                        weighted_value = row[44],
                        formatted_weighted_value = row[45],
                        weighted_value_currency = row[46],
                        rotten_time = row[47],
                        owner_name = row[48],
                        cc_email = row[49],
                        origem = row[50],
                        porte = row[51],
                        setor = row[52],
                        cargo = row[53],
                        area = row[54],
                        casodeuso = row[55],
                        produtos = row[56],
                        explicacaonegocio = row[57],
                        org_hidden = row[58],
                        person_hidden = row[59]
            )
                    deals.append(deal)
            except Exception as e:
                logging.error(e)
                return None