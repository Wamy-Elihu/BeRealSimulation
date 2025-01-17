import random
import datetime

def generate_random_time():
    try:
        start_time = datetime.datetime.combine(datetime.date.today(), datetime.time(9, 0))
        end_time = datetime.datetime.combine(datetime.date.today(), datetime.time(21, 0))
        random_time = start_time + datetime.timedelta(seconds=random.randint(0, int((end_time - start_time).total_seconds())))
        return random_time
    except Exception as e:
        print(f"Erreur lors de la génération de l'heure aléatoire : {e}")
        return None

def send_notification_to_user(user, notification_time):
    try:
        print(f"Notification envoyée à {user} à {notification_time}")
    except Exception as e:
        print(f"Erreur lors de l'envoi de la notification à {user} : {e}")

def send_notifications(users):
    notification_time = generate_random_time()
    if notification_time:
        for user in users:
            send_notification_to_user(user, notification_time)
    else:
        print("Impossible de générer l'heure de notification.")
        
generate_random_time()
send_notification_to_user(user, notification_time)
send_notification(users)
