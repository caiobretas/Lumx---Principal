from uuid import uuid4
class PipedriveDealFields:
    def __init__(self,id,key,name,order_nr,field_type,json_column_flag,add_time,update_time,last_updated_by_user_id,edit_flag,details_visible_flag,add_visible_flag=None,important_flag=None,bulk_edit_allowed=None,filtering_allowed=None,sortable_flag=None,searchable_flag=None,active_flag=None,projects_detail_visible_flag=None):
            if id: self.id = int(id)
            else: self.id = int(str(uuid4()).replace('-', ''), 16)
            self.key = key
            self.name = name
            self.order_nr = order_nr
            self.field_type = field_type
            self.json_column_flag = json_column_flag
            self.add_time = add_time
            self.update_time = update_time
            self.last_updated_by_user_id = last_updated_by_user_id
            self.edit_flag = edit_flag
            self.details_visible_flag = details_visible_flag
            self.add_visible_flag = add_visible_flag
            self.important_flag = important_flag
            self.bulk_edit_allowed = bulk_edit_allowed
            self.filtering_allowed = filtering_allowed
            self.sortable_flag = sortable_flag
            self.searchable_flag = searchable_flag
            self.active_flag = active_flag
            self.projects_detail_visible_flag = projects_detail_visible_flag
    
    def __repr__(self):
        return f'ID: {self.id} - Tipo: {self.field_type}'
    
    def to_tuple(self):
        return (self.id,self.key,self.name,self.order_nr,self.field_type,self.json_column_flag,self.add_time,self.update_time,self.last_updated_by_user_id,self.edit_flag,self.details_visible_flag,self.add_visible_flag,self.important_flag,self.bulk_edit_allowed,self.filtering_allowed,self.sortable_flag,self.searchable_flag,self.active_flag,self.projects_detail_visible_flag)
    
class PipedriveDealFieldOptions:
    
    def __init__(self, dealField_id, id=None, label=None):
        self.id = id
        self.dealField_id = dealField_id
        self.internal_id = f'{id}{dealField_id}'
        self.label = label
    
    def __repr__(self):
        return f'Label: {self.label} - Id: {self.id} - DealFieldId: {self.dealField_id}'
    
    def to_tuple(self):
        return (self.id, self.dealField_id, self.internal_id, self.label)
        
    