# Git Notes

- - - -

# Setup

## User Setup
Once you create an account on Github, you can 

- - - -

# Repository Checks and Changes

## Fetch Changes

Fetches changes from remote and saves to your local repo,
it won't update any files just will show you changes that will happen

`git fetch`

## Pull Changes

Updates your repo and pulls changes from remote to update your local code

`git pull`

You can pull for a specific branch from remote 

`git pull origin remote_branch_name`

## Push Changes

Pushes your local commits to the remote repo

`git push`

## Check Staging Area

Show all status for branch, staging area.
Be sure to fetch changes to see if your repo is up to date before checking status

`git status`

- - - -

# Merging Branches


## Preparing
1. Make sure your staging area is clear, because merging may write over any files.
2. Make sure your branches are all up to date before merging.
3. Checkout the branch you want to merge into first

`git checkout master`

4. Then try merging a branch into that branch you're currently on

`git merge branch_to_merge_from`

You can also specify branch to merge to and from

`git merge branch_from branch_to`

## Fast-Forward Merge
If there are no issues, you can just push your changes to save.

If any conflicts occur, go to the files and fix them

````bash
<<<<<<< HEAD
head content
=======
branched content
>>>>>>> branch_to_merge
````
You can also use merge tools like Mend

To set a mergetool globally:

`git config --global merge.tool meld`

Then it will be used when calling mergetool

`git mergetool`

Or specify a tool

`git mergetool --tool=meld`

Once you fix the errors, commit the change to finish merging.

- - - -

## Troubleshooting
If you fail the merge or have to go back, you can checkout the branch again

`git checkout`

You can reset the staging area and undo changes to files

`git reset --mixed`

Or abort the merge altogether

`git merge --abort`
