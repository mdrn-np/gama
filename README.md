![Logo](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/th5xamgrr6se0x5ro4g6.png)

# Gama

Our project revolves around the idea of building a browser extension that empowers users to navigate the web with confidence by detecting and warning them about phishing sites, fake reviews, and other online threats.

## Requirements

- Python 3.11
- Whois cli
- pip

## Installation

Install gama with git & pip

```bash
    > git clone https://github.com/PhuyalGaurav/gama.git
    # now be in the gama folder & make a venv
    > cd gama
    \gama> python -m venv venv
    # install all the dependencies
    \gama> venv\Scripts\activate
    (venv) .. \gama> pip install -r requirements.txt


```

## Deployment

To deploy this project run

```bash
  # be in the root gama folder
  # make sure you have your venv activated
  \gama>venv\Scripts\activate
  (venv) .. \gama> cd backend
  (venv) .. \gama\backend> python app.python
  # Now the local server should be running
```

## API Reference

#### Check For phishing

```http
  GET /phishing?url=
```

| Parameter          | Type     | Description                                     |
| :----------------- | :------- | :---------------------------------------------- |
| `url` **Required** | `string` | Gives true if phishing link detected else false |

#### Get all reports

```http
  GET /reports
```

| Parameter | Type | Description                                                     |
| :-------- | :--- | :-------------------------------------------------------------- |
| None      | none | Returns all the reports that are repoted by user (saved on db). |

#### Get details about a website

```http
  GET /details?url=
```

| Parameter | Type   | Description                                      |
| :-------- | :----- | :----------------------------------------------- |
| url       | string | the link of the website whose details is neededs |

| value returned     | Type   | Description                                                     |
| :----------------- | :----- | :-------------------------------------------------------------- |
| Name               | string | Returns all the reports that are repoted by user (saved on db). |
| registrar          | string | The registrar of the domain.                                    |
| registrant_country | string | The country of the registrant.                                  |
| creation_date      | Date   | The date when the domain was created.                           |
| expiration_date    | Date   | The date when the domain will expire.                           |
| last_updated       | Date   | The date when the domain was last updated.                      |
| dnssec             | bool   | The registrant of the domain.                                   |
| registrant         | string | Returns all the reports that are repoted by user (saved on db). |
| emails             | string | The associated emails of the domain.                            |
| country_name       | string | The country name of the domain.                                 |

#### Report a website by a user

```http
  POST /report
```

| Parameter | Type   | Description                                  |
| :-------- | :----- | :------------------------------------------- |
| Url       | string | url of the website which is to be blocked    |
| reason    | string | the reason why the website should be blocked |

#### Report a mis identified website by a user

```http
  POST /report_mistake
```

| Parameter | Type   | Description                                    |
| :-------- | :----- | :--------------------------------------------- |
| Url       | string | url of the website which is to be unblocked    |
| reason    | string | the reason why the website should be unblocked |

#### Check if a review is real of fake through ML

```http
  POST /review
```

| Parameter | Type   | Description                       |
| :-------- | :----- | :-------------------------------- |
| review    | string | The review which is to be checked |

| Value returned | Type | Description            |
| :------------- | :--- | :--------------------- |
| prediction     | bool | True if review is fake |

#### Check if a news is real of fake through ML

```http
  POST /news
```

| Parameter | Type   | Description                     |
| :-------- | :----- | :------------------------------ |
| news      | string | The news which is to be checked |

| Value returned | Type | Description            |
| :------------- | :--- | :--------------------- |
| prediction     | bool | True if review is fake |

#### Make a specic review to primary check

```http
  PUT /reports/{id}?real=
```

| Parameter | Type    | Description                                   |
| :-------- | :------ | :-------------------------------------------- |
| id        | integer | the id of the report to be made ture or false |
| real      | bool    | The boolen value of the report to be set.     |

## Usage/Examples

After the server has been set up. Add the frontend extention to your web browser

## Appendix

Any additional information goes here

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Authors

![Logo](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/th5xamgrr6se0x5ro4g6.png)

