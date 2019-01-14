# myWebsite2


[![Build Status](https://travis-ci.com/ionescu77/myWebsite2.svg)](https://travis-ci.com/ionescu77/myWebsite2)

[![Coverage Status](https://coveralls.io/repos/github/ionescu77/myWebsite2/badge.svg?branch=master)](https://coveralls.io/github/ionescu77/myWebsite2?branch=master)

myWebsite2 is myWebsite upgraded & migrated to django 1.11.16 and python 3.6.7 (thanks @alexinntekt)

[you can also find the old read.me below]

- created a new github private repository
- added gitignore from the start
- added GNU GPL v3.0 license (you use it it remains open source, not closed source)
- extended this README


# myWebsite

#Notes to (mainly) myself:

Codul sursă de la site-ul meu, mereu în lucru.

Run coverage locally and generate nice html reports (in ./reports/coverage)
```
python3 src/manage.py jenkins --enable-coverage --coverage-format html blogengine
```

Run tests locally with jenkins (django style does not work anymore)

```
python3 src/manage.py jenkins blogengine
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
- adaugare Disqus pentru comentarii [Completed](https://github.com/ionescu77/myWebsite/issues/12)
- adăugare formular de contact
- css pt social icons
- code refactoring
- django i18n & localizare RO, DE, EN
- image credit
- CDN și alternativă la CDN pt boostrap, jquery
- publicare automată bookmark-uri folosind evernote API
- publicare imagini în articolele de blog
- optimizare SEO, meta și Structured Data Markup - schema.org
