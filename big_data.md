---
layout: big_data
title: Big Data
---

## Colaborative discussion posts

### Initial Post 1 

Tejada (2023) describes the ways of processing large quantities of data. In the current world, data is often described as the biggest assets a company may have (Abdulghany, 2022). But what is data exactly? How it is stored and processed? How do we ensure it is secure? Tejada (2023) provides a comprehensive description of Lambda and Kappa architecture. The distinction is made between batch and stream ("speed") processing. The essence of this distinction is it is not a distinction between different data types or sources, as it would usually be a case. Batch processing would happen in a FinTech company receiving settlement data for all transactions that happened a day before, for example. Streaming would be used for information that needs to be accessed in real-time - such as (using FinTech company for clarity again) transaction errors information. 

It is important to specify what the article talks about in order to be able to get a proper look at what message Tejada (2023) is trying to convey. The processing architecture described in the article concerns the events data and its backup (hot and cold storage). 

Now that we clarified the first point, we can move on to evaluation of "opportunities, limitations, risks and challenges associated with such a large-scale process of data collection." The opportunities with such vasts amounts of data are absolutely endless. The more we get the more we are able to build. HPE Experts (2021) discuss the monetisation of data which required mature data strategy within a company. The data a FinTech collects can help other companies build a profile of their potential customer and hence increase sales (all following GDPR and other legal regulations of course). 

Limitations we have with large quantities of data are latency and the physical storage. The machines are what builds a cloud and there is some finite space on earth to store such machines - this is the first limitation. The second one is speed - this is a technical limitation. Speed can be increased horizontally or vertically (Meli, 2021). Both of these scalings mean adding more computing power by adding new machines or extending capabilities of current ones. Because of this the limiation is either physical (as mentioned already above) or technological (what humanity is capable of building).

Risks with such large data processing seem quite obvious - data leaks and exposure of large number of people at once (Chin, 2023). If we do not take a proper care of the processing and security of IT systems responsible for such processing - malicious actors might steal the data and put at risk not only individuals but also whole states (if, for example, government critical infrastructure information is stolen during streaming). 

Challenges are tightly coupled with limitations. We ought to remember scaling clouds is not a free exercise. The companies can have access to Cloud storing and computing services, but everything comes at a price (Snowflake, 2022). The job of Analytics/Data Engineers (2023) in an enterprise is to provide the company with data it needs but also to optimise costs and efficiency as much as possible. With large quantities of data it is becoming a bigger and bigger challenge.

References:

1. Tejada (2023) Big Data Architectures. Available at: https://learn.microsoft.com/en-us/azure/architecture/data-guide/big-data/ (Accessed 27 January 2023).

2. Abdulghany, A. (2022) Data analytics: Why data is your company's biggest asset, Reea Global. Available at: https://reeaglobal.com/why-data-is-your-companys-biggest-asset/ (Accessed: February 7, 2023).

3. HPE Experts (2021) Discover the hidden value of data, Community.hpe.com. Available at: https://community.hpe.com/t5/tech-insights/discover-the-hidden-value-of-data/ba-p/7129295#.Y-KIJ-zMK3I (Accessed: February 7, 2023).

4. Meli, J. (2021) A guide to horizontal and vertical scaling in the cloud, CloudCheckr. Available at: https://cloudcheckr.com/cloud-automation/horizontal-vertical-cloud-scaling/ (Accessed: February 7, 2023).

5. Chin, K. (2023) Biggest data breaches in US history [updated 2023]: Upguard, RSS. Available at: https://www.upguard.com/blog/biggest-data-breaches-us (Accessed: February 7, 2023).

6. Snowflake Pricing & Cost Structure (2022) Snowflake. Available at: https://www.snowflake.com/pricing/ (Accessed: February 7, 2023).

7. Coursera (2023) What is a data engineer?: A guide to this in-demand career, Coursera. Available at: https://www.coursera.org/articles/what-does-a-data-engineer-do-and-how-do-i-become-one (Accessed: February 7, 2023).

### Summary post 1

