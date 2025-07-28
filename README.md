# Swansea Women's Aid Website

A full-stack charity website developed for Swansea Women’s Aid, built as part of the Level 5 Diploma in Web Application Development (Unit 4). This platform provides support and information for women and children experiencing domestic abuse, allowing users to read the latest news, donate securely, and get in touch through a simple contact form.

The site is designed with accessibility, user experience, and scalability in mind. It includes a secure CMS for staff to manage blog posts and a donation system integrated with Stripe. The project demonstrates full CRUD functionality, user authentication, relational database use, and clean, maintainable code.

---

## Table of Contents

- [Overview](#overview)
- [UX Design](#ux-design)
- [Features](#features)
- [Database Schema](#database-schema)
- [Technologies Used](#technologies-used)
- [Installation & Deployment](#installation--deployment)
- [Testing](#testing)
- [Bugs & Issues](#bugs--issues)
- [Future Enhancements](#future-enhancements)


## UX Design

The overall goal was to create a clean, accessible, and supportive online presence for Swansea Women’s Aid, prioritising ease of use for vulnerable users while also keeping things functional and manageable for staff.

### Login Placement

I moved the login link from the top navigation to the footer because the login area is only used by Swansea Women’s Aid staff. This helped simplify the main navigation and reduce any confusion for public users who don’t need to access it.

<details>
<summary><strong>Figma Designs</strong></summary>

#### Homepage Wireframe
![Homepage Wireframe](static/images/figma-home-wireframe.png)

#### High-Fidelity Mockup
![High Fidelity Homepage](static/images/figma-home-final.png)

#### Mobile Layout Example
![Mobile Mockup](static/images/figma-home-mobile.png)

</details>

---

<details>
<summary><strong>User Stories</strong></summary>

| As a...           | I want to...                                      | So that I can...                                  |
|------------------|---------------------------------------------------|---------------------------------------------------|
| Vulnerable user  | Access help quickly                               | Feel safe and supported                          |
| Public visitor   | Read about types of abuse                         | Understand the signs and know how to help others |
| Staff member     | Log in securely                                   | Update the site with latest news and info        |
| Donor            | Make a secure donation online                     | Support the charity’s mission                    |
| Volunteer        | See how I can get involved                        | Offer my time and skills to help                 |

</details>

---

### Design Decisions

*(To be added)*

---

### Accessibility Considerations

*(To be added)*


### Stripe Redirect URLs

After a little research, I found that using `request.build_absolute_uri()` was a better option than hardcoding my Stripe success and cancel URLs. It automatically generates the full URL based on the current environment (local or deployed), which meant I didn’t have to manually switch between localhost and Heroku URLs while testing. This made my Stripe integration more reliable and flexible.

## Features

- Responsive layout for desktop and mobile
- Informational homepage with support messaging
- Blog section with CRUD functionality for staff
- Secure login and logout via Django Allauth
- Donation form integrated with Stripe
- Contact form with success message confirmation
- Custom admin panel with user permissions
- 404 and 500 error pages

## Technologies Used

- Django 4.2 (Python 3.11)
- PostgreSQL (via Heroku)
- Bootstrap 5
- HTML5 / CSS3 
- Stripe API (for payments)
- Cloudinary (for image hosting)
- Git & GitHub
- Heroku (deployment)

## Installation & Deployment

### Local Installation

To run this project locally:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/charity-site-ms4.git
    cd charity-site-ms4
    ```

2. **Create a virtual environment** and activate it:
    ```bash
    python -m venv env
    source env/bin/activate  
    ```

3. **Install project dependencies**:
    ```bash
    pip install -r requirements.txt
    ```


4. **Create a `.env` file** in the root directory and add the following environment variables:

```env
SECRET_KEY=your_django_secret_key
STRIPE_SECRET_KEY=your_stripe_secret_key
DEBUG=True

These variables are used to keep sensitive information out of the codebase. The `.env` file is included in `.gitignore` and not committed to version control.

- `SECRET_KEY`: Required by Django for cryptographic signing and session management.
- `STRIPE_SECRET_KEY`: Used for processing payments securely via Stripe.
- `DEBUG`: Set to `True` in development. This should be overridden to `False` in production using Heroku config vars.


5. **Apply database migrations** and run the server:
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

---

## Deployment (Heroku)

The live site is deployed on [Heroku](https://swansea-womens-aid.herokuapp.com/), using PostgreSQL and Stripe integration for donation processing.

### Deployment Steps

1. **Created a Heroku app**:
    ```bash
    heroku create swansea-womens-aid
    ```

2. **Provisioned a PostgreSQL database** using Heroku's add-ons:
    ```bash
    heroku addons:create heroku-postgresql:hobby-dev
    ```

3. **Configured environment variables** in Heroku to keep sensitive information secure. The following variables were added via the Heroku dashboard:
    - `SECRET_KEY` – Django secret key
    - `STRIPE_SECRET_KEY` – Stripe test secret key used for donation payments

4. **Pushed the code to Heroku**:
    ```bash
    git push heroku main
    ```

5. **Applied migrations** and optionally created a superuser:
    ```bash
    heroku run python manage.py migrate
    heroku run python manage.py createsuperuser
    ```

6. **Disabled debug mode** by setting:
    - `DEBUG = False` in environment variables
    - Secret keys are **not** committed to the repo and are stored securely

---

### Static Files

- Static files are collected and served using **WhiteNoise**:
    ```bash
    python manage.py collectstatic
    ```

---

Let me know if your app uses:
- Cloudinary (for media)
- Any other env vars like `STRIPE_PUBLIC_KEY`  
I can update this again in seconds. You’re very close to having a submission-ready README!


## Testing

### Overview

Testing was carried out throughout development to ensure functionality, usability, and responsiveness. Due to time constraints and project scope, manual testing was the primary method used.

### Manual Testing

Manual tests were performed on all key features using a range of browsers (Chrome, Firefox, Safari) and devices (laptop, tablet, mobile). The following areas were tested:

| Feature                      | Test Performed                                                                 | Outcome        |
|-----------------------------|----------------------------------------------------------------------------------|----------------|
| Homepage                    | Checked responsiveness and link functionality                                   | Pass ✅         |
| Navigation bar              | Checked visibility, responsiveness, and active links                            | Pass ✅         |
| Blog list & detail pages    | Confirmed posts display correctly, with readable formatting                     | Pass ✅         |
| Admin blog functionality    | Staff users can create, edit, and delete posts via Django admin                 | Pass ✅         |
| Contact form                | Tested required fields and success message upon submission                      | Pass ✅         |
| Stripe donation form        | Verified with test card, handled success/cancel flows                           | Pass ✅         |
| User authentication         | Tested login, logout, restricted page access for unauthenticated users          | Pass ✅         |
| 404 / 500 error pages       | Triggered intentionally to confirm custom error pages are displayed             | Pass ✅         |
| Footer login link           | Confirmed visibility and restricted access only for staff                       | Pass ✅         |

### Stripe Testing

Stripe’s test environment was used with the following test cards:

- **Successful payment**: `4242 4242 4242 4242`
- **Declined card**: `4000 0000 0000 0002`

Both redirect flows and success messages were verified.


## Database Schema

The application uses a PostgreSQL database with three custom models: `Post`, `Donation`, and `ContactMessage`.

### Post Model

| Field        | Type               | Description                                 |
|--------------|--------------------|---------------------------------------------|
| `title`      | CharField          | Title of the blog post                      |
| `slug`       | SlugField (unique) | URL-friendly identifier                     |
| `content`    | TextField          | Body content of the post                    |
| `created_on` | DateTimeField      | Timestamp when post was created             |
| `author`     | ForeignKey to User | Link to Django’s built-in user model        |

Posts are ordered by `created_on` in descending order. Each post has a dynamic detail URL generated by its slug.

---

### Donation Model

| Field        | Type              | Description                                      |
|--------------|-------------------|--------------------------------------------------|
| `name`       | CharField         | Name of the donor                                |
| `email`      | EmailField        | Optional email address of the donor              |
| `amount`     | DecimalField      | Donation amount in GBP                           |
| `message`    | TextField         | Optional message left by the donor               |
| `timestamp`  | DateTimeField     | Time donation was made (default: now)            |

This model stores Stripe-processed donations for internal record-keeping.

---

### ContactMessage Model

| Field          | Type          | Description                                   |
|----------------|---------------|-----------------------------------------------|
| `name`         | CharField     | Name of the user submitting the message       |
| `email`        | EmailField    | Email address of the user                     |
| `message`      | TextField     | The message content                           |
| `submitted_at` | DateTimeField | Automatically set when message is submitted   |

Messages are handled via the site’s contact form and stored for admin review.
