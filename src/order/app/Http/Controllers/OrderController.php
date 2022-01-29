<?php

namespace App\Http\Controllers;

use App\Models\Order;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;

class OrderController extends Controller
{
    /**
     * @param Request $request
     * @return JsonResponse
     */
    public function showOrder(Request $request): JsonResponse
    {
        $order = new Order();

        return response()->json($order->find($request->route('id')));
    }

    /**
     * @param Request $request
     * @return JsonResponse
     */
    public function createOrder(Request $request): JsonResponse
    {
        $order = new Order();

        $order->create([
                "food_id"  => $request->food_id,
                "drink_id" => $request->drink_id
            ]
        );

        return response()->json($order->find($order->id()));
    }

    /**
     * @param Request $request
     * @return JsonResponse
     */
    public function updateOrder(Request $request): JsonResponse
    {
        $order = (new Order())->find($request->route('id'));

        $order->fill([
                "food_id"  => $request->food_id,
                "drink_id" => $request->drink_id
            ]
        )->save();

        return response()->json($order->find($order->id()));
    }

    /**
     * @param Request $request
     * @return JsonResponse
     */
    public function deleteOrder(Request $request): JsonResponse
    {
        $order = new Order();

        $order->find($request->route('id'))->delete();

        return response()->json([],204);
    }
}
