## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Todo](#todo)

## General info
Website of hotel.
<br>
![image](![alt text](main_page.png))
	
## Technologies
Project is created with:
* Python version: 3.13.3
* Django version: 5.1.8
	
## Setup
1. **Clone the repository** to your local environment:
   ```bash
   git clone https://github.com/YourRepository.git
   cd YourRepository
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
     -Linux/MacOS:
     ```
     source venv/bin/activate
     ```
3. Install dependencies:
   In project folder:
   ```
   pip install -r requirements.txt
   ```
4. Add .env file with:
   ```
   SECRET_KEY="here_place_you_secret_key"
   DEBUG=True
   ```
   To get you SECRET_KEY run this command:
   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```
4. Start project local:
   ```
   python manage.py runserver
   ```
   The server will be available at: http://127.0.0.1:8000/


## Todo
- Home Page
    - Language selection
        Choose between English and Polish.

    Pages:
    - Rooms (Room presentation)
        List of rooms with description, price.
    - Reservation (Implement online reservation system)
        Integration with payment system module.
    - Information (Hotel information)
        Localization of hotel, history, contact.
    - Reviews (Opinions)
        Guest reviews (To add a review, a reservation must be made first. You will need to provide your name and reservation number).
    - Services (Optional for later)
        Additional services like spa or restaurant.

- Add payment system
    Implement payment system - maybe create bank system, and connect between them.
- Admin (Admin panel)
    Admin panel for managing reservations and content.
- Security (for later)
    Improve security.