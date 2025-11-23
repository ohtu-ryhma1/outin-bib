# Scrum
This document describes how our development team uses scrum.

## Implementations

### Product Backlog
The product backlog contains all planned features as user stories. The product backlog aims to follow the DEEP criteria.

### User Stories
User stories are implemented as GitHub issues. Their title describes the intended functionality. Acceptance criteria is included as a task, and is described using robot tests.

### Tasks
Tasks are implemented as sub-issues on user stories. Tasks describe individual technical aspects of the user story. Sub-tasks are implemented as sub-issues of tasks. They split the task into smaller components, useful for time estimation and planning.

### Time estimates
Time estimates for product backlog are categorized into small/medium/large/epic. Time estimates are not provided for sprint user stories. Time estimates are created for sub-tasks. This allows for more granular and real-time estimates.

### Burn Up
Burn Up graphs are automatically created for each sprint. They track the custom field "Time-estimate" defined for sub-tasks. The Burn Up graph updates daily.

## Definition of Done

### User Stories
- Acceptance criteria fulfilled
- All tasks complete
- All unit-tests passing
- All robot-tests passing
- All branch code reviewed
- Merged to dev branch

### Tasks
- All sub-tasks complete
- All unit-tests passing
- All robot-tests passing

### Sub-tasks
- Functionality implemented