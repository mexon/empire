# When Will The Sun Set?

I wrote this script to answer the question, when will the sun set on the British Empire?  With the Chagos Islands being returned to Mauritius sovereignty, there will now be enough of a gap between the eastern and western extents of the British Empire that it will sometimes be dark for the entire territory.  When, exactly, that will happen is a fairly complicated question.  I wrote the script to double-check my answer.

Everything is hard-coded.  To use it to answer other questions, edit the code.

The `places` variable holds the coordinates of all potential places that may be the last on a given day to experience sunset, or the first to experience sunrise.  It is not necessary to list all places part of the empire.  Only reasonable candidates at the extreme east and west are necessary.  But it's also important to remember that the seasons play a factor: if the western-most point is in the northern hemisphere, a more easterly but southerly point may in fact be the relevant point during the northern summer.

You can also comment out certain points, such as British Antarctic Territory, depending on your interpretation of what actually counts.

The start date for the search is hard-coded to 2026.  Barring extreme astronomical events, this should not affect the result.

To run:

```
> python3 empire.py
Oeno Island sunset 2026-03-21 02:53:00+00:00
```
