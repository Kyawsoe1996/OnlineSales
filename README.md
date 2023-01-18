# OnlineSales
Step
1. First python manage.py migrate
2. python manage.py createsuperuser
3. Go To Dashboard, and Register Products,Category,Warehouse,Stocks

4.To enable google login For Customer, You have to do the following setup
	On django Admin,   Go To Site
  On Admi add => http://localhost:8000
  ![image](https://user-images.githubusercontent.com/40347669/213112143-03d6d0c8-410a-4990-a7d9-c5db1e257889.png)
5. Create Site As follow
![image](https://user-images.githubusercontent.com/40347669/213111642-28679618-2a68-4f97-9abf-ba118c19497f.png)


6. And then Go to Social Accounts => Social Applications And Create Social application for Google.
  Make sure  you make available sites to add on choosen sites. Add client_id and secret from your google Oauth 
  And saved it. Now you can successfully login with google
![image](https://user-images.githubusercontent.com/40347669/213111697-a4662b58-56f8-44a4-8c31-ddb122b00c60.png)


