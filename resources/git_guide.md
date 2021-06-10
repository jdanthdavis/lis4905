# **Git Guide - Workflow**

### ***Get Initial Work!***
1. Clone repo (if available, creates local repo)
   ```
   git clone path_to_repo
   ```

**Or...**

2. Create repo - ***YOU*** own it! (**For our work, it is already available**--so do ***NOT*** create a new one!)  
**However,** if it were **not** already available--create a new one: [Remote Repos: Initial push](http://www.qcitr.com/usefullinks.htm#lesson6 "Remote Repos: Initial push")

### 1. ***Create (or checkout) develop branch from master***
**checkout:** Switch branches or restore working tree files.  
Updates files in working directory to match version stored in that branch.

1. Switch to master branch (or restores working tree files).
   ```
   git checkout master
   ```
2. Switch to develop branch, -b option creates new branch, then checks out.  
**Note:** -b option *will* cause error, if branch already created!
   ```
   git checkout -b develop
   ```


### 2. ***Display all branches and local/remote branch tracking***

1. Display all branches
**Note:** -a option displays *all* branches!
   ```
   git branch -a
   ```
2. Check local/remote branch tracking
   ```
   git branch -vv   # doubly verbose (displays local/remote associations)
   ```


### 3. ***Set local/remote branch tracking***
**Note:** *ONLY* set *develop* branch (*not* your other branches, or push other branches to remote repo)--also, master branch should already be set.  

1. If develop branch checked out: 
   ```
   git branch -u origin/develop
   ```
2. If *not* on develop branch:
   ```
   git branch -u origin/develop develop
   ```
3. Now, pushing and pulling simple!
   ```
   git pull or git push
   ```
4. Also, very helpful git status command displays state of working directory and staging area!
   ```
   git status
   ```


### 4. ***Create (or checkout) feature branch(es) from develop***
"***feature***" branch can be a new feature, or a fix.  

1. Switch to feature branch, -b option creates new branch, then checks out.  
**Note:** -b option *will* cause error, if branch already created!
   ```
   git checkout -b feature_branch
   ```
2. For our development use this format (**branch-type**="feat" or "fix"):
   ```
   firstinitiallastname_branch-type_branch-name-id
   Example: jdoe_feat_update-project-1
   ```


### 5. ***Do *ALL* work on feature branch(es)!***
**Note:** ***After*** checking out **your** feature branch!  

1. Do work, test and fix!

2. Stage changes
   ```
   git add .
   ```
3. Commit changes
   ```
   git commit -m "your commit description"
   ```


### 6. ***Get latest updates from develop branch***
After your changes are committed to your local branch, get latest updates from "develop" branch.  
Steps below make sure your **local** *develop* branch is up to date with your **remote** *develop* branch before pushing changes!

1. Switch to develop branch
   ```
   git checkout develop
   ```
2. Get latest changes from remote develop branch
   ```
   git pull
   ```
3. Switch back to your branch
   ```
   git checkout yourbranch
   ```
4. Merge develop branch into your branch
   ```
   git merge develop
   ```


### 7. ***After feature branch(es) tested, merge/push into develop***
**Note:** Each "*feature*" branch **MUST** be tested, prior to pushing to develop branch!  

1. Check current branch
   ```
   git status
   ```
2. Switch to develop branch (if necessary)
   ```
   git checkout develop
   ```
3. merge feature branch changes into develop
   ```
   git merge feature_branch
   ```
4. **Be sure** on develop branch!
   ```
   git status
   ```
5. **After** testing/fixing, push your changes to remote develop branch
   ```
   git push
   ```


### 8. ***DO ONLY IF YOU OWN REPO: After develop tested, merge/push into master***
**Note:** ***Do NOT*** merge/push to master, ***UNLESS YOU OWN IT!***  
**Note:** "*develop*" branch **MUST** be tested, prior to pushing to master branch!  

1. **After** working on ***your*** branch, **Step 5 (above)**, switch to develop branch
   ```
   git checkout develop
   ```
2. Get latest changes from remote develop branch
   ```
   git pull
   ```
3. Switch to your branch
   ```
   git checkout yourbranch
   ```
4. Merge develop branch into your branch
   ```
   git merge develop
   ```
5. Switch to develop branch
   ```
   git checkout develop
   ```
6. merge your branch changes into develop
   ```
   git merge yourbranch
   ```
7. Switch to master branch
   ```
   git checkout develop
   ```
8. merge develop into master
   ```
   git merge develop
   ```
9. **Be sure** on master branch!
   ```
   git status
   ```
10. **After** testing/fixing, push your changes to remote master branch
   ```
   git push
   ```
11. Switch to develop branch
   ```
   git checkout develop
   ```
12. **Be sure** on develop branch!
   ```
   git status
   ```
13. **After** testing/fixing, push your changes to remote develop branch
   ```
   git push
   ```


### 9. ***DON'T FORGET TO PUSH--see above!***
**Note:** ***Do NOT*** merge/push to master, ***UNLESS YOU OWN IT! :)***

1. Switch to develop, if necessary (*after* merging feature_branch into develop)
   ```
   git checkout develop
   ```

2. Push local develop to remote develop
   ```
   git push
   ```

3. Switch to master, if necessary (*after* merging develop into master)
   ```
   git checkout master
   ```

4. Push local master to remote master
   ```
   git push
   ```

### 10. ***Cleanup!***
**Note:** Remove **ALL** "*feature*" branches (local *and* remote) after successful merge/push into master/develop branches!  

