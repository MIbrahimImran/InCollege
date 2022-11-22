class Settings:
    def __init__(self, sms_notifications=True, email_notifications=True, ad_notifications=True, language="English"):
        self.sms_notifications = sms_notifications
        self.email_notifications = email_notifications
        self.ad_notifications = ad_notifications
        self.language = language
