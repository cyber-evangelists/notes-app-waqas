run_db:
dockerrun --name firstproject_postgres -p 5432:5432 -e POSTGRES_PASSWORD=waqas123HFD -e POSTGRES_DB=firstproject -v ${PWD}/db_data:/var/lib/postgresql/data -d postgres