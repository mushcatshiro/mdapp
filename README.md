# wiki project

to facilitate a markdown based wiki which the data are all stored in remote git repository. data are clone to `static` folder and is rendered to html upon request.

## setup

```bash
>> python -m venv $proj_name
>> pip install -r requirements.txt
>> setup.sh
```

## backlog

- [x] inter-markdown links
- [x] config
    - [x] logging formatting
- [x] error handling
- [ ] setup.sh
- [ ] gunicorn/requirements.txt
- [x] complicated static folder structure
- [x] database support
    - [x] proper md rendering in page view
    - [x] validate new md file indexing
- [ ] full-text-search support
- [ ] html cleanup
    - [x] search box
    - [x] index doc link
    - [ ] pagination
- [ ] access control
- [ ] markdown
    - [ ] styling
    - [ ] multi-level unordered list


## known limitations

1. no duplicated filename is allowed
