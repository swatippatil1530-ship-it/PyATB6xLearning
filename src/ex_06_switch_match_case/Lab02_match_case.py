print("enter the which test you want to run")
test_type = input("enter the test type: API,UI,PERFORMANCE,SECURITY: ")

match test_type:
    case "API":
        print("we are running POSTMAN API")
    case "UI":
        print("we are running Selenium UI")
    case "PERFORMANCE":
        print("we are running PERFORMANCE testing")
    case "SECURITY":
        print("we are running SECURITY testing")
    case _:
        print("invalid test type")