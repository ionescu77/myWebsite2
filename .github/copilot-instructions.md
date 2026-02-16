# Copilot Instructions for myWebsite2

## Repository Overview

myWebsite2 is a personal blog and website built with **Django 3.2** and **Python 3.8+**, using **PostgreSQL 10.6** as the database. Features a blog engine, static content pages, and modern UI with light/dark theme support.

### Recent Updates (Feb 2026)
- ✨ Light/dark theme switcher with 7 accent color palettes
- 📝 New About Me and Services pages
- ⚡ Converted static pages from flatpages to direct views (40-70% faster)
- 🎨 Improved typography with modern system fonts
- 📱 Enhanced mobile responsiveness

### Features
- **Blog Engine**: Full-featured blog with categories, tags, and RSS feeds
- **Theme System**: User-selectable light/dark themes with persistent preferences
- **Static Pages**: Fast-loading About and Services pages (no database queries)
- **Admin Interface**: Django admin for content management
- **SEO**: Sitemap generation and structured URLs

### Technology Stack
- **Backend**: Django 3.2.x (production version)
- **Python**: 3.8 (current), with matrix testing for 3.10 and 3.12
- **Database**: PostgreSQL 10.6
- **Testing**: tox with Django matrix testing (3.2, 4.2, 5.2)
- **CI/CD**: GitHub Actions
- **Code Quality**: Coveralls, Codacy, DeepSource

## Project Structure

```
myWebsite2/
├── .github/
│   ├── workflows/        # CI/CD workflows (ci.yml, black.yml)
│   └── dependabot.yml    # Dependency management
├── src/                  # Main Django application
│   ├── manage.py         # Django management command
│   ├── blogengine/       # Main blog app
│   ├── accounts/         # User accounts app
│   ├── landing/          # Landing page app
│   ├── ionescu77v2Project/ # Project settings
│   │   ├── settings/     # Environment-specific settings (local, staging, production, test)
│   │   └── urls.py       # URL configuration
│   └── templates/        # Django templates
├── requirements/         # Python dependencies
│   ├── base.txt          # Base dependencies
│   ├── local.txt         # Local development
│   ├── production.txt    # Production
│   └── test.txt          # Testing
├── tox.ini               # Tox configuration for matrix testing
├── passenger_wsgi.py     # WSGI entry point
├── README.md             # Project documentation
└── TESTING.md            # Testing documentation
```

## Building and Testing

### Environment Setup

**Required Environment Variables:**
```bash
# Local development
export SECRET_KEY_RAZ="--some-key--"
export DJANGO_SETTINGS_MODULE="ionescu77v2Project.settings.local"

# Production
export SECRET_KEY_IONESCU77="--some-key--"
export DJANGO_SETTINGS_MODULE="ionescu77v2Project.settings.production"
export DB_NAME_IONESCU77="--some-db-name--"
export DB_USER_IONESCU77="--some-db-user--"
export DB_PASS_IONESCU77="--some-db-pass--"
export DB_PORT_IONESCU77="--some-db-port--"
```

### Testing

**ALWAYS use tox for running tests.** This project uses Django matrix testing.

**Test Matrix Status:**

| Python | Django | Status | Notes |
|--------|--------|--------|-------|
| 3.8 | 3.2 (current) | ✅ Required to pass | Production version |
| 3.10 | 4.2 (LTS) | ⚠️ Informational only | Compatibility testing |
| 3.12 | 5.2 (future) | ⚠️ Informational only | Forward compatibility |

**Installation:**
```bash
pip install tox
```

**Run all matrix tests:**
```bash
tox
```

**Run tests for specific Django version:**
```bash
# Django 3.2 (current production) - MUST PASS
tox -e py38-django32

# Django 4.2 (informational only)
tox -e py310-django42

# Django 5.2 (informational only)
tox -e py312-django52
```

**Important Notes:**
- Only **Django 3.2** tests (py38-django32) are required to pass
- Django 4.2 and 5.2 tests are informational (can fail)
- Tests require PostgreSQL to be running
- Database migrations run automatically before tests via `commands_pre` in tox.ini

