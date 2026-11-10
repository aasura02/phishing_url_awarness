## Test 1
Input: https://www.example.com/login
Expected: No listed warning signs found.
Actual: No listed warning signs found.
Status: PASS

## Test 2
Input: http://192.0.2.10/account
Expected: IP address and HTTP warnings.
Actual: IP address and HTTP warnings.
Status: PASS

## Test 3
Input: http://example.com@sample.invalid/login
Expected: @ symbol and HTTP warnings.
Actual: @ symbol and HTTP warnings.
Status: PASS 

## Test 4
Input: https://a.b.c.d.e.example.invalid/path
Expected: Many hostname segments warning.
Actual: URL has many hostname segments. Review carefully!
Status: PASS

## Test 5
Input: https://xn--example.invalid/
Expected: Punycode warning.
Actual: URL contains punycode. Review carefully!
Status: PASS
