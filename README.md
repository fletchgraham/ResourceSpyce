# ResourceSpyce
python wrapper for the ResourceSpace API

## Example

```python
from resourcespyce import ResourceSpace

rs = ResourceSpace(
    base_url='http://my.resourcespace/api/?',
    user='admin',
    private_key='personal-api-key'
    )

print(rs.do_search('dog'))
```

The above example would print out the json response.