To summarise this thread, we have many challenges related to storing and processing big data. There is limited physical space on earth, which at some point can force companies to be more selective with the data they store. Currently, speaking from personal experience, many companies follow the approach “the more we store the better” without giving it a second thought, as the storage is cheap (Snowflake, 2022). 


Processing such vast amounts of data can have high risks for society (Chin, 2023) - as personal data gets exposed, we can all become targets of malicious actors. Information that the companies hold against our names, can be used for stealing from us, blackmailing us etc.


It is no coincidence that it is said that the data a company holds is its biggest asset (Abdulghany, 2022). Information has always been important in business and now more than ever, with internet based businesses, the rich database is a huge asset, that requires careful security, processing and architecture considerations.


I believe it is inevitable that the data held globally grows. What’s important is that companies are well aware of all the risks and limitations and so that the data professionals handling the data sets and analytics code bases for said companies are also well aware of that and have it as a priority to be very selective and considerate when building data warehouses.

### Initial Post 2

Personal data is considered sensitive and it comes natural that it shall be handled with appropriate care. In order to ensure customers’ privacy rights, in relation to their data being handled by companies, several governing bodies have come up with policies that enforce a certain set of standards. General Data Protection Rights (GDPR) and the Information Commissioner’s Office (ICO) are two examples of such policies, introduced by the European Union and within the UK, respectively. 

The main difference between GDPR and the ‘Security’ rule of ICO is that GDPR is a legally binding policy that describes standards needed to be met when handling PII. ICO on the other hand provides guidance on how to achieve said standards. Therefore, some of the GDPR’s most important rules would say:

Personal data must be pseudonymised and encrypted.
It must be stored only for a valid reason and no longer than necessary.
Customers must have a right to have their data deleted upon Data Subject Request.
Personal data must be stored securely to prevent exposure during malicious actors’ cyber attacks.
Only a limited number of people within the organisation must have access to the PII.
Customers must be informed about how their data is being handled.

Meanwhile the ‘Security’ rule of the ICO focuses more on how to adhere to these standards, providing guidance such as:

Regular testing, software updates and quick fixes of security vulnerabilities.
Staff training on handling PII and on GDPR rules.
Strong cyber security infrastructure should be in place.
Regular security audits and penetration testing shall take place.
Incident management plan and clearly identified responsibilities for management of incident and its reporting to the authorities.

In summary, GDPR provides the ‘what’ and ICO provides the ‘how’, when it comes to handling PII. Breach of GDPR will have legal consequences for a company that has to adhere to GDPR rules, while ICO ‘Security’ rule does not have to be compliant with in full as there may be tweaks or other, potentially better ways, to achieve required security of PII. 

References:

EU (no date) Lex - 02016R0679-20160504 - en - EUR-lex, EUR. Available at: https://eur-lex.europa.eu/eli/reg/2016/679/2016-05-04 (Accessed: April 2, 2023). 
ICO, About the Guide to Data Protection (no date) ICO. Available at: https://ico.org.uk/for-organisations/guide-to-data-protection/about-the-guide-to-data-protection/ (Accessed: April 2, 2023). 

### Summary post 2

References


Snowflake Pricing & Cost Structure (2022) Snowflake. Available at: https://www.snowflake.com/pricing/ (Accessed: February 7, 2023).

Chin, K. (2023) Biggest data breaches in US history [updated 2023]: Upguard, RSS. Available at: https://www.upguard.com/blog/biggest-data-breaches-us (Accessed: February 7, 2023).

Abdulghany, A. (2022) Data analytics: Why data is your company's biggest asset, Reea Global. Available at: https://reeaglobal.com/why-data-is-your-companys-biggest-asset/ (Accessed: February 7, 2023).

## Learning outcomes

### Web scraping

Below you can find a code snippet from Unit 3 formative activities
This web scrapping script reads a website, finds all occurences of
'data scientist' in sentences and exports this data to a JSON file.

```python
from bs4 import BeautifulSoup
import requests
import re
import json

website = 'https://www.sas.com/en_us/insights/analytics/what-is-a-data-scientist.html'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')

find_data_scientist = soup.body.find_all(string=re.compile('[dD]ata [sS]cientist'))

find_data_scientist = list(find_data_scientist)

output = json.dumps(find_data_scientist)
```

