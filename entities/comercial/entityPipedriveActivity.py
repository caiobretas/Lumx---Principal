
class PipedriveActivity:
    
    def __init__(self,id = None,done = None,type = None,duration = None,subject = None,company_id = None,user_id = None,conference_meeting_client = None,conference_meeting_url = None,conference_meeting_id = None,due_date = None,due_time = None,busy_flag = None,add_time = None,marked_as_done_time = None,public_description = None,location = None,org_id = None,person_id = None,deal_id = None,active_flag = None,update_time = None,update_user_id = None,source_timezone = None,lead_id = None,location_subpremise = None,location_street_number = None,location_route = None,location_sublocality = None,location_locality = None,location_admin_area_level_1 = None,location_admin_area_level_2 = None,location_country = None,location_postal_code = None,location_formatted_address = None,project_id = None,):
        
        self.id = int(id)
        self.done = bool(done)
        self.type = type
        self.duration = duration
        self.subject = subject
        self.company_id = int(company_id)
        self.user_id = int(user_id)
        self.conference_meeting_client = conference_meeting_client
        self.conference_meeting_url = conference_meeting_url
        self.conference_meeting_id = conference_meeting_id
        self.due_date = due_date
        self.due_time = due_time
        self.busy_flag = bool(busy_flag)
        self.add_time = add_time
        self.marked_as_done_time = marked_as_done_time
        self.public_description = public_description
        self.location = location
        self.org_id = org_id
        self.person_id = person_id
        self.deal_id = deal_id
        self.active_flag = bool(active_flag)
        self.update_time = update_time
        self.update_user_id = update_user_id
        self.source_timezone = source_timezone
        self.lead_id = lead_id
        self.location_subpremise = location_subpremise
        self.location_street_number = location_street_number
        self.location_route = location_route
        self.location_sublocality = location_sublocality
        self.location_locality = location_locality
        self.location_admin_area_level_1 = location_admin_area_level_1
        self.location_admin_area_level_2 = location_admin_area_level_2
        self.location_country = location_country
        self.location_postal_code = location_postal_code
        self.location_formatted_address = location_formatted_address
        self.project_id = project_id
        
        
        
    def to_tuple(self):
        return (self.id,self.done,self.type,self.duration,self.subject,self.company_id,self.user_id,self.conference_meeting_client,self.conference_meeting_url,self.conference_meeting_id,self.due_date,self.due_time,self.busy_flag,self.add_time,self.marked_as_done_time,self.public_description,self.location,self.org_id,self.person_id,self.deal_id,self.active_flag,self.update_time,self.update_user_id,self.source_timezone,self.lead_id,self.location_subpremise,self.location_street_number,self.location_route,self.location_sublocality,self.location_locality,self.location_admin_area_level_1,self.location_admin_area_level_2,self.location_country,self.location_postal_code,self.location_formatted_address,self.project_id,)