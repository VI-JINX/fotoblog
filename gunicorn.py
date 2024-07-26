import multiprocessing
import sys

# Nombre de travailleurs Gunicorn, ajustez selon vos besoins
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'gthread'  # Utilisez gthread pour les applications basées sur Python 3.x

# Adresse IP et port pour écouter les requêtes de Nginx
bind = '127.0.0.3:8000'  # Par exemple, écoute sur localhost:8001

# Fichiers d'erreur et de journalisation
# errorlog = '/var/log/gunicorn/error.log'
# accesslog = '/var/log/gunicorn/access.log'

# Activer le débogage si nécessaire
debug = False

# Gérer les demandes lentement pour éviter le blocage de Gunicorn
timeout = 30

# Configuration spécifique pour les applications Django
proc_name = 'fotoblog'  # Remplacez par le nom de votre projet Django

# Options supplémentaires selon vos besoins
# Redirection de la sortie vers le terminal
sys.stdout = sys.stderr

# Désactiver la redirection de la sortie
capture_output = False
