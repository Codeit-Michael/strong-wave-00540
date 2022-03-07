## BOOTSRAP CSS CLASS/ID TAGS

**.container{}**
>Style class for group of elements work together (in a div). It will get indented on the mid-part of the html. To make it apply for the whole template, instead of `container`, try `container-fluid`

***

**.col{}**
>Divides the template depends on how many tag has `col`. Example, you had 2 divs:
```
<div class="col">Column 1</div>
<div class="col">Column 2</div>
```
What we'll have is 2 different columns since we configure 2 columns

>`col-{screensize}-{int}` - for sizing the column. *screensize* can be `sm, md,lg` means small, medium, and large. *int* dictates how many spaces it will be occupying.

>You can put 3 kind of class per tag to addapt on different screen sizes like; class="col-sm-12 col-md-6 col-lg-3"

***