# Gama

Our project revolves around the idea of building a browser extension that empowers users to navigate the web with confidence by detecting and warning them about phishing sites, fake reviews, and other online threats.

## Requirements

- Python 3.11
- Whois cli
- pip

## Installation

Install gama with git & pip

```bash
    > git clone https://github.com/PhuyalGaurav/gama.git
    # now be in the gama folder & make a venv
    > cd gama
    \gama> python -m venv venv
    # install all the dependencies
    \gama> venv\Scripts\activate
    (venv) .. \gama> pip install -r requirements.txt


```

## Deployment

To deploy this project run

```bash
  # be in the root gama folder
  # make sure you have your venv activated
  \gama>venv\Scripts\activate
  (venv) .. \gama> cd backend
  (venv) .. \gama\backend> python app.python
  # Now the local server should be running
```

## API Reference

#### Check For phishing

```http
  GET /phishing?url=
```

| Parameter          | Type     | Description                                     |
| :----------------- | :------- | :---------------------------------------------- |
| `url` **Required** | `string` | Gives true if phishing link detected else false |

#### Get all reports

```http
  GET /reports
```

| Parameter | Type | Description                                                     |
| :-------- | :--- | :-------------------------------------------------------------- |
| None      | none | Returns all the reports that are repoted by user (saved on db). |

#### Get details about a website

```http
  GET /details?url=
```

| Parameter | Type   | Description                                      |
| :-------- | :----- | :----------------------------------------------- |
| url       | string | the link of the website whose details is neededs |

| value returned     | Type   | Description                                                     |
| :----------------- | :----- | :-------------------------------------------------------------- |
| Name               | string | Returns all the reports that are repoted by user (saved on db). |
| registrar          | string | The registrar of the domain.                                    |
| registrant_country | string | The country of the registrant.                                  |
| creation_date      | Date   | The date when the domain was created.                           |
| expiration_date    | Date   | The date when the domain will expire.                           |
| last_updated       | Date   | The date when the domain was last updated.                      |
| dnssec             | bool   | The registrant of the domain.                                   |
| registrant         | string | Returns all the reports that are repoted by user (saved on db). |
| emails             | string | The associated emails of the domain.                            |
| country_name       | string | The country name of the domain.                                 |

#### Report a website by a user

```http
  POST /report
```

| Parameter | Type   | Description                                  |
| :-------- | :----- | :------------------------------------------- |
| Url       | string | url of the website which is to be blocked    |
| reason    | string | the reason why the website should be blocked |

#### Report a mis identified website by a user

```http
  POST /report_mistake
```

| Parameter | Type   | Description                                    |
| :-------- | :----- | :--------------------------------------------- |
| Url       | string | url of the website which is to be unblocked    |
| reason    | string | the reason why the website should be unblocked |

#### Check if a review is real of fake through ML

```http
  POST /review
```

| Parameter | Type   | Description                       |
| :-------- | :----- | :-------------------------------- |
| review    | string | The review which is to be checked |

| Value returned | Type | Description            |
| :------------- | :--- | :--------------------- |
| prediction     | bool | True if review is fake |

#### Check if a news is real of fake through ML

```http
  POST /news
```

| Parameter | Type   | Description                     |
| :-------- | :----- | :------------------------------ |
| news      | string | The news which is to be checked |

| Value returned | Type | Description            |
| :------------- | :--- | :--------------------- |
| prediction     | bool | True if review is fake |

#### Make a specic review to primary check

```http
  PUT /reports/{id}?real=
```

| Parameter | Type    | Description                                   |
| :-------- | :------ | :-------------------------------------------- |
| id        | integer | the id of the report to be made ture or false |
| real      | bool    | The boolen value of the report to be set.     |

## Usage/Examples

After the server has been set up. Add the frontend extention to your web browser

## Appendix

Any additional information goes here

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Authors