## Artefacts

### Unit 1

I have come across one of the four Vs of data that I have not heard before: Veracity.

Veracity is a characteristic of BigData that refers to its consistency, accuracy, quality and trustworthiness. It is a tough task to achieve high quality data at scale, with many petabytes of data flowing through an enterprise. This is why it is one of the key pillars to achieve, when designing a BigData architecture. It serves the business as only with correct data, correct data-driven decision can be made at scale.

Reference:
 - Cristobal, S. (2021) Two more V's in big data: Veracity and value, Datascience.aero. Available at: https://datascience.aero/big-data-veracity-value/ (Accessed: April 7, 2023). 

### Unit 2

In this Unit we had a collaborative discussion, which one can read in sections above. Other than that, I have also learned how important it is to set up the data type in a correct way. Information Technology is all about 0s and 1s. Data is no differrent. If we want to handle data correctly at scale, we must ensure that the data types are consisted and aligned with the type of input required by functions we use to transform the data. Seemingly the same date, but just with a different format (eg. '01.01.2023' vs '01/01/2023') can cause our ETL to fail if not handled correctly. It is this 0s and 1s precision that is mesmerizing when it comes to data. It can also become a huge pain at times :)

References:
- Smallcombe, M. (2020) Data ingestion vs. ETL: Differences &amp; Priorities, Integrate.io. Integrate.io. Available at: https://www.integrate.io/blog/data-ingestion-vs-etl/ (Accessed: April 7, 2023). 
- Data ingestion: The first step to a sound data strategy (no date) Stitch. Available at: https://www.stitchdata.com/resources/data-ingestion/ (Accessed: April 7, 2023). 

### Unit 3

In this week part of my activities were to write a summary post which you can also find in the sections above. I have also created a web scrapping script that you can find below:

