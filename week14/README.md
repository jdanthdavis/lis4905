# LIS4905_5900 Directed Independent Study

## Mark K. Jowett, Ph.D.

### Week 14 Requirements:

1. Meet as a team: 

    a. Invoke **git pull** (updates local version of repository to latest version of remote repository)
	
	b. Review updated project database: deleted **prc_notes** attribute in **program_course** table.
	
	
2. **Be sure that the following triggers have been modified as per Week12 recorded discussion**: also, *be sure* to match the attribute requirements of the history tables:
   
	a. insert/update triggers for **course_pref_history** table
	   
	b. insert/update triggers for **course_history** table	


3. Team Assignments:
	
	a. Add CRUD functionality to the **program_course** table, with the following requirements--**Note: No need to create additional user interfaces.**:
		
		1. Adding or modifying a **course** allows multiple **programs** to be added or removed from that particular **course**.  
		(**Note**: no need to provide same functionality to *program* area.")
		2. Deleting a course deletes all associated programs to that particular course.
		3. Deleting a program deletes all associated courses to that particular program.
	
4. Divide above responsibilities **equally** among team members.


5. Push to "lis4905_5900_fall19" repo.
