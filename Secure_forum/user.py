from flask_login import UserMixin
class User(UserMixin):
   def __init__(self,userid):
      self.id = userid
   
   def get_id(self):
      return (self.id)