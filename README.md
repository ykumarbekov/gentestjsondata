**GENTESTDATA - Console utility to generate test data in JSON format based on input schema**
------------------------
run:
    python main.py options, or python main.py --h|help

program arguments:
    output-path: Output path for generated files
    file-name: file name uses as base name for generated files
    file-count: number of generated files, must be 0 or above
    file-prefix: prefix for generated files, can be - count, random or uuid
    schema: JSON schema, can be file or row passed as program argument
    data-lines: number of lines in generated files
    clear-output-data: remove previously generated files, based on base file name

By default utility reads configuration values from default.ini, which uses as initialization data and
can be used without non-obligatory parameters

running example:
python main.py --file-count=3 \
--file-prefix='uuid' \
--schema='{"date":"timestamp:", "name": "str:rand", "type":"['client', 'partner', 'government']", "age": "float:rand"}' \
--clear-output-data=1

Generated data

_{"date": 1573824466.167286, "name": "a20f05d8d82a4d878864c2bbd6feb4f2", "type": " partner", "age": "41"}_
_{"date": 1573824466.167349, "name": "901158261ab142dab9103d27854948fa", "type": "client", "age": "78"}_
...

Example of incorrect schema:

_{"date":"timestamp:", "name": "str:rand", "type":"['client', 'partner', 'government']", "age": "float:rand"}'_

WARNING - Number of processed elements: 3 doesn't equal actual elements: 4
As we see age cannot be float:random
------------------------

Using test cases:
run: python test_gentestdata.py -v

------------------------

- Short project structure:
1. main.py: Start main function - run process
2. argparser.py: Parsing, validation program arguments
3. processor.py: Run main process for generating and saving results to files
4. jsongendata.py: Additional class uses for parsing schema and generating output JSON row
5. tools.py: different useful functions