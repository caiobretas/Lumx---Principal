from business.geral.verificaSeparadorTransforma import verificar_e_transformar_string

class PipedriveDeal:
    def __init__(self,id,title,value,currency,add_time,update_time,stage_change_time,active,deleted,status,probability,next_activity_date,next_activity_time,next_activity_id,last_activity_id,last_activity_date,lost_reason,visible_to,close_time,pipeline_id,won_time,first_won_time,lost_time,products_count,files_count,notes_count,followers_count,email_messages_count,activities_count,done_activities_count,undone_activities_count,participants_count,expected_close_date,last_incoming_mail_time,last_outgoing_mail_time,label,stage_order_nr,person_name,org_name,next_activity_subject,next_activity_type,next_activity_duration,next_activity_note,formatted_value,weighted_value,formatted_weighted_value,weighted_value_currency,rotten_time,owner_name,cc_email,origem,porte,setor,cargo,area,casodeuso,produtos,explicacaonegocio,org_hidden,person_hidden):
            self.id = id
            self.title = title
            self.value = value
            self.currency = currency
            self.add_time = add_time
            self.update_time = update_time
            self.stage_change_time = stage_change_time
            self.active = active
            self.deleted = deleted
            self.status = status
            self.probability = probability
            self.next_activity_date = next_activity_date
            self.next_activity_time = next_activity_time
            self.next_activity_id = next_activity_id
            self.last_activity_id = last_activity_id
            self.last_activity_date = last_activity_date
            self.lost_reason = lost_reason
            self.visible_to = visible_to
            self.close_time = close_time
            self.pipeline_id = pipeline_id
            self.won_time = won_time
            self.first_won_time = first_won_time
            self.lost_time = lost_time
            self.products_count = products_count
            self.files_count = files_count
            self.notes_count = notes_count
            self.followers_count = followers_count
            self.email_messages_count = email_messages_count
            self.activities_count = activities_count
            self.done_activities_count = done_activities_count
            self.undone_activities_count = undone_activities_count
            self.participants_count = participants_count
            self.expected_close_date = expected_close_date
            self.last_incoming_mail_time = last_incoming_mail_time
            self.last_outgoing_mail_time = last_outgoing_mail_time
            self.label = label
            self.stage_order_nr = stage_order_nr
            self.person_name = person_name
            self.org_name = org_name
            self.next_activity_subject = next_activity_subject
            self.next_activity_type = next_activity_type
            self.next_activity_duration = next_activity_duration
            self.next_activity_note = next_activity_note
            self.formatted_value = formatted_value
            self.weighted_value = weighted_value
            self.formatted_weighted_value = formatted_weighted_value
            self.weighted_value_currency = weighted_value_currency
            self.rotten_time = rotten_time
            self.owner_name = owner_name
            self.cc_email = cc_email
            self.org_hidden = org_hidden
            self.person_hidden = person_hidden
            
            # condições específicas para campos customizados
            if origem:
                if origem != "-":
                    self.origem = verificar_e_transformar_string(origem)
                else: self.origem = []    
            else: self.origem = []
            
            if porte:
                if porte == "-":
                    self.porte = []
                else:
                    self.porte = verificar_e_transformar_string(porte)
            else:
                self.porte = []

            if setor:
                if setor == "-":
                    self.setor = []
                else:
                    self.setor = verificar_e_transformar_string(setor)
            else:
                self.setor = []

            if cargo:
                if cargo == "-":
                    self.cargo = []
                else:
                    self.cargo = verificar_e_transformar_string(cargo)
            else:
                self.cargo = []

            if area:
                if area == "-":
                    self.area = []
                else:
                    self.area = verificar_e_transformar_string(area)
            else:
                self.area = []

            if casodeuso:
                if casodeuso == "-":
                    self.casodeuso = []
                else:
                    self.casodeuso = verificar_e_transformar_string(casodeuso)
            else:
                self.casodeuso = []

            if produtos:
                if produtos == "-":
                    self.produtos = []
                else:
                    self.produtos = verificar_e_transformar_string(produtos)
            else:
                self.produtos = []

            if explicacaonegocio:
                if explicacaonegocio == "-":
                    self.explicacaonegocio = explicacaonegocio
                else:
                    self.explicacaonegocio = None
            else: self.explicacaonegocio = None

            
    def to_tuple(self)->tuple:
        return (self.id,self.title,self.value,self.currency,self.add_time,self.update_time,self.stage_change_time,self.active,self.deleted,self.status,self.probability,self.next_activity_date,self.next_activity_time,self.next_activity_id,self.last_activity_id,self.last_activity_date,self.lost_reason,self.visible_to,self.close_time,self.pipeline_id,self.won_time,self.first_won_time,self.lost_time,self.products_count,self.files_count,self.notes_count,self.followers_count,self.email_messages_count,self.activities_count,self.done_activities_count,self.undone_activities_count,self.participants_count,self.expected_close_date,self.last_incoming_mail_time,self.last_outgoing_mail_time,self.label,self.stage_order_nr,self.person_name,self.org_name,self.next_activity_subject,self.next_activity_type,self.next_activity_duration,self.next_activity_note,self.formatted_value,self.weighted_value,self.formatted_weighted_value,self.weighted_value_currency,self.rotten_time,self.owner_name,self.cc_email,self.origem,self.porte,self.setor,self.cargo,self.area,self.casodeuso,self.produtos,self.explicacaonegocio,self.org_hidden,self.person_hidden)