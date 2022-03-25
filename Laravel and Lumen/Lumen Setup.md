# Enabling Facades
In `bootstrap/app.php` uncomment the following lines

```php
$app->withFacades();

$app->withEloquent();
```

This enables Faces and using db functions in the project

# Enabling Authentication
Uncommenting the following lines to enable middleware and authentication

```php
// Middleware
$app->middleware([
    App\Http\Middleware\ExampleMiddleware::class
]);

// Authentication
$app->routeMiddleware([
    'auth' => App\Http\Middleware\Authenticate::class,
]);

// ...

// Register Apps
$app->register(App\Providers\AppServiceProvider::class);
 $app->register(App\Providers\AuthServiceProvider::class);
 $app->register(App\Providers\EventServiceProvider::class);
```
