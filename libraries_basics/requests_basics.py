import requests

# request types
r = requests.get('http://api.github.com/events')
r = requests.post('http://api.github.com/events', \
                   data = {'key':'value'})
r = requests.put('http://httpbin.org/put', data = {'key':'value'})
r = requests.delete('http://httpbin.org/delete')
r = requests.head('http://httpbin.org/get')
r = requests.options('http://httpbin.org/get')                   

# check responce status
r.status_code == requests.codes.ok
# OR 
r.raise_for_status()
# embed in a try-except statement
try:
    r.raise_for_status()
except Exception as exc:
    print 'There was a problem : {}'.format(exc)
    
# passing parameters in URLs
payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
r = requests.get('http://api.github.com/events', params=paylaod)
#http://httpbin.org/get?key1=value1&key2=value2&key2=value3      
            
    ##      Saving Downloaded Files to the Hard Drive   ##

# pattern to use for saving a DLed stream to a file :
with open(filename, 'wb') as fb:
    for piece in r.iter_content(byte_size): # byte_size ~ 10000
        fb.write(piece)

        
                  

