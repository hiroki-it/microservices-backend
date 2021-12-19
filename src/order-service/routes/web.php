<?php

use App\Models\Order;
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

    $router->get('/', function () use ($router) {
        return (new Order())->find(1);
    });

    $router->post('/', function () use ($router) {
        $order = (new Order())->create([
                "food_id"  => 1,
                "drink_id" => 1
            ]
        );
    });
});
