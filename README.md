### Overview
This project shows an idea how one can use hooks and fixtures to generate meaningful reports when testing API.
At the end, PyTest should generate a report containing cURL of request and JSON of response in the HTML document. The whole magic happens in `tests/conftest.py` file via hooks and special debug fixture.
Obviously assertions are made to fail on purpose, so you can see the results.

### How this works
My main idea was to pass data about requests being processed in tests from tests themself to either reports or debug console.
Here's what happens in the repository:
- `TestBase` class has defined property `last_response`. Also this class contains assertion method that can validate response status code. Before assertion it assigns the response to `self.last_response` making it's value to be available globally.
- In `conftest.py` I've defined reporting hook that serves two functions: first it setts attributes with test status to be available for fixture to access it (necessary for console debug)
and second - it pulls `last_response` from test method parent (in this case TestBase) and puts this data to report HTML file generated. PyTest HTML report allows for using `extras` to put additional data to reports.
- Also in `conftest.py` there's `failure_report` fixture which checks if the test failed and if so - it prints debug information.

### Installation
Setup virtual environment for Python3 (https://docs.python-guide.org/dev/virtualenvs/). Then run Pip installation

`pip install -r requirements.txt`

### Running
Run tests using command

`pytest tests/ --html=report.html --self-contained-html`