1. Display all branches (-a option displays *all* branches)
   ```
   git branch -a
   ```

2. Delete ***local*** feature branch
   ```
   git branch -d feature_branch
   ```

3. Delete ***remote*** feature branch
   ```
   git branch -d -r origin/branchname
   ```

### 11. ***Comparing branches!***

1. Compare local branch with its remote branch:
   ```
   git fetch
   ```

2. Then, diff branches
   ```
   git diff <local branch> <remote>/<remote branch>
   Example: git diff develop origin/develop
   ```

3. Compare two (local) branches (displays all commits in branch2 that are *not* in branch1): ***must*** use *two* dots.
   ```
   git diff branch1..branch2
   Example: git diff develop..branchname
   ```


# Notes:
### Generally, **three** branch types:  
1. **master**: Production code only--***NO** bugs!
2. **develop**: This branch will be the "live" version of your software.   
If you are working on a team, this is the branch that developers will push to on a regular basis with new features.
3. **feature**: Can be *many*** "feature" branches--depending upon team size.  
**Note:** Each "*feature*" branch **MUST** be tested, prior to merging/pushing to **"develop"** branch.  
***Features should never interact directly with master!***  
For us, "*feature*" branch can be new feature, or fix (see example above).

### Pull requests
1. Why? Tell others about changes you've pushed to a branch in a remote repo.  
[About pull requests](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests "About pull requests")  
2. Provide opportunities for code review!
3. Example: Submit your pull request making sure to select  ***develop*** as branch for merging!
   
### Some important commands:
- git status # displays state of working directory and staging area
- git branch # displays local branches
- git branch -r # displays remote branches
- git branch -a # displays *all* branches
- git branch -vv # doubly verbose (displays local/remote associations)
- git log  
  **Note:** **Very** important to know where HEAD is pointing!  
  **Example:** (HEAD -> master, origin/master)
- git log --oneline --decorate --graph --all # look 'em up! ;)
- git fetch # brings in new data from remote repository, but does *not* integrate!
- git pull # like git fetch and git merge; brings local branch up-to-date with its remote branch
- If remote branch deleted, but still appears in "git branch -a":
- git remote prune origin # will remove all stale branches
- git fetch -p (or git pull -p) # remote branches will be pruned  
("Pruning" cleans up unreachable or "orphaned" Git objects.)
- **git code letters**:
    - A = added
    - C = copied
    - D = deleted
    - M = modified
    - R = renamed
    - T = change in type
    - U = updated but unmerged
    - X = "unknown" change type (likely bug, report it)
- **Remove folder/directory from remote repo, but *not* from local:**
   ```
   git rm -r --cached FolderName
   git commit -m "Removed folder from remote repo"
   git push
   ```


### Example Git Work Flow (***ONLY*** do in ***your own*** practice repo):
   ```
   git init (initializes repo in current directory)
   touch myfile.txt (creates file w/o any content)
   git status (checks status - new file *not* staged or tracked)
   git add myfile.txt (stages file, but not yet committed)
   git status (displays staged file, not yet committed)
   git commit -m "your commit message" (commits file with message)
   git status (displays nothing to commit)
   (Note: If previously pushed files, displays branch is ahead of master, w/number of commits)
   (add text to myfile.txt)
   git status (Displays "Changes not staged for commit:")
   git add . (stages **all** new and modified files, but not deleted files)
   git commit -m "added text to myfile.txt" (commits change)
   git log (displays log of all commits, in reverse chronological order, with its SHA-1 checksum)
   git log --oneline --decorate --graph --all (research these options ;)
   (create another file called "myfile2.txt")
   cat > myfile2.txt
   Hello World!
   Press Ctrl+d, Ctrl+c
   git status (displays new file *not* tracked)
   git add .
   git commit -m "added second file"
   git log --oneline (terse log display) 
   ls -al (lists files in current directory, including hidden files, and in long format)
   git checkout [commitID] (use commitID of "added text to myfile.txt" commit)
   ls -al (checkout commandID reverted back in time--now **only** one file!)
   git checkout master (switch to master branch--**now** back to two files!)
   ls -al (list directory files)
   git branch (displays all branches)
   (create branch to do work)
   git branch not-good (creates not-good branch)
   git branch (displays branches, master is starred--currently used!)
   git checkout not-good (switch to not-good branch)
   git branch (displays branches, and currently used branch!)
   (add file called "test.txt")
   cat > test.txt
   Only a test!
   Press Ctrl+d, Ctrl+c
   git add .
   git commit -m "Hmm, probably not good! :)"
   git log --oneline (pay particular attention to HEAD!)
   ls -al (check test.txt is in current directory)
   git checkout master (switch master branch)
   ls -al (test.txt **gone**!)
   (Try this again! ;)
   git branch is-good (create new branch is-good)
   git checkout is-good (switch to new branch)
   git branch (verify current branch)
   (create new file "newfile.txt")
   cat > newfile.txt
   Another test!
   Press Ctrl+d, Ctrl+c
   ls -al (verify "newfile.txt" is there, and "test.txt" not there!)
   git add .
   git commit -m "added newfile.txt"
   git branch (verify current branch)
   git checkout master (switch to master branch)
   git branch (verify current branch)
   git diff is-good master (check for conflicts between branches--if so, fix conflicts!)
   git merge is-good (merge is-good branch with master)
   ```
