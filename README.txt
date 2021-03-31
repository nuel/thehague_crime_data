=====================================

CRIME COUNTS PER NEIGHBORHOOD

Compiled by nuel

-------------------------------------

In this README:

0. Introduction
1. About this dataset
2. Content and structure
3. Delict codes explanation


================
| INTRODUCTION |
----------------
This project was part of a larger effort to investigate the
cyber division of the Dutch police -- in particular their
latest developments in terms of predictive policing. This
dataset is an effort to take back some transparency and
insight into the data that's being used behind the scenes
to predict and "prevent" crime.

When technology that is barely understood produces
questionable results that are taken as infallible truths, and
when these become guiding principles to enact violence,
marginalized people will always end up paying the price. 1312



======================
| ABOUT THIS DATASET |
----------------------

In 2018, Dutch police in The Hague (whose jurisdiction extends
to several nearby cities) ran a public website where residents
could check local crime stats. The numbers were very local: they
were grouped per neighborhood, which in many cases is not bigger
than just a few streets.

However, the website only let you view one month at a time
and always filtered on one specific type of crime.

That's why I decided to scrape the raw data. In the folder
"data", you'll find the complete dataset that the police
website uses. This includes crime counts, but also the
geographical boundaries for each neighborhood.

If you want to scrape a fresh copy yourself, the scripts I
wrote to compile the dataset are also included.



=========================
| CONTENT AND STRUCTURE |
-------------------------

- SQLite
    In `data/delicts.db` you'll find the complete dataset
    as a sqlite database. This is probably the easiest to
    work with if you want to do some pattern analysis.

- JSON
    The dataset is also available as JSON. There's a folder
    for each year of data, which contains a file for each
    district. These, in turn, group delict counts per
    neighborhood, per month, per delict code. Basically,
    the structure is like this:

    > Year
      > District
        > Delict code
          > Month
            > Neighborhood

- Boundaries
    The file `data/areas.txt` contains the name and
    geographical boundaries of each district code. (The
    same code used for the JSON filenames.) They are in a
    custom format that uses commas and pipe characters to
    separate values.

- Scripts
    If you want to compile the dataset yourself, the scripts
    I wrote to scrape and organize the data are also included.
    Just run `python script_name.py`.


===========================
| DELICT CODE EXPLANATION |
---------------------------

The dataset uses delict codes to distinguish crime types.
Their names can be found by inspecting the web form and
are listed below:

[100]   Theft while on scooter
[101]   Theft from bike
[102]   Street robbery
[104]   Burglary (both attempted and successful)
[105]   Theft while on or in motorized vehicle
[106]   Motor vehicle theft
[107]   Shoplifting
[108]   Pickpocketing
[109]   Violent threat
[110]   Abuse
[111]   Vandalism
[117]   Robbery
