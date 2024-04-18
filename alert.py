class AlertMessage:
    def show_alert(self):
        self.alert.setVisible(True)
        self.alert_title.setVisible(True)
        self.alert_text.setVisible(True)

    def hide_alert(self):
        self.alert.setVisible(False)
        self.alert_title.setVisible(False)
        self.alert_text.setVisible(False)