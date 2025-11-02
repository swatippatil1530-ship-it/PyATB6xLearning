"""Q - You receive an API response code from your test script.
Write an if-else block to check whether the response is successful (status code 200) or not.

I/P response = 404 , O/P ❌ Failed API Request
I/P response = 200 , O/P ✅ Passed API Request
"""

#Q-1:
API_RESPONSE_CODE = int(input("Enter a response code from script: "))

if API_RESPONSE_CODE == 200:
    print("✅ Passed API Request")
elif API_RESPONSE_CODE == 404:
     print("❌ Failed API Request")
else:
    print("enter a valid response code from script!!")
