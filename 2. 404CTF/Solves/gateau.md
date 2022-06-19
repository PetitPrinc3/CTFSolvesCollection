# Du Gateau

Cookies are :

```
username=user;password=sha512(password)
```

With a known username and pasword, create Cookies

```
username=user;username=admin;password=sha512(password)
```

> Get the admin sha512 in the password recovery source page

Alter the last letter of the base64 cookie and voilà
