# Data Anonymization
## What is data anonymization?
Data anonymization is the process of removing personally identifiable information from datasets to ensure the anonymity of the people described in the datasets. Data anonymization is usually used when transferring data between organizations or owners so that the data can be analyzed and evaluated without unintentionally compromising people's privacy. Data anonymization is useful in many contexts, like medical data, social network data, or other data that might be sensitive. Data anonymization has become especially important with the emergence of Big Data, which could result in massive wide-scale breaches of individuals' privacy. This is especially troubling given how extensively personla data is traded for commercial purposes (for example, consider Cambridge Analytica, whose foundational dataset for clandestine U.S. voter targeting efforts--which significantly swayed the results of the 2016 presidential election--was licensed fromw well-known data brokers).

Data anonymization is not a perfect strategy. For one, data anonymization reduces the utility of data. Secondly, whenever data is anonymized, there is always a risk that it can be de-anonymized, especially if the anonymized dataset is compared with other data. This is an especially prevalent risk nowadays given the quantity of data that is collected; there are so many public datasets to cross-reference that it is likely, through clever procedures, that someone could de-anonymize data. For example, a researcher demonstraated this by taking an "anonymized" dataset of Netflix movie rentals and correlating this data with public IMDB reviews, allowing him to identify the individuals and get access to their complete rental histories. Other researchers at the Imperial College London and Belgium's Universite Catholique de Louvain were able to correctly re-identify 99.98% of individuals in anonymized data sets with just 15 demographic attributes.

However, data anonymization is still _important_, even if it is not a perfect solution. Good data anonymization requires mixing multiple strategies and carefully considering the potential harms that might result from the data being de-anonymized and mitigating these harms by limiting the amount of data made available. We should consider _who_ should actually have access to complex data about people and set strict access controls.
## Use cases for data anonymization (E)
## Strategies & Tools
There are five broad categories of anonymization operation:
* generalization, which replaces values with more generic ones
* suppression, which removes specific values from datasets
* anatomization, which disassociates relations between quasi-identifiers and sensitive attributes
* permutation, which disassociates relations between a quasi-identifier and sensitive attribute by dividing a number of data records into group and mixing their sensiive values in every group
* perturbation, which replaces original values with new ones by interchanging, adding noise, or creating synthetic data

Not every strategy is best-suited to every type of data. For example, suppression and random substitution (a type of perturbation) would be good for useless attributes but are unhelpful for data that is actually significant. Also, some kinds of perturbation, like numeric variance, are best for numeric/dates data and not helpful for text data.

The are many existing tools for data anonymization in Python, like:
* The Faker & Fake Factory libraries, which generate fake data (see an example [here](https://www.districtdatalabs.com/a-practical-guide-to-anonymizing-datasets-with-python-faker))
* Using built-in pandas operations, like deleting columns, encoding columns, or other approaches (see an example [here](https://medium.com/codex/data-anonymization-with-python-8976db6ded36))
## Our Solution (E)
## Sources
[Wikipedia](https://en.wikipedia.org/wiki/Data_anonymization#cite_note-:0-6)

[An Efficient Big Data Anonymization Algorithm Based on Chaos and Perturbation Techniques](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7512893/)

[Netflix paper, Arvind Narayanan](https://web.archive.org/web/20131216184011/http://33bits.org/about/netflix-paper-home-page/)

[Why you can't really anonymize your data](https://web.archive.org/web/20140109052803/http://strata.oreilly.com/2011/05/anonymize-data-limits.html)

[Researchers spotlight the lie of 'anonymous' data](https://techcrunch.com/2019/07/24/researchers-spotlight-the-lie-of-anonymous-data/)

[8 Anonymization Strategies with PostgreSQL](https://blog.taadeem.net/english/2019/01/03/8_anonymization_strategies_with_postgres)]