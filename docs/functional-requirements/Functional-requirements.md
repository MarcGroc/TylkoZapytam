# Tylko Zapytam - Functional Requirements

## 1. Introduction

- The purpose of this document is to describe the functional requirements of the application.

### 1.1 Purpose
- Purpose of this application is to provide a platform for Clients to ask questions, book calls and get answers from other Clients(experts).
- The application will be available on the web and mobile devices. 
- The application will be available in Polish.

### 1.2 Scope



### 1.3 Definitions, acronyms and abbreviations

| Term                          | Definition                                               |
|-------------------------------|----------------------------------------------------------|
| Client                        | A person who uses the application.                       |
| Expert                        | A person who has a lot of knowledge in a specific field. |
| Question                      | A question asked by a Client.                            |
| Answer                        | An answer given by an expert.                            |
| Call                          | A call between a Client and an expert.                   |
| Rating                        | A rating given by a Client to an expert.                 |
| Comment                       | A comment given by a Client to an expert.                |
| Category                      | A category of questions.                                 |
| Tag                           | A tag of a question.                                     |
| Notification                  | A notification sent to a Client.                         |
| Message                       | A message sent to a Client.                              |
| Payment                       | A payment made by a Client.                              |
| Wallet                        | A wallet of a Client.                                    |
| Transaction                   | A transaction made by a Client.                          |
| Report                        | A report made by a Client.                               |
| Ban                           | A ban given to a Client.                                 |
| Admin                         | A person who has access to the admin panel.              |
| Moderator                     | A person who has access to the moderator panel.          |
| Superuser                     | A person who has access to the superuser panel.          |
| Client panel                  | A panel where a Client can manage his account.           |
| Expert panel                  | A panel where an expert can manage his account.          |
| Admin panel                   | A panel where an admin can manage the application.       |
| Moderator panel               | A panel where a moderator can manage the application.    |
| Superuser panel               | A panel where a superuser can manage the application.    |
| Question panel                | A panel where a Client can manage his questions.         |
| Answer panel                  | A panel where an expert can manage his answers.          |
| Call panel                    | A panel where a Client can manage his calls.             |
| Rating panel                  | A panel where a Client can manage his ratings.           |
| Comment panel                 | A panel where a Client can manage his comments.          |
| Category panel                | A panel where an admin can manage categories.            |
| Tag panel                     | A panel where an admin can manage tags.                  |
| Notification panel            | A panel where a Client can manage his notifications.     |
| Message panel                 | A panel where a Client can manage his messages.          |
| Payment panel                 | A panel where a Client can manage his payments.          |
| Wallet panel                  | A panel where a Client can manage his wallet.            |
| Transaction panel             | A panel where a Client can manage his transactions.      |
| Report panel                  | A panel where a Client can manage his reports.           |
| Ban panel                     | A panel where a Client can manage his bans.              |
| Client management panel       | A panel where an admin can manage Clients.               |
| Expert management panel       | A panel where an admin can manage experts.               |
| Question management panel     | A panel where an admin can manage questions.             |
| Answer management panel       | A panel where an admin can manage answers.               |
| Call management panel         | A panel where an admin can manage calls.                 |
| Rating management panel       | A panel where an admin can manage ratings.               |
| Comment management panel      | A panel where an admin can manage comments.              |
| Notification management panel | A panel where an admin can manage notifications.         |
| Message management panel      | A panel where an admin can manage messages.              |
| Payment management panel      | A panel where an admin can manage payments.              |
| Wallet management panel       | A panel where an admin can manage wallets.               |
| Transaction management panel  | A panel where an admin can manage transactions.          |
| Report management panel       | A panel where an admin can manage reports.               |
| Ban management panel          | A panel where an admin can manage bans.                  |

### 1.4 References

| Document ID | Title | Version | Date | Author | Description |
|-------------|-------|---------|------|--------|-------------|
|             |       |         |      |        |             |
### 1.5 Overview

- Platform allow to full interactions between Clients and experts.
- Clients can ask questions, book calls and rate experts.
- Experts can answer questions, book calls and rate Clients.
- Clients and experts can communicate with each other.
- Clients and experts can manage their accounts.
- Admins can manage the application.
- Moderators can manage the application.
- Superusers can manage the application.

## 2. Overall description


