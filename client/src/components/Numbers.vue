<template>
    <div class="row">
        <div class="col-2"></div>
        <div class="col-8">
            <h1>Insira os números desejados ou insira -1
            para sair e gerar seu resultado:</h1>
            <div class="my-5">
                    <div class="row">
                    <div class="col-2">
                        <label for="inputNumber"
                        class="font-weight-bold">
                            <h2>Número: </h2>
                        </label>
                    </div>
                    <div class="col-8">
                        <input class = "form-control form-control-lg"
                        placeholder = "Insira um número inteiro positivo"
                        maxlength="3">
                    </div>
                    <div class="col-2">
                        <button
                        class="btn btn-success btn-lg mb-2">
                        ENVIAR
                        </button>
                    </div>
                    </div>
            </div>
        </div>
        <div class="col-2"></div>
    </div>
</template>
