#######################################################################

## This script takes generated output (xml) from REQ test run
## and outputs a json file with REQ and its test status (PASS/FAIL).

#######################################################################
import json, os, math
import xml.etree.ElementTree as ET

def test_REQ(filename = 'test_REQ.json'):      
    # input xml (generated from test run)
    try:
        root = ET.parse('output.xml').getroot()
    except FileNotFoundError:
        raise FileNotFoundError("output.xml not found. JSON creation failed!")

    ## collect elements from xml generated from tests run
    # reqID               = root.findall('suite/suite')
    # reqStatus           = root.findall('suite/suite/status')
    testSuite           = root.findall('suite/suite/suite')
    testSuiteTestType   = root.findall('suite/suite/suite/doc')
    testSuiteStatus     = root.findall('suite/suite/suite/status')
    testSuiteDoc        = root.findall('suite/suite/suite/test/doc')
    testSuiteTag        = root.findall('suite/suite/suite/test/tag')    

    # clear existing json (if any)
    try:
        os.remove(filename)
        print("Cleared previous JSON file for test REQ info.")
    except OSError:
        pass
        

    # initialize json file
    with open(filename, mode='w') as file:
        json.dump({"tests":[]}, file, indent=4)
    
    # collect data from xml for addition to json file
    data = []
    for (testSuiteVal, testSuiteStatusVal, 
         testSuiteDocVal, testSuiteTagVal,
         testSuiteTestTypeVal) in zip(testSuite, testSuiteStatus, 
                                     testSuiteDoc, testSuiteTag, testSuiteTestType):
        # set data to append json object

        # Format hr:min:sec for start/finish time
        sec_val = math.floor(float(testSuiteStatusVal.get('start')[17:]))
        start_val = testSuiteStatusVal.get('start')[:17]+str(sec_val).zfill(2)

        val = {
            "testInfo": 
            {
                "projectKey":"",
                "summary":"SURS-"+str(testSuiteTagVal.text),
                "testType":testSuiteTestTypeVal.text,
                "definition":testSuiteVal.get('name'),
                "requirementKeys":[
                    testSuiteTagVal.text
                    ],
            },
            "start":start_val+'+00:00',
            "finish":start_val+'+00:'+str(math.ceil(float(testSuiteStatusVal.get('elapsed')))).zfill(2),
            "comment":testSuiteDocVal.text,
            "status":testSuiteStatusVal.get('status')
            }
        data.append(val)

    # write to json file
    with open(filename, mode='r') as file:
        file_data = json.load(file)
    file_data["tests"] = file_data["tests"] + data
    with open(filename, mode='r+') as file:
        json.dump(file_data, file, indent=2)
    print('Successfully written test REQ info to JSON file!')

## call test REQ for module
test_REQ()
