## Bug Report – Heroku Deployment Issues

During the deployment phase of my Django project to Heroku, I ran into a few frustrating issues that slowed things down quite a bit. Initially, the app wouldn't build successfully. The error logs pointed to issues with static files and database configuration.

### What happened:
- Heroku threw a `ModuleNotFoundError` for `dj_database_url`, even though it was in my requirements.txt.
- I also forgot to run `collectstatic`, so static files weren’t displaying correctly after deployment.
- There were some environment variable mismatches — the `ALLOWED_HOSTS` setting and missing secret key caused an error on first launch.

### How I resolved it:
- I reinstalled all my dependencies into the virtual environment and double-checked that they were added to requirements.txt using `pip freeze > requirements.txt`.
- I added the necessary environment variables (like `SECRET_KEY`, `DATABASE_URL`, `DEBUG=False`) via the Heroku dashboard.
- I ran `python manage.py collectstatic` and committed the changes.
- Finally, I updated `ALLOWED_HOSTS` to include my Heroku app’s domain.

### Stripe Integration Issues:
Stripe integration issue was caused by the package not being installed in the virtual environment. Error shown was `ModuleNotFoundError: No module named 'stripe'`. Resolved by running `pip install stripe` inside the activated virtualenv. Stripe and its dependencies installed successfully.

### Stripe Integration Debug Summary

- Stripe gave an `UndefinedValueError` because it couldn’t find `STRIPE_SECRET_KEY`.
- The `.env` file does include `STRIPE_SECRET_KEY=sk_test_...` but Django wasn’t picking it up.
- Possible reasons I considered:
  - The `.env` file wasn’t in the same folder as `manage.py`
  - It wasn’t being loaded properly by `decouple`
  - The virtual environment might’ve needed a restart

- There was also a missing import:
  - `donation_thank_you` was imported in `core/urls.py` but didn’t exist in `views.py`

- I installed Stripe successfully with pip, but the project still failed due to the missing secret key.

### Resolution

- I realised the `.env` file was missing the `STRIPE_SECRET_KEY` line completely — I added it manually and restarted the server.
- After that, the app loaded correctly.

### Debug Summary: Post Timestamp Not Displaying

- I noticed that the post list was showing the title, snippet, and author, but **not the date and time**.
- I double-checked the template and saw it was using `{{ post.timestamp }}`—which looked right at first glance.
- But then I remembered the field in my `Post` model is actually called `created_on`, not `timestamp`.
- After changing the template line to `{{ post.created_on|date:"F j, Y, g:i a" }}`, the date and time showed up perfectly.
- Just one of those little naming mismatches that’s easy to overlook!