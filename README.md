# OHTU Miniproject

## Development instructions
### Installation
1. Install [Poetry](https://python-poetry.org/)
2. Clone the repository `git clone https://github.com/ohtu-ryhma1/outin-bib.git`
3. Run `db_helper.py`: `poetry run python src/db_helper.py`
4. Define .env file in project root with following variables:
```
DATABASE_URL=
TEST_ENV=true
SECRET_KEY=
```
> DATABASE_URL: URI to postgreSQL database <br>
> TEST_ENV: Enables or disables resetting the database via /reset_db <br>
> SECRET_KEY: Defines Flask- secret key (unused) <br>

### Usage
1. Start the Flask server: `poetry run python src/index.py`
2. Server address is `http://localhost:5001/`

## Links
- [Product / Sprint Backlog](https://github.com/orgs/ohtu-ryhma1/projects/1)

- [CI](https://github.com/ohtu-ryhma1/outin-bib/actions/workflows/ci.yaml)
