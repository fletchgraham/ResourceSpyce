# ResourceSpyce
python wrapper for the ResourceSpace API

## Example

```python
from resourcespyce.spyce import Spyce

RS = Spyce(
    base_url='http://my.resourcespace/api/?',
    user='admin',
    private_key='personal-api-key'
    )

print(RS.do_search('dog'))
```

The above example would return the json response.