- [@octokatherine](https://www.github.com/octokatherine)

![Logo](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/th5xamgrr6se0x5ro4g6.png)

# Gama

Our project revolves around the idea of building a browser extension that empowers users to navigate the web with confidence by detecting and warning them about phishing sites, fake reviews, and other online threats.

## Requirements

- Python 3.11
- Whois cli
- pip

## Installation

Install gama with git & pip

```bash
    > git clone https://github.com/PhuyalGaurav/gama.git
    # now be in the gama folder & make a venv
    > cd gama
    \gama> python -m venv venv
    # install all the dependencies
    \gama> venv\Scripts\activate
    (venv) .. \gama> pip install -r requirements.txt


```

## Deployment

To deploy this project run

```bash
  # be in the root gama folder
  # make sure you have your venv activated
  \gama>venv\Scripts\activate
  (venv) .. \gama> cd backend
  (venv) .. \gama\backend> python app.python
  # Now the local server should be running
```

## API Reference

#### Check For phishing

```http
  GET /phishing?url=
```

| Parameter          | Type     | Description                                     |
| :----------------- | :------- | :---------------------------------------------- |
| `url` **Required** | `string` | Gives true if phishing link detected else false |

#### Get all reports

```http
  GET /reports
```

| Parameter | Type | Description                                                     |
| :-------- | :--- | :-------------------------------------------------------------- |
| None      | none | Returns all the reports that are repoted by user (saved on db). |

#### Get details about a website

```http
  GET /details?url=
```

| Parameter | Type   | Description                                      |
| :-------- | :----- | :----------------------------------------------- |
| url       | string | the link of the website whose details is neededs |

| value returned     | Type   | Description                                                     |
| :----------------- | :----- | :-------------------------------------------------------------- |
| Name               | string | Returns all the reports that are repoted by user (saved on db). |
| registrar          | string | The registrar of the domain.                                    |
| registrant_country | string | The country of the registrant.                                  |
| creation_date      | Date   | The date when the domain was created.                           |
| expiration_date    | Date   | The date when the domain will expire.                           |
| last_updated       | Date   | The date when the domain was last updated.                      |
| dnssec             | bool   | The registrant of the domain.                                   |
| registrant         | string | Returns all the reports that are repoted by user (saved on db). |
| emails             | string | The associated emails of the domain.                            |
| country_name       | string | The country name of the domain.                                 |

#### Report a website by a user

```http
  POST /report
```

| Parameter | Type   | Description                                  |
| :-------- | :----- | :------------------------------------------- |
| Url       | string | url of the website which is to be blocked    |
| reason    | string | the reason why the website should be blocked |

#### Report a mis identified website by a user

```http
  POST /report_mistake
```

| Parameter | Type   | Description                                    |
| :-------- | :----- | :--------------------------------------------- |
| Url       | string | url of the website which is to be unblocked    |
| reason    | string | the reason why the website should be unblocked |

#### Check if a review is real of fake through ML

```http
  POST /review
```

| Parameter | Type   | Description                       |
| :-------- | :----- | :-------------------------------- |
| review    | string | The review which is to be checked |

| Value returned | Type | Description            |
| :------------- | :--- | :--------------------- |
| prediction     | bool | True if review is fake |

#### Check if a news is real of fake through ML

```http
  POST /news
```

| Parameter | Type   | Description                     |
| :-------- | :----- | :------------------------------ |
| news      | string | The news which is to be checked |

| Value returned | Type | Description            |
| :------------- | :--- | :--------------------- |
| prediction     | bool | True if review is fake |

#### Make a specic review to primary check

```http
  PUT /reports/{id}?real=
```

| Parameter | Type    | Description                                   |
| :-------- | :------ | :-------------------------------------------- |
| id        | integer | the id of the report to be made ture or false |
| real      | bool    | The boolen value of the report to be set.     |

## Usage/Examples

After the server has been set up. Add the frontend extention to your web browser
. Make sure that developer mode is enabled.

![Alt text](image.png)

## Appendix

Any additional information goes here

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Authors

- [@octokatherine](https://www.github.com/octokatherine)

- [@octokatherine](https://www.github.com/octokatherine)
