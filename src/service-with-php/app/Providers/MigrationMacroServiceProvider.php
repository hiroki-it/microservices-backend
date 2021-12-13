<?php

namespace App\Providers;

use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\ServiceProvider;

class MigrationMacroServiceProvider extends ServiceProvider
{
    /**
     * Register any application services.
     *
     * @return void
     */
    public function register()
    {
        Blueprint::macro("systemColumns", function () {
            $this->string("created_at")
                ->comment("レコード作成日")
                ->nullable();
            $this->string("updated_at")
                ->comment("レコード更新日")
                ->nullable();
        });

        Blueprint::macro("dropSystemColumns", function () {
            $this->dropColumn(
                "created_at",
                "updated_at"
            );
        });
    }
}