### 2.1 Product perspective

The application will be available on the web and mobile devices.


### 2.2 Product functions

- Clients can ask questions, book calls and rate experts.
### 2.3 Client characteristics

- Clients of the platform are professionals or individuals seeking expert advice or assistance on a short-notice basis.
- Clients may be seeking assistance in a wide variety of fields, including technical, business, creative, or personal matters.
- Clients value convenience, flexibility, and cost-effectiveness in their search for expert assistance.
- Clients may be located anywhere in the world and may come from a variety of cultural backgrounds.
- Clients may be seeking assistance for a variety of reasons, such as to solve a problem, gain new insights, or simply to have someone to bounce ideas off of.
- Clients may have varying levels of technical proficiency and may be comfortable using different communication platforms and tools.
- Clients may be willing to pay a premium for high-quality, expert assistance.
- Clients may have different levels of familiarity with the platform and may need varying levels of support and guidance in using its features.


### 2.4 Constraints

- The application will be available in Polish.

## 3. Specific requirements

### 3.1 Functional requirements

#### 3.1.1 Client

- Client can register an account.
- Client can log in to his account.
- Client can log out from his account.
- Client can change his password.
- Client can change his email.
- Client can change his username.
- Client can change his phone number.

#### 3.1.2 Expert

- Expert can register an account.
- Expert can log in to his account.
- Expert can log out from his account.
- Expert can change his password.
- Expert can change his email.
- Expert can change his username.
- Expert can change his avatar.
- Expert can change his phone number.
- Expert can change his description.
- Expert can change his categories.
- Expert can change his tags.
- Expert can change his price.
- Expert can change his availability.
- Expert can change his timezone.

#### 3.1.3 Question

- Client can ask a question.
- Client can edit his question.
- Client can delete his question.

#### 3.1.4 Answer

- Expert can answer a question.
- Expert can edit his answer.
- Expert can delete his answer.

#### 3.1.5 Call

- Client can book a call.
- Client can cancel his call.
- Client can rate his call.
- Client can comment his call.
- Expert can book a call.
- Expert can cancel his call.
- Expert can comment his call.
- Client can see his calls.
- Expert can see his calls.
- Expert can see his ratings.
- Client can see his comments.
- Expert can see his comments.
- Client can see his notifications.
- Expert can see his notifications.
- Client can see his messages.
- Expert can see his messages.
- Client can see his payments.
- Expert can see his payments.
- Client can see his wallet.
- Expert can see his wallet.
- Client can see his transactions.
- Expert can see his transactions.
- Client can see his reports.
- Expert can see his reports.
- Client can see his bans.
- Expert can see his bans.

#### 3.1.6 Category

- Admin can create a category.
- Admin can edit a category.
- Admin can delete a category.
- Admin can see categories.
- Admin can see category questions.
- Admin can see category answers.
- Admin can see category calls.
- Admin can see category ratings.
- Admin can see category comments.
- Admin can see category notifications.
- Admin can see category messages.
- Admin can see category payments.
- Admin can see category wallets.
- Admin can see category transactions.
- Admin can see category reports.
- Admin can see category bans.
- Admin can see category Clients.
- Admin can see category experts.
- Admin can see category questions.
- Admin can see category answers.
- Admin can see category calls.
- Admin can see category ratings.
- Admin can see category comments.
- Admin can see category notifications.
- Admin can see category messages.
- Admin can see category payments.
- Admin can see category wallets.
- Admin can see category transactions.
- Admin can see category reports.
- Admin can see category bans.
- Expert can see categories.
- Client can see categories.

#### 3.1.7 Tag

- Admin can create a tag.
- Admin can edit a tag.
- Admin can delete a tag.
- Admin can see tags.
- Client can see tags.
- Expert can see tags.


#### 3.1.2 Question management

- Admin can see questions.
- Admin can see question answers.
- Admin can see question calls.
- Admin can see question ratings.
- Admin can see question comments.
- Admin can see question notifications.
- Admin can see question messages.
- Admin can see question payments.
- Expert can see questions.
- Client can see questions.
- Moderator can see questions.
- Superuser can see questions.
- Client can edit his question.
- Client can delete his question.
- Expert can edit his question.


#### 3.1.3 Answer management

