# dpfilter
### BugBounty , sort and delete duplicates param value without missing original value replace qsreplace tool

## Usage
```bash
chmod +x dpfilter.py && sudo mv dpfilter.py /usr/bin/dpfilter
cat urls.txt | dpfilter
```
OR
```bash
python3 dpfilter.py urls.txt 
```

# Description
```bash
cat urls.txt | qsreplace FUZZ | sort -u
```
above example will change parameters value and then remove duplicates , this example many used in bugbounty to delete duplicate parameters value <br> 
but will return all parameters value [FUZZ] <br>
this problem because some parameters value are required to open the page , alike [https://www.example.com/page.php?path=/users/view] <br>
its sort and delete unqiue yes but missing original param value <br>
this script will read urls.txt and delete all duplicates without missing original param value.
