# Keto Snack Box Subscription Service

Stream Four Project: Full Stack Frameworks with Django - Code Institute

[![Build Status](https://travis-ci.org/SianJade/keto-subscription-box.svg?branch=master)](https://travis-ci.org/SianJade/keto-subscription-box)

A live desktop demo can be found [here](https://keto-subscription-and-store.herokuapp.com/). The source code for this project can be found [here](https://github.com/SianJade/keto-subscription-box).

## UX

The purpose of this project is to offer users a monthly, curated box of snacks and other products catered towards users who are following the ketogenic diet, or are looking to begin following the ketogenic diet. The service offers users the opportunity to discover new ketogenic snakcs, foods, or other suitable products which they may not have tried before or have previously been aware of. As the ketogenic diet can be quite limiting, this box offers users the chance to potentially widen their food intake or add some more variety to their diet. As with many other subscription box services, the cost of the box itself each month is less than the cost would be were the user to individually purchase all of the items featured in the box each month. Users can subscribe on a month to month basis, or on a three or six monthly basis for a slightly reduced average monthly cost than the month to month option.

Businesses who wish to stock their own keto-friendly products in the box could also see a benefit to themselves from this service as there is potential for their products and brand to be introduced to new clients, which in turn could create new, returning customers to their business if the clients like their products which are featured in the box.

The site itself allows for customers to customize their box contents to an extent. The contents of each month's box will always be unknown until the customer receives the box, however, the option is available for customers to input any dietary restrictions, allergies, or food intolerances upon the creation of their account via a small form with dropdown menus - this ensures customers are not receiving items which they cannot use in their box each month, or putting them at risk of exposure to allergens - these preferences will be saved for future reference along with the rest of the customer's information.

The site also allows for purchases of individual items via a seperate online shop, where users can purchase items featured in past boxes as well as products which have not been featured in boxes at all. This allows users who do not wish to receive unknown items each month, or who perhaps cannot afford to pay for a monthly box to still browse and purchase keto products that they wish to try or that they know they will like.

An [ER model](https://github.com/SianJade/keto-subscription-box/blob/8d4d676b8198a21fff4f40e8547d9489914fc4b4/static/wireframes/ER%20Model.png) and [wireframes](https://github.com/SianJade/keto-subscription-box/tree/8d4d676b8198a21fff4f40e8547d9489914fc4b4/static/wireframes) for this project across all screen sizes can be found in the Wireframes folder, which is located within Static folder in the GitHub repository.

## User Stories
### User Story One:
As a newcomer to the keto diet, I would like to be able to discover a range of snacks which fit into my new diet, as finding keto-friendly snacks can be quite difficult. A subscription box would allow me to discover and sample new products every month, adding variety to my diet and opening me up to new brands and products which I may not have been previously aware of.

### User Story Two:
As a vegan on the keto diet, it often proves extremely difficult for me to find snacks in stores which are suitable for me to consume as most vegan snacks tend to be relatively high in carbohydrates. Rather than spending extended periods of time scouring the internet and researching what snacks are both vegan and keto-friendly, I would like to be able to simply input my dietary preferences and have a box of appropriate foods and snacks curated and shipped to me every month in order to remove a lot of unnecessary legwork on my end.

### User Story Three:
As somebody who follows the keto diet but lives in a rural area with little to no access to health food shops from which to purchase keto products, I would like to be able to find a range of products to suit my diet all in one place online and have them delivered to my door at a time that is convenient for me.

### Uer Story Four:
As a person who suffers from type 2 diabetes and has limited mobilty, my doctor has advised me to try out the keto diet to try and improve my health, however, it can be somewhat difficult for me to get out to the shops to find and purchase foods that are suitable for me to eat. A curated box of foods that has been put together to suit my dietary needs and that can be delivered to me at my home on a regular basis would be extremely helpful to me.

### User Story Five:
As a UK resident, I would like to be able to purchase one of the various keto subscription boxes available online, however none of these currently exisiting boxes ship to the UK as the companies are all US based and do not offer international shipping - I would like for there to be a UK equivalent of these boxes which I am able to purchase and enjoy.

## Features
### Existing Features
- The site features the ability for users to purchase one of three subscription tiers to a monthly, curated subscription box - these subscriptions are between one and six months in duration, each at a slightly more reduced cost depending on which tier the user chooses to purchase. The site also features a seperate 'Shop All Items' section, which essentially functions as an ecommerce site for users to browse and purchase keto-friendly snacks, foods, and supplements should they not wish to purchase a box which they do no know the exact contents of. The name of each of the products on the 'Products' page is clickable and when clicked will link the user to a page containing more information - such as a description, nutritional values, and ingredients - about the selected product.

- In order to ensure that the user is aware of the site's purpose and features upon hitting the landing page, Bootstrap cards have been implemented - one to explain to the user that subscription boxes are available and featuring a button to take them to the subscriptions page if they are interested, and one explaining that the site also features a store full of non-mystery ketogenic items that they are arble to browse and purchase, as well as a button to take them to that page should they wish to view the products.

- In order to avoid information overload to the user, only the product's description is visible upon the individual product information page loading - the nutritional information and ingredients are only displayed once the user clicks the chevron icon beside the respective headings to activate the 'see more' function, which will then display the information the user wishes to read. Each product's nutritional values are displayed in a bootstrap table for ease of reading, and so that they are displayed as they would appear on the label on the back of the physical product so that the information is presented to the user in a way that is familiar and recognisable to them.

- Across the top of the homepage and on the site's subscription and shop pages, a Javascript countdown to a Summer sale to make users aware that a sale will be ocurring on the site soon should they wish to come back to buy products at discounted prices. This countdown is displayed in red text so as to catch the user's eye and convey a sense of urgency and importance. The Javascript which powers this countdown is in a separate file to the Javascript which provides the functionality of the 'see more' buttons beside the Nutrition Value and Ingredients headings on a product's page - this is to ensure that each JavaScript function is only loaded in on pages where it is required, in order to avoid errors if an element referred to within the Javascript does not exist on the page on which the function has been loaded, which would have been a possibility were both functions to be in the same file as one another.

- The site also features a keyword search box in the nav bar so that if user's wish to search for a product by name, brand, or flavour in order to locate a product more quickly then they are able to do that also.

- Other than on the landing page, the site does not feature any background colours or image in order to allow the information within the site, such as the products available and their respective descriptions, to be presented to users clearly, in a way with understandable information architecture, and without distraction or colour schemes which make text difficult to read, as well as to give the site a clean and modern feel in its design. The navbar, however, is a light grey colour so as to provide some clear differentiation between it and the site's content for the user.

- The site also featured django's flash messages at the top of the page, below the nav bar, to inform users of warnings or success messages, such as if the user has paid for an item successfully, created their account successfully, logged out, or if payment cannot be taken from the given card. These messages persist only until the user refreshes or navigates away from the page. In future releases I would like to make these messages more stylised and prominent for the user to notice them wth more ease.

### Features Left to Implement
- In future versions of the site I would like to add recurring billing to the site so that user's subscriptions can renew and have the appropriate payment taken from their account automatically once they have reached the end of their chosen subscription tier. For this to work I would also have to implemnt a feature that allows for the user's payment details to be saved so that payment can be taken automatically once their subscription renews.

- I would also like to implement a system which allows the user to select a previously saved shipping sddress from an address book that contains every address they have ever had their products shipped to in the past, so that they do not have to fill out their shipping details every time they place a new order, thus saving time and adding to ease of use for the user.

- In future releases I would also like to add product filters which would allow the user to refine products by price and category, or to filter by certain allergens so that only products which do not contain those allergens in their ingredients list will appear in the filtered results, as well as filtering by dietary restrictions such as vegetarianism or veganism.

- The ability for users to update their email address or other account details is another feature I would like to add to the site in future releases, in case the user no longer has access to the email address which they used to sign up to the site, or should they change their name and wish to update this in their user details on the site.

- In future releases I would alsolike to add the functionality for users to persist their cart contents across devices and browsing sessions - saving their cart contents upon ending the session or logging out, and persisting them in memory until next time they log in to their account on the site should they wish to save things for later purchase.

## Technologies Used
- [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
    - The project uses HTML5 to construct the pages within the application.

- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3)
    - The project uses CSS3 in order to style the HTML5 and Bootstrap elements and components.

- [Bootstrap (ver 4.3.1)](https://getbootstrap.com/)
    - The project uses the Bootstrap 4 grid and components in order to achieve a responsive layout and styling.

- [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference)
    - This project uses Javascript to power the countdown to the Summer Sale as seen on the home page and product/subscription pages, as well as to control the see more/less buttons on the product nutrition value tables and ingredient lists.

- [Python (ver 3.0)](https://www.python.org/download/releases/3.0/)
    - The project uses Python in order to retrieve required information from the databases of products, subscriptions, orders, and users, as well as to create views and models utilised by Django. Python is also used to create functions which allow the user to create an account, log in and out, and to make purchases of products and subscriptions.

- [Django (ver 1.11.24)](https://www.djangoproject.com/)
    - This project uses Django as its main framework to create each of the applications within the site as well as to create the models used for each database, including products, ingredients, nutritional values, subscriptions, orders, and users.

- [Jinja (ver 2.10)](https://jinja.palletsprojects.com/en/2.10.x/)
    - The project uses the Jinja templating langauge in order to extend the base HTML and prevent unnecessary repetition of HTML code, allowing existing code to be reused where possible. The use of Jinja also allows for variables containing information retrieved from the database to be injected into the HTML and/or looped over to display lists of ingredients and nutritional values for each product.


## Testing
- When setting up Travis' continuous integration, the build was failing with the error "Module not found: no module named env" - this was due to the env.py file being in my .gitignore file and so not being visible to Travis. To resolve this issue I changed `import env` in settings.py in the keto directory to 
    `try:
        import env
    except ModuleNotFoundError:
        pass`
    This resolved the failing build issue and got the build to start passing.

- Automated unit testing has been implemented across the models and forms within this project where relevant, although I would like to expand these tests to cover the views in the future and try to acheive full test coverage for the site as a whole. These tests are split into `test_models.py` and `test_forms.py` files within the folders for their relevant apps to ensure separation of concern. To manually run the tests yourself, simply run the command `python3 manage.py test` in the terminal - this will show all tests as passing.

- One quite large issue I ran into when testing the site's functionality manually stemmed from within my `cart_contents` function in my shopping cart app. Upon trying to add a subscription to the shopping cart, the Django debugger screen displayed the error `No Product matches the given query`, once this error had been hit upon adding a subscription to the cart, the whole site broke down and errors were thrown across all screens as a result. This error could be traced back to my contexts.py file in  my shopping cart app - whilst I had configured `cart_contents` to take an argument of `id`, the function could only interoret this as an id from my Product model. Due to the `get_object_or_404` that was in place for if a product id could not be found, when I subscription was added to the cart, the `cart_contents` funciton within coxtexts.py interpreted that as a product whose id could not be found, as I had failed to correctly ammend the `cart_contents` function to take in both product ids and subscription ids. However, as my products and subscriptions are both in seperate models, this meant that a product can have an id of 1, and so can a subscription, so once added to the cart, the `cart_contents` function had no way of being able to ascertain whether the newly added id was that or a Product or a Subscription, however because the Porduct model appears before the Subscription model in the database, the cart simply interpreted all ids as Product ids, even if they were not. To resolve this, I added two if statements to my `cart_contents` function - one to append Products to the cart via the product id and one to append subscriptions via the subscription id.

- The site's checkout function has been tested using Stripe's dummy card and payments for both products and subscriptions were processed successfully and upon successful payment a new OrderLineItem - or SubscriptionLineItem  depending on the type of item purchased - was successfully added to the Order model alongside the user's name and shipping information. Should you wish to test the payment functionality yourself, please do so using Stripe's provided dummy card which has a Card Number of `4242424242424242` and a CVV of any random three digits, the expiry month and year must also be in the future in order for the payment to successfully be taken - should no card number or cvv be input, or an expiry date which has already passed then the payment will not be processed and an error message will be returned.

- When viewing the cart contents in the cart view, the product quantity is displayed outside of the quantity input box - this is although I have tried to template the current product quantity into the quantity input, as this quantity cannot be given a default value to stop the site breaking when 'adjust cart' is clicked and no new qunaitity has been input - instead if no value has been input into the field, the site throws an error of `invalid literal for int() with base 10`. Unfortunately I have not been able resolve this issue as of yet and the only way to get rid of the error screen is by clicking the browser's back button. This is a huge issue and something I am urgently looking to resolve.

- The site's user creation function has also been manually tested to ensure that user's can successfully create a profile - which is required in order for them to be able to proceed to the checkout and complete their purchase. This can be done either by clicking the `Register` nav link to access the account creation form, or otherwise the user will be prompted to log in or sign up should they attempt to checkout without being authenticated.

- The site has been checked for responsiveness across a variety of web browsing applications on both PC and handheld devices, and on a multitude of screen sizes - all features were found to be fully responsive and fit well within each screen size. The only slight issue of note is that on very small screens, the sale countdown numbers can become a little wonky, although this is something I will look to resolve in the future.

- One other issue that was discorvered during my manual testing of the site's functionality is that the chevron icons beside the Nutrition Value and Ingredient headings needs to be clicked twice on the intial click in order for the SeeMore function to execute and the respective product information to be shown. However, after this initial click, the button only requires one click each time to show and hide the information as intended, unless the page has been reloaded, in which case it takes two clicks again. So far I have not been able to establish the cause of this error, and so have not been able to provide a fix for it, however this is an issue I will look to fix in future releases.

- All HTML code was run through the [W3C HTML Validator](https://validator.w3.org/) and returned no errors.

- All CSS code was run through the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) and returned no errors.

- All Javascript files were run through [JS Hint](https://jshint.com/) and returned no errors.

- All Python files were run through the [PEP8 Online Checker](http://pep8online.com/) and indentation, trailing whitespace, and missing blank lines were ammended accordingly so that no errors or warnings were returned.


## Deployment
- The application is hosted via [Heroku](https://keto-subscription-and-store.herokuapp.com/), with the source code being available on [GitHub](https://github.com/SianJade/keto-subscription-box), and is deployed from the master branch - this allows the deployed application to automatically update with any new commits that are made to the master branch.
    - To deploy the to Heroku successfully, all of the project's requirements must be saved to a `requirements.txt` file via the `pip freeze` command in the terminal.
    - I then had to set the config vars manually in Heroku in the application's settings tab as Heroku cannot view environment variables stored inside the env.py file as this file is within `.gitignore` since it contains passwords and secret keys and other potentially sensitive informatin - here I set the config vars key value pairs to match the contents of the key value pairs in my environment variables so that Heroku has access to the information for the application to be able to run.
    - Then to ensure my Heroku app updated in realtime with my commits to my Github repository, I opened up the 'Deploy' tab inside my Heroku dashboard, and connected the Heroku app to the respective GitHub repo and enabled automatic deploys so that all pushes to the master branch on Github would also be pushed to Heroku, meaning I did not have to also push to Heroku manually.
    
- To run this application locally:
    - Click the green 'clone or download' button in the [GitHub repository for the project](https://github.com/SianJade/keto-subscription-box).
    - Copy the link provided by clicking the clipboard button to the right of the link.
    - In your terminal, type `git clone`, paste in the previously copied link, and hit return.
    - The application should now be installed on your device.

- Alternatively, if you have the GitPod browser extension, a small green button reading `gitpod` will be visible next to the `clone or download` button; to run the application localling gitpod simply click this green button and ensure you are logged into your GitHub account.


## Credits

### Content and Media
- All product images, descriptions, ingredient lists, and nutritional values were taken from product listings on [Amazon](https://www.amazon.co.uk/).


### Acknowledgements

