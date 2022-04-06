# Installation
`sudo apt install git`

# SSH - Setup
Create SSH key for project

`ssh-keygen`

Then add the public key to Github's settings

# Config
`nano ~/.ssh/config`

And add the following for git

```bash
# Github
Host github.com
        User git
        Hostname ssh.github.com
        PreferredAuthentications publickey
        IdentityFile ~/.ssh/gh_notes # Add your own key here

```
