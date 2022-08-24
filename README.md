# Lab: 27 - Django Models

Go to http://127.0.0.1:8000/ to see the snacks list and click each list to see details.

Go to http://127.0.0.1:8000/drink to see the drink list and click each list to see details.

## Feature Tasks and Requirements
[snack_tracker_project](/snack_tracker_project/snack_tracker_project)

[snacks APP](/snack_tracker_project/snacks)

### Model
- [x] create snack_tracker_project project
- [x] create snacks app
- [x] Add snacks app to project
- [x] create Snack model
  - [x] make sure it extends from proper base class
  - [x] add name as a CharField with maximum length of 64 characters.
  - [x] add purchaser ForeignKey related to Django’s built in user model with CASCADE delete option.
  ``from django.contrib.auth import get_user_model``
  - [x] add description TextField
- [x] add model to admin
- [x] modify Snack model have user friendly display in admin
- [x] create migrations and migrate data
- [x] create a super user
- [x] run development server
- [x] Add a few snacks via Admin panel
- [x] create another user and more snacks via Admin panel
- [x] confirm that snacks behave as expected with proper name, purchaser and description.

### Views for Snacks App
- [x] create SnackListView
  - [x] extend ListView
  - [x] give a template of snack_list.html
  - [x] associate Snack model
- [x] update url patterns for project
  - [x] empty path should include snacks.urls
- [x] update snacks app urls
    - [x] empty sub-path should be handled by SnackListView
    - [x] Don’t forget to use as_view()
- [x] add detail view
  - [x] link snack_detail.html template
  - [x] associate Snack model

### Templates
- [x] Add templates folder in root of project
  - [x] register templates folder in project settings TEMPLATES section
- [x] create base.html ancestor template
  - [x] add main html document
  - [x] use Django Templating Language to allow child templates to insert content
- [x] create snack_list.html template
  - [x] extend base template
  - [x] use Django Templating Language to display each snack’s name
- [x] view home page (aka snack_list) and confirm snacks showing properly
- [x] create snack_detail.html template
  - [x] template should extend base
  - [x] content should display snack’s name, description and purchaser
- [x] add link in snack_list template to related detail page for each snack
- [x] Add a link back to Home (aka snack_list) page from detail page.
### User Acceptance Tests
- [x] Test Snack pages
  - [x] make sure test extends TestCase instead of SimpleTestCase used in previous class.
  - [x] verify status code
  - [x] verify correct template use
  - [x] use url name instead of hard coded path

### Stretch Goals
- [x] add styling
  - [x] create static folder at root of project
  - [x] update STATICFILES_DIRS
  - [x] create base.css file which styles base.html elements
  - [x] load static css in base.html file
- [x] Test SnackDetailView
- [ ] Test Snack model
- [x] add multiple models
- [ ] use an alternate test runner
- [ ] add more advanced fields to models, e.g. created time stamp