### Manual Testing (Alternative)

For quick testing without tox:
```bash
cd src
export SECRET_KEY_RAZ="test§$%§$§%"
export DJANGO_SETTINGS_MODULE="ionescu77v2Project.settings.test"
python manage.py test blogengine accounts
```

### Coverage Reporting

Generate coverage reports locally:
```bash
cd src
python manage.py jenkins --enable-coverage --coverage-format html blogengine
```
Reports are generated in `./reports/coverage`

## CI/CD Workflows

### GitHub Actions

**Main CI Workflow** (`.github/workflows/ci.yml`):
- Runs on pull requests and pushes to `develop` branch
- Matrix testing with Django 3.2, 4.2, and 5.2
- PostgreSQL service container on port 5432
- Coverage upload to Coveralls (Django 3.2 only)
- **Required check**: Only Django 3.2 tests must pass

**Black Formatter** (`.github/workflows/black.yml`):
- Code formatting checks

## Development Guidelines

### Code Changes
- Make changes in the `src/` directory
- Follow existing Django patterns and conventions
- Test changes with `tox -e py38-django32` before committing
- Run database migrations if models change: `python src/manage.py migrate`

### Django Apps
1. **blogengine**: Main blog functionality (posts, comments, categories, tags, RSS feeds)
2. **accounts**: User authentication and account management
3. **landing**: Landing page functionality (About, Services pages with theme switcher)

### Settings Files
- `base.py`: Shared settings across all environments
- `local.py`: Local development settings
- `test.py`: Test environment settings
- `staging.py`: Staging environment settings
- `production.py`: Production environment settings

### Database Configuration
- Database settings are in `database_production.py` and `database_staging.py`
- Test database is configured in tox.ini (github-actions database)

## Common Tasks

### Running the Development Server
```bash
cd src
export SECRET_KEY_RAZ="your-key"
export DJANGO_SETTINGS_MODULE="ionescu77v2Project.settings.local"
python manage.py runserver
```

### Creating Migrations
```bash
cd src
python manage.py makemigrations
python manage.py migrate
```

### Installing Dependencies
```bash
# For local development
pip install -r requirements/local.txt

# For testing
pip install tox
```

## Key Constraints and Conventions

1. **ALWAYS run tox tests** before considering changes complete
2. **Django 3.2 is the current production version** - changes must be compatible
3. **PostgreSQL is required** for testing and development
4. **Disable pagers** when using git commands: `git --no-pager status`
5. **Environment variables are required** for running the application
6. **Tests are located** in `tests.py` files within each app directory
7. **Coverage threshold**: Monitor coverage but specific threshold not enforced

## Validation Steps

Before finalizing any code changes:
1. Run `tox -e py38-django32` to ensure Django 3.2 compatibility
2. Check that no syntax errors exist
3. Verify database migrations are created if models changed
4. Ensure code follows existing patterns in the codebase
5. Check that environment variables are documented if new ones are added

## Troubleshooting

### Common Issues
- **Tox fails**: Ensure PostgreSQL is running and accessible
- **Import errors**: Check that all dependencies are in requirements files
- **Test database errors**: Verify DATABASE_NAME, DATABASE_USER, DATABASE_PASSWORD are set
- **Migration conflicts**: Run `python manage.py migrate` to resolve

### Build Time Expectations
- Tox tests: ~2-5 minutes depending on the environment
- Database migrations: ~10-30 seconds

## Deployment Workflow

- **dev** → local.txt → virtualenv (Python 3.8 & runserver)
- **staging** → ionescu77.avproiect.com (Python 3.8 & mod_wsgi)
- **production** → ionescu77.com (Python 3.8 & mod_wsgi)

## Additional Notes

- The project uses mod_wsgi for staging and production deployments
- Deployment workflow uses git hooks and shell scripts
- Project has been migrated multiple times (Python 2 → Python 3, Django 1.x → 3.2)
- Future upgrades to Django 4.2+ are being monitored via matrix testing
- Code quality is monitored by Codacy and DeepSource
- Static pages (About, Services) were converted from flatpages to direct views for better performance
