# Reel Reviews

Reel Reviews is a film review website where users can search for a film by its title, receive information about that film (the poster image, title, release date, and description) and then rate and review it. The user can create, edit, and delete film lists, along with creating, editing and deleting film reviews. The website was developed mobile first but is fully responsive on all standard screen sizes. 

![Image of my responsive website](#)
[Link to the deployed site](#)

## Contents 

* [User Experience (UX)](#user-experience-ux)
  * [Project Goals](#project-goals)
  * [Developer and Business Goals](#developer-and-business-goals)
  * [User Stories](#user-stories)
* [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Typography](#typography)
  * [Icons and Images](#icons-and-images)
  * [Features](#features)
  * [Accessibility](#accessibility)
  * [Wireframes](#wireframes)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries-and-programs-used)

* [Deployment](#deployment)
  * [Local Deployment](#local-deployment)

* [Testing](#testing)
  * [Automated Testing](#automated-testing)
    * [W3 Nu HTML Validator](#w3-nu-html-validator)
    * [W3C CSS Validation Service](#w3c-css-validation-service)
    * [Wave](#wave-testing)
    * [Lighthouse](#lighthouse-testing)
    * [JS Hint](#js-hint)
  * [Manual Testing](#manual-testing)
  * [Bugs](#bugs)

* [Credits](#credits)
  * [Code Sections](#code-sections)
  * [Media](#media)
  * [Text](#text)
  * [Acknowledgements](#acknowledgements)

## User Experience (UX)
### Project Goals
The focal goal for Reel Reviews is to allow users to successfully register an account, log in to the site and be able to not only receive information about films they search, but also to be able to rate and review these films. 

* The site allows users to enter their own unique username, their email and password in order to register for an account, this username and password are then used to log in. Once logged in the user is brought to the Search page to encourage them to begin searching for and reviewing films they've watched. They are greeted with a personalised message saying 'Welcome (your username)' along with a Flash message confirming that they have been successfully logged in
* Users are required to add a Film List before they can submit any film reviews, this is done easily with the user being able to provide a list name, and optionally a genre if they wish to.
* When a user enters a film title into the search bar all films available that match that search term will be displayed on screen, depending on screen size the films will be shown with 1, 2, or 3 films per row. These film cards provide the poster image, title, release date, and description of the film in an accordion to avoid excess information cluttering the screen. A Review button sits at the bottom of each film card encouraging users to give their opinion about films they have seen.
* When this Review button is clicked the user is taken to a review form in which they are prompted to fill in the title of the film they wish to review, their star rating, and which Film List they would like to add this review to. They also have the option of providing a written review of the film, but this is not required. After submitting their film review users are brought to the My Reviews page where they can view all of their reviews, sorted by best to worst rated.

### Developer and Business Goals 
* The footer of the site contains social media links for Facebook, Twitter, and Instagram to encourage users to share their reviews with other online, ultimately with the goal of promoting the website to others
* A key developer goal for this site was to focus on full accessibility for users, whether that being accessibility in terms of being able to have a great user experience no matter what device they use. Or accessible in terms of those with different needs, such as screen readers, being able to access and enjoy the site


### User Stories
As a user I want to be able to...
1. Quickly and easily register for an account, and then log in to my account. If any issues occur such as me choosing a username that is already in use when registering, or typing in the wrong password when loggin in I want to be given a specific warning to allow me to fix my mistake
2. I want to be able to use the site on desktop, and mobile devices so I can share my reviews with friends while out, or even write out reviews while on my way home from the cinema. I want to have the same quality of experience no matter the device type or size
3. I want a large and broad selection of films available to be able to review, if the site doesn't have most of the films I want to review then there is no point in me using it
4. I want to be able to edit or delete my film lists or reviews whenever I choose to do so
5. I want the site to look aesthetically pleasing, but more importantly for everything to be readable, and easily navigable without confusion or specific instructions necessary

## Design
### Colour Scheme

![Image of colour scheme](/filmreview/docs/M3.png)
The predominant colour scheme of this site is grey and blue tones, with aspects of green denoting that a button being hovered over should be clicked. 

* The grey, blue tones were inspired by the aesthetic design of the film review site [LetterBoxd](https://letterboxd.com/) as I wanted a background to be reminiscient of the darkness of a cinema setting but also allow the colours of the film poster images to pop against the dark grey background.
* White is used for text throughout the site as it is easily readable against the dark grey background and navbar, and white draws the eye meaning that users are reading any information they need to know
* The Favicon and brand logo is a light yellow and pink icon of a film reel as I wanted the colours of this to really stand out against the grey of the site, and the other tabs in a users browser 

### Typography

[Google Fonts](https://fonts.google.com/) provided the fonts I used on my site
![Image of Navbar Title font](/filmreview/docs/limelight.png)
* Limelight is the font used for my navbar title, this is a Sorkin type font that is a rendition of more typical sans-serif fonts. I selected this as my title font as it's very visually evocative of cinema and film typography which fits the theme of my site and conveys that theme to the user

![Image of body font](/filmreview/docs/Noto-Sans-Japanese.png)
* The body of my site is all Noto Sans Japanese font, this font is also a sans-serif which maintains consistency throughout the typography used. I chose this font primarily for its readibility as I want users to always be able to clearly read all text, along with its sleek and classic font style.

### Icons and Images

* I created a Favicon for this site using the png converter on the [Favicon](https://favicon.io/) website as I couldn't find an icon of a film reel on sites like FontAwesome. The film reel logo and favicon easily conveys the theme of the site to users and adds a pop of colour to draw the eye when amongst many others tabs in a users browser bar. The icon itself was sourced from [Flaticon](https://www.flaticon.com/) and will be attributed to its individual creator in the credits section of this document.
* All icons used throughout the site were provided by [FontAwesome](https://fontawesome.com/)
* The image on the index page was created by myself by sourcing popular film poster images (that will be individually attributed in the credits section) and splicing these together to create a banner like effect to showcase different films available on the site


### Features
The Reel Reviews website is comprised of 7 different sections, Home, Signup, Login, Search, Add Film Review, My Reviews, My Film Lists

| Section | Feature | Photograph or gif |
| --- | --- | --- |
| The Home page appears on page load and welcomes the user to the site, it features a triptych of film poster images along with basic information about what users can do on the site | The user is welcomed to the site and immediately sees the 3 poster images which aim to draw the user in and provide a great pop of colour to the home page | ![Index welcome image](/filmreview/docs/index-welcome.png) |
| | The home page feature description section introduces the user to the capabilities of the site in an easily digestible way so that users are aware of what they can do | ![Index feature description](/filmreview/docs/index-features.png) | 
| The Signup page allows users to enter their details to create an account | The user must enter a username, their email and password to signup | ![Sign Up form](/filmreview/docs/signup-form.png) |
| | There is a limit to how long a username can be, and all fields must be filled in otherwise a warning will display that this must be completed. The password a user provides is hashed using Werkzeug security so that all information is secure | ![Sign up form warning](/filmreview/docs/signup-form-warning.png) |
| | The username a user adds must be unique, and so if they attempt to register with a username that is already taken they will receive a Flash message warning | ![Username taken warning](/filmreview/docs/username-taken-warning.png)|
| The Login page allows users to login to their account | If a user enters incorrect information they are warned and prompted to try again | ![Incorrect Login warning](/filmreview/docs/wrong-login-warning.png)|
| The Search page appears simple and plain at first to encourage the focus to be on users searching for films as that is the functionality of the page | The user is welcomed by their username to add a personalised feel, they can then search any film by title. This search runs through API data from [TMDB API](https://www.themoviedb.org/) and is returned as JSON data which is formatted and displayed to the user | ![search bar](/filmreview/docs/search-bar.png) |
| | When a user has searched for a film every film in TMDB API that matches that title will be displayed on screen, in different row configurations depending on screen size | ![Search results](/filmreview/docs/film-data-accordion.png) |
| | Once a user finds the film they wanted to search for they can click the accordion button to drop down the release date and description. A review button sits at the bottom of each film card so that a user can click the button that corresponds to the film they wish to review. This review button when hovered over becomes larger and its background colour turns green to indicate it should be clicked | ![Film accordion data](/filmreview/docs/film-drop-down.png)|
| | If a user searches for a film that doesn't exist within TMDB API an error message will display acknowledging that unfortunately this film could not be retrived | ![Film not found warning](/filmreview/docs/film-not-found.png)| 
| The Add Film Review form is comprised of form fields for the film title, the star rating, an optional written review and a custom selector to choose a film list, before clicking the Submit Review button | The form has 3 required fields, as shown by the red asterisk by each field, if these forms aren't filled out a warning is shown. | ![Film review form](/filmreview/docs/film-review-form.png)|
| | The star rating form field works by the user hovering over each star icon which increment in value as you go further to the right, clicking on the star you want to award will save the value | ![Star Rating](/filmreview/docs/star-rating.gif)| 
| | If a user attempts to submit a film review either without selecting a film list, or without having a film list created they will be redirected to the form that allows them to add a film list | ![Film list is necessary](/filmreview/docs/addFilmListRedirect.gif) |
| The My Reviews page features an add film button, and once users have reviewed films it will display each review, sorted by highest star rating to lowest | The Add Film review button exists to allow users to submit reviews without having to use the search functionality if they don't want to, or if a film isn't available on the search functionality. This button brings the user to the add film review form | ![my reviews page](/filmreview/docs/my-reviews.png) |
| | The film review accordion displays the film title, when the accordion is clicked it drop downs to display star rating, and written review (if the user provided one) | ![Film Review info](/filmreview/docs/film-review-info.png)|
| | Edit and delete buttons sit underneath the star rating and review when the film accordion is dropped down, this allows a user to change any aspect of their review, or brings them to a modal which allows them to delete the review if they wish. This delete modal provides defensive programming and is also featuring if a user attempts to delete a film list | ![Delete modal](/filmreview/docs/delete-modal.png)|
| The My Film Lists page features a button that allows a user to create their film list, then displays the existing film lists to the user | The Add Film List button when clicked takes the user to a form where they can create their own film lists. They must give their list a name, which has a character limit for design purposes, and can also enter a genre if they wish to group film reviews by genre | ![Add Film List](/filmreview/docs/add-film-list.png) |
| | The film lists display the title given by the user, their username, and which genre they entered (if they did), along with edit and delete buttons that work the same way as the edit and delete film review buttons mentioned above | ![film list](/filmreview/docs/my-film-lists.png)|


* Future Implementations:
  * Ideally I wanted to be able to display film cards with their respective film information and when a user clicked the review button the review form would be pre-populated with the poster image and title that they had selected. This wasn't achievable as tutor support couldn't advise me on how to do so without using Mongo DB and I didn't have time to restart my entire project. In the future this would be the desired functionality of the site and I regret that I couldn't accomplish this
  * Another key future implementation would be to program the film lists so that users can assign a film review to a specifc list and when they clicked on that list all the reviews associated would be displayed. This wasn't possible for me to do on my own with my current knowledge, and again was something that tutor support were unfortunately unable to advise me on how to accomplish this
  * A business goal for a future implementation would be to allow users to add their friends by username so they could see what their friends have watched and reviewed. It would also be great if users could comment on, or like these reviews to provide a sense of interactivity and communication between users.

### Accessibility 
As always accessibility is a constant thought throughout the planning and development of any project
* [Lighthouse Accessibility Score]()
* I prioritised using fonts that are readable and dyslexia friendly, with a film site many suggested fonts were ideal for film posters yet were much more difficult to read. This informed my decision to choose simpler fonts to maintain readability for every user. By developing my site mobile first I was able to ensure that font size is always readable no matter the screen size, therefore ensuring that all text is fully accessible
* Semantic HTML was used throughout the site with the inclusion of descriptive alt tags wherever necessary, and aria labels to allow screen readers to describe what the purpose of different buttons are
* I used the [Ally Color Contrast Accessibility Validator]() to check for any colour contrast issues and received the following result
* I used the [WAVE]() Web Accessibility tool to ensure there were no accessibility issues for the site. This resulted in the following message
!!!!!! Finish Accessibility !!!!!!

### Wireframes
!!!!!! Need to complete !!!!!

### Languages Used
* This project utilised HTML, CSS, and Python predominantly, with a small amount of JavaScript being used to automatically update the copyright information in the footer

### Frameworks, Libraries, and Programs Used
* [Adobe XD](https://helpx.adobe.com/uk/support/xd.html) was used to create the Wireframes seen above
* [ALLY](https://color.a11y.com/) was used to test for colour contrast issues on the site
* [Bootstrap](https://getbootstrap.com/) was utilised to create a core html structure so that my time could be spend on creating the databases and core functionality rather than doing all styling myself
* [CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate the Python used in my project
* [ElephantSQL](https://www.elephantsql.com/) was used to host the database for this site
* [Favicon](https://favicon.io/) was utilised to create a Favicon for my site's browser tab, and the logo for the navbar
* [Flask](https://flask.palletsprojects.com/en/2.3.x/) was utilised to set up this project, in conjunction with Python and aided in the functionality of the databases
* [Font Awesome version 6](https://fontawesome.com/) was used for all icons seen across the site
* [Gifox](https://gifox.app/) was used to create a video/gif to demonstrate hover effects and redirect functionality for this readme document
* [Github](https://github.com/) was used to store the repository for this quiz project, with Github Pages hosting the site
* [Gitpod](https://www.gitpod.io/) is the environment in which this project was created and worked on
* Google Chrome Developer Tools was used as a debugging tool, and to help visualise the site in different screen sizes to ensure that user experience remained clean and efficient no matter the device utilised by the user
* [Google Fonts](https://fonts.google.com/) provided the links for both fonts used on the site, and aided in selecting fonts that are complimentary to one another
* [Heroku](https://www.heroku.com/?) was used in addition to Github as the deployment platform for this site due to the use of databases
* [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) was used due to it being a templating lanuage which enabled me to have a base.html template with all other html pages inheriting core functionality from this
* [SQLAlchemy](https://www.sqlalchemy.org/) was used for the creation and maintenance of the relational databases used in the project
* [Tech Sini](https://techsini.com/multi-mockup/index.php) aided in the creation of a multi-device mockup image so that I could test the appearance and functionality of the site on multiple device sizes, and provided the image seen at the beginning of this document
* [WAVE](https://wave.webaim.org/) Web Accessibility Evaluation Tool was used to test my site against accessibility criteria.
* [Werkzeug](https://werkzeug.palletsprojects.com/en/2.3.x/) was used mainly for password hashing to ensure security of information in the Users database
* [WTForms](https://wtforms.readthedocs.io/en/3.0.x/) aided in rendering form fields without me having to hard code them, and provided CSRF protection 

* In addition to the Frameworks, Libraries, and Programs used I encorporated the use of [TMDB API](https://developers.themoviedb.org/3/getting-started) which allowed me to connect to the API, retrieve their film data, and display that to users when they search for films. The use of this API was integral to the functioning of my site

### Deployment 
!!!!! Need to deploy and write down steps for Heroku !!!!!!

## Testing
## Automated Testing

### W3 Nu HTML Validator 
I used the W3 Nu HTML Validator multiple times throughout development to ensure the HTML being used was sufficient and compliant with industry standards, the results of which can be found below
* [Index page](/filmreview/docs/testing/index-HTML-check.png)
* [Sign Up page](/filmreview/docs/testing/signup-HTML-check.png)
* [Log in page](/filmreview/docs/testing/login-HTML-check.png)
* [Search Page](/filmreview/docs/testing/search-HTML-check.png)
* [Add Film Review page](/filmreview/docs/testing/review-form-HTML-check.png) the Film Review page returned 2 errors due to the jinja templating being used, the errors ask me to add things that aren't possible due to how the code works. These errors do not affect the user in any way but hopefully in the future I can find a way around these errors
* [My Reviews page](/filmreview/docs/testing/review-page-HTML-check.png)
* [My Film Lists page](/filmreview/docs/testing/lists-HTML-check.png)
* [Film List Form](/filmreview/docs/testing/film-form-HTML-check.png)

### W3C CSS Validation Service
* [CSS Check](/filmreview/docs/testing/css-validate.png)
* As displayed above, no errors were found in my CSS file
* There is one warning raised which mentions "Due to their dynamic nature, CSS variables are currently not statically checked". This is related to line 98 of my file which is essential for the functioning of my star rating. As this is just a warning about the variable not currently being checked I'm happy to leave the warning as it is

### CI Python Linter
I used the CI Python Linter to test the validity and PEP8 compliance of my Python code used throughout this project, no files returned any errors which demonstrates that I've always followed PEP8 compliance rules. Below I have attached screenshots showing the validation results and that no errors were found
* [Init File](/filmreview/docs/testing/init-check.png)
* [Models File](/filmreview/docs/testing/models-check.png)
* [Routes File](/filmreview/docs/testing/routes-check.png)
* [Env File](/filmreview/docs/testing/env-check.png)
* [Run File](/filmreview/docs/testing/run-check.png)

### Wave Testing
!!!!!!! Need to deploy !!!!!!!

### Lighthouse Testing
## Desktop
* [Index not logged in](/filmreview/docs/testing/D-index-not-loggedin.png) The only recommendation to improve the performance of the index page is to eliminate render-blocking resources, this is predominantly caused by Bootstrap, Fontawesome, and Google Font links used in my base.html file. I have added defer attributes to Javascript links, and made sure to place script files outside of the head element wherever possible
* [Index logged in](/filmreview/docs/testing/D-index-loggedin.png)
* [Log in form](/filmreview/docs/testing/D-Login.png)
* [Sign up form](/filmreview/docs/testing/D-signup.png)
* [Search page](/filmreview/docs/testing/D-search.png)
* [Add film review page](/filmreview/docs/testing/D-review-form.png)
* [My reviews page](/filmreview/docs/testing/D-my-reviews.png) The only issue with the reviews page was concerning the aria-labels for the review cards as they don't have unique ids. This is due to using a Jinja loop to populate the cards meaning they cannot have unique ids and must be targetted with the same id as one another to function
* [My film lists page](/filmreview/docs/testing/D-filmlists.png) The only recommendation for this page was the same as above with the My Reviews page. I'd like to learn how to avoid this in the future but I'm satisfied with leaving this as in for now
* [Film list form](/filmreview/docs/testing/D-add-film-list.png)

## Mobile
* [Index not logged in](/filmreview/docs/testing/M-index-not-logged-in.png) The performance score for the index page was affected by the same issues for both mobile and browser, see above for a description of these recommendations
* [Log in form](/filmreview/docs/testing/M-login.png)
* [Sign up form](/filmreview/docs/testing/M-signup.png)
* [Search page](/filmreview/docs/testing/M-search.png) The search page again was similarly affected with the render-blocking resources warning as shown for the index page
* [Add film review page](/filmreview/docs/testing/M-film-review.png) Again this was affected by render-blocking resources
* [My reviews page](/filmreview/docs/testing/M-film-reviews.png)
* [My film lists page](/filmreview/docs/testing/M-filmlists.png) The only warning given for performance relates to render-blocking resources
* [Film list form](/filmreview/docs/testing/M-add-filmlist.png)

## Improvements Made
* As briefly mentioned above, the main improvements made as a result of the Lighthouse testing related to adding defer attributes to script links in the base.html file. This improved the rating by 5-10 points on each test but still didn't bring the overall score to above 90, I regret not being able improve this further
* Additionally I realised I had forgotten to add an alt image tag on the navbar logo which I added after being warned by Lighthouse to do so
* The accessibility score for both form pages was improved after I received a warning of insufficient colour contrast for the form submit buttons. I altered the background and font colours of both forms and this warning was resolved

## Manual Testing
### Testing User Stories

| User Story | Was this met? | Evidence |
| --- | --- | --- |
| 1. Easily register for an account, and login, be given warnings if any information entered is incorrect | Yes, flash message warnings are given for choosing an already taken username, not filling out all required forms, and for entering login information that is incorrect | ![Warning example](/filmreview/docs/signup-form-warning.png)|
| 2. The site should be fully responsive for all device sizes | Yes, using a mobile first approach, and then adding media queries for larger screen sizes ensured that the site is fully responsive with no issues for any screen sizes | ![Responsivity image](!!!!!!!!!!!!!!) |
| 3. There should be a broad selection of films available | Yes, while fully testing the site there was only one film that I found was unavailable due to the API not having its film data. An apology message is shown in this instance | ![Film not found](/filmreview/docs/film-not-found.png)|
| 4. Be able to edit or delete film lists or reviews at any time | Yes, edit and delete buttons are featured on the cards for both film lists and film reviews, with form information being pre-populating so that users know what they are editing. There is also defensive programming used so that when a user clicks delete a modal appears asking if they are sure as this action is permanent | ![Delete Modal](/filmreview/docs/delete-modal.png)|
| 5. Be readable, aesthetically pleasing, and easily navigable | Yes, I think the styling of the site is aesthetically pleasing and suitable to the theme of the site, along with all text being readable no matter the screen size. The site is easily navigable with a Bootstrap hamburger bar. The site also features logic so that if a user is not logged in they are unable to navigate to pages that require a login to access. If a user who isn't logged in types the url to navigate to a page that required a login they will be redirected to the login page with a flash message explaining they must be logged in| ![Hamburger image](/filmreview/docs/Hamburger-image.png) ![Login required](/filmreview/docs/login-required.png) |
### Full Testing

The site has been tested rigorously throughout development and after development was completed, this includes both manual and automated testing to ensure nothing is missed
* General:
  * All navbar links direct the user to the correct page, and those that require a user to be logged in are not displayed unless they are logged in
* Home page:
  * The navbar hamburger icon when clicked on any page drops down the navbar menu and all links when hovered over become purple to allow the user to know what they are about to click on
  * All social media links in the footer open in a new tab so as to not redirect the user away from the site for them to not be able to return
  * The copyright date is automatically updated depending on the year using Javascript found in the base.html file
* Login page:
  * The username field field is restricted to a maximum of 20 characters and users are physically incapable of entering anymore
  * The password field is limited to 80 characters so that a hash can be done meaning that the password is not stored in its original value in the database to ensure security
  * When hovered the Login button enlarges and the background colour turns light green to encourage users to click it
  * If a user enters incorrect username or password information they're greeted with a flash message explaining that their username or password is incorrect
  * When a user does login they're redirected to the search page with a flash message reading "You've been logged in" to alert users that they were successful
* Sign Up page:
  * The username field is restricted to 20 characters again and must be unique otherwise a flash message appears stating "This username has already been taken, please choose another"
  * If a user doesn't enter a valid email they are met with a flash message stating "Invalid email", along with the input bar turning red and a red exclamation mark appearing to indicate an error
  * When hovered the Sign Up button enlarges and the background colour turns light green to encourage users to click it
* Search page:
  * The user is greeted with a personalised welcome message which takes their username from the Users database to acknowledge who has been logged in
  * When hovered the Search button enlarges and the background colour turns light green to encourage users to click it
  * If a user attempts to click the Search button without entering any search term they are warned that they must enter a title to click the button
  * When the Search button is clicked the relevant film accordion cards are displayed featuring its title and the Review button, when the accordion button is clicked the release date and description are also displayed. Each accordion functions individually so the information beyond the accordion will only be displayed for the film card that has been clicked on
  * When hovered the Review button enlarges and the background colour turns light green to encourage users to click it
  * When the Review button is clicked the user is brought to the Review A Film form
  * If a user enters a film title or string that TMDB API doesn't include they receive an apology message and are encouraged to search for another film
* Film review form:
  * All required form fields must be filled in or the user will receive a warning asking them to "Please fill in this field"
  * The star rating system works by allowing the user to select the number star icon that corresponds with the rating they wish to award the film
  * The written review field is not required to allow users who are in a rush, or simply don't have anything to say to rate the film without having to write a formal review. If a written review is entered there is a minimum character length of 3, with a maximum character length of 200 to ensure the review cannot go on forever. If the maximum character limit is exceeded the textarea doesn't allow anymore characters to be physically entered
  * The film list selector is a required field and so if a user does not select a list to add their review to they are redirected to the Add Film List form and a message flashes explaining "Please create a Film List before adding reviews"
  * When a film review form is submitted a message flashes on the screen saying "Your review has been added successfully" to alert the user that their review is complete
  * When hovered the Submit Review button enlarges and the background colour turns light green to encourage users to click it
* My Reviews page:
  * When hovered the Add Film Review button enlarges and the background colour turns light green to encourage users to click it. This button when clicked redirects the user to the Add Film Review form to allow for them to review films both through this button and by searching for film data
  * Film reviews are displayed in accordion cards where the film title is always displayed and if the accordion button is clicked the star rating and written review attributed to this film will be displayed. The film reviews are sorted by popularity so a user will see all their top rated films at the top of their screen, descending to their most disliked films at the bottom of the screen
  * The review cards feature edit and delete buttons, both buttons enlarge when hovered over to indicate they can be clicked. The edit button when clicked redirects the user to the Review A Film form where the title, and written review (if completed) of that film is pre-populated. When they submit the edited review they are told "Your review has been updated" by a flash message and the film card reflects these changes
  * The delete button when clicked opens a modal asking the user if they're sure they wish to delete this review as this is a permanent action, they can then click Cancel, or the X at the modal corner to cancel this action. Or click the red Delete button to permanently delete their review
* My Films Lists page:
  * When hovered the Add Film List button enlarges and the background colour turns light green to encourage users to click. When clicked they are redirected to an Add Film List where they can create a list where the list name is a required field, and the genre is optional. The list name field has a maximum character length of 20, and if not filled in a warning will display. The list field features placeholder text giving suggestions for what a user might want to call their list if they have trouble thinking of their first title
  * The Add film list button when hovered over enlarges and turns a shade of light green, when clicked the user is directed back to the My Film Lists page with a message stating "Your Film List has been successfully created"
  * If a user clicks the edit button on a film list they are taken to the Edit Film List form where the title of that list is pre-populated. Editing the title or genre changes that data, and a message appears saying "Your film list was edited successfully"
  * If a user clicks the delete button on a film list a modal appears asking if they're sure as this will also delete all related film reviews and cannot be undone. If the red delete button is now clicked the film list will disappear, along with the related film reviews
* Logout: 
  * If the user clicks Log Out in the navbar they are logged out and redirected to the Home page along with a message confirming that they have been logged out. They are now unable to access pages that require login, but regain access to the Log In and Sign Up pages

## Bugs

| Bug | Have this been solved? | How? |

## Credits
### Code Sections

### Media

## Acknowledgements