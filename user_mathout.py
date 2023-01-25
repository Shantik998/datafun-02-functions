e_code
    _run_code(code, mod_globals, init_globals,
  File "/Users/shantikandel/.vscode/extensions/ms-python.python-2023.1.10091012/pythonFiles/lib/python/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_runpy.py", line 124, in _run_code
    exec(code, run_globals)
  File "/Users/shantikandel/datafun_project2/datafun-02-functions/user_math.py", line 104, in <module>
    print(f"sales of products based on product size ={sales_of_product(12, 30, 32)}")
TypeError: sales_of_product() missing 1 required positional argument: 'operating_expenses'
(base) Shantis-MacBook-Pro:datafun-02-functions shantikandel$  cd /Users/shantikandel/datafun_project2/datafun-02-functions ; /usr/bin/env /usr/bin/python3 /Users/shantikandel/.vscode/extensions/ms-python.python-2023.1.10091012/pythonFiles/lib/python/debugpy/adapter/../../debugpy/launcher 51820 -- /Users/shantikandel/datafun_project2/datafun-02-functions/user_math.py 
your code here
Explore some functions in the math module

math.comb(5,1) = 5
math.perm(5,1) = 5
get_area_of_lot(6, 2) = 12

number of defect product produced per hour =24

sales of products based on product size =126

revenue after deducting discount= 390.72