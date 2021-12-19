<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

final class Order extends Model
{
    protected $fillable = [
        'food_id', 'drink_id',
    ];

    /**
     * @var int
     */
    private int $id;

    /**
     * @var int
     */
    private int $food_id;

    /**
     * @var int
     */
    private int $drink_id;
}
