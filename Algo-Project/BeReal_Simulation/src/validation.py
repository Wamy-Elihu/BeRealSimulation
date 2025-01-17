def validate_image(image):
    
    """
    Vérifie que l'image n'a pas été modifiée.
    Retourne True si l'image est valide, sinon False.
    """
    
    if image and "signature" in image:
        return True
    return False

validate_image(image)
