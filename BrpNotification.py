import requests, json, logging, os, re

parkway = []
url = "https://server-utils.herokuapp.com/proxy/?encoded=true&type=json&url=aHR0cHMlM0ElMkYlMkZucHMtYmxyaS5jYXJ0b2RiLmNvbSUyRmFwaSUyRnYyJTJGc3FsJTNGY2IlM0QxNTIxMDgwODgwMDAwJTI2Zm9ybWF0JTNEZ2VvanNvbiUyNnElM0RTRUxFQ1QlMjBsaXZlX3JvYWRfc2VnbWVudHMubmFtZSUyQ2xpdmVfcm9hZF9zZWdtZW50cy50aGVfZ2VvbSUyQ2xpdmVfcm9hZF9zZWdtZW50cy5jYXJ0b2RiX2lkJTJDbGl2ZV9yb2FkX3NlZ21lbnRzX3N0YXR1cy5pc19jbG9zZWQlMkNsaXZlX3JvYWRfc2VnbWVudHNfc3RhdHVzLmlzX29wZW4lMkNsaXZlX3JvYWRfc2VnbWVudHNfc3RhdHVzLmlzX3dhcm5lZCUyMEZST00lMjBsaXZlX3JvYWRfc2VnbWVudHMlMjBMRUZUJTIwSk9JTiUyMGxpdmVfcm9hZF9zZWdtZW50c19zdGF0dXMlMjBPTiUyMGxpdmVfcm9hZF9zZWdtZW50cy5jYXJ0b2RiX2lkJTNEbGl2ZV9yb2FkX3NlZ21lbnRzX3N0YXR1cy5zZWdtZW50X2lkJTIwV0hFUkUlMjBsaXZlX3JvYWRfc2VnbWVudHNfc3RhdHVzLmFyY2hpdmVkJTNEZmFsc2UlMjBPUiUyMGxpdmVfcm9hZF9zZWdtZW50c19zdGF0dXMuYXJjaGl2ZWQlMjBJUyUyME5VTEwlMjBPUkRFUiUyMEJZJTIwbGl2ZV9yb2FkX3NlZ21lbnRzLnNlZ21lbnRfb3JkZXI="
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
r = requests.get(url, headers=headers)
data = r.json()
for marker in data['data']['features']:
    miles = re.findall(r"[-+]?\d*\.\d+|\d+", marker['properties']['name'])
    if len(miles) == 2:
        marker['properties']['start'] = miles[0]
        marker['properties']['end'] = miles[1]
        parkway.append(marker['properties'])
