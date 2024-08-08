from plyer import notification

def send_notification(title, message, timeout):
    notification.notify(
        title=title,
        message=message,
        app_icon = "assets/PesuIcon.ico",
        timeout=timeout
    )
