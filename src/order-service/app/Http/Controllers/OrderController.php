<?php

namespace App\Http\Controllers;

use App\Models\Order;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;

class OrderController extends Controller
{
    /**
     * @param int $id
     * @return JsonResponse
     */
    public function showOrder(int $id)
    {
        $order = new Order();

        return response()->json($order->find($id));
    }

    /**
     * @param Request $request
     * @return JsonResponse
     */
    public function createOrder(Request $request)
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
     * @param int     $id
     * @return JsonResponse
     */
    public function updateOrder(Request $request, int $id)
    {
        $order = (new Order())->find($id);

        $order->fill([
                "food_id"  => $request->food_id,
                "drink_id" => $request->drink_id
            ]
        )->save();

        return response()->json($order->find($order->id()));
    }

    /**
     * @param int $id
     * @return JsonResponse
     */
    public function deleteOrder(int $id)
    {
        $order = new Order();

        $order->find($id)->delete();

        return response()->json([],204);
    }
}