- [Link to Unit 4 exercise of data cleaning](https://github.com/piotr1204Essex/piotr1204Essex.github.io/blob/main/unit4.ipynb)

### Unit 4

This week I learned about data cleaning and transformation. Fortunately I have professional experience with this area. I have completed the test provided in the Unit and scored 100%. The test focused solely on Python functions and applications. When it comes to data cleaning and ETL processes there are many more tools and techniques that can and should be applied when ti comes to BigData. I have researched more about Airflow (orchestrating tool) and DBT (Data Build Tool). Speaking from my professional (but personal experience) it seems that the vast majority of the companies use SQL-based DBT to clean and transform data, while python is used more as a scripting language to trigger tasks in Airflow. In light of this, learning python for data cleaning might be a redundant task and soI focused more on improving my SQL related skills and knowledge about tooling. I have completed two online courses on Udemy. They are both paid, unfortunately, but I can recommend them for anyone interested if they are willing to pay.

WIKI submission:

DAG - Directed Acyclic Graph. It shows dependencies on the task that shall run before the downstream tasks run. It is acyclic if and only if one task follows another without looping back to the previous one. It is a basis for setting up procedures in eg. Airflow for orchestrating tasks that need to be completed on the Data Warehouse.

References:
- Apache Airflow course: https://www.udemy.com/share/102HOA3@irbbUiusOqY58BEb-jFv9YdbSh2Rqm6p7LLqRaJ6OVFuBt36DB_k0tT4YNS95M6t/
- DBT course: https://www.udemy.com/share/105KXo3@Zv7_9pqefEbPWaGn6_HD_9X2pm3kIeUaHiXsiGuIFl3FVAa9H-0qMpmL3PNuUYRO/
- Team, T.A. (no date) What is Apache airflow?, Astronomer. Available at: https://www.astronomer.io/airflow/ (Accessed: April 7, 2023). 
- Barcheski, J. (2023) DBT (Data Build Tool) overview: What is DBT and what can it do for My Data Pipeline?, Analytics8. Available at: https://www.analytics8.com/blog/dbt-overview-what-is-dbt-and-what-can-it-do-for-my-data-pipeline/ (Accessed: April 7, 2023). 

### Unit 5

In this Unit we learned more about data cleaning as well as a bout data collections. One thing in particular I consider extremely important and that is to have clear automation functions focused on the required task. It falls close to the principles of software engineering (Singh, 2022) which specify that each function should have a single responsibility. It helps with management of the code as well as it helps to understand where and issue happened should an error occur. 

One of the most prominent issues that can occur on big data is duplication (Sharon Rithika et al., 2023). Data cleaning tasks and procedures introduced to avoid such duplications are absolutely crucial. There are tools for automating that. Apart from the ones mentioned in the previous Unit, there is also Monte Carlo (Monte Carlo, 2023) that helps with data observability and quality. It uses Machine Learning models to learn about a standard behaviour of the data sets (number of daily inputs, usual pace at which dimensions change and so on and so forth). When an anomaly is detected it triggers an alert to the Data Engineering team that can handle it. 

References:
- Singh, R. (2022) 8 software engineering principles to live by, CalliCoder. CalliCoder. Available at: https://www.callicoder.com/software-development-principles/ (Accessed: March 24, 2023). 
- Sharon Rithika, Ramachandran, A. and Gaikwad, M. (2023) Data Ingestion Best Practices Simplified 101 - learn, Hevo. Available at: https://hevodata.com/learn/data-ingestion-best-practices/ (Accessed: April 7, 2023). 
- Monte Carlo: Data Reliability delivered (2023) Monte Carlo Data. Available at: https://www.montecarlodata.com/ (Accessed: April 7, 2023). 

### Unit 6

In this Unit we had to submitt the Team project which consumed a lot of my time. You can find links to the artefacts I created under Team Project section. There are as well final reports submission (which is a shared work with other team members) which were submitted under the assignment requirements.

### Unit 7

In this Unit I learned how to transform flat database model into a normalised one. I have also compelted the exercise of building a simple data design logic, paying attention to functional dependencies of the entities. Part of the Team Project was critical evaluation of constraints and limitations of a chosen design. This work was also submitted in Team Project's reports. I cannot stress enough how much I learned over this team project when it comes to critical evaluation of your own design. It is a difficult task to objectively critique your own design, but it is an important one. There is no golden rule when it comes to BigData design and architecture, there are however best practices (Cheema, 2022). It is the critical evaluation of possible implementation that allows to make an informed decision about the best choice for the environment in which the architecture will be applied. 

You can find below the links to the artefacts created as a part of exercise during this Unit.

References:
- Cheema, P. (2022) Big Data Architecture (Best Practices, Tips &amp; Tools), WEKA. Available at: https://www.weka.io/learn/file-system/big-data-architecture/ (Accessed: April 7, 2023). 

- [Link to Normalisation Task solution](https://github.com/piotr1204Essex/piotr1204Essex.github.io/blob/main/Normalisation_task.xlsx)
- [Link to the screenshot of ERD of a relational database with primary and foreign keys](https://github.com/piotr1204Essex/piotr1204Essex.github.io/blob/main/Screenshot%202023-03-02%20at%2017.53.00.png)

### Unit 8

In this Unit we discussed compliance and regulatory requirements for companies that handle BigData. BigData comes with big responsibility. Companies that handle individuals' information must be very careful in doing so. In today's world, cyber attacks are more common than ever (Irwin, 2023). Personal information shall never be exposed to malicious actors as it can put at harm an individual. Personal information is, generally, defined by GDPR (GDRP EU, 2016) as any piece of information that allows to identify an invididual. It can be an email address, phone number, home address etc. So the first piece of regulation is the aforementioned GDPR. This relates to security standards required when handling PII (Personally Identifiable Information). The second huge part of requirements is the local governing law that specifies data residency (Staff, 2022). Data residency is being understood as the actual, physical place where the data, containing PII, is being stored. These days most of the data sits within the public Cloud (vmware, 2022), but what regulators care about is where the physical storage of the data is taking place. 

In general, I learned about these two main aspects, not to mention the cybersecurity infrastructure. Cybersecurity infrastructure is out of the scope as it is a responsibility of Site Reliability Engineers and Cyber Security experts. The topics discussed in this Unit concern the data protection on the Data Warehouse side. 

Modern Data warehouses (such as Snowflake) introduce masking policies on their cloud-based data warehouses. This is the first and probably most important tool when it comes to compliance with GDPR and related regulations. It allows to hide the information from data consumers (whether data engineering team or end-user consumers who access the data via a BI visualisation Tool). But what happens if an individual would like their data to be removed from the comapny's database? This is where database design comes in. The challenge with BigData nowadays is not only answering the questions of streaming vs batching or how many semantic layers the datawarehouse needs, but also how tostructure the warehouse in such a way, that upon Data Subject request, the company is able tocomply with such request and delte an individual's information. 

The summary of my learning from this Unit is, that BigData comes with a tremendous number of challenges. The technical ones are one one side, but the regulatory ones are as tough to tackle. In my personal opinion, it is extremely important that we, as a society, have such regulations in place. It allows all of us to live in a safer world, which is becomnig more and more digital. 

References:
- Irwin, L. (2023) List of data breaches and cyber attacks in February 2023 – 29.5 million records breached, IT Governance UK Blog. Available at: https://www.itgovernance.co.uk/blog/list-of-data-breaches-and-cyber-attacks-in-february-2023-29-5-million-records-breached (Accessed: April 7, 2023). 
- Lex - 32016R0679 - en - EUR-lex (2016) EUR. Available at: https://eur-lex.europa.eu/eli/reg/2016/679/oj (Accessed: April 7, 2023). 
- Staff, I.C. (2022) Data residency laws by country - overview, InCountry. Available at: https://incountry.com/blog/data-residency-laws-by-country-overview/ (Accessed: April 7, 2023). 
- What is a public cloud? - definition - how it works? (2022) VMware. Available at: https://www.vmware.com/topics/glossary/content/public-cloud.html (Accessed: April 7, 2023). 
- Using dynamic data masking¶ (no date) Using Dynamic Data Masking | Snowflake Documentation. Available at: https://docs.snowflake.com/en/user-guide/security-column-ddm-use (Accessed: April 7, 2023). 
- How to establish Data Masking Standards for GDPR (no date) Talend. Available at: https://www.talend.com/resources/how-to-establish-data-masking-standards-gdpr/ (Accessed: April 7, 2023). 

### Unit 9

In this Unit we paid attention to the Data Base Management Systems. Systems have become so complex and complicated these days, that a new role in corporate environment emerged, which is a Systems Architect (2023). Their sole responsibility is to design a system, taking into account all business, technical and regulatory requirements and limitations. Such system that would serve the company well and meet as many business needs as possible (ideally all). 

When it comes to Data Base System implementation, there are several factors worth considering. First of them is cost, then access, logical structure and physical organisation. 

Storage costs has become very cheap, with new cloud-based technologies (Snowflake, 2023). If the storage is cheap, then the actual factor which creates bills is the computing power. As the data volume increases, storage price rises relatively slow, but computing price may increase exponentially, if a system is designed incorrectly. There are some general SQL Query performance best practices (Snaidero). But this is thinking on a very low, granular level. If we zoom out, we need to think about the data ingestion and all of the layers of the architecture. Usually, data warehouse consists of several layers (Cheema, 2022) which means that the data flows numerous times from ingestion point to the end consumer. It is being transformed, cleaned and validated at each step. It is important to consider that the system design consists of all necessary layers to ensure the data quality but no more than that. There is also a concept of materialisations (DBT, 2023) which not only plays important part in data warehouse architecture and data quality, but also in amount of computing power consumed on each run of queries within the warehouse.

When it comes to the access, first thing that comes to mind is the GDPR regulation (elaborated on in the previous Unit). The system must ensure not only correct masking policies and other data protection procedures, but also that the users with justified access can access certain tables or information from the data warehouse. If designed incorrectly, there may be regulatory repercussions as well as internal repercussions (if employees see the information they should not have access to). 

Logical structure of the data warehouse is an extension to the points raised before in this Unit and the previous ones too. All of the technical, business and regulatory requirements come down to the logical structure of the database that must account for all of these needs. 

Last but not least is the physical organisation. As mentioned in the previous Unit there are some regulations in certain countries when it comes to the data sphysical storage place (eg. Turkey (Data Localisation requirements in Turkiye)). There is also another, important consideration to be taken into account when deisgining a data base management system. Companies that rely on real-time access to their data (eg. Twitter, Facebook etc.) must ensure, that in order for their product to work correctly, the information stored in the DBMS is always available. It has become a standard, to store replicas/duplicates of the whole database in different locations across the world (IBM, 2022). There may be not only software related issues to retrieving the data but also natural disasters (such as hurracane, tsunami etc.). If any of such cases would happen to the place where a company physically stores data, the failover procedure must be in place in order to access the data from replica and keep the product running. If there was no such procedures, the companies would loose huge amounts of money, simply because people would not be able to use their products. Therefore, data physical organisation is important not only from the regulatory point of view but also from the business continuity point of view. 

One could talk and talk about all important aspects without stopping and I must admit that this is incredibly interesting topic. What I have learned however through the lectures and my research, is that all companies are different. There exists a myriad of tools that can support Systems Architect with design of a DBMS and all of them work differently. What I noticed is, for example a multi-cloud approach (Tobin, 2020) that companies implement. It leverages the advantages of different tools (different clouds in this example) to the advantage of a company. I encourage anyone interested to have a read at this approach.  

References:
- What does a systems architect do? (with skills and salaries) (2023). Available at: https://sg.indeed.com/career-advice/finding-a-job/what-does-systems-architect-do (Accessed: April 7, 2023). 
- Understanding storage cost¶ (no date) Understanding Storage Cost | Snowflake Documentation. Available at: https://docs.snowflake.com/en/user-guide/cost-understanding-data-storage (Accessed: April 7, 2023). 
- Snaidero, B. (no date) SQL Server Query Performance Guidelines tutorial, SQL Server Tips, Techniques and Articles. MSSQLTips. Available at: https://www.mssqltips.com/sqlservertutorial/3200/sql-server-query-performance-guidelines-tutorial/ (Accessed: April 7, 2023). 
- Cheema, P. (2022) Big Data Architecture (Best Practices, Tips &amp; Tools), WEKA. Available at: https://www.weka.io/learn/file-system/big-data-architecture/ (Accessed: April 7, 2023). 
- Materializations: DBT developer hub (2023) dbt Developer Hub RSS. Available at: https://docs.getdbt.com/docs/build/materializations (Accessed: April 7, 2023). 
- Data Localisation requirements in Turkiye (no date) NOW. Available at: https://cms-lawnow.com/en/ealerts/2023/01/data-localisation-requirements-in-turkiye (Accessed: April 7, 2023). 
- (no date) Overview of the failover process. Available at: https://www.ibm.com/docs/en/tbsm/6.2.0?topic=failover-overview-process (Accessed: April 7, 2023). 
- Tobin, D. (2020) Multi-cloud data analytics: What, why, and how, Integrate.io. Integrate.io. Available at: https://www.integrate.io/blog/multi-cloud-data-analytics/ (Accessed: April 7, 2023). 

### Unit 10

### Unit 11

### Unit 12

## Team Project

### Database design

Below the list of artefacts which were created by me and hence was the contribution to the team's project. 

- [Link to SQL file generating tables](https://github.com/piotr1204Essex/piotr1204Essex.github.io/blob/main/essex_hairdressing_project_Physical_Export_create.sql)
- [Link to the pipeline overview](https://github.com/piotr1204Essex/piotr1204Essex.github.io/blob/main/hair_dresser_architecture.drawio.png)
- [Link to the Entity Relationship Diagram](https://github.com/piotr1204Essex/piotr1204Essex.github.io/blob/main/essex_hairdressing_project-2023-02-18_14-22.png)

Other than that, we have split the work of writing the text equally between the three of us and so around 30% of the text written in reports submitted was written by me. 

### API Security