- Admin can see answers.
- Admin can see answer calls.
- Admin can see answer ratings.
- Admin can see answer comments.
- Admin can see answer notifications.
- Admin can see answer messages.
- Admin can see answer payments.
- Expert can see answers.
- Client can see answers.
- Moderator can see answers.
- Superuser can see answers.
- Expert can edit his answer.
- Expert can delete his answer.
- 

#### 3.1.4 Comment management

- Admin can see comments.
- Admin can see comment notifications.
- Admin can see comment messages.
- Client can see comments.
- Moderator can see comments.
- Superuser can see comments.
- Client can edit his comment.
- Client can delete his comment.
- Expert can edit his comment.
- Expert can delete his comment.


#### 3.1.5 Vote management

- Admin can see votes.
- Admin can see vote notifications.
- Admin can see vote messages.
- Client can see votes.
- Moderator can see votes.
- Superuser can see votes.
- Client can vote.
- Expert can vote.
- 
#### 3.1.6 Tag management

#### 3.1.7 Notification management


#### 3.1.8 Search management

- Client can search.
- Expert can search.
- Admin can search.
- Moderator can search.
- Superuser can search.
- Client can search for expert.
- Expert can search for expert.
- Admin can search for expert.
- Moderator can search for expert.
- Superuser can search for expert.
- Client can search for category.
- Expert can search for category.
- Admin can search for category.
- Moderator can search for category.
- Superuser can search for category.
- Client can search for tag.
- Expert can search for tag.
- Admin can search for tag.
- Moderator can search for tag.
- Superuser can search for tag.

#### 3.1.9 Report management

- Client can report.
- Expert can report.
- Admin can see reports.
- Moderator can see reports.
- Superuser can see reports.

#### 3.1.10 Client profile management

- Client can see his profile.
- Client can see his questions.
- Client can see his answers.
- Client can see his calls.
- Client can see his ratings.
- Client can see his comments.
- Client can see his notifications.
- Client can see his messages.
- Client can see his payments.
- Client can see his wallet.
- Client can see his transactions.
- Client can see his reports.
- Client can see his bans.

#### 3.1.11 Client settings management


#### 3.1.12 Client statistics management

#### 3.1.13 Client ranking management


#### 3.1.14 Client reputation management


#### 3.1.15 Client badges management

#### 3.1.16 Client notifications management

#### 3.1.17 Client messages management

#### 3.1.18 Client favorites management

#### 3.1.19 Client history management

#### 3.1.20 Client activity management


### 3.2 Non-functional requirements

#### 3.2.1 Performance requirements

- The system should be able to handle 1000 Clients at the same time.
- The system should be able to handle 1000 experts at the same time.
- The system should be able to handle 1000 questions at the same time.
- The system should be able to handle 1000 answers at the same time.
- The system should be able to handle 1000 calls at the same time.
- The system should be able to handle 1000 ratings at the same time.
- The system should be able to handle 1000 comments at the same time.
- The system should be able to handle 1000 notifications at the same time.
- The system should be able to handle 1000 messages at the same time.
- The system should be able to handle 1000 payments at the same time.
- The system should be able to handle 1000 wallets at the same time.
- The system should be able to handle 1000 transactions at the same time.
- The system should be able to handle 1000 reports at the same time.
- The system should be able to handle 1000 bans at the same time.
- The system should be able to handle 1000 categories at the same time.
- The system should be able to handle 1000 tags at the same time.
- The system should be able to handle 1000 votes at the same time.
- The system should be able to handle 1000 searches at the same time.
- The system should be able to handle 1000 Client profiles at the same time.


#### 3.2.2 Security requirements


#### 3.2.3 Software quality attributes

- The system should be easy to use.
- The system should be easy to learn.
- The system should be easy to maintain.
- The system should be easy to extend.
- The system should be easy to test.
- The system should be easy to deploy.
- The system should be easy to scale.
- The system should be easy to integrate.
- The system should be easy to debug.
- The system should be easy to monitor.
- The system should be easy to backup.
- The system should be easy to restore.
- The system should be easy to upgrade.
- The system should be easy to downgrade.
- The system should be easy to migrate.
- The system should be easy to recover.
- The system should be easy to secure.
- The system should be easy to protect.
- The system should be easy to optimize.

#### 3.2.4 Business rules

#### 3.2.5 Other requirements





