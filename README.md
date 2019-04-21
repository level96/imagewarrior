# Django

```bash
pip install 
```

Register APP

```python
INSTALLED_APPS = [
    # ...
    'imagewarrior.django_compat',
    # ... 
]
```

Register TEMPLATE TAGS

```python
TEMPLATES = [
    {
        'BACKEND': ...,
        'DIRS': [
            ...
        ],
        'OPTIONS': {
            'loaders': ...,
            'context_processors': [
                ...
                'imagewarrior.django_compat.context_processors.imagewarrior',
            ],
        },
    },
]

```

in Template

