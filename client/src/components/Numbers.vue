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
                        v-model="number"
                        maxlength="3">
                    </div>
                    <div class="col-2">
                        <button
                        class="btn btn-success btn-lg mb-2"
                        @click="addNumber">
                        ENVIAR
                        </button>
                    </div>
                    </div>
            </div>
        </div>
        <div class="col-2"></div>
    </div>
</template>

<script>

/* import axios from 'axios'; */

export default {
  data() {
    return {
      numbers: [],
      number: null,
    };
  },

  methods: {
    addNumber() {
      const num = parseInt(this.number, 8);
      console.log(num);
      if (Number.isNaN(num)) {
        window.alert('Insira um valor!');
      } else if (num < -1) {
        console.log(typeof this.number);
        window.alert('Insira um valor positivo!');
      } else if (num === -1) {
        this.postNumbers();
      } else {
        this.numbers.push(this.number);
        this.number = null;
      }
      console.log(typeof num);
      console.log(this.numbers);
    },
    postNumbers() {
      console.log('teste');
    },
  },
  created() {
  },
};
</script>
