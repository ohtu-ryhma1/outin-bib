# End Report
**Team members**
- Halla-Aho Veeti
- Petrova Anastasia
- Hätönen Leevi
- Kauhanen Markus

**Course:** Ohjelmistotuotanto

**Period:** 2/25

## 1. Project Overview
The goal of the project was to develop a web application for managing references/citations using the BibTeX-format. Key functionality included support for the BibTeX-format, CRUD-operations and importing and exporting references in the .bib file-format. The development of the project was executed using scrum, following agile software development principles. Most notably automated unit- and integration testing was implemented to allow for continuous integration.

## 2. Sprint Summaries and Challenges

### Sprint 1 – Adding and Viewing References
- Set up the Flask backend, database, and basic front-end pages
- Implement creating and viewing simple references
- **Challenges**
    - Coordination and communication while working remotely
    - Dividing the work into tasks without interdependencies
    - Converting the course boilerplate app

### Sprint 2 – Support for BibTeX-reference Types and Editing References
- Implemented support for the BibTeX-format
- Added editing functionality
- Switched the database implementation to the SQLAlchemy ORM
- **Challenges:**
    - The workload was too high, this was adjusted for the next sprint

### Sprint 3 – Searching References
- Added a search feature.
- Improved the UI
- Refactored the program architecture
- **Challenges:**
    - Parallelising work
    - Refactoring the architecture took a loot of effort, leading

### Sprint 4 – Importing/Exporting References
- Added import and export features
- Refactored robot-tests.
- Further improved the UI
- Improved communication between frontend and backend.
- **Challenges:**
    - Developing new robot-tests during UI changes

## 3. What Went Well
- All team members were active and contributed to different parts of the project.
- Robust and systematic scrum implementation
- Documentation quality and overall project architecture
- Integration tests

## 4. What Could Have Been Done Better
- More detailed sprint planning; multiple tasks often overlapped near the deadline.
- Excessive use of feature branches caused unnecessary work and overlap. Using only a single branch per user story in the last sprint improved the workflow substantially and helped with merge-conflicts and overlapping work.

## 5. Key Takeaways
- Good quality unit-testing pays off in the long term.
- Integration testing with Robot Framework allowed detecting problems early.
- Implementing a complex external specification (BibTeX) proved quite difficult, both for storing data and validating it.
- Effective communication and using tools such as Github Projects to manage the scrum workflow made managing development easier.

## 6. What We Would Like to Learn Next
- Working in bigger teams on more complex projects
- Further develop and hone the systematic approach to development
- Maximize work not done to produce more value to the customer

## 7. Reflection
The project was an invaluable experience for learning how to develop software in a team. Getting hands-on experience with using agile methods was necessary to be able to further improve working a team.Challenges were bound to occur, but overcoming them ultimately gained even more experience.  Unfortunately the project was quite short, but it serves as a good introduction to the course *Ohjelmistoprojekti*.
