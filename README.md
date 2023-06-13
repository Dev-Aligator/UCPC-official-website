# UCPC Registration System





<!-- Banner -->

<center><a href="https://github.com/Dev-Aligator/UCPC-official-website" title="UCPC-Official-website"><img src="/home/aligator/UCPC_WebRegistration/register/static/register/images/layout2023/background.png" width="960" height="540"></a></center>
<!-- style="max-width=100%;" -->
<!-- Status -->




[![](https://img.shields.io/website?style=for-the-badge&url=https://ucpc.uit.edu.vn/info/)](https://ucpc.uit.edu.vn/info/)

**UCPC-official-website** is the official **registration** website for UCPC 2023 - the twelve season of the UIT Collegiate Programming Contest. Built with Django, it enables contestants to register and participate in the contest, and organizers to manage the evenot and publish results. This repositry contains all code and resources needed to run the website


### Tech Stack

- HTML, CSS and Javascript
- Python <a href="https://docs.djangoproject.com/en/3.1/">Django</a> Framework

Hit <a href="#" title="Star SwiftSend" target="_self">:star2:</a> to show some :heart:

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Development Environment Setup: Linux


<details>
<summary>
Step 1: Installing Python 3.10
</summary>
<br>
Download <a href="https://www.python.org/downloads/">Python 3.10 or higher</a>
<br><br>

```bash
  sudo pacman -S python3  # If you're using an Arch-based Distro
```

</ul>

Verify the installation from the command prompt (Terminal) using the following command,

```bash
  python --version
```

Installed version of python will be printed.
</details>

---

<details>
<summary>
Step 2: Installing Git
</summary>
<br>

```bash
  sudo pacman -S git
```

</details>

---

<details>
<summary>
Step 3: Clone the Repository
</summary>
<br>

```bash
  git clone https://github.com/Dev-Aligator/UCPC-official-website.git
```

</details>

---


<details>
<summary>
Step 4: Creating Virtual Environment
</summary>
<br>
Install virtualenv
<br><br>

```bash
pip3 install virtualenv
```

Creating Virtual Environment named `myvenv`

```bash
virtualenv myvenv -p python3.10
```

To Activate `myvenv`

```bash
myvenv\Scripts\activate
```

To deactivate `myvenv`

```bash
deactivate
```
</details>

---

<details>
<summary>
Step 5: Installing Requirements
</summary>
<br>
Note: Before installing requirements, Make sure Virtual Environment is activated.
<br><br>

```bash
pip install -r requirements.txt
```
</details>

---

<details>
<summary>
Step 6: Making database migrations
</summary>
<br>

```bash
python manage.py makemigrations
python manage.py migrate
```
</details>

---

<details>
<summary>
Step 7: Creating superuser to access Admin Panel
</summary>
<br>

```bash
python manage.py createsuperuser
```
</details>

---

<details>
<summary>
Step 8: Running the Project in local server
</summary>
<br>
<b>Note:</b> Before running the project in local server, Make sure you activate the Virtual Environment.
<br><br>

```bash
python manage.py runserver
```
</details>

---




<p align="center">Dev-Aligator</p>
<p align="center">
<a href="https://github.com/Dev-Aligator/">
<img src="https://user-images.githubusercontent.com/58631762/120077716-60cded80-c0c9-11eb-983d-80dfa5862d8a.png" width="19">
</a>