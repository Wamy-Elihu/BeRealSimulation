from validation import validate_image

def publish_image(image):
    """
    Publie l'image si elle est valide.
    """
    if validate_image(image):
        print("Image publiée avec succès.")
    else:
        print("Échec de la validation de l'image. Publication annulée.")
        
publish_image(image)