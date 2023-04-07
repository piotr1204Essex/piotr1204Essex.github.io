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

## Links to artefacts

### Unit 1

I have come across one of the four Vs of data that I have not heard before: Veracity.

Veracity is a characteristic of BigData that refers to its consistency, accuracy, quality and trustworthiness. It is a tough task to achieve high quality data at scale, with many petabytes of data flowing through an enterprise. This is why it is one of the key pillars to achieve, when designing a BigData architecture. It serves the business as only with correct data, correct data-driven decision can be made at scale.

Reference:
 - Cristobal, S. (2021) Two more V's in big data: Veracity and value, Datascience.aero. Available at: https://datascience.aero/big-data-veracity-value/ (Accessed: April 7, 2023). 

### Unit 2

### Unit 3

### Unit 4

- [Link to Unit 4 exercise of data cleaning](https://github.com/piotr1204Essex/piotr1204Essex.github.io/blob/main/unit4.ipynb)

### Unit 5

### Unit 6

### Unit 7

- [Link to Normalisation Task solution](https://github.com/piotr1204Essex/piotr1204Essex.github.io/blob/main/Normalisation_task.xlsx)
- [Link to the screenshot of ERD of a relational database with primary and foreign keys](https://github.com/piotr1204Essex/piotr1204Essex.github.io/blob/main/Screenshot%202023-03-02%20at%2017.53.00.png)

### Unit 8

### Unit 9

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


