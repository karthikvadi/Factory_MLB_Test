import unittest, csv
import HtmlTestRunner
import xmlrunner
from datetime import datetime



# the .py file name is Calculator and the class name is also Calculator
from MLB_Test import MLB_Test

# test data file path, the fils is a csv file.
test_data_file_path = './test_data.csv'
test_Output_data_file_path ='/Test_Output.csv'
# test data file object
test_data_file_object = None
test_Output_data_file_object =None
# test data row list.
test_data_row_list = list()
test_Output_data_row_list=list()
# load test data from ./test_data.csv file.
def load_test_data():
    global test_data_file_object, test_data_row_list
    # open test data csv file.
    test_data_file_object = open(test_data_file_path, 'r')
    # read the csv file and return the text line list.
    csv_reader = csv.reader(test_data_file_object, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        test_data_row_list.append(row)

    print('open and load data from test_data.csv complete.')
    
    
def load_Output_data_file():
    global test_Output_data_file_object, test_Output_data_row_list,csv_writer
    test_Output_data_file_object = open('Test_Output.csv', 'a') 
    # open test data csv file.
 
    # read the csv file and return the text line list.
    csv_writer = csv.writer(test_Output_data_file_object, delimiter=',')
    header = ['Date Time','DSN','Test_Name','Min','Max','Result','Unit','Pass/Fail']
    csv_writer.writerow(header)
 
    print('open Write to csv complete')


# close and release the test data file object.
def close_test_data_file():
    global test_data_file_object
    if test_data_file_object is not None:
        test_data_file_object.close()
        test_data_file_object = None
        print('close file test_data.csv complete.')
        
# close and release the test data file object.
def close_test_Output_data_file():
    global test_Output_data_file_object
    if test_Output_data_file_object is not None:
        test_Output_data_file_object.close()
        test_Output_data_file_object = None
        print('close file test_Output_data.csv complete.')

'''
This is the TestCase class that test MLB Test class functions.
'''
class TestMLB(unittest.TestCase):

    # this is the MLB class instance.
    MLB = None

    # class level setup function, execute once only before any test function.
    @classmethod
    def setUpClass(cls):
        load_test_data()
        load_Output_data_file()
        print('')
        print('setUpClass')

    # class level setup function, execute once only after all test function's execution.
    @classmethod
    def tearDownClass(cls):
        close_test_data_file()
        close_test_Output_data_file()
        print('')
        print('tearDownClass')

    # execute before every test case function run.
    def setUp(self):
        self.MLB_Test = MLB_Test()
        print('')
        print('setUp')

    # execute after every test case function run.
    def tearDown(self):
        # release the Calculator object.
        if self.MLB_Test is not None:
            self.MLB_Test = None
        print('')
        print('tearDown')
    def assertBetween(self, value, min, max):
        """Fail if value is not between min and max (inclusive)."""
        self.assertGreaterEqual(value, min)
        self.assertLessEqual(value, max)


    # below are function that test MLB_Test class's.
    def MLB_DVDD_12V0_V(self):
        
        Test_Name = ""
        
        # get each row text from the csv file.
        print('')
        
        for row in test_data_row_list:
            Test_Name = row[0]
            #print(Test_Name)
            if(Test_Name == 'DVDD_12V0_V'):
                Test_Name = row[0]
                print('******',Test_Name,'******')
                # the first column in the text line is x value.
                min_v = float(row[1])
                # the second column in the text line is y value.
                max_v = float(row[2])
                # the third column in the text line is Test Expected Value value.
                unit = row[3]
                PF , result = self.MLB_Test.DVDD_12V0_V(min_v, max_v)
                # datetime object containing current date and time
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                print(dt_string,'DSN',Test_Name ," Min: ", min_v ," Max: ",max_v, "Result:",result,unit,"Pass/Fail: " , PF)
                Output = dt_string,'DSN',Test_Name , min_v ,max_v,result,unit , PF
                
                csv_writer.writerow(Output)
                self.assertTrue(min_v <= result <= max_v)
                
                
    def DVDD_5V1_V(self):
        Test_Name = ""
        # get each row text from the csv file.
        print('')
        for row in test_data_row_list:
            Test_Name = row[0]
            #print(Test_Name)
            if(Test_Name == 'DVDD_5V1_V'):
                Test_Name = row[0]
                print('******',Test_Name,'******')
                # the first column in the text line is x value.
                min_v = float(row[1])
                # the second column in the text line is y value.
                max_v = float(row[2])
                # the third column in the text line is Test Expected Value value.
                unit = row[3]
                PF , result = self.MLB_Test.DVDD_5V1_V(min_v, max_v)
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                print(dt_string,'DSN',Test_Name ," Min: ", min_v ," Max: ",max_v, "Result:",result,unit,"Pass/Fail: " , PF)
                Output = dt_string,'DSN',Test_Name , min_v ,max_v,result,unit , PF
                csv_writer.writerow(Output)
                self.assertTrue(min_v <= result <= max_v)

        
    
    
    
   


def build_test_suite():
    # create unittest.TestSuite object.
    test_suite = unittest.TestSuite()
    # add each test function to the test suite object.
    test_suite.addTest(TestMLB('MLB_DVDD_12V0_V'))
    test_suite.addTest(TestMLB('DVDD_5V1_V'))
    # test_suite.addTest(TestMLB('AVDD_5V0_V'))
    # test_suite.addTest(TestMLB('DVDD_3V3_V'))
    # test_suite.addTest(TestMLB('AVDD_3V3_V'))
    # test_suite.addTest(TestMLB('DVDD_3V3_SW_V'))
    return test_suite

def build_text_report():
    test_suite = build_test_suite()
    # create unittest.TextTestRunner() object.
    test_runner = unittest.TextTestRunner()
    # run the test suite.
    test_runner.run(test_suite)

    # run below code to run all test function
    # unittest.main()

'''
# generate html report.
def build_html_report():
    test_suite = build_test_suite()
    test_runner = HtmlTestRunner.HTMLTestRunner(output='./html_report')
    test_runner.run(test_suite)

# generate xml result.
def build_xml_report():
    test_suite = build_test_suite()
    test_runner = xmlrunner.XMLTestRunner(output='./reports/xml_report')
    test_runner.run(test_suite)
# generate csv report.
def build_csv_report():
    test_suite = build_test_suite()
    test_runner = HtmlTestRunner.HTMLTestRunner(output='./html_report')
    test_runner.run(test_suite)
'''
if __name__ == "__main__":

    build_text_report()

    #build_xml_report()