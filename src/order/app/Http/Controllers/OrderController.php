<?php

namespace App\Http\Controllers;

use App\Http\Requests\OrderRequest;
use App\Models\Order;
use Illuminate\Http\JsonResponse;

class OrderController extends Controller
{
    /**
     * @param OrderRequest $orderRequest
     * @return JsonResponse
     */
    public function indexOrder(OrderRequest $orderRequest): JsonResponse
    {
        return response()->json();
    }

    /**
     * @param OrderRequest $orderRequest
     * @return JsonResponse
     */
    public function showOrder(OrderRequest $orderRequest): JsonResponse
    {
        $order = new Order();

        return response()->json($order->find($orderRequest->route('id')));
    }

    /**
     * @param OrderRequest $orderRequest
     * @return JsonResponse
     */
    public function createOrder(OrderRequest $orderRequest): JsonResponse
    {
        $order = new Order();

        $order->create([
                "food_id"  => $orderRequest->food_id,
                "drink_id" => $orderRequest->drink_id
            ]
        );

        return response()->json($order->find($order->id()));
    }

    /**
     * @param OrderRequest $orderRequest
     * @return JsonResponse
     */
    public function updateOrder(OrderRequest $orderRequest): JsonResponse
    {
        $order = (new Order())->find($orderRequest->route('id'));

        $order->fill([
                "food_id"  => $orderRequest->food_id,
                "drink_id" => $orderRequest->drink_id
            ]
        )->save();

        return response()->json($order->find($order->id()));
    }

    /**
     * @param OrderRequest $orderRequest
     * @return JsonResponse
     */
    public function deleteOrder(OrderRequest $orderRequest): JsonResponse
    {
        $order = new Order();

        $order->find($orderRequest->route('id'))->delete();

        return response()->json([],204);
    }
}
