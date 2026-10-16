<p align="center">
  <img src="media/school.png" alt="School Partner Directory logo" width="120">
</p>

# School Partner Directory

**A full-stack directory that connects schools with local businesses, nonprofits and government partners, built with Django.**
4th place of 32 teams, Coding & Programming, FBLA Canada National Leadership Conference 2024, after a live pitch and demo.

[Live demo](https://fbla2024.pythonanywhere.com) · [Report a bug](https://github.com/abtinmbm/FBLA2024/issues)

## Features

- **Self-serve partner management:** school staff add partners, programs and opportunities (internships, volunteering, career programs) through profile and resource-sharing modules, without needing a developer. Seeded with 25+ organizations.
- **Partner profiles** describing each organization's mission, services and areas of expertise.
- **Fast search** with Fuse.js fuzzy matching, so typos and partial names still find the right partner.
- **Rich content editing** with CKEditor 5, and reCAPTCHA on forms.
- **Responsive UI** with Tailwind CSS and jQuery.

## Tech stack

| Layer | Tools |
| --- | --- |
| Backend | Django, SQLite |
| Frontend | HTML, Tailwind CSS, jQuery, Fuse.js |
| Libraries | django-admin-interface, django-ckeditor-5, django-recaptcha |
| Hosting | PythonAnywhere (hosting, migrations, static files, production debugging) |

## Running locally

```bash
git clone https://github.com/abtinmbm/FBLA2024.git
cd FBLA2024
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata demo     # sample partners and programs
python manage.py runserver
```

Then open http://127.0.0.1:8000/.

To reset the local database from scratch (deletes all data):

```bash
rm db.sqlite3
python manage.py migrate && python manage.py loaddata demo
```

### Configuration

Secrets are read from environment variables. Without them the app runs in local development mode with Google's public reCAPTCHA test keys.

| Variable | Purpose |
| --- | --- |
| `DJANGO_SECRET_KEY` | Django secret key (required in production) |
| `DJANGO_DEBUG` | `1` for development (default), `0` for production |
| `RECAPTCHA_PUBLIC_KEY`, `RECAPTCHA_PRIVATE_KEY` | Your reCAPTCHA site keys |
