# LIS4905_5900 Directed Independent Study

## Mark K. Jowett, Ph.D.

### Week 15 Requirements:

1. Meet as a team: 

    a. Invoke **git pull** (updates local version of repository to latest version of remote repository)
	
	b. Review updated project and test CRUD functionality in all project areas, including *history* tables using **both** valid and invalid data.
	
	
2. Team Assignments:
	
	a. Update **all** tables to permit atypical (but, necessary) characters in *notes* attribute. Possible scenarios:
		
		1. Additional e-mail addresses added to *instructor* table (would require *@* symbol).
		2. Possible required use of following characters in other *notes* attributes: <, >, /, (, ), etc.
		3. **However**, **be sure** to use htmlspecialchars() function when displaying data, to mitigate against cross-site scripting (XSS) attacks.

3. **Be sure** to include login functionality, and use similar color/design as per existing project.

4. Divide above responsibilities **equally** among team members.


5. Push to "lis4905_5900_fall19" repo.

6. Demo: solution for masking sensitive data, and git file versions.
