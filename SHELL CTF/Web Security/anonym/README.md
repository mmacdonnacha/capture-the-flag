# anonym

## Description

50 points

Anonymous are back and they really hate robots.

[http://3.142.122.1:8887](http://3.142.122.1:8887)

---

## Solution

Clue is in the description robots.

Websites have a file named robots.txt that lists urls that are not to be scrapped by web scrapers.

Checking 3.142.122.1:8887/robots.txt and we find a single webpage listed.

```
User-agent: \*
Disallow: /yfhdgvs.txt
```

Opening the url 3.142.122.1:8887/yfhdgvs.txt will show the flag.  

Flag: `SHELL{n0_ro80t5_4llow3d_50886509749a98ef14ec2bc45c57958e}`