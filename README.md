Description
===========

A check for cookie respawning using Verizon's UIDH. Included in the repo is the code
required to both run crawls and analyze the resulting databases. You can also find
download links below for the databases I collected.

For my thoughts, read my Freedom to Tinker [post](https://freedom-to-tinker.com/blog/englehardt/verizons-tracking-header-can-they-do-better/).

Scripts
=======

* OpenWPM-0.2.1/ - modified [OpenWPM v0.2.1](https://github.com/citp/OpenWPM/releases/tag/v0.2.1)
* list_domains.py - lists the domains where turn.com's respawned IDs are found
* respawning.py - checks for cookies that may be respawned from the XUID header

Data
====

I ran a few crawls in parallel on EC2 on two different days. I used three different machines, but was sure to clear state between each crawl. You can find the data [here](https://webtransparency.cs.princeton.edu/verizon/).The name of the sqlite database indicates the configuration of the machine.
* 'u': UIDH string (string 1 or string 2)
* 'd': day the crawl took place on (day 1 or day 2)
* 'm': the machine the crawl was run on (machine 1, 2, or 3).
