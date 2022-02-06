<?php

namespace App\Http\Requests;

use Illuminate\Contracts\Validation\Validator;
use Illuminate\Http\Exceptions\HttpResponseException;
use Illuminate\Http\Request as IlluminateRequest;

abstract class Request extends IlluminateRequest
{
    /**
     * NOTE:
     * FormRequestクラスのメソッドをオーバーライドします．
     * バリデーション前のページにリダイレクトせずに，バリデーション結果をJSONデータとしてレスポンスできるようにします．
     *
     * @param Validator $validator
     */
    protected function failedValidation(Validator $validator)
    {
        throw new HttpResponseException(
            response()->json(
                [
                    "errors" => $validator->errors()],
                422
            )
        );
    }
}
