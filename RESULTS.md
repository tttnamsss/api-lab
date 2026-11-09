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
  
## Part A - Step A4, status codes when the other user reads, changes and deletes: 
  
## Part B 
1. 
2. 
3. 
4. 
5. 
6. 
7. 
8. 