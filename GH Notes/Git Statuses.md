# Local Branches
## Show branches

Prints Local branches

`git branch [Options]`

Options:
* -r | Remote Branches
* -a | All Branches, local and remote

## Show Current Branch
Print status of current branch

`git status [Options]`

Options:
* -sb | Short Branch, Shows remote branch local is tracking

## Create New Branch
Just create branch \
`git branch new_branch`

You can checkout a new branch you create in one line \
`git checkout -b new_branch`

## Delete Local Branches
Make sure your changes are saved or merged with other branches before deleting a branch

`git branch -d branch_to_delete`

## Delete Remote Branches
Make sure you delete the local first to be sure it's safe to delete remote.
You have to push a delete command to remote to delete it

`git push origin --delete remote branch_to_delete`

## Rename Local Branch
You can rename a local branch

`git branch -m branch_name new_branch_name`

- - - -

# Remote Branches
## View Remote Branches
Use show to view all branches and which remote branches the local ones are tracking

`git remote show origin`

## Checkout Remote Branches
In 'detached' mode you can see remote branches by checking them out

`git checkout origin/remote_branch`

This won't save and you can clear all changes by checking out a different branch

# Save Remote Branch as Local
You will have to create a new local branch then pull the changes from remote

`git checkout -b local_branch`

`git pull origin remote_branch`

To set upstream, you will have to push to the remote branch and set upstream

`git push --set-upstream origin remote_branch`

# Tracking Remote Branch
Once on a local branch you can make it track a remote branch