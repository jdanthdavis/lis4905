# **Git Guide**

### ***Get Initial Work!***
1. Clone repo (if available, creates local repo)
   ```
   git clone path_to_repo
   ```

**Or...**

2. Create repo (**It is already available**--so do ***NOT*** create a new one!)  
**However,** if it were **not** already available--create a new one: [Remote Repos: Initial push](http://www.qcitr.com/usefullinks.htm#lesson6 "Remote Repos: Initial push")

### 1. ***Create develop Branch from master***
**checkout:** Switch branches or restore working tree files.  
Updates files in working directory to match version stored in that branch.

1. Switch to master branch (or restore working tree files).
   ```
   git checkout master
   ```
2. Switch to develop branch, -b option creates new branch, then checks out.  
**Note:** -b option *will* cause error, if branch already created!
   ```
   git checkout -b develop
   ```


### 2. ***Create feature Branch(es) from develop***
"***feature***" branch can be a new feature, or a fix.  

1. Switch to feature branch, -b option creates new branch, then checks out.  
**Note:** -b option *will* cause error, if branch already created!
   ```
   git checkout -b feature_branch
   ```
2. For our development use this format (**branch-type**="feat" or "fix"):
   ```
   <firstinitiallastname>_<branch-type>_<branch-name>  
   ```
3. Do work, test and fix!


### 3. ***After feature Branch(es) Tested, merge into develop***
**Note:** Each "*feature*" branch **MUST** be tested, prior to pushing to develop branch!  

1. Switch to develop branch.
   ```
   git checkout develop
   ```
2. merge into develop
   ```
   git merge feature_branch
   ```
3. Test and fix!


### 4. ***After develop Tested, merge into master***
**Note:** "*develop*" branch **MUST** be tested, prior to pushing to master branch!  

1. Switch to master branch.
   ```
   git checkout master
   ```
2. merge into master
   ```
   git merge develop
   ```
3. Test and fix!


### 5. ***Cleanup!***
**Note:** Remove any "*feature*" branches after successful merge into master branch!  

1. Remove feature branch
   ```
   git branch -d feature_branch
   ```


# ***Commiting and Pushing Changes (Your Work)!***

### 1. ***Commit your changes to your local branch***
Stage and commit **your** changes to **your** local branch *first*.

1. **Note:** This is done **after** checking out **your** feature branch!
2. Stage changes
   ```
   git add .
   ```
3. Commit changes
   ```
   git commit -m "your commit description"
   ```

### 2. ***Get Latest Updates from develop Branch***
Now that your changes are committed to your local branch, get latest updates from "develop" branch.  
Steps make sure **your** local branch is up to date with "develop" branch before pushing **your** changes to remote repo!

1. Switch to develop branch.
   ```
   git checkout develop
   ```
2. Get latest changes from remote repo
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
5. **After** testing/fixing, push your changes to remote repo
   ```
   git push
   ```
6. Submit your pull request on Bit Bucket making sure to select  ***develop*** as the branch for merging!

# Notes:
### Generally, **three** branch types:  
1. **master**: Production code only--***NO** bugs!
2. **develop**: This branch will be the "live" version of your software.   
If you are working on a team, this is the branch that developers will push to on a regular basis with new features.
3. **feature**: Can be *many*** "feature" branches--depending upon team size.  
**Note:** Each "*feature*" branch **MUST** be tested, prior to pushing to "develop" branch.  
Also, "*feature*" branch can be a new feature, or a fix.

### Some important commands:
- git status
- git branch
- git log  
  **Note:** **Very** important to know where HEAD is pointing!  
  **Example:** (HEAD -> master, origin/master)
- Also, git log --oneline --decorate --graph --all (look em up! ;)

### Workflow model:
1. git checkout master
2. git checkout -b develop
3. git checkout -b feature_branch  
  # do work, test and fix!
4. git checkout develop
5. git merge feature_branch  
  # test and fix!
6. git checkout master
7. git merge develop
8. git branch -d feature_branch

### Overall workflow:
1. develop branch created from master
2. feature branch(es) created from develop
3. After feature branch(es) tested, merge into develop
4. After develop tested, merge into master
5. Delete feature branch(es)
6. If issue in master, create feature (fix) branch from master
7. When feature (fix) branch tested, merge into both develop and master
8. Delete feature (fix) branch

### Example Git Work Flow:
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
