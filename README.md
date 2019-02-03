### Overview
This project shows an idea how one can use hooks and fixtures to generate meaningful reports when testing API.
At the end, PyTest should generate a report containing cURL of request and JSON of response in the HTML document. The whole magic happens in `tests/conftest.py` file via hooks and special debug fixture.
Obviously assertions are made to fail on purpose, so you can see the results.

### Installation
Setup virtual environment for Python3. Then run Pip installation
`pip install -r requirements.txt`

### Running
Run tests using command
`pytest tests/ --html=report.html --self-contained-html`