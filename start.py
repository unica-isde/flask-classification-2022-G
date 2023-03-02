import subprocess
subprocess.Popen("systemctl restart redis-server.service", shell=True)
import unittest
from tests import test_ml,test_queue,test_redis
import io
import contextlib



def start_test (test_name):
    """return test status"""
    outcome=""
    suite = unittest.TestLoader().loadTestsFromModule(test_name)
    with io.StringIO() as buf:
        # run the tests
        with contextlib.redirect_stdout(buf):
            unittest.TextTestRunner(stream=buf).run(suite)
        # process (in this case: print) the results
        a = []
        a.append(buf.getvalue())
        for x in a:
            if x.__contains__("OK"):
                outcome="YES"
            else:
                outcome="NO"
    return outcome

def selection():
    # the method returns the number of the selection made by the user
        s= input("Which test do you want start?\n"
                  "you can enter the relative number:\n"
                  "1 - Machine Learning\n"
                  "2 - Queue\n"
                  "3 - Redis\n"
                  "4 - All tests\n\n\n"
                 "If you do not want to start the tests but only start the Web Server, click on:\n"
                  "5 - Start  Web server for image classification\n\n"
                 "Clik on \"0\"  to Exit....\n")
        return s



def zero_selection ():
    print ("Exit...\n")
    return (0)

def one_selection():
    print ("Machine Learning test in course....\n")
    if (start_test (test_ml)=="YES"):
        print("Test is OK! Go on...\n")
        status="YES"
    else:
        print("Test is KO. Please verify ...\n")
        status="NO"
    return status

def two_selection():
    status=""
    print ("Queue test in course....\n")
    if start_test(test_queue)=="YES":
        print("Test is OK! Go on...\n")
        status="YES"
    else:
        print("Test is KO. Please verify setting file\n")
        status="NO"
    return status

def three_selection():
    print ("Redis Connection test in course....\n")
    if start_test(test_redis)=="YES":
        print("Test is OK! Go on...\n")
        status="YES"
    else:
        print("Test is KO... i try to fix redis server.\n")
        status = "NO"
        subprocess.Popen("systemctl restart redis-server.service", shell=True)
    return status

def four_selection():
    print ("All Tests start....\n\n\n")
    status_Machine_Learning_test=one_selection()
    status_Queue_test=two_selection()
    status_Redis_Connection_test= three_selection()
    status =[status_Machine_Learning_test,status_Queue_test,status_Redis_Connection_test]
    return status

def five_selection():
    print ("Web server for image classification starts....\n")
    subprocess.Popen("systemctl restart redis-server.service", shell=True)
    subprocess.Popen(
        "x-terminal-emulator -e \"python worker.py\" & x-terminal-emulator -e \"python worker_histo.py\" & x-terminal-emulator -e \"python runserver.py\"",
        shell=True)

def tests_selection ():
    sel=selection ()
    print ("Your selection is: ", sel,"... please wait...\n")

    if sel=="0":
       zero_selection()

    elif sel=="1":
        one_selection()
        tests_selection()

    elif (sel=="2"):
        two_selection()
        tests_selection ()

    elif (sel=="3"):
        three_selection()
        tests_selection ()

    elif (sel=="4"):
        four_selection()
        tests_selection ()

    elif (sel=="5"):
        five_selection()

    else:
        print ("Invalid selection. Please try again.\n")
        tests_selection()

tests_selection ()
