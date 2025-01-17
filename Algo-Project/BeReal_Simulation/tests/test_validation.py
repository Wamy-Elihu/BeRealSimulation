from validation import validate_image

def test_validate_image():
    assert validate_image("image_data_with_signature") == True, "Test échoué : L'image devrait être valide."
    assert validate_image("image_data_without_signature") == False, "Test échoué : L'image ne devrait pas être valide."
    assert validate_image(None) == False, "Test échoué : L'image ne devrait pas être valide."

if __name__ == "__main__":
    test_validate_image()
    print("Tous les tests de validation d'image ont réussi.")
    
test_validate_image()