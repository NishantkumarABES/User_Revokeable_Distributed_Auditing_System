
from collections import defaultdict

class ACL:
    def __init__(self):
        self.record = defaultdict(defaultdict(list))

    def remove_user(self, user_id):
        pass

    def add_user(self, user_id):
        pass

    def change_permission(self, user_id, file_id, mode):
        pass

    
    
