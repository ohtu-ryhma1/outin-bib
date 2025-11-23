# BibTeX Reference Manager

[![Changelog](https://img.shields.io/badge/changelog-C3B091?style=for-the-badge)](CHANGELOG.md)
[![Product Backlog](https://img.shields.io/badge/product%20backlog-C3B091?style=for-the-badge)](https://github.com/orgs/ohtu-ryhma1/projects/1/views/1)
[![Sprint Backlog](https://img.shields.io/badge/sprint%20backlog-C3B091?style=for-the-badge)](https://github.com/orgs/ohtu-ryhma1/projects/1/views/4)
[![Sprint Burnup](https://img.shields.io/badge/sprint%20burnup-C3B091?style=for-the-badge)](https://github.com/orgs/ohtu-ryhma1/projects/1/insights/12) <br>
[![GitHub Actions](https://img.shields.io/github/actions/workflow/status/ohtu-ryhma1/outin-bib/ci.yaml?style=for-the-badge)](https://github.com/ohtu-ryhma1/outin-bib/actions/workflows/ci.yaml)
[![Codecov](https://img.shields.io/codecov/c/github/ohtu-ryhma1/outin-bib?style=for-the-badge)](https://codecov.io/gh/ohtu-ryhma1/outin-bib)
[![License](https://img.shields.io/github/license/ohtu-ryhma1/outin-bib?style=for-the-badge&color=C3B091)](LICENSE)
![Python Version](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Fohtu-ryhma1%2Foutin-bib%2Frefs%2Fheads%2Fmain%2Fpyproject.toml&style=for-the-badge&color=C3B091)

BibTeX Reference Manager is a tool for managing references using the BibTeX-format. It implements all official reference types and additional third-party/extended types.

## Development instructions

### Installation
1. Install [Poetry](https://python-poetry.org/)
2. Clone the repository `git clone https://github.com/ohtu-ryhma1/outin-bib.git`
3. Run `poetry install`
4. Create a .env file in the project root with the following variables:
```
PRODUCTION_DB_URL=<url>
TEST_DB_URL=sqlite+pysqlite:///:memory:
TEST_DB=true
SECRET_KEY=key
```
> PRODUCTION_DB_URL: connection string for production database <br>
> TEST_DB_URL: connection string for testing database (default: sqlite) <br>
> TEST_DB: use test database (default: true) <br>
> SECRET_KEY: define the Flask secret_key

### Usage
1. Start the Flask server: `poetry run invoke start`
2. The server address is: `http://localhost:5001/`

### Testing
- Run unit tests and coverage with `poetry run invoke coverage`
- To generate a coverage report, run `poetry run invoke coverage-report`
