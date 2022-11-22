class Message:
    def __init__(self, message_id, message, sender_id, receiver_id, read):
        self.message_id = message_id
        self.message = message
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.read = read
