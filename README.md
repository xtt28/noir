# noir

An anonymous online message board.

## Screenshots

![Post timeline](https://i.imgur.com/41rU9aB.png)
![Viewing a post](https://i.imgur.com/mAxFCXO.png)
![Creating a post](https://i.imgur.com/UrUkAED.png)
![Viewing your profile](https://i.imgur.com/X0iDuHm.png)

## Features

- Anonymously create posts
- Browse through posts with smooth infinite scroll
- Beautiful, responsive design

## Development

### Setting up

```shell
# Clone the repository with Git
git clone https://github.com/xtt28/noir.git

# Switch to the repository directory
cd noir

# Create a virtual environment
python3 -m venv .venv

# Use the virtual environment
source .venv/bin/activate

# Install the dependencies
pip install -r requirements.txt
```

### Usage

```shell
# Switch to the Django project directory
# (you will have run `cd noir` twice)
cd noir

# Set up your database
./manage.py migrate

# Run the development server
./manage.py runserver
```

#### How do I deploy a Django project?

Follow the Django [deployment checklist](https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/)
and run `manage.py check --deploy` to prepare your instance of the software for
deployment.

### Development with the Tailwind CLI

> Follow the instructions at <https://github.com/timonweb/pytailwindcss> to set
> up your development environment with Tailwind CSS.

Having completed the above, issue the following command while in the project
directory:
```shell
./manage.py tailwind
```

This will listen for Tailwind style changes and rebuild the CSS as necessary.

## Tech Stack

### Frontend

- Tailwind CSS
- htmx

### Backend

- Django
- SQLite (by default)