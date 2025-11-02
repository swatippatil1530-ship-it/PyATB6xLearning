"""
Q3
You want to check whether a web page loads within 3 seconds (performance test condition).

load_time = 4.2
⚠️ Page load too slow: 4.2 seconds
"""

page_load_time = float(input("Enter a page load time in seconds: "))
if page_load_time <=0:
    print("enter a valid page load time")
elif page_load_time < 3:
    print("web page load time is within 3 seconds")
else:
    print(" ⚠️ web page load time is too slow",page_load_time)