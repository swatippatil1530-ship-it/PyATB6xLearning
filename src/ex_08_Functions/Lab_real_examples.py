#in API testing
def validate_status_code(response_code):
    if response_code == 200:
        print("request is successful")
    else:
        print("Error in request")
validate_status_code(200)
validate_status_code(404)
validate_status_code(response_code=100)
validate_status_code(input("enter your status code:"))
