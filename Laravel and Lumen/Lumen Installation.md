# Package Requirements
Packages needed are PHP extensions.
PHP version must be >=8.0

* composer
* php-mbstring
* php-pdo
* phpunit
* php-xml

# Creating a New Project
Creating a new project will make dir in pwd

`composer create-project --prefer-dist laravel/lumen <project name>`

## Environment Setup
In your .env file, set the application key to a random string ~32 chars long

By default `$_ENV` is globally available for values in the .env

To pull which environment you're on, use `environment()`

```php
// Pull current environment
$environment = app()->environment();

// Check if local environment
if (app()->environment('local')) {}

// Check if either local or staging
if (app()->environment('local', 'staging')) {}
```

- - - -

# Starting Development Server
Use Laravel's built in PHP dev server wrapper

In project folder

`php artisan serve`

Use custom port

`php artisan serve --port=9000`

Or use PHP's built in dev server

`php -S localhost:8000 -t public`

Now you can access the site on http://localhost:8000
