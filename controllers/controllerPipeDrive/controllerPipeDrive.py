import requests
import json
import logging
from controllers.controllerHTTP.controllerHTTPBase import ControllerHTTPBase
from entities.comercial.entityPipedriveDeal import PipedriveDeal
class ControllerPipeDrive ( ControllerHTTPBase ):
    def __init__(self):
        self.apikey = '106c62e486639ed0a7f04fe67f55f3dcad4392ad'
        self.baseUrl = 'https://lumxstudios.pipedrive.com/api'
        self.version = 'v1'
    
    def getDeals(self) -> list[PipedriveDeal]:
        try:
            action = 'deals'
            url = f'{self.baseUrl}/{self.version}/{action}?api_token={self.apikey}'            
            jsonResponse = self.get(url,type='json')
            listDeals: list[PipedriveDeal] = []
            result: list[dict] = jsonResponse['data']
            for obj in result:
                deal = PipedriveDeal(
                id=obj.get('id',None),
                value=obj.get('value',None),
                title=obj.get('title',None),
                currency=obj.get('currency',None),
                add_time=obj.get('add_time',None),
                update_time=obj.get('update_time',None),
                stage_change_time=obj.get('stage_change_time',None),
                active=obj.get('active',None),
                deleted=obj.get('deleted',None),
                status=obj.get('status',None),
                probability=obj.get('probability',None),
                next_activity_date=obj.get('next_activity_date',None),
                next_activity_time=obj.get('next_activity_time',None),
                next_activity_id=obj.get('next_activity_id',None),
                last_activity_id=obj.get('last_activity_id',None),
                last_activity_date=obj.get('last_activity_date',None),
                lost_reason=obj.get('lost_reason',None),
                visible_to=obj.get('visible_to',None),
                close_time=obj.get('close_time',None),
                pipeline_id=obj.get('pipeline_id',None),
                won_time=obj.get('won_time',None),
                first_won_time=obj.get('first_won_time',None),
                lost_time=obj.get('lost_time',None),
                products_count=obj.get('products_count',None),
                files_count=obj.get('files_count',None),
                notes_count=obj.get('notes_count',None),
                followers_count=obj.get('followers_count',None),
                email_messages_count=obj.get('email_messages_count',None),
                activities_count=obj.get('activities_count',None),
                done_activities_count=obj.get('done_activities_count',None),
                undone_activities_count=obj.get('undone_activities_count',None),
                participants_count=obj.get('participants_count',None),
                expected_close_date=obj.get('expected_close_date',None),
                last_incoming_mail_time=obj.get('last_incoming_mail_time',None),
                last_outgoing_mail_time=obj.get('last_outgoing_mail_time',None),
                label=obj.get('label',None),
                stage_order_nr=obj.get('stage_order_nr',None),
                person_name=obj.get('person_name',None),
                org_name=obj.get('org_name',None),
                next_activity_subject=obj.get('next_activity_subject',None),
                next_activity_type=obj.get('next_activity_type',None),
                next_activity_duration=obj.get('next_activity_duration',None),
                next_activity_note=obj.get('next_activity_note',None),
                formatted_value=obj.get('formatted_value',None),
                weighted_value=obj.get('weighted_value',None),
                formatted_weighted_value=obj.get('formatted_weighted_value',None),
                weighted_value_currency=obj.get('weighted_value_currency',None),
                rotten_time=obj.get('rotten_time',None),
                owner_name=obj.get('owner_name',None),
                cc_email=obj.get('cc_email',None),
                origem=obj.get('bbe24d81b815f65cc5553f6a733a2ce2b0f2ef15',None),
                porte=obj.get('deb57dca3f160392cd7040397cd4e2601f8dfb52',None),
                setor=obj.get('501c73f30bca5a80b56f4f6c9c9c10b5025a23c6',None),
                cargo=obj.get('c9ff5a2bffa8d5fcc550bab41319f3ae90ab7b95',None),
                area=obj.get('5df3964cce9339365f6b82e1525608bf4eb98835',None),
                casodeuso=obj.get('c2a06a45bbaea121d2381a0522d1ee0c270ef82c',None),
                produtos=obj.get('a770d0a943fe1d6c3632d9d2b98085c8083ec330',None),
                explicacaonegocio=obj.get('de5e5bf203c5e2a0561c723c2ac7163089fcb53c',None),
                org_hidden=obj.get('org_hidden',None),
                person_hidden=obj.get('person_hidden',None))
                
                listDeals.append(deal)
            return listDeals
        
        except Exception as e:
            logging.error(e)
    
    def getDealsFields(self) -> list[PipedriveDeal]:
        try:
            action = 'dealFields'
            url = f'{self.baseUrl}/{self.version}/{action}?api_token={self.apikey}'
            jsonResponse = self.get(url,type='json')
            return jsonResponse
        except Exception as e:
            logging.error(e)
            
    def getFlowbyDealId(self, dealId):
        try:
            action = f'deals/{dealId}/flow'
            url = f'{self.baseUrl}/{self.version}/{action}?api_token={self.apikey}'
            jsonResponse = self.get(url)
            return jsonResponse
        except Exception as e:
            logging.error(e)