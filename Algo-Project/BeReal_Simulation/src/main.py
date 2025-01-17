from capture import capture_image
from publication import publish_image
from notification import send_notifications

def user_interface():
    print("Capture d'une image...")
    image = capture_image()
    if image:
        publish_image(image)
    else:
        print("Impossible de capturer l'image.")

def notification_interface():
    users = ["Utilisateur1", "Utilisateur2", "Utilisateur3"]
    print("Envoi des notifications...")
    send_notifications(users)

if __name__ == "__main__":
    user_interface()
    notification_interface()