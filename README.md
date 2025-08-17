## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Todo](#todo)

## General info
Industrial Illusion Hotel Main Page
<br>
<br>
![alt text](https://github.com/Eiffo/Industrial_Illusion_Hotel/blob/main/Industrial_Illusion/static/img/main_page.png)
	
## Technologies
Project is created with:
* Python version: 3.13.3
* Django version: 5.1.8
* SQLite 3.49.2
* HTML5 + CSS3

	
## Setup
1. **Clone the repository** to your local environment:
   ```bash
   git clone https://github.com/Eiffo/Industrial_Illusion_Hotel
   cd Industrial_Illusion_Hotel
   ```
2. Create a virtual environment (optional):
   ```
   python -m venv venv
   ```
   * Activate on:
     - Windows:
	     ```
	     .\venv\Scripts\activate
	     ```
     - Linux/MacOS:
	     ```
	     source venv/bin/activate
	     ```
3. Install dependencies:
   In project folder:
   ```
   pip install -r requirements.txt
   ```
4. Add ".env" file with:
   ```
   SECRET_KEY="your_secret_key"
   DEBUG=True
   ```
   * To create .env file on:
      - Windows:
	     ```
	     echo SECRET_KEY="your_secret_key" > .env
	     echo DEBUG=True >> .env
	     ```
     - Linux/MacOS:
	     ```
	     echo 'SECRET_KEY="your_secret_key"' > .env
	     echo 'DEBUG=True' >> .env
	     ```
   
   To generate your SECRET_KEY run this command:
   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```
6. Start project locally:
   ```
   python manage.py migrate
   python manage.py runserver
   ```
   The server will be available at: http://127.0.0.1:8000/


## Todo
- [ ] Home Page:
    - [x] Language selection: 
        Choose between English and Polish.
<<<<<<< HEAD
=======
    - [ ] Translate everything: 
        Translete everything to English.
>>>>>>> 84ec26b (Language changes)

    Pages:
    - [x] Rooms (Room presentation): 
        List of rooms with description, price.
    - [x] Reservation (Implement online reservation system): 
        Integration with payment system module.
    - [x] Information (Hotel information): 
        Localization of hotel, history, contact.
    - [ ] Reviews (Optional): 
        Guest reviews (To add a review, a reservation must be made first. You will need to provide your name and reservation number).
    - [ ] Services (Optional for later): 
        Additional services like spa or restaurant.

- [ ] Add payment system: 
    Implement payment system - maybe create bank system, and connect between them.
<<<<<<< HEAD
- [ ] Admin (Admin panel): 
=======
- [x] Admin (Admin panel): 
>>>>>>> 84ec26b (Language changes)
    Admin panel for managing reservations and content.
- [ ] Security (for later): 
    Improve security.
