<?php

use App\Http\Controllers\OrderController;
use Laravel\Lumen\Routing\Router;

/** @var Router $router */

/*
|--------------------------------------------------------------------------
| Application Routes
|--------------------------------------------------------------------------
|
| Here is where you can register all of the routes for an application.
| It is a breeze. Simply tell Lumen the URIs it should respond to
| and give it the Closure to call when that URI is requested.
|
*/

$router->group(['prefix' => 'orders'], function () use ($router) {
    // NOTE: Laravel8系のRouteの記法には非対応
    $router->get('/{id}', 'OrderController@showOrder');
    $router->get('/', 'OrderController@indexOrder');
    $router->post('/', 'OrderController@createOrder');
    $router->put('/{id}', 'OrderController@updateOrder');
    $router->delete('/{id}', 'OrderController@deleteOrder');
});
