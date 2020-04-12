# Keto Snack Box Subscription Service

Stream Four Project: Full Stack Frameworks with Django - Code Institute

[![Build Status](https://travis-ci.org/SianJade/keto-subscription-box.svg?branch=master)](https://travis-ci.org/SianJade/keto-subscription-box)
 
## UX

The purpose of this project is to offer users a monthly, curated box of snacks and other products catered towards users who are following the ketogenic diet, or are looking to begin following the ketogenic diet. The service offers users the opportunity to discover new ketogenic snakcs, foods, or other suitable products which they may not have tried before or have previously been aware of. As the ketogenic diet can be quite limiting, this box offers users the chance to potentially widen their food intake or add some more variety to their diet. As with many other subscription box services, the cost of the box itself each month is less than the cost would be were the user to individually purchase all of the items featured in the box each month. Users can subscribe on a month to month basis, or on a three or six monthly basis for a slightly reduced average monthly cost than the month to month option.

Businesses who wish to stock their own keto-friendly products in the box could also see a benefit to themselves from this service as there is potential for their products and brand to be introduced to new clients, which in turn could create new, returning customers to their business if the clients like their products which are featured in the box.

The site itself allows for customers to customize their box contents to an extent. The contents of each month's box will always be unknown until the customer receives the box, however, the option is available for customers to input any dietary restrictions, allergies, or food intolerances upon the creation of their account via a small form with dropdown menus - this ensures customers are not receiving items which they cannot use in their box each month, or putting them at risk of exposure to allergens - these preferences will be saved for future reference along with the rest of the customer's information.

The site also allows for purchases of individual items via a seperate online shop, where users can purchase items featured in past boxes as well as products which have not been featured in boxes at all. This allows users who do not wish to receive unknown items each month, or who perhaps cannot afford to pay for a monthly box to still browse and purchase keto products that they wish to try or that they know they will like. The store allows for users to filter products by their price, or item category such as drinks or snacks for ease of browsing. 

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
- The site features a page which displays three subscription tiers for the user to choose from, between one and six months in duration, each at a slightly more reduced cost depending on which tier the user chooses to purchase.

- The site also features a seperate 'Shop All Items' section 

### Features Left to Implement
- In future versions of the site I would like to add recurring billing to the site so that user's subscriptions can renew and have the appropriate payment taken from their account automatically once they have reached the end of their chosen subscription tier. For this to work I would also have to implemnt a feature that allows for the user's payment details to be saved so that payment can be taken automatically once their subscription renews.

- I would also like to implement a system which allows the user to select a previously saved shipping sddress from an address book that contains every address they have ever had their products shipped to in the past, so that they do not have to fill out their shipping details every time they place a new order, thus saving time and adding to ease of use for the user.

- In future releases I would also like to extend the functionality of the product filters beyond simply filtering by price and category - I would like to add the  ability for users to filter out certain allergens so that only products which do not contain those allergens in their ingredients list will appear in the filtered results, as well as filtering by dietary restrictions such as vegetarianism or veganism.

- The ability for users to update their email address or other account details is another feature I would like to add to the site in future releases, in case the user no longer has access to the email address which they used to sign up to the site, or should they change their name and wish to update this in their user details on the site.

## Technologies Used
- [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
    - The project uses HTML5 to construct the pages within the application.

- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3)
    - The project uses CSS3 in order to style the HTML5 and Bootstrap elements and components.

- [Bootstrap (ver 4.3.1)](https://getbootstrap.com/)
    - The project uses the Bootstrap 4 grid and components in order to achieve a responsive layout and styling.

- [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference)
    - This project uses Javascript in order for the product filters to function, allowing the user to filter by product price or product category.

- [Python (ver 3.0)](https://www.python.org/download/releases/3.0/)
    - The project uses Python in order to retrieve required information from the databases of products, subscriptions, orders, and users, as well as to create views and models utilised by Django. Python is also used to create functions which allow the user to create an account, log in and out, and to make purchases of products and subscriptions.

- [Jinja (ver 2.10)](https://jinja.palletsprojects.com/en/2.10.x/)
    - The project uses the Jinja templating langauge in order to extend the base HTML and prevent unnecessary repetition of HTML code, allowing existing code to be reused where possible. The use of Jinja also allows for variables containing information retrieved from the database to be injected into the HTML and/or looped over to display lists of ingredients and nutritional values for each product.


## Testing
- When setting up Travis' continuous integration, the build was failing with the error "Module not found: no module named env" - this was due to the env.py file being in my .gitignore file and so not being visible to Travis. To resolve this issue I changed `import env` in settings.py in the keto directory to 
    `try:
        import env
    except ModuleNotFoundError:
        pass`
This resolved the failing build issue and got the build to start passing.

- When creating the relationship between the Product model and the NutritionValue models, I initially tried to create a one


## Deployment


## Credits

### Content and Media
- All product images, descriptions, ingredient lists, and nutritional values were taken from product listings on [Amazon](https://www.amazon.co.uk/).


### Acknowledgements

