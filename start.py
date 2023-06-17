import subprocess
import unittest
from tests import test_ml, test_redis, test_queue
import io
import contextlib


class TestRunner:
    @staticmethod
    def start_test(test_name):
        """return test status"""
        outcome = ""
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
                    outcome = "YES"
                else:
                    outcome = "NO"
        return outcome

    @staticmethod
    def selection():
        # the method returns the number of the selection made by the user
        s = input("Which test do you want to start?\n"
                  "You can enter the relative number:\n"
                  "1 - Machine Learning\n"
                  "2 - Queue\n"
                  "3 - Redis\n"
                  "4 - All tests\n\n\n"
                  "If you do not want to start the tests but only start the Web Server, click on:\n"
                  "5 - Start Web server for image classification\n\n"
                  "Click on \"0\" to Exit....\n")
        return s

    @staticmethod
    def zero_selection():
        print("Exit...\n")
        return 0

    @staticmethod
    def one_selection():
        print("Machine Learning test in progress....\n")
        if TestRunner.start_test(test_ml) == "YES":
            print("Test is OK! Go on...\n")
            status = "YES"
        else:
            print("Test is KO. Please verify ...\n")
            status = "NO"
        return status

    @staticmethod
    def two_selection():
        print("Queue test in progress....\n")
        if TestRunner.start_test(test_queue) == "YES":
            print("Test is OK! Go on...\n")
            status = "YES"
        else:
            print("Test is KO. Please verify setting file\n")
            status = "NO"
        return status

    @staticmethod
    def three_selection():
        print("Redis Connection test in progress....\n")
        if TestRunner.start_test(test_redis) == "YES":
            print("Test is OK! Go on...\n")
            status = "YES"
        else:
            print("Test is KO... trying to fix redis server.\n")
            status = "NO"
            subprocess.Popen("systemctl restart redis-server.service", shell=True)
            subprocess.Popen("service redis-server start", shell=True)
        return status

    @staticmethod
    def four_selection():
        print("All Tests starting....\n\n\n")
        status_Machine_Learning_test = TestRunner.one_selection()
        status_Queue_test = TestRunner.two_selection()
        status_Redis_Connection_test = TestRunner.three_selection()
        status = [status_Machine_Learning_test, status_Queue_test, status_Redis_Connection_test]
        return status


    @staticmethod
    def five_selection():
        print("Web server for image classification starting....\n")
        subprocess.Popen("systemctl restart redis-server.service", shell=True)
        subprocess.Popen("service redis-server start", shell=True)
        if(subprocess.Popen(
            "x-terminal-emulator",
            shell=True,stdout=True).returncode!=None):
            subprocess.Popen(
                "x-terminal-emulator -e \"python worker.py\" & x-terminal-emulator -e \"python worker_histo.py\" & x-terminal-emulator -e \"python runserver.py\"",
                shell=True)
        else:
            subprocess.Popen(
                "python3 worker.py & python3 worker_histo.py & python3 runserver.py",
                shell=True)

    @staticmethod
    def tests_selection():
        sel = TestRunner.selection()
        print("Your selection is: ", sel, "... please wait...\n")

        if sel == "0":
            return TestRunner.zero_selection()

        elif sel == "1":
            TestRunner.one_selection()
            TestRunner.tests_selection()

        elif sel == "2":
            TestRunner.two_selection()
            TestRunner.tests_selection()

        elif sel == "3":
            TestRunner.three_selection()
            TestRunner.tests_selection()

        elif sel == "4":
            TestRunner.four_selection()
            TestRunner.tests_selection()

        elif sel == "5":
            TestRunner.five_selection()

        else:
            print("Invalid selection. Please try again.\n")
            TestRunner.tests_selection()


TestRunner.tests_selection()
