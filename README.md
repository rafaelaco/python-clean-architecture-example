# Tip
Run the following to create a virtual environment and install the dependencies:
- `python3 -m venv venv`
- `. venv/bin/activate`
- `pip3 install -r requirements.txt`

# Structure
- `domain/`: have the entites responsible to the most important business rules
- `application/`: have the application business rules and will use entities to fulfill the use cases
- `adapters/`: have the adapters to transform the external data to a format that works to the internal layers (business rule layers)
- `infrastructure/`: the external tools needed to make the platform work (frameworks, databases, etc)

# Flow
Web (infrastructure) -> Controller (adapters) -> Use Case (application) -> Entity (domain)

# Test
Run the project with `python3 main.py` and the command below in terminal or postman:
```
curl --location --request POST 'http://localhost:5000/input' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "Martin"
}'
```