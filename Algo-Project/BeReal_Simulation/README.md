BeReal Simulation Project

Ce projet simule certaines fonctionnalités clés de l'application BeReal. C'est un travail réalisé par James JACKSON et TCHIKAYA NDING Wamy-Elihu.

Pour ce faire, nous avons recourru a l'assistance de l'outil intelligent "TAK", un modèle de LLM monté par la boîte phospho.ai.
Nous nous en sommes notamment servi de cet outil pour savoir quelle structure serait la plus adaptée pour notre projet. 
Les codes ont tous été edité à la main avant d'être également vérifiés à l'aide de l'assistant de Mistral.ai, "Le chat", une intelligence artificielle très pratique en analyse de code et en support en cas de bug à corriger.

Nous avons choisi BeReal car nous aimions bien le fonctionnement de l'application et nous trouvions ça cool d'essayer de reproduire des intéractions de celle-ci.

Le code est structuré de manière modulaire pour faciliter la compréhension et la maintenance.

voici la Structure du Projet:

src/ : Contient le code source principal.

capture.py : Gère la capture d'images.

validation.py : Valide les images pour s'assurer qu'elles n'ont pas été modifiées.

notification.py : Génère et envoie des notifications à des heures aléatoires.

publication.py : Publie les images après validation.

main.py : Point d'entrée principal pour exécuter l'application.

tests/ : Contient les tests unitaires pour valider le fonctionnement du code.

test_validation.py : Tests pour la validation des images.


Quant aux Fonctionnalités Implémentées:

-Capture d'Image (capture.py)

capture_image(): Simule la capture d'une image brute, sans filtres ni modifications, pour reproduire l'expérience authentique de BeReal.

-Validation d'Image (validation.py)

validate_image(image): Vérifie que l'image capturée n'a pas été modifiée, en recherchant une signature spécifique dans les données de l'image.

-Publication d'Image (publication.py)

publish_image(image): Publie l'image si elle est validée avec succès, reproduisant ainsi le processus de partage authentique de BeReal.

-Notification Synchronisée (notification.py)

generate_random_time(): Génère une heure aléatoire pour l'envoi de notifications, simulant l'aspect spontané de BeReal.

send_notifications(users): Envoie des notifications à tous les utilisateurs à l'heure générée, encourageant la capture d'images en temps réel.


Exécution des Tests:

Pour exécuter les tests unitaires et vérifier le bon fonctionnement des fonctions, c'est la commande suivante :

python tests/test_validation.py