# wiki
Hackerspace wiki

## Prerequisites

- Django-wiki (will downgrade Django to 1.6.11, handle with care)
```bash
$(sudo) pip install wiki
```

- South
```bash
$(sudo) pip install south
```

**You might also want** to use virtualenv for this, to keep the Django-admin Python environment separate from your normal environment.

## Installation instructions

1. Clone repo into wherever you want it
2. Sync the database
```bash
$python manage.py syncdb
$python manage.py migrate
```
**IMPORTANT:** This requires you have South installed, as it adds the migrate function and changes syncdb to accomodate it.
