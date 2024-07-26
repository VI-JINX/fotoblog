from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from blog.models import Photo  # Assurez-vous d'importer correctement votre modèle Photo

def restore_permissions():
    try:
        content_type = ContentType.objects.get_for_model(Photo)

        # Permission 'change_photo'
        permission_change_photo = Permission.objects.create(
            codename='change_photo',
            name='Can change photo',
            content_type=content_type,
        )
        print(f"Permission 'change_photo' restored successfully.")

        # Permission 'delete_photo'
        permission_delete_photo = Permission.objects.create(
            codename='delete_photo',
            name='Can delete photo',
            content_type=content_type,
        )
        print(f"Permission 'delete_photo' restored successfully.")

        # Permission 'view_photo'
        permission_view_photo = Permission.objects.create(
            codename='view_photo',
            name='Can view photo',
            content_type=content_type,
        )
        print(f"Permission 'view_photo' restored successfully.")

    except Exception as e:
        print(f"Failed to restore permissions: {str(e)}")

# Appelez la fonction pour restaurer les permissions nécessaires
restore_permissions()
