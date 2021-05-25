# myWebsite2

![Python](https://img.shields.io/badge/Python-3.6.8-blue)
![Django](https://img.shields.io/badge/Django-2.2.18-blue)
![Postgresql](https://img.shields.io/badge/Postgresql-10.6-blue)
![Build Status](https://github.com/ionescu77/myWebsite2/actions/workflows/ci.yml/badge.svg?branch=develop)
[![Coverage Status](https://coveralls.io/repos/github/ionescu77/myWebsite2/badge.svg?branch=master)](https://coveralls.io/github/ionescu77/myWebsite2?branch=develop)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/be6b62fc78134fe0998e0c3321372197)](https://www.codacy.com/gh/ionescu77/myWebsite2/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ionescu77/myWebsite2&amp;utm_campaign=Badge_Grade)
[![DeepSource](https://deepsource.io/gh/ionescu77/myWebsite2.svg/?label=active+issues&show_trend=true)](https://deepsource.io/gh/ionescu77/myWebsite2/?ref=repository-badge)

## About

myWebsite2 is myWebsite upgraded & migrated to django ~1.11.16~ 2.2.19 and python 3.6.7 (thanks @alexinntekt, @ionescu77)

[you can also find the old read.me below]

- created a new github private repository
- added gitignore from the start
- added GNU GPL v3.0 license (you use it it remains open source, not closed source)
- extended this README


## Environment
- environment variables needed:

```bash
# production
SECRET_KEY_IONESCU77="--some-key--"
export SECRET_KEY_IONESCU77
export DJANGO_SETTINGS_MODULE="ionescu77v2Project.settings.production"
DB_NAME_IONESCU77="--some-db-name--"
DB_USER_IONESCU77="--some-db-user--"
DB_PASS_IONESCU77="--some-db-pass--"
DB_PORT_IONESCU77="--some-db-port--"
export DB_NAME_IONESCU77 DB_USER_IONESCU77 DB_PASS_IONESCU77 DB_PORT_IONESCU77
```

# myWebsite

#Notes to (mainly) myself:

Codul sursă de la site-ul meu, mereu în lucru.

Run coverage locally and generate nice html reports (in ./reports/coverage)
```
python3 src/manage.py jenkins --enable-coverage --coverage-format html blogengine
```

Run tests locally with jenkins (django style does not work anymore)

```
python3 src/manage.py jenkins blogengine accounts
```
20181120

Workflow (using git hooks & shell scripts for deployment):
- dev -> local.txt -> virtualenv (python 3.6 & runserver)
- test -> staging.txt -> ionescu77.avproiect.com (python 3.6 & mod_wsgi)
- live -> production.txt -> ionescu77.com (python 3.6 & & mod_wsgi)

2016.03.08

Am zis să public codul poate asta mă motivează să îi dau bice și să încep să mai și scriu câte ceva.

2015.12.11


#Future sprints
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
