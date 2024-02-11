<br/>
<p align="center">
  <a href="https://github.com/abtinmbm/FBLA2024">
    <img src="https://raw.githubusercontent.com/abtinmbm/FBLA2024/main/media/school.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">School Partner Directory</h3>

  <p align="center">
    A platform to facilitate meaningful partnerships between schools and external stakeholders, fostering a collaborative ecosystem that enriches educational experiences and empowers students to thrive in a dynamic world.
    <br/>
    <br/>
    <a href="https://fbla2024.pythonanywhere.com">View Demo</a>
    .
    <a href="https://github.com/abtinmbm/FBLA2024/issues">Report Bug</a>
    .
    <a href="https://github.com/abtinmbm/FBLA2024/issues">Request Feature</a>
  </p>
</p>



## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)

## About The Project

Welcome to the School Partner Resource Directory, an innovative platform developed for the FBLA2024 competition, designed to bridge the gap between schools, community organizations, government entities, and businesses. Our platform serves as a dynamic hub where schools can seamlessly connect with partners across various sectors, empowering students to discover valuable opportunities for growth and collaboration.

Comprehensive Partner Database: Our platform hosts an extensive directory of partners from diverse sectors, including local businesses, government agencies, nonprofit organizations, and community groups, providing schools with a rich ecosystem of potential collaborators.

Customized Profiles: Partners can create detailed profiles showcasing their mission, services, and areas of expertise, allowing schools to make informed decisions when seeking collaborations that align with their goals and values.

Resource Sharing: Partners can share resources such as educational materials, internship opportunities, volunteer programs, and career development initiatives, empowering schools to provide students with valuable learning experiences beyond the classroom.



## Built With

- Our project is built with Django for a solid foundation.
- We use django-admin-interface for streamlined content management.
- django-ckeditor-5 enables dynamic content creation.
- Security is ensured with django-recaptcha.
- Image processing is handled with Pillow.
- HTML, CSS, and Tailwind CSS ensure sleek aesthetics and responsiveness.
- Fast and relevant search results are provided by Fuse.js.
- Smooth interactivity is achieved with jQuery.





## Getting Started


### Prerequisites

Clone the repo:

```sh
git clone https://github.com/abtinmbm/FBLA2024.git
```

### Installation

To install the required packages, run the following command
`pip install -r requirements.txt`




## Usage

After modifying models, new migrations must be generated:
`python manage.py makemigrations`

The generated migrated files must be applied to the database:
`python manage.py migrations`

You may import demo data with the following command:

`python manage.py loaddata demo`

Finally, run the server:

`python manage.py runserver`

#### RESET COMMAND (DESTRUCTIVE)
Alternatively, the following commands can be used to destructively reset the server in one line:
##### WINDOWS (LOCAL)
`rm db.sqlite3 | python manage.py makemigrations | python manage.py migrate | python manage.py loaddata demo | python manage.py runserver`
##### Linux (python-anywhere)
`python manage.py makemigrations && python manage.py migrate && python manage.py loaddata demo`
