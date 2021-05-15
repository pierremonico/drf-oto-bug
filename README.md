# About

Simple repo to demonstrate a bug where you can't set a reverse relationship on a model through a POST call.

## Getting started

- `pipenv install`
- `pipenv shell`
- `./manage.py makemigations`
- `./manage.py migrate`
- `./manage.py test`

The test will raise a `wines.models.Bottle.cork.RelatedObjectDoesNotExist: Bottle has no cork.` exception, even though the API returns a `201` for `Bottle` creation with the field `cork` properly set (more below).

## More explanations

Two models have been created, `Bottle` and `Cork`.

`Cork` holds a `OneToOneField` field named `bottle` that points to the `Bottle` model. The `related_name` is set to `cork`.

Let's imagine we create a `Cork` object that holds the `id` `21`.

You could now create a `Bottle` object through a `POST` request to the API and set the `cork` field in the JSON data to `21`. This works, returns a `201`, and the body has the field `cork` properly set to `21`.

However, this is actually not persisted in the database.

You can run the server and try for yourself using `./manage.py` and querying the `api/bottles` and `api/corks` resources.
