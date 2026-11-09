# API lab results 
  
## Part 0 
- Step 0.1, the number of pizza names: 243
- Step 0.3, status code of the request without a token: HTTP/1.1 401 Unauthorized
- Step 0.4, the name of your pizza: The Weak Carbonara
- Step 0.12, results of the three runs without a session (optional): all test are fail.
- Step 0.16, blocks of "how many of the three tools are excluded": 0, 1, 2, and 3 tools excluded
  
## Defect report 
- Title: Excluding all tools returns Internal Server Error (500)
- Request: POST /api/pizza with body {"excludedTools": ["Knife", "Pizza cutter", "Scissors"]}
- Expected result: Status code 400 with a JSON error message explaining that no pizza satisfies the request.
- Actual result: Status code 500 Internal Server Error
- Severity: Medium
  
## Part A 
- Step A4, status codes when the other user
    - reads: 404
    - changes: 400
    - deletes: 400 
  
## Part B 
1. Your tests talk to a real server over the internet. Name two kinds of failure that they can find and a unit test with stubs cannot. Then give one reason to write unit tests with stubs as well. 
</br><b><u>Answer</u></b> Internal server error and interface issues. write unit tests with stubs because it can run internal code quickly with out connect with internet

2. Why does every test create its own user with a new name, rather than use the public token? How will you apply the same idea to the shared shop or hotel in Project 2? 
</br><b><u>Answer</u></b> if we share token, other can edit while we testing. In project 2 create separate to prevent resource collision on shared systems.

3. Explain in your own words why the tests send every request through one session. If you did Step 0.12, describe what happened in your three runs.
</br><b><u>Answer</u></b> To preserve cookies (like AWSALB) so that requests consistently route to the same backend server behind the load balancer. step 0.12 without the session cookie, the load balancer routed requests to different servers that did not recognize the newly created user, leading to intermittent 401 Unauthorized failures (flaky tests).

4. Which block of the excluded tools revealed the defect in Step 0.16? Why is a 500 with an empty body worse for an app that calls the API than a 400 with a message? Why does the test stay in the suite as xfail instead of being deleted? 
</br><b><u>Answer</u></b> this block ["Knife", "Pizza cutter", "Scissors"]. status 500 gives the client application no helpful context. xfail keeps the test visible and tracks the known defect without failing the entire test suite, and will automatically fail when the developer fixes the bug due to strict=True.

5. How many tests does base choice coverage need for the model in Step A1, and how many would all combinations coverage need? Show how you counted. 
</br><b><u>Answer</u></b> base choice coverage = 9 tests (1 + (3-1) + (4-1) + (2-1) + (3-1)). all combinations coverage = 72 tests (3 * 4 * 2 * 3)

6. In Step A4, which status codes did you get when the other user read, changed and deleted the rating? Which codes would you expect? Is the difference a defect? Explain. 
</br><b><u>Answer</u></b> reads: 404, changes: 400, deletes: 400. expect between 400 and 499. No difference, because the system successfully blocked unauthorized access using a 4xx status code.

7. Create madeup.txt with the line Authorization: token 0000000000000000, a made-up token of 16 characters, and run the command below. What comes back? Is this a defect, and what could a stranger do with it on a real system? Only read with this token, and never create or change anything with it. 
curl -H "@madeup.txt" https://quickpizza.grafana.com/api/ratings
</br><b><u>Answer</u></b>  it return data back. it defect for security vulnerability allowing unauthorized strangers to read private data on a real system.

8. Name one thing that an API test checks better than a test through the web pages, and one thing that only a test through the web pages can check. 
</br><b><u>Answer</u></b> 
    - API test checks better: Response data structures, JSON schemas, HTTP status codes, and edge-case inputs at the backend level.
    - Web page test checks only: Visual layouts, user interface rendering, frontend client interactions, and end-user visual experience.