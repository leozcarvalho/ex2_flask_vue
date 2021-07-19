<template>
    <div class="row">
        <div class="col-2"></div>
        <div v-if = "finished === false" class="col-8">
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
         <div v-else class="col-8">
            <h1 class="text-center">Resultado</h1>
            <div class="mt-5">
              <h2>Numeros inseridos: {{this.numbers}}</h2>
              <h2>Ordem inversa: {{this.reverse}}</h2>
              <h2>Soma: {{this.sum}}</h2>
              <h2>Média: {{this.med}}</h2>
              <h2>Valores superiores a média: {{this.upmed}}</h2>
              <h2>Valores inferiores a 7: {{this.underseven}}</h2>
              <div class="container mt-5">
                <div class="row">
                  <div class="col text-center">
                    <button
                      class="btn btn-primary btn-lg"
                      @click="reset">REINICIAR
                    </button>
                  </div>
                </div>
              </div>
            </div>
         </div>
        <div class="col-2">
        </div>
    </div>
</template>

<script>

import axios from 'axios';

export default {
  data() {
    return {
      numbers: [],
      number: null,
      result: [],
      reverse: [],
      sum: 0,
      med: 0,
      upmed: 0,
      underseven: 0,
      finished: false,
    };
  },

  methods: {
    addNumber() {
      const num = parseInt(this.number, 10);
      if (Number.isNaN(num)) {
        window.alert('Insira um valor!');
      } else if (num < -1) {
        this.number = null;
        window.alert('Insira um valor positivo!');
      } else if (num === -1) {
        this.postNumbers();
      } else {
        this.numbers.push(num);
        this.number = null;
      }
    },
    postNumbers() {
      const path = 'http://localhost:5000/numbers';
      const payload = {
        numbers: this.numbers,
      };
      axios.post(path, payload)
        .then((res) => {
          this.result = res.data;
          this.reverse = res.data.reverse;
          this.sum = res.data.sum;
          this.med = res.data.med;
          this.upmed = res.data.upmed;
          this.underseven = res.data.underseven;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
      this.finished = true;
    },
    reset() {
      this.finished = false;
      this.numbers = [];
      this.number = null;
    },
  },
  created() {
  },
};
</script>
