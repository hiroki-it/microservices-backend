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
    $router->get('/{id}', [OrderController::class, 'showOrder']);
    $router->post('/', [OrderController::class, 'createOrder']);
    $router->put('/{id}', [OrderController::class, 'updateOrder']);
    $router->delete('/{id}', [OrderController::class, 'deleteOrder']);
});
