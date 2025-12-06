# Django Matrix Testing

This repository uses **tox** to run tests against multiple Django versions to ensure compatibility and prepare for future Django upgrades.

## Django Versions Tested

The test matrix includes:

1. **Django 3.2.x** (Current) - Python 3.8
   - This is the current production version
   - Tests MUST pass for this version
   - Used for deployment decisions

2. **Django 4.2.x** (Current LTS) - Python 3.10
   - Long-term support until April 2026
   - Tests are informational only (can fail)
   - Helps identify upgrade blockers

3. **Django 5.2.x** (Future LTS) - Python 3.12
   - Long-term support until April 2028
   - Tests are informational only (can fail)
   - Helps plan for future migrations

## Running Tests Locally

### Prerequisites

Install tox:
```bash
pip install tox
```

Ensure PostgreSQL is running and accessible with the test database configured.

### Run All Matrix Tests

```bash
tox
```

### Run Tests for Specific Django Version

```bash
# Django 3.2 with Python 3.8
tox -e py38-django32

# Django 4.2 with Python 3.10
tox -e py310-django42

# Django 5.2 with Python 3.12
tox -e py312-django52
```

## GitHub Actions Integration

The CI workflow (`.github/workflows/ci.yml`) runs all three Django versions in a matrix:

- **Django 3.2**: Required to pass (blocks merge if fails)
- **Django 4.2**: Informational only (doesn't block merge)
- **Django 5.2**: Informational only (doesn't block merge)

This approach allows us to:
- Maintain stability with the current Django version
- Get early warnings about compatibility issues
- Plan upgrades proactively

## Tox Configuration

The `tox.ini` file defines:
- Test environments for each Django version
- Python version compatibility
- Database settings
- Dependencies specific to each Django version

## Known Issues

When running tests against Django 4.2+ and 5.2+, you may see compatibility errors such as:
- Deprecated API usage (e.g., `force_text` → `force_str`)
- Template library changes
- Package version incompatibilities

These are expected and help identify what needs to be fixed before upgrading Django.

## Next Steps

To upgrade to a newer Django version:
1. Review test failures for that version
2. Fix compatibility issues identified by the matrix tests
3. Update `requirements/base.txt` to the new Django version
4. Update the CI workflow to require the new version to pass
