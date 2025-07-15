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

*(To be added – colors, fonts, layout rationale)*

---

### Accessibility Considerations

*(To be added – contrast, font size, keyboard nav, etc.)*


### Stripe Redirect URLs

After a little research, I found that using `request.build_absolute_uri()` was a better option than hardcoding my Stripe success and cancel URLs. It automatically generates the full URL based on the current environment (local or deployed), which meant I didn’t have to manually switch between localhost and Heroku URLs while testing. This made my Stripe integration more reliable and flexible.
