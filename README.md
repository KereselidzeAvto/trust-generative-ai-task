# trust-generative-ai-task



### Install requirements 



```
pip install requirements.txt
```


```
python -m pytest .\Tests\buy_product_tests.py --alluredir=allure_report
python -m pytest .\Tests\registration_tests.py --alluredir=allure_report
```



### Allure report

```
allure serve .\allure_report\
```