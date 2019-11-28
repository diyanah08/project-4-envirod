# EviroD – Events Ecommerce
###### Project 4: Full Stacks Framework with Django - Code Institute
This website aims to sell seats for events as well as function as a way for users to book one of the three available venues for an event.

This website aims to create a community of environmentally aware individuals who will work together to take small steps to change their way of life and become more environmentally friendly.

## The website
A website can be found [here.](https://envirod.herokuapp.com/)

## UX
This website can be used by anyone who signs up and is interested in green initiatives.

Below are several user stories for the website:
- As the head of the company, I want to be able to get money through the sales of tickets for events so that I will be able to continue the non-profit initiative.
- As an environmental enthusiast, I want to be able to find events that will help me understand the environment better and learn more.
- As a company involved in environmental development, I want to be able to find a place to hold an event where I can share about the work that my company does.

Below is the detailed UX planning of the website from the Strategy to the Surface.

#### Strategy:
With environmental issues becoming more prominent, many are increasingly aware of the effects of what our actions can do. As such, more and more people are making a conscious effort to change their lifestyle.

However, not everyone knows where to start or what to do. This website aims to help people take the step in the right direction. It also helps to connect people to a community that have the same objectives. Having a community will encourage change and hence make the earth better.

#### Scope:
On the site educators will be able to:

- CREATE a new user and be able to login
- CREATE new enquiries to book a venue for an event.
- READ[search] through events that will be held by:
	- Description
	- Location
	- Tag/Theme
- UPDATE[edit] booking enquires, profile and password.
- DELETE booking enquiries.

The site will include:
- A database events from which users will be able to register for the events and make payment

Below is the database schema for the website.
- ![Database Schema](https://github.com/diyanah08/project-4-envirod/blob/master/static/images/envirod_database_schema.jpg) 


#### Structure:
The site will use Django with multiple apps with different views.py to display different pages.

A navigation link will be found at the top of the page for easy and intuitive navigation. The navigation varies before and after a user logs in.

Before login, the navigation will include:
- About Us
	- About
	- Location
- Login
	- Login
	- New User
- Browse

After login, the navigation will include:
- About Us
	- About
	- Location
- Profile
	- View Profile
	- Edit Profile
	- Change Password
- Events
	- Browse Events
	- Your Events History
	- Plan an Event
	- View Created Events
- Cart
- Logout

#### Skeleton:
On entering the site, the landing page will have a carousel of images and an instruction about the site.

A user can browse the events without login in by clicking the Browse navigation. The user however, will be unable to register for the event.

The user can login or register for an account by clicking the Login navigation and choosing either to login or register an account.

Once logged in, a user will be redirected to the events page. There, they can register for an event.

When the Register button on each event is clicked, it will be added to the Cart. For the cart, the user will be able to pay for the event.

Once paid, the user can view their Events History by clicking on the navigation bar Events and clicking the sub navigation Your Events History.

Additionally, the user can also plan an event by clicking the navigation Plan an Event and filling in a form for the admin to look through and get back to the user about.

The events created can be viewed, edited and deleted by clicking the navigation link View Created Events under the Events navigation.

#### Surface:
As the site is about the environment, it is styled with green and earthy colours. The fonts are fun and inviting so that users will feel comfortable navigating through the site.

## Features

### Existing Features
###### 1) Home Page & Footer
- On the landing page in a carousel of some images. Each photo comes with a caption related to the picture and the site. Below the carousel is and introduction to the site for users to know what they can do throughout the site.
- The footer for this site is the company’s name along with its slogan. The footer will be seen at the bottom of every page.

###### 2) Navigation Bar [Bootstrap]
- A navigation bar is located the top of every page to allow users quick navigation.
- The navigation bar has dropdown options to avoid too many links to be on it. It is also is collapsible to be mobile responsive.
- Navigations for before login are:
	1. About
        - about us
        - locations
	2. Login
        - login
        - register
	3. Browse
- Navigations after login in are:
	1. About
        - about us
        - locations
	2. Profile
        - view profile
        - edit profile
        - change password
	3. Events
        - browse events
        - view events history
        - plan an event,
        - view created events
	4. Cart
	5. Logout

###### 3) About Us/Locations:
- The About Us page has the company logo and a paragraph about the company.
- The Locations page has the addresses of the three location of the company.
- It also includes a mapbox map with popups.
- Each popup has the name, address and a link for directions. The link will open to a new page with the Google Map for directions. All the user have to do is type in their start location.

###### 4) Login/New User/Forget Password
On the login navigation, users can either login if they already have an account or register for an account.
- If a user clicks on the login option, the page will load a login form with the login button, the forget password button which will lead to the forget password page and a register for an account button, which will lead to the Register for an account page.

###### 5) Browse
Before a user login or register for an account, they are still able to browse through the catalog of events.
- The page only shows 3 events at the time to prevent overload of information.
- Pagination and Filters are used.

###### 6) View Events
Once a user logs in, the user can view all events or filter/search for the events. There are both the filter/search function as well as the pagination.

However, unlike the Browse Page, the user will be able to see the Register button. When clicked a Bootstrap Toast will appear

###### 7) Cart/Payment
The cart page will show the events that the user wants to register for. Here, the user can either remove an event from the cart or checkout and pay for the registered event. Stripe is used for processing of payment.

###### 8) View Events History
Once the user has successfully paid for an event, the events can be viewed in the View Events History page. A read more button shows and hides the details of the events.

###### 9) Plan an Event/View Created Event
This page consists of a form where users can create an event the they want to hold at EnviroD.
Once the created an event, they will be able to view, edit or delete is on the View Created Event Page

###### 10) View Profile/Edit Profile/Change Password
A user can view and edit his profile or change his password at these navigation links.

###### 11) Logout
When a user clicks the Logout navigation, he will be logged out and redirected to the home page.

### Features Left to Implement
1) A calendar view of the events that a user has registered for
2) Email reminders of events/recommended for you email based on events that have been registered by user before
3) Mapbox to be visible on Internet Explorer

## Technologies Used
- HTML
    - [BOOTSTRAP](https://getbootstrap.com/docs/4.3/getting-started/introduction/) was used for several components in the site.
- CSS
    - [GOOGLE FONTS](https://fonts.google.com/) used to provide a variety of fonts through out the site.
- Django/Python
- JavaScript
- [Stripe](https://stripe.com/)
	- Used to process payment
- [Mapbox](https://mapbox.com)
- [Mailgun](https://www.mailgun.com/)
	- Used to send emails for reset password
- AWS S3
	- Used for storage of static files
- GitHub
	- Used for version control 
- Heroku
	- Used for deployment

## Testing
For this project, no automated testing was used.
Instead, manual testing was conducted.

The steps were: 
###### 1) Loading the site to the Home Page

- On the landing page shows with carousel and captions related to the picture and the site. Below the carousel is and introduction to the site for users to know what they can do throughout the site.
- The footer for this site is the company’s name along with its slogan. The footer will be seen at the bottom of every page.

###### 2) Navigation Bar [Bootstrap]
- A navigation bar is located the top of every page to allow users quick navigation. Each navigation is clicked to ensure it loads the right pages.

###### 3) About Us/Locations
- The About Us page has the company logo and a paragraph about the company.
- The Locations page loads the mapbox.
- Each popup shows the address of the location.
- Each popup has a clickable directions link that will open to a google map direction page on a new tab.

###### 4) Login/New User/Forget Password
On the login navigation, users can either login if they already have an account or register for an account.
- If a user clicks on the login option, the page will load a login form with the login button, the forget password button which will lead to the forget password page and a register for an account button, which will lead to the Register for an account page.
- If a user enters an incorrect username or password, an error message will appear at the top of the page.
- The forget password page will load a form where users will have to type in the email they registered for an account from to reset the password. The user will receive an email and they have to follow the steps to reset the password.
- The New User page will load a form which user have to fill in a details such as first name, last name, email, address, username, password and so on
	- if a user enters an email or a username that has already been used and tries to create and account, an alert will show, prompting the user to use a different username or email
	- if a user enter a password that is too simple, the site will prompt the user to enter a different one
	- as the user has to enter the password chosen twice, if they do not match, there will be an error message.
- Once the registration is successful, the user is automatically logged in and redirected to the Home page with an alert at the top of the page.


###### 5) Browse
Before a user login or register for an account, they are still able to browse through the catalog of events.
- The page only shows 3 events at the time to prevent overload of information.
- Pagination is used and when the user clicks on next, last, first or previous, the events will load accordingly.
- Events can be searched/filtered by description, location and tags. They can do this by using the form that is above the events.
	- The user can use all three filters, two or any one of the filters to search
	- The user can also select multiple tags to search/filterby
- However, they will be unable to register for the event.
- Instead, they will see a Login to Register button at the bottom of each event.
- When clicked, the login page will be loaded.

###### 6) View Events
Once a user logs in, they will be redirected to the View Events page. Similar to the Browse page, the user can view all events or filter/search for the events. They is both the filter/search function as well as the pagination.

However, unlike the Browse Page, the user will be able to see the Register button.

- When the register button is clicked, the page will load with a bootstrap Toast on the top right-hand corner indicating what has been added to the cart/registered.
- From there, the user can checkout or close to register for more events.
	a) If the user clicks close, the page will redirect back to the view events page and a user can continue to register for events
	b) If a user clicks the checkout button, the user will be directed to the cart page.

###### 7) Cart/Payment
The cart page will show the events that the user wants to register for. Here, the user can either remove an event from the cart or checkout and pay for the registered event.
- If the user removes an event from the cart, the amount will decrease and if the user removes the event completely, there will be no more events in the cart
- If the user clicks the CheckOut button, the user will be directed to the payment page.
    - First, there will be an overview of the amount that the user has to pay.
	- Then when the user clicks Proceed to Payment, a form will load where the user has to fill up his details including the Credit Card Number, CVC Number and Date of Expiry of the card.

If a user keys in a wrong/invalid credit card/cvc number or an expired credit card, the payment will be unsuccessful and the page will load the payment form again with and error message at the top.

If the payment was successful, the page will load a thank you message.


###### 8) View Events History
Once the user has successfully paid for an event, the events can be viewed in the View Events History page by clicking the link under the Events dropdown navigation.
- There the user can see what they have registered for as the name of the event and an About Event button.
- When the button is clicked, the full information will be shown.
- When the button is clicked again, the full information will be hidden.

###### 9) Plan an Event/View Created Event
A user is able to plan an event with EnviroD. When the Plan an Event link is clicked, a page will load with a form. At the top of the form is a box with instructions.
- When a user tries to submit the form and the date or time format is wrong, there will be an error message at the top of the page.
- If the form is valid, the form will be submitted and there will be a success message at the top of the page and the page will redirect to the View Created Event Page.

- The View Created Event Page will have events that a user has created with all its details. At the bottom of each event, there will be an Edit and Delete button.
- If the user clicks on the Edit button, a form with the details of the event will be loaded and the user can edit and then click Save.
- If the user clicks the Delete button, a pop up will appear prompting the user to confirm the delete. If the user confirms, the page will refresh and show the remaining events created left.

###### 10) View Profile/Edit Profile/Change Password
A user can view his profile by clicking the link View Profile. The page will load all the user’s details that he has input during the registration of an account.
- On the view profile page is also an Edit Profile button and a Change Password button.
- When clicked, the page will load up forms with the details.
- If a user wants edits and saves his profile, the new profile will be shown after the Save button is clicked.
- Similarly, if the user wants to change his password, the change password page will load when he clicks Change Password and a form is rendered. Upon filling in and saving, the user will have changed his password.
- The Edit Profile and Change Password pages can also be reached by clicking the navigations in the dropdown navigation of Profile.

###### 11) Logout
When a user clicks the Logout navigation, he will be logged out and redirected to the home page with a success message at the top of the page.
The user will then only be able to see the Navigations for before login:
1. About
    - about us
    - locations
2. Login
    - login
    - register
3. Browse


##### The above steps for testing were done on:


| BROWSERS          | DEVICES                                    | TEST OUTCOMES                                                                                                                                                         |
| ----------------- |:------------------------------------------:| -------------------------------------------------------------------------:|
| Windows Edge      | Windows 10                                 | Testing appeared to pass                                                  |
| Google Chrome     | Windows 10, Samsung S9, Samsung Galaxy Tab | Testing appeared to pass                                 	             |
| Firefox           | Windows 10                                 | Testing appeared to pass                                                  |
| Safari            | iPhone 6 & 7, iPad Pro, MacBook Pro        | Testing appeared to pass                                                  |
| Samsung Internet  | Samsung S9, Samsung Galaxy Tab             | Testing appeared to pass                                                  |
| Internet Explorer | Windows 10                                 | Mapbox did not load up.						    						 |

###### Unfortunately, the issue reflected above have yet to be resolved at the point of submission.

## Deployment
This project was hosted through GitHub Pages.
- A GitHub repository was created for this project and titled ‘project-4-envirod.
- Throughout the project, regular commits were made when significant additions or edits were made.
- The commits were then pushed to the master branch of the repository.
- Heroku was then used to deploy the project.
- This was done by setting up a project in Heroku, moving the SQLite databased used in Django to Postgress and then a git push Heroku master command was done to deploy the site.
- Files for the project committed to GitHub can be pulled and run locally [here.](https://github.com/diyanah08/project-4-envirod)
- The link to the webpage can be found [here.](https://envirod.herokuapp.com/)

## Credits
#### Codes Acknowledgements
##### The following sites were used as reference codes to help in the project. Most of the codes used were edited to fit the context of the project.
- The back button javascript codes were gotten from [here.](https://www.w3schools.com/jsref/met_his_back.asp)
- The crispy-forms documentation were gotten from [here.](https://django-crispy-forms.readthedocs.io/en/latest/install.html)
- The Django pagination documentation were gotten from [here.](https://docs.djangoproject.com/en/2.2/topics/pagination/)
- The Django filters documentation were gotten from [here.](https://simpleisbetterthancomplex.com/tutorial/2016/11/28/how-to-filter-querysets-dynamically.html)



#### Media
- The photos used in this site were obtained from:
	- [PEXELS](pexels.com)
		Photo by Min An on Pexels
		Photo by Artem Beliaikin from Pexels
		Photo by Jatuphon Buraphon from Pexels
		Carousel Talk: Photo by 祝 鹤槐 from Pexels
	- Google images
		[Here](http://www.mylittlearchitect.com/en/exhibition-home-sweet-home-curated-by-my-little-architect/), [Here](https://www.lislelibrary.org/calendar/lisle-library-district-adult-discussion-groups) and [Here](https://www.experiencedays.co.uk/make-your-own-terrarium-workshop-in-worthing)
	- [Pony](https://ponyorm.org/) was used to create the database schema.