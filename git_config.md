Setup username and email

```bash
git config --global user.name "USERNAME"
git config --global user.email "EMAIL@ADDRESS.com"
```

Then store the credential
```bash
git config --global credential.helper store
```

Finally create a token in github on settings -> Developer settings -> Personal access tokens. Then copy the new created token and paste while pushing a commit.
