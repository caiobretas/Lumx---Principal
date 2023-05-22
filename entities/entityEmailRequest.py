from datetime import datetime
from uuid import uuid4
class EmailRequest:
    def __init__(self,
        id=None,
        external_id=None,
        draft_id=None,
        email_id=None,
        datetime:datetime =None,
        request_type=None,
        contact_id=None,
        contact_name=None,
        from_=None,
        to_=None,
        subject=None,
        answered=False,
        atacchment=False,
        pending=False,
        concluded=False
        ):
        self.id = str(uuid4()) if id == None else id
        self.external_id = external_id
        self.draft_id = draft_id
        self.email_id = email_id
        self.datetime = datetime
        self.request_type = request_type
        self.contact_id = contact_id
        self.contact_name = contact_name
        self.from_ = from_
        self.to_ = to_
        self.subject = subject
        self.answered = answered
        self.atacchment = atacchment
        self.pending = pending
        self.concluded = concluded

    def __repr__(self) -> str:
        return f'Date: {self.datetime} - Request Type: {self.request_type} - To: {self.to_} - Concluded: {self.concluded}'
    
    def to_tuple(self) -> tuple:
        return (self.id, self.external_id, self.draft_id, self.email_id, self.datetime, self.request_type, self.contact_id, self.from_, self.to_, self.subject, self.answered, self.atacchment, self.pending, self.concluded)