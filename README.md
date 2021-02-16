# ![ART.IAL](/media/logo.png) #

[ART.IAL](https://art-ial-app.herokuapp.com/) is an e-commerce website with artwork gallery where you can not only view but also purchase available artwork.

At the beginning of 2020, my sister started experimenting with paint on canvases that has now gained popularity amongst family, friends, colleagues as well as enquiries from her followers on Instagram. I have therefore decided to commit in creating a website for my sister as a professional platform to sell her artwork. After my graduation, this site will be used as fully functional e-commerce platform.

![Site display on different screens](/wireframes/testing-images/responsive-design.jpg)

---

## Contents ##

- [!ART.IAL](#)
  - [Contents](#contents)
  - [UX](#ux)
    - [Project Goals](#project-goals)
    - [Site Owner Goals](#site-owner-goals)
    - [Site Visitor/User Goals](#site-visitoruser-goals)
    - [User Stories](#user-stories)
    - [User Requirements and Expectations](#user-requirements-and-expectations)
      - [**Requirements**](#requirements)
      - [**Expectations**](#expectations)
    - [Design Choices](#design-choices)
      - [**Fonts**](#fonts)
      - [**Colours**](#colours)
  - [Wireframes](#wireframes)
    - [**Site Map**](#site-map)
    - [**Site Layout**](#site-layout)
  - [Information Architecture](#information-architecture)
    - [Database Choice](#database-choice)
    - [Database Modelling](#database-modelling)
      - [**Profile App**](#profile-app)
        - [Profile](#profile)
      - [**Product App**](#product-app)
        - [Product](#product)
        - [Product Category](#product-category)
        - [Collection Name](#collection-name)
        - [Images Folder](#images-folder)
        - [Artwork Images](#artwork-images)
        - [Tag](#tag)
      - [**Checkout App**](#checkout-app)
        - [Order](#order)
        - [Order Line](#order-line)
      - [**Home App**](#home-app)
        - [About Section](#about-section)
        - [Social Media Icons](#social-media-icons)
  - [Technologies](#technologies)
    - [Languages](#languages)
    - [Libraries & Tools](#libraries--tools)
  - [Features](#features)
    - [Implemented Features](#implemented-features)
      - [**User Account**](#user-account)
      - [**Super User**](#super-user)
      - [**Gallery page**](#gallery-page)
      - [**Shop page**](#shop-page)
      - [**Shopping bag**](#shopping-bag)
      - [**Payments**](#payments)
    - [Future Features](#future-features)
  - [Changes applied since planning](#changes-applied-since-planning)
  - [Testing](#testing)
  - [Deployment](#deployment)
    - [Deploying art.ial to Heroku](#deploying-artial-to-heroku)
  - [Credits](#credits)
    - [Images](#images)
    - [Image editing](#image-editing)
    - [Code ideas](#code-ideas)
  - [Acknowledgements](#acknowledgements)

---

## UX ##

### Project Goals ###

This project is my final project for the Code Institute's Full stack development programme. The main goal of this project is to create an e-commerce site using Django framework, which is hosted with AWS as well as implementing a fully functional payment system with Stripe.

### Site Owner Goals ###

- Provide the users with a professional e-commerce online shop to allow secure purchases
- Make profit selling artwork
- Promote the artwork and the brand of the artist

### Site Visitor/User Goals ###

- View new artwork produced by the artist
- Ability to buy artwork online

### User Stories ###

**As a user (*applies to all site users*) I am able to:**

1. Access the site on my mobile, tablet and desktop which is adapted to provide the best experience.

2. Easily navigate through the website without too much thought and find what I am looking for quickly.

3. Identify instantly what the site is all about and what it has to offer.

4. Contact the site owner using a simple form.

5. Find key information about the artwork I am interested in (such as images, title, dimensions, etc)

6. Filter the artwork in the gallery page to identify new, available, and sold artwork.

7. Add the artwork in my shopping bag.

8. Change the content of my shopping bag before continuing to completion (add more or remove the artwork).

9. See full breakdown of the total cost, including the shipping charge before proceeding to payment.

10. Purchase the artwork using my card in a secure environment.

11. Receive an email confirmation once I complete the payment.

**As a new site user I am able to:**

1. Create an account.

**As a returning user I am able to:**

1. Login to my existing account and make a quicker purchase.

2. View, save, and update my personal information.

3. View past orders.

4. Make purchases quicker by having stored information such as address.

5. Change or reset my password securely.

**As a superuser (site owner) I am able to:**

1. Securely add, edit and delete the information for the specific artwork listed on the website.

2. Change the tags on the products to specify new, available, an sold artwork.

3. Receive enquiries from the site users after they fill in the contact form straight to my email inbox.

4. Get an email with the customer orders when the purchases are made.

5. Manipulate social media icons in the footer of the site (turn social media icons *on/off* and edit URL's).

6. Edit content in the `About` section of the `Home` page.

7. Manipulate what images are displayed in the carousels (New Artwork and Gallery Preview).

8. View history of all orders with minimal order information.

[Back to content](#contents)

### User Requirements and Expectations ###

#### **Requirements** ####

- Visually pleasant app design
- Easy site navigation
- Information of the content layed out in a simple and clear way on both mobile and larger screens
- Self-explanatory icons where text is absent

#### **Expectations** ####

- User information is protected by the site
- User is able to manipulate elements of the particular page
- Quick app load time

[Back to content](#contents)

### Design Choices ###

#### **Fonts** ####

- *Headers, titles*

  ```font-family: 'Krona One', sans-serif;```

- *Paragraphs, descriptions*

  ```font-family: 'Exo', sans-serif;```

#### **Colours** ####

![Colour palette](/wireframes/colour-palette/colour-palette.jpg)

[Back to content](#contents)

## Wireframes ##

### **Site Map** ###

Firstly, I have created a site [map](/wireframes/site-map/sitemap.png) to enable me to clearly plan the site design before I started working on the wireframes. It has also helped me to visualize what apps I will need to create to make this project fit for purpose.

### **Site Layout** ###

I designed my site moc-ups using [balsamiq wireframes](https://balsamiq.com/). I was focusing on defining the basic layout structure of the app and identifying how displays would change on different screen sizes such as [mobile](/wireframes/site-wireframes/gallery-buy.mobile.png), [tablet](/wireframes/site-wireframes/gallery-buy.tablet.png), and [desktop](/wireframes/site-wireframes/gallery-buy.desktop.png).

You can view all wireframes created for this project in [site wireframes](/wireframes/site-wireframes) folder.

[Back to content](#contents)

---

## Information Architecture ##

### Database Choice ###

### Database Modelling ###

#### **Profile App** ####

##### Profile #####

| **Title** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | ---
 Username | username | OneToOneField 'User' |  on_delete=models.CASCADE
 Full Name | profile_full_name | CharField | max_length=70, null=True, blank=True
 Phone number | profile_phone_number | CharField | max_length=20, null=True, blank=True
 Address Line1 | profile_address_line1 | CharField | max_length=60, null=True, blank=True
 Address Line2 | profile_address_line2 | CharField | max_length=60, null=True, blank=True
 Town/City | profile_town_or_city | CharField | max_length=50, null=True, blank=True
 County | profile_county | CharField | max_length=50, null=True, blank=True
 Postcode | profile_postcode | CharField | max_length=20, null=True, blank=True
 Country | profile_country | CountryField | blank_label='Country', null=True, blank=True

#### **Product App** ####

##### Product #####

| **Title** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | ---
 Product Category | product_category | ForeignKey 'Product Category' | null=True, blank=True, on_delete=models.SET_NULL
 Title | title | CharField | max_length=254
 Collection Name |collection_name | ForeignKey 'Collection Name'| null=True, blank=True, on_delete=models.SET_NULL
 Description | description | TextField | max_length=800
 Author | author | CharField | max_length=254
 Dimensions | dimensions | CharField | max_length=70, null=True, blank=True
 Price | price | DecimalField |max_digits=6, decimal_places=2, validators=[MinValueValidator(0.01)]
 Images Folder| images_folder| ForeignKey 'Images Folder'| null=True, blank=True, on_delete=models.SET_NULL
 Sku | sku | CharField | max_length=254, null=True, blank=True
 Tag| tag | ForeignKey 'Tag'| null=True, blank=True, on_delete=models.SET_NULL
 Featured as New | ft_new | BooleanField | default=False
 Featured as Preview | ft_preview| BooleanField | default=False

##### Product Category #####

| **Title** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | ---
Programmatic Name | name | CharField | max_length=50
Friendly Name | friendly_name | CharField | max_length=50, null=True, blank=True

##### Collection Name #####

| **Title** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | ---
Programmatic Name | name | CharField | max_length=50
Friendly Name | friendly_name | CharField | max_length=50, null=True, blank=True

##### Images Folder #####

| **Title** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | ---
Title | title | CharField | max_length=254
Artwork Images | imgs | ForeignKey 'Artwork Images'| null=True, blank=True, on_delete=models.SET_NULL

##### Artwork Images #####

| **Title** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | ---
Title | title | CharField | max_length=254
Image | img | ImageField | null=True, blank=True
Image Url | image_url | URLField | max_length=1024, null=True, blank=True

##### Tag #####

| **Title** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | ---
Programmatic Name | name | CharField | max_length=50
Friendly Name | friendly_name | CharField | max_length=50, null=True, blank=True

#### **Checkout App** ####

##### Order #####

| **Title** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | ---
Order Number | order_number | CharField | max_length=32, null=False, editable=False
Profile | profile | ForeignKey 'Profile' | on_delete=models.SET_NULL, null=True, blank=True, related_name='orders'
Full Name | full_name | CharField | max_length=70, null=False, blank=False
Email | email | EmailField | max_length=254, null=False, blank=False
Phone number | phone_number | CharField | max_length=20, null=False, blank=False
Address Line1 | address_line1 | CharField | max_length=60, null=False, blank=False
Address Line2 | address_line2 | CharField | max_length=60, null=False, blank=False
Town/City | town_or_city | CharField | max_length=50, null=False, blank=False
County | county | CharField | max_length=50, null=True, blank=True
Postcode | postcode | CharField | max_length=20, null=True, blank=True
Country | country | CountryField | blank_label='Country*', null=False, blank=False
Purchase Date | purchase_date | DateTimeField | auto_now_add=True
Delivery Cost | delivery_cost | DecimalField | max_digits=6, decimal_places=2, null=False, default=0
Order Total | order_total | DecimalField | max_digits=10, decimal_places=2, null=False, default=0
Grand Total | grand_total | DecimalField | max_digits=10, decimal_places=2, null=False, default=0
Original Cart | original_cart | TextField | null=False, blank=False, default=''
Stripe Pid | stripe_pid | CharField | max_length=254, null=False, blank=False, default=''
Comment | comment | TextField | max_length=254, null=True, blank=True

##### Order Line #####

| **Title** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | ---
Order | order | ForeignKey 'Order' | null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems'
Product | product | ForeignKey 'Product' | null=False, blank=False, on_delete=models.PROTECT
Item Total | item_total | DecimalField | max_digits=6, decimal_places=2, null=False, blank=False, editable=False
Datetime | datetime | CharField | null=True, blank=True, max_length=20

#### **Home App** ####

##### About Section #####

| **Title** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | ---
Title | title | CharField | max_length=254
Description | description | TextField | max_length=800
Image | img| ImageField | null=True, blank=True
Image Url | img_url | URLField | max_length=1024, null=True, blank=True

##### Social Media Icons #####

| **Title** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | ---
Title | title | CharField | max_length=254
Icon | icon | CharField | max_length_50
Icon url | icon_url | URLField | max_length=1024, default= '', null=True, blank=True

[Back to content](#contents)

---  

## Technologies ##

### Languages ###

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Python](https://www.python.org/)

### Libraries & Tools ###

- [jQuery](https://jquery.com/)
- [Popper](https://popper.js.org/)
- [Popper JS](https://popper.js.org/)
- [Bootstrap](https://getbootstrap.com/)
- [Flask](https://www.fullstackpython.com/flask.html)
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
- [Font-Awesome](https://fontawesome.com/icons?d=gallery)
- [Google fonts](https://fonts.google.com/)
- [Git](https://git-scm.com/)
- [GitHub](https://github.com/)
- [Heroku](https://www.heroku.com/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Color editor](https://coolors.co/)
- [Image editor](https://www.birme.net/)

[Back to content](#contents)

---

## Features ##

Art-ial website is designed using five applications: `Home`, `Products`, `Profiles`, `Bag`, and `Checkout`.

### Implemented Features ###

- The site has **responsive design** when viewed on mobile, tablet, and desktop.
- **Easy navigation** to external sites, such as social media accounts.
- The user is given feedback when they interact with the website (i.e. when items are added/deleted from cart, or payment is processed, or they send an enquiry using the form on `Home` page).
- **Purchased** artwork is immediately allocated ***sold*** tag, removed from `Shop` page and is only visible in the `Gallery` page.

#### **User Account** ####

- The users are able to **create** an account where they can store personal information such as their address and **edit** their details.
- **Password re-set**.
- **User** can completely delete their account.

#### **Super User** ####

- Existing content about the **artwork** can be edited, updated, archived or completely deleted by the **Super User** in the front end.
- The **Super User** is able to **add new** artwork to `Gallery` and `Shop` sections of the site.
- The **Super User** is able to change the content displayed in `About` section of the site.
- The **Super User** is able to change the pictures displays in New Artwork and Gallery preview carousels located in `Home` page.
- The **Super User** is able to add/remove/edit additional ***social media*** icons displayed in the footer.
- The **Super User** is able to see history of all orders.

#### **Gallery page** ####

- **Search function** in the gallery page to narrow down and search for *all artwork*, *new*, *sold* or *available to purchase* artwork.
- The artwork has allocated tags that are clearly visible to allow the user to identify if it's available for purchase or it's newly added or still available for purchase.
- **Room view** image is available for the users to view to enhance experience.

#### **Shop page** ####

- All of the artwork listed on this page is available for purchase.
- **Room view** image is available for the users to enhance shopping experience.

#### **Shopping bag** ####

- Items added to the shopping bag appear in the shopping cart.
- Artwork can be removed from the shopping bag.
- The user can choose to proceed to payment.

#### **Payments** ####

- Existing users who have previously made a purchase and are logged in, have their delivery address pre-populated when they proceed to payment.
- Checkout page shows the summary of the order.
- Payment can be made by card using Stripe.

### Future Features ###

- The **Super User** can update ***video banner*** content and ***contact info***.
- The **Super User** is able switch quick links ***on*** and ***off***, and add others.

[Back to content](#contents)

---

## Changes applied since planning ##

---

## Testing ##

Testing information can be found in a separate [Testing.md](Testing.md) file.

[Back to content](#contents)

---

## Deployment ##

**The Art-ial** project was deployed using the **VS Code IDE**, using **Git** and **GitHub** for version control. It is hosted on **Heroku** and all static files, including images, are hosted in **AWS S3 Bucket**. **Stripe** is used for payments and **gMail** for an email account.

Before deploying the application, install the following:

- Python 3
- PIP
- Git
- Heroku CLI

### Local Deployment ###

To deploy Art-ial locally, take the following steps:

1. From the applications [repository](https://github.com/neringabickmore/art-ial.git), click the *code* button and download the zip file.

    Alternatively, you can clone the repository using the following line in your terminal:

```terminal
git clone https://github.com/neringabickmore/art-ial.git
```

2. Access the folder in your terminal window and install the application's required modules with the following command:

```terminal
pip3 install -r requirements.txt
```

3. Create `env.py` file to hold your environmental variables in the root level of the application:

```python

import os

os.environ.setdefault('STRIPE_SECRET_KEY', 'YOUR_STRIPE_SECRET_KEY')
os.environ.setdefault('STRIPE_PUBLIC_KEY', 'YOUR_STRIPE_PUBLIC_KEY')
os.environ.setdefault('STRIPE_WH_SECRET', 'YOUR_STRIPE_WH_SECRET')
os.environ.setdefault('DATABASE_URL', 'YOUR_DATABASE_URL')
os.environ.setdefault('SECRET_KEY', 'YOUR_DJANGO_SECRET_KEY')
os.environ.setdefault('DEVELOPMENT', 'True')

os.environ.setdefault('EMAIL_HOST_USER', 'YOUR_EMAIL_USER')
os.environ.setdefault('EMAIL_HOST_PASSWORD', 'YOUR_EMAIL_PASSWORD')
os.environ.setdefault('EMAIL_HOST', 'smtp.google.com') # for gmail
os.environ.setdefault('DEFAULT_ORDER_EMAIL', 'DEFAULT_EMAIL')
```

If you plan to make your repository public, ensure you add it to .gitignore before committing.

4. If your IDE terminal, migrate the models to create the database using the following commands:

```terminal
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser to access the admin panel using the following command:

```terminal
python manage.py createsuperuser
```

Then follow the instructions to create the superuser.

6. After you login to the admin panel, you can add data to be displayed in your app. Refer to [database modeling](#database-modelling). Alternatively, if you have data fixtures, use the following command to load data into the database:

```terminal
python manage.py loaddata <fixture_name>
```

7. To initiate the application, type the command `python manage.py runserver` in your terminal. The application is now available in your browser at the address: `http://localhoset:8000`

### Deployment to Heroku ###

To deploy the app to Heroku, use the following steps:

1. Ensure you have the following dependancies installed in your app, such as PostgressSQL driver for Python, WSHI HTTP Server and dj database url that connects the the app with the database:

```terminal
pip3 install psycopg2-binary

pip3 install install gunicorn

pip3 install dj_database_url
```

2. If you haven't already, create `requirements.txt` file containing all of the dependancies:

```terminal
pip3 freeze > requirements.txt
```

3. Create a `Procfile` that contains the following: `web: gunicorn art_i_al.wsgi:application`.
4. Push these newly created files to your repository master.
5. Login to Heroku and create a new app.
6. In Heroku dashboard of the new app, click **deploy**, then **deployment** method and select **GitHub** to connect your app to your github repository for automatic deployment.
7. In Heroku Resources tab, navigate to **Add-Ons** section and search for **Heroku Postgres**. I recommend you choose hobby level for this application.
8. In settings tab, navigate to **Reveal Config Vars** and add the following variables:

| **KEY**               | **VALUE**                          |
| --------------------- | -----------------------------------|
| AWS_ACCESS_KEY_ID     | ACCESS_KEY_ID_PROVIDED_BY_AWS      |
| AWS_SECRET_ACCESS_KEY | SECRET_ACCESS_KEY_PROVIDED_BY_AWS  |
| DATABASE_URL          | YOUR_DATABASE_URL                  |
| DEFAULT_ORDER_EMAIL   | DEFAULT_EMAIL                      |
| EMAIL_HOST            | smtp.google.com (if using gmail)   |
| EMAIL_HOST_PASSWORD   | YOUR_EMAIL_PASSWORD                |
| EMAIL_HOST_USER       | YOUR_EMAIL_USER                    |
| SECRET_KEY            | YOUR_DJANGO_SECRET_KEY             |
| STRIPE_PUBLIC_KEY     | YOUR_STRIPE_SECRET_KEY             |
| STRIPE_SECRET_KEY     | YOUR_STRIPE_PUBLIC_KEY             |
| STRIPE_WH_SECRET      | YOUR_STRIPE_WH_SECRET              |
| USE_AWS               | True                               |

1. In settings.py in your IDE, temporarily comment out the database and use below code instead (make sure you do not commit!):

```python
DATABASES = {
        'default': dj_database_url.parse('POSTGRESS URL')
    }
```

10. In terminal, migrate the models to create the Postgress database using the following commands:

```terminal
python manage.py makemigrations
python manage.py migrate
```

11. Create a superuser to access the admin panel using the following command:

```terminal
python manage.py createsuperuser
```

Then follow the instructions to create the superuser.

12. After you login to the admin panel, you can add data manually to be displayed in your app. Refer to [database modeling](#database-modelling) for required data.

    Alternatively, if you have data fixtures, use the following command to load data to the Postgress database:

```terminal
python manage.py loaddata <fixture_name>
```

13. Remove the temporary database from settings.py and uncomment the original code, then push the code to origin.
14.  Back to in **Heroku dashboad**, deploy the application.
15.  To view the site, click on **View App**.

### Hosting Media files in AWS ###

The *static* and *media file*s* are hosted in the [AWS S3 Bucket](https://aws.amazon.com/). To host them, you need to create an account in AWS and create your S3 basket with **public access**. More about setting it up you can read in [Amazon S3 documentation](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html) and this [tutorial](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html).

[Back to content](#contents)

---

## Credits ##

### Images ###

### Image editing ###

- I have used the snippet tool for capturing screengrabs which I saved as images.
- MS Paint 3D to edit images as required.
- A handy [Birme](https://www.birme.net/?target_width=300&target_height=300&quality=100&border_width=1&border_color=%23bd3d3a) site allowed me to resize the images all at once.
- I have also used [giphy.com](https://giphy.com/) to convert MP4 video files to gif files used in Testing.md.

### Code ideas ###


[Back to content](#contents)

---

## Acknowledgements ##


[Back to content](#contents)
