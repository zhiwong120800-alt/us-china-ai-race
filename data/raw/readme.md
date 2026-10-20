# Annual scholarly publications on artificial intelligence - Data package

This data package contains the data that powers the chart ["Annual scholarly publications on artificial intelligence"](https://ourworldindata.org/grapher/annual-scholarly-publications-on-artificial-intelligence?v=1&csvType=full&useColumnShortNames=false&utm_source=chatgpt.com) on the Our World in Data website. It was downloaded on October 19, 2026.

### Active Filters

A filtered subset of the full data was downloaded. The following filters were applied:

## CSV structure

Each row is an observation for an entity (usually a country or region) at a timepoint.

- "Entity" — the name of the entity, e.g. "United States".
- "Code" — our internal entity code. For most countries this is the [ISO alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) code, e.g. "USA"; historical and other non-standard entities get a custom code.
- "Year" or "Day" — the timepoint. Annual data has a "Year" column holding an integer year; otherwise a "Day" column holds a date string in the form "YYYY-MM-DD".
- The final column is the data column — the time series that powers the chart. Downloaded with the "full data" option it corresponds to the time series below; with "only selected data visible in the chart" it is transformed depending on the chart type, so the correspondence may be less direct.


## Metadata.json structure

The .metadata.json file contains metadata about the data package. The "charts" key contains information to recreate the chart, like the title, subtitle etc. The "columns" key contains information about each of the columns in the csv, like the unit, timespan covered, citation for the data etc.

## How we process data at Our World in Data

Our World in Data is almost never the original producer of the data - almost all of the data we use has been compiled by others. If you want to re-use data, it is your responsibility to ensure that you adhere to the sources' license and to credit them correctly. Please note that a single time series may have more than one source - e.g. when we stitch together data from different time periods by different producers or when we calculate per capita metrics using population data from a second source.

Preparing this data involves several processing steps. Depending on the data, this can include standardizing country names and world region definitions, converting units, calculating derived indicators such as per capita measures, as well as adding or adapting metadata such as the name or the description given to an indicator.
[Read about our data pipeline](https://docs.owid.io/projects/etl/).

## Detailed information about the data


### AI scholarly publications - Field: All
Scholarly publications on AI, including journal articles, conference papers, working papers, and preprints. The data only covers articles with an English-language title or abstract.
Last updated: April 27, 2026  
Next expected update: October 2026  
Date range: 2016–2024  
Unit: publications  
Source: Center for Security and Emerging Technology (2026) – with minor processing by Our World in Data  

#### How to cite this data

Center for Security and Emerging Technology (2026) – with minor processing by Our World in Data

#### What you should know about this data
- The data covers scholarly publications on AI, including journal articles, conference papers, working papers, and preprints.
- Articles are flagged as AI-related using machine learning models trained on subject tags from arXiv, an open repository for scientific papers.
- The models only run on articles with English titles or abstracts. Research published only in other languages is missed. Coverage of Chinese research is also limited, since many Chinese journals are not in the underlying sources.
- An article counts for a country if at least one of its authors is affiliated with an institution there. If authors are based in different countries, it counts once for each.
- Authors are linked to the country of the institution they worked at when the article was published, not their country of origin.

#### Notes on our processing step for this indicator
We calculate regional and global totals from the country-level data CSET provides, following our [region definitions](https://ourworldindata.org/world-region-map-definitions). Countries that are not covered by the source are excluded from these totals.


## Sources

These are the sources behind the data in this package. Each time series above names the ones it draws on in its citation.

### Center for Security and Emerging Technology – Country Activity Tracker: Artificial Intelligence

ETO's Country AI Activity Metrics dataset includes national-level metrics for AI-related research, patents, and private-market investment.

The metrics are derived from a variety of underlying data sources, including ETO's Merged Academic Corpus for research data; The Lens, PATSTAT, and 1790 Analytics for patents; and Crunchbase for company and investment data.

The dataset focuses on countries, not organizations or individuals, and on AI and its subfields. There are many ways to assess countries' AI activities, and the three types of metrics included here, while meaningful, are not exhaustive. The data also has a lag, making counts incomplete for recent years; the lag is especially significant for patent data.

Producer: Center for Security and Emerging Technology  
Published: 2026-03-19  
Retrieved on: 2026-04-27  
Retrieved from: https://cat.eto.tech/  
Direct download: https://zenodo.org/records/19103157/files/cat.zip?download=1  
License: CC BY-NC 4.0 (https://eto.tech/tou/)  

Citation: Emerging Technology Observatory [Country Activity Tracker: Artificial Intelligence](https://cat.eto.tech/?expanded=Summary-metrics)

    