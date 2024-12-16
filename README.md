# Diamond Price Prediction 👨🏻‍🔧

## Project Description: 👨‍🏫
- The "Grocery Store Management System" is a web-based application designed to automate and manage various aspects of a grocery store.
- This system allows store administrators to manage products and inventory efficiently, while customers can browse products, add items to their cart, and place orders online.
- The system provides a user-friendly interface for customers and a robust backend to ensure smooth operations.


## Backend Modules:
- **mysqlConn.py:** makes connection between Python and MySQL.
- **product.py:** Contains functions such as add product , remove product and retrieve the list of products.
- **cart.py:** Contains functions such as add item into cart , remove item from the cart and view cart items.
- **order.py:** Contains functions such as create order details and view order details.
- **app.py:** This is the main Python file that triggers the entire Web-Application. This file contains flask app , routing url functions and  APIs to communicate between frontend and backend.


## Frontend templates folder:
- **login.html:** User login page.
- **register.html:** User registration page.
- **home.html:** Home page of grocery store.
- **products.html:** Products page where user sees available products.
- **cart.html:** Cart page.
- **order.html:** Order page.


## Features:
**1. User Authentication & Session Management:**
- Implemented secure login and registration systems using Flask sessions, ensuring data integrity and user session management.
- Stored user credentials and information securely in the user table within the MySQL database.

**2. Product Management with Full CRUD Functionality:**
- Enabled administrators to perform CRUD operations (Create, Read, Update, Delete) on product data, allowing for easy management of the store’s inventory.
- Product details, including names, prices, and descriptions, are stored and managed in the product table.

**3. Shopping Cart with Real-Time Updates:**
- Developed a dynamic shopping cart system where users can add, update, or remove products, with changes reflected in real-time.
- The cart table in the database tracks all items added by each user, ensuring accurate order processing.

**4. Order Processing and Management:**
- Facilitated smooth order placement by integrating a comprehensive order management system, allowing users to review their cart items and finalize purchases.
- Implemented features to store and retrieve order details in the order table, with automatic total price calculation.

**5. Responsive and User-Centric Design:**
- Designed the frontend using Bootstrap to ensure the application is fully responsive and optimized for various devices, providing a consistent user experience across desktops, tablets, and smartphones.
- Created an intuitive user interface that enhances the shopping experience, making navigation and interaction effortless.

**6. Efficient Database Interaction with MySQL:**
- Connected the application to a MySQL database using a custom Python module (mysqlConn.py), enabling efficient data handling.
- Wrote optimized SQL queries to perform operations on the user, product, cart, and order tables, ensuring fast and reliable data processing.

**7. Seamless API Integration for Frontend-Backend Communication:**
- Built and integrated custom APIs to handle data requests and responses between the frontend and backend, enabling real-time data interaction and smooth user experiences.



## Tools and Technologies Used: 🛠

- **Frontend: HTML , CSS**
- **Programming Language: Python**
- **Web Framework: Flask** - Used for backend logic, routing URLs, and integrating with the frontend.
- **Machine Learning: Supervised Learning** - To predict the Diamond Price.


## Installation Instructions 🛣

1. Clone the repository:

```bash
  git clone <Paste repository link here>

```

2. Install dependencies:

```bash
  pip install -r requirements.txt
```




## Usage Instructions 🛣

1. Run the application:
```bash
  python app.py
```

2. Access the application:
- Open a web browser and go to http://localhost:5000 or http://127.0.0.1:5000.
- Enter the input values.
- Hit the submit button to get the estimated Diamond Price.


## Results: 🙌
Project Demo Link :
https://github.com/user-attachments/assets/7b42ce49-023c-4615-99ac-48062d5f1f2c

Webapplication Screenshots: 
  <img width="960" alt="Screenshot (3370)" src="https://github.com/user-attachments/assets/986885d6-61bb-46d3-bdad-06b66f35d4d4">
  <img width="960" alt="Screenshot (3371)" src="https://github.com/user-attachments/assets/50539574-e6f5-4883-b18b-3bc7552cced3">
  <img width="960" alt="Screenshot (3372)" src="https://github.com/user-attachments/assets/7d3b5dd0-e385-444a-be29-cd3794edf83a">



<div class="text-center">
  <h1>😍THANK YOU !😍</h1>
</div>

