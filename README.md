# myWebsite2

![Python](https://img.shields.io/badge/Python-3.6.8-blue)
![Django](https://img.shields.io/badge/Django-3.2-blue)
![Postgresql](https://img.shields.io/badge/Postgresql-10.6-blue)
![Build Status](https://github.com/ionescu77/myWebsite2/actions/workflows/ci.yml/badge.svg?branch=develop)
[![Coverage Status](https://coveralls.io/repos/github/ionescu77/myWebsite2/badge.svg?branch=master)](https://coveralls.io/github/ionescu77/myWebsite2?branch=develop)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/be6b62fc78134fe0998e0c3321372197)](https://www.codacy.com/gh/ionescu77/myWebsite2/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ionescu77/myWebsite2&amp;utm_campaign=Badge_Grade)
[![DeepSource](https://deepsource.io/gh/ionescu77/myWebsite2.svg/?label=active+issues&show_trend=true)](https://deepsource.io/gh/ionescu77/myWebsite2/?ref=repository-badge)

## About

Personal blog and website built with Django 3.2 and Python 3.8+. Features a blog engine, static content pages, and modern UI with light/dark theme support.

**Recent Updates (Feb 2026):**
- ✨ Light/dark theme switcher (ongoing)
- 📝 New About Me and Services pages
- ⚡ Converted static pages from flatpages to direct views (40-70% faster)

## Features

- **Blog Engine**: Full-featured blog with categories, tags, and RSS feeds
- **Theme System**: User-selectable light/dark themes with persistent preferences
- **Static Pages**: Fast-loading About and Services pages (no database queries)
- **Admin Interface**: Django admin for content management
- **SEO**: Sitemap generation and structured URLs

## Testing

This project uses tox for testing across multiple Django versions. For detailed information about running tests and the Django matrix testing strategy, see [TESTING.md](TESTING.md).

### Test Matrix Status

| Python | Django | Status | Notes |
|--------|--------|--------|-------|
| 3.8 | 3.2 (current) | ✅ Passing | Production version |
| 3.10 | 4.2 (LTS) | ⚠️ Informational | Compatibility testing |
| 3.12 | 5.2 (future) | ⚠️ Informational | Forward compatibility |

Quick start:
```bash
# Install tox
pip install tox

# Run all matrix tests
tox

# Run tests for specific Django version
tox -e py38-django32   # Django 3.2 (current)
tox -e py310-django42  # Django 4.2 (current LTS)
tox -e py312-django52  # Django 5.2 (future LTS)
```

## Environment Variables

### Local Development
```bash
export SECRET_KEY_RAZ="--your-secret-key--"
export DJANGO_SETTINGS_MODULE="ionescu77v2Project.settings.local"
```

### Production
```bash
export SECRET_KEY_IONESCU77="--your-secret-key--"
export DJANGO_SETTINGS_MODULE="ionescu77v2Project.settings.production"
export DB_NAME_IONESCU77="--db-name--"
export DB_USER_IONESCU77="--db-user--"
export DB_PASS_IONESCU77="--db-password--"
export DB_PORT_IONESCU77="--db-port--"
```

## Development

### Run Coverage Reports
```bash
python3 src/manage.py jenkins --enable-coverage --coverage-format html blogengine
```

### Deployment Workflow
- **dev** → local.txt → virtualenv (Python 3.8 & runserver)
- **staging** → ionescu77.avproiect.com (Python 3.8 & mod_wsgi)
- **production** → ionescu77.com (Python 3.8 & mod_wsgi)

## Future Sprints

- [x] adaugare Disqus pentru comentarii [Completed](https://github.com/ionescu77/myWebsite/issues/12)
- [ ] adăugare formular de contact
- [x] css pt social icons
- [ ] code refactoring
- [ ] django i18n & localizare RO, DE, EN
- [x] image credit
- [ ] CDN și alternativă la CDN pt boostrap, jquery
- [ ] publicare automată bookmark-uri folosind evernote API
- [ ] publicare imagini în articolele de blog
- [ ] optimizare SEO, meta și Structured Data Markup - schema.org
- [ ] migrare la Wagtail, care rezolva si din punctele de mai sus: i18n, imagini, seo

## License

GNU GPL v3.0 - Open source license

---

*Personal blog by Răzvan Ionescu - Frankfurt am Main*
