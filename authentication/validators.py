from django.core.exceptions import ValidationError

class ContainsLetterValidators:
    def validate(self, password, user=None):
        if not any(char.isalpha() for char in password):
            raise ValidationError('Le mot de passe doit contenir au moins une lettre', code  = 'password_no_letters')
        if not any(char.isdigit() for char in password):
            raise ValidationError('Le mot de passe doit contenir au moins un chiffre')
        
    def get_help_text(self):
        return 'Le mot de passe doit contenir au moins une lettre majuscule ou miniscule et un chiffre'
