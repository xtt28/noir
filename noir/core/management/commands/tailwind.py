import os
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """A Django CLI command that enables Tailwind development.
    
    Upon execution of the command through manage.py, the Tailwind CSS CLI will
    start watching for HTML file changes and rebuilding the output Tailwind CSS
    file.
    
    Attributes:
        help: A string that describes the command's function."""

    help = "Starts the Tailwind CSS development watcher."

    def handle(self, *args, **options):
        """Invoked upon execution of the command through the CLI.

        Starts watching for class changes and automatically rebuilds the CSS via
        the Tailwind CLI that has been installed by the pytailwindcss package.

        Args:
            args: The arguments passed to the command in the CLI.
            options: The options passed to the command in the CLI.
        """
        os.system("tailwindcss -i static/css/in.css -o static/css/out.css --watch")
