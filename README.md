This is a minimal reproducible example for [issue 344](https://github.com/typeddjango/django-stubs/issues/344) in [typeddjango/django-stubs](https://github.com/typeddjango/django-stubs).

This was created by running:

```
$ django-admin startproject project
$ cd project
$ ./manage.py startapp app
```

Then, I added the files [requirements.txt](https://github.com/eyqs/django-stubs-issue-344/blob/main/project/requirements.txt), [setup.cfg](https://github.com/eyqs/django-stubs-issue-344/blob/main/project/setup.cfg), and [models.py](https://github.com/eyqs/django-stubs-issue-344/blob/main/project/app/models.py) to reproduce the bug